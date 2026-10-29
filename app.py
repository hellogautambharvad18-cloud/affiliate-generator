import os,re,json,html,io,zipfile,tempfile,shutil,hashlib,secrets,base64
from pathlib import Path
from urllib.parse import urlparse,unquote
from datetime import date,timedelta
from flask import Flask,render_template,request,jsonify,send_file
from openai import OpenAI
import requests
from bs4 import BeautifulSoup,NavigableString,Comment
import rcssmin,rjsmin
from design2_fixes import (seo_images,scrub_image_alts,strip_third_party_fa_kit,
 retheme_reference_css,retheme_html_inline,make_fda_registered_badge,
 is_non_product_image,reviewer_photo_slot)

app=Flask(__name__)
import traceback
from werkzeug.exceptions import HTTPException
import auth,niches,design15
auth.init(app)

def _swap_header_for_banner(soup,banner_html):
 """Replace the page's <header> (hero) with a title banner and return the new
 banner tag, so callers can place the page body directly below it. Returns
 None when the page has no <header>."""
 hdr=soup.find('header')
 if hdr is None:return None
 tag=BeautifulSoup(banner_html,'html.parser').find()
 hdr.replace_with(tag)
 return tag

def _faq_question_text(el):
 """A FAQ question's text for structured data, ignoring decorative toggle icons
 such as the "+" inside <span class="faq-icon">."""
 parts=[t for t in el.find_all(string=True) if t.find_parent(class_=re.compile(r'faq.?icon|toggle.?icon',re.I)) is None]
 return re.sub(r'\s+',' ',''.join(parts)).strip()

def _log_failure(endpoint,exc):
 """Send a failure to the server log (so it shows in Render's Logs tab) and to
 the admin error log (/admin/errors). Never raises: reporting must not hide
 the original error from the user."""
 try:
  tb=traceback.format_exc()
  app.logger.error('%s failed: %s: %s\n%s',endpoint,type(exc).__name__,exc,tb)
  ctx=(f'product={request.form.get("product_name","")!r} domain={request.form.get("domain","")!r} '
       f'design={request.form.get("design","")!r} niche={request.form.get("niche","")!r} '
       f'provider={request.form.get("ai_provider","")!r}')
  auth.record_error(endpoint,f'{type(exc).__name__}: {str(exc)[:300]}',ctx+'\n\n'+tb)
 except Exception:pass

@app.errorhandler(Exception)
def _unhandled(exc):
 """Anything not already handled inside a route: log it, then answer with a
 clean message. HTTP errors (404, 401, 413...) pass through untouched."""
 if isinstance(exc,HTTPException):return exc
 _log_failure(request.endpoint or request.path,exc)
 if request.path.startswith('/api/'):
  return jsonify(error='Something went wrong on our side. Please try again.'),500
 return ('<h1>Something went wrong</h1><p>Please go back and try again.</p>',500)

def _request_hint():
 """The publisher description with the chosen niche folded in."""
 nid=request.form.get('niche',niches.DEFAULT_NICHE)
 if not niches.valid_niche(nid):nid=niches.DEFAULT_NICHE
 return niches.build_hint(nid,request.form.get('subniche',''),request.form.get('product_hint',''))
app.config['MAX_CONTENT_LENGTH']=150*1024*1024
BASE=Path(__file__).resolve().parent
TEMPLATE_DIR=BASE/'templates'
BUNDLED_ASSETS_DIR=BASE/'bundled_assets'  # Static template images — no internet needed
TEMPLATES={
 '1':{'name':'Design 1 — BloodPril Editorial','source':'design-1.source.md','old':'BloodPril','old_domains':['bloodprilofficial.com']},
 '2':{'name':'Design 2 — JellyTide Premium','source':'design-2.source.md','old':'JellyTide','old_domains':['jellytide.com','jellytideus.com','mwebauditly.com']},
 '3':{'name':'Design 3 — VapoCept Editorial','source':'design-3.source.md','old':'VapoCept','old_domains':['vappocept.com']},
 '4':{'name':'Design 4 — BreathiZen Premium','source':'design-4.source.md','old':'BreathiZen','old_domains':['bbreathizen.com','mwebtracepoint.com']},
 # Design 5's own product photos (gallery shots, pricing-card bottle images)
 # aren't hosted on the scraped site's own domain at all — they sit on the
 # page-builder tool's asset bucket instead
 # (storage.googleapis.com/uxpilot-auth.appspot.com/...). Without that host
 # listed here, strip_old_product_images() never recognizes them as images
 # to replace, so every generated site — regardless of brand — keeps
 # showing the original Gelagen product's own photos untouched.
 '5':{'name':'Design 5 — Gelagen Editorial','source':'design-5.source.md','old':'Gelagen','old_domains':['gellagen.com','storage.googleapis.com']},
 # Design 6 used to be a scraped "Gelagen Gallery" template (Tailwind
 # classless-div markup with no consistent class hooks for populate()'s
 # generic card-matching heuristics to grab onto) — it kept shipping every
 # generated site with leftover content, pricing and even product photos
 # from the original scraped biotin-gummy product, regardless of brand. It's
 # now a from-scratch native design ("Aurora") built on the same reliable
 # string-template contract as designs 8-10, with no scrape-dependent
 # population logic to go wrong.
 '6':{'name':'Design 6 — Aurora (Native, Auto-Themed)','source':'design-6.source.md','old':None,'old_domains':[],'native':True},
 '7':{'name':'Design 7 — MemoVolt Structured','source':'design-7.source.md','old':'MemoVolt','old_domains':['memovoltus.com']},
 '8':{'name':'Design 8 — Clarity (Native, Auto-Themed)','source':'design-8.source.md','old':None,'old_domains':[],'native':True},
 '9':{'name':'Design 9 — Bold (Native, Auto-Themed)','source':'design-9.source.md','old':None,'old_domains':[],'native':True},
 '10':{'name':'Design 10 — Playful (Native, Auto-Themed)','source':'design-10.source.md','old':None,'old_domains':[],'native':True},
 '11':{'name':'Design 11 — Surge (Native, Auto-Themed)','source':'design-11.source.md','old':None,'old_domains':[],'native':True},
 '12':{'name':'Design 12 — Terra (Native, Auto-Themed)','source':'design-12.source.md','old':None,'old_domains':[],'native':True},
 '13':{'name':'Design 13 — Verdict (Native, Auto-Themed)','source':'design-13.source.md','old':None,'old_domains':[],'native':True},
 '14':{'name':'Design 14 — Teal Classic (Native, Auto-Themed)','source':'design-14.source.md','old':None,'old_domains':[],'native':True},
 '15':{'name':'Design 15 — Dynamic Unique (Native, Auto-Themed)','source':'design-15.source.md','old':None,'old_domains':[],'native':True},
 '16':{'name':'Design 16 — Editorial (Native, Auto-Themed)','source':'design-16.source.md','old':None,'old_domains':[],'native':True},
}
ALL_OLD_BRANDS=['BloodPril','JellyTide','VapoCept','BreathiZen','Gelagen','MemoVolt']
OLD_REVIEWER_NAMES=['Dr. Lena Kessler','Tobias Engel']
ALL_OLD_DOMAINS=[d for t in TEMPLATES.values() for d in t['old_domains']]

# ── Image slot names ──
KEEP_IMG_STEMS={
 # 'how-it-works' was removed from this set — it's the ORIGINAL scraped
 # BloodPril template's own mechanism infographic, which may carry that
 # product's own baked-in text/branding. Keeping it here auto-downloaded
 # and showed the wrong brand's graphic on every generated site that
 # didn't upload its own how-it-works.* image; it now falls through to
 # localize_images()'s how-it-works branch instead, which removes the
 # image outright (and warns) when no upload exists.
 '1':{'badge-usa','badge-fda','badge-gmp','badge-natural','reviewer-1','reviewer-2','reviewer-3','stars','cards','guarantee'},
 # NOTE: "keep" is only safe for genuinely generic, brand-agnostic graphics
 # (badge seals, star ratings, generic stock reviewer photos). Anything that
 # is actual product photography or a screenshot of the ORIGINAL scraped
 # product's real checkout/order page still shows THAT product's real
 # branding no matter what the file gets renamed to — jellytide_checkout.webp
 # and jellytide_description.webp are a full "JELLY TIDE" checkout-page
 # screenshot and product/label photo, not generic icons, so they were
 # removed from this list (they now fall through to the normal
 # no-upload-provided removal path instead of being auto-displayed).
 '2':{'jellytide-all-natural-ingredients','jellytide-made-in-usa','jellytide-gmp-certified','jellytide-fda-approved','jellytide_review_1','jellytide_review_2','jellytide_review_3','jellytide-credit-cards','60_days'},
 # 'vapocept-benefits' was removed from this list — it's the "Benefits"
 # section's own product photo (a labeled VapoCept box/bottle render, per
 # its figcaption "Benefits composition built from the product artwork"),
 # not a generic brand-agnostic graphic like the badges/reviewer photos
 # below. Keeping it here re-downloaded and displayed the ORIGINAL
 # VapoCept-branded packaging on every generated site regardless of
 # product — same anti-pattern already fixed for design 2's
 # jellytide_checkout.webp/jellytide_description.webp above.
 # 'vapocept-how-it-work' (the original scraped mechanism infographic) was
 # removed from this set for the same reason as design 1's 'how-it-works'
 # above — same fix, same rationale.
 '3':{'review-1','review-2','review-3','gmp-certified','made-in-usa','all-natural','money-back-gurantee','cards_cc'},
 # breathizen-payment (a full pricing-package graphic) and
 # breathizen-6-bottles-guarantee (an actual BreathiZen bottle photo) are
 # real product/marketing photography, not generic badges — same reasoning
 # as design 2 above.
 '4':{'breathizen-review-1','breathizen-review-2','breathizen-review-3','breathizen-review-4','breathizen-reviews','breathizen-guarantee'},
 # 'gelagen-how-it-works' removed — same reason as design 1/3 above.
 '5':{'badge-usa','badge-fda','badge-gmp','badge-natural','member-1','member-2','member-3','cards','bonus-1','bonus-2','bonus-3','bonus-4','bonus-5','bonus-6','guarantee-badge'},
 '6':set(),
 # 'how-it-works-infographic' removed — same reason as design 1/3/5 above;
 # this was literally the MemoVolt mechanism graphic.
 '7':{'badge-usa','badge-fda','badge-gmp','badge-natural','member-1','member-2','member-3','atc','cards','bonus-memory-shield-diet','bonus-5-minute-brain-reboot','bonus-caregivers-survival-guide','guarantee-badge'},
}
HERO_STEMS={
 '1':set(),  # Design 1: bottle-3 is template hero but we use user's hero.png or bottle-3.png
 '2':{'jellytide_hero','jellytide_bottle'},
 # 'breathizen-order-page' used to be listed here too, so localize_images()
 # treated the "How To Order" section's checkout-page screenshot slot as
 # just another hero-photo alias — silently reusing the hero product shot
 # there regardless of what the publisher actually uploaded. That section's
 # own copy explicitly calls it "the official, fully secured {brand}
 # checkout" / alt="Official Secure Order Page — Checkout", so showing the
 # same product photo again reads as a mismatch. It's routed to the
 # 'checkout' manual slot instead now (via _keep_role's 'order-page' match
 # below), the same upload that already fills the "Stock Is Limited" CTA's
 # checkout screenshot — one uploaded checkout.png now fills both.
 '3':set(),'4':{'breathizen-hero'},
 '5':{'gelagen-hero-shot'},'6':set(),'7':set(),
}
# Design 1 special: template uses bottle-3 as hero image slot
DESIGN1_HERO_STEM='bottle-3'
BOTTLE_STEMS={
 '1':{'bottle-2','bottle-3','bottle-6'},'2':{'jellytide_prod_2_bottle','jellytide_prod_3_bottle','jellytide_prod_6_bottle'},
 '3':{'vapocept-2-bottle','vapocept-3-bottle','vapocept-6-bottle'},
 '4':{'breathizen-3-bottles','breathizen-6-bottles-guarantee'},'5':{'gelagen-2-bottles','gelagen-3-bottles','gelagen-6-bottles'},
 '6':set(),'7':{'memovolt-2-bottles','memovolt-3-bottles','memovolt-6-bottles'},
}
# "payment" and "checkout" were removed from this list — on design 2 those
# keywords matched jellytide_checkout.webp, which turned out to be a full
# screenshot of the ORIGINAL product's real checkout page (bottle photos,
# competitor branding, real prices) rather than a generic "we accept these
# cards" icon strip. A renamed filename doesn't change what's actually in
# the picture, so anything this imprecise is not safe to auto-reuse —
# "credit" (payment-method logos) stays since that's a genuinely generic,
# brand-agnostic icon strip in every design that uses it.
# 'how-it-works' was removed from this generic list — a substring match here
# classified ANY how-it-works-named stem (e.g. "gelagen-how-it-works",
# "how-it-works-infographic") as a safe-to-keep generic badge regardless of
# the per-design KEEP_IMG_STEMS set above, which is exactly the wrong-brand
# mechanism-infographic leak those per-design edits were meant to close.
# That image slot is handled on its own in localize_images() instead (an
# uploaded how-it-works.* wins; with no upload, the <img> is removed, never
# the original scraped template's own graphic).
GENERIC_KEEP_KW=('badge','reviewer','stars','cards','guarantee','trust','natural','fda','gmp','usa','review','member','bonus','credit','60_days','atc','money-back','certified','approved','secure')
# Both "bottle-N" and "N-bottles" naming are accepted — the web form's own
# on-screen hint tells users to name files "1-bottles.jpg"/"3-bottles.jpg"/
# "6-bottles.jpg", which didn't match this dict at all, so uploads named
# exactly as instructed were silently falling back to generic placement
# instead of their intended slot.
MANUAL_SLOTS={'hero':0,
 'bottle-1':0,'bottle1':0,'1-bottle':0,'1-bottles':0,
 'bottle-2':0,'bottle2':0,'2-bottle':0,'2-bottles':0,
 'bottle-3':1,'bottle3':1,'3-bottle':1,'3-bottles':1,
 'bottle-6':2,'bottle6':2,'6-bottle':2,'6-bottles':2,
 'how-it-works':None,'howitworks':None,'how_it_works':None,
 'reviewer-1':None,'reviewer1':None,'reviewer-2':None,'reviewer2':None,'reviewer-3':None,'reviewer3':None,'reviewer-4':None,'reviewer4':None,
 'bonus-1':None,'bonus1':None,'bonus-2':None,'bonus2':None,'bonus-3':None,'bonus3':None,'bonus-4':None,'bonus4':None,'bonus-5':None,'bonus5':None,'bonus-6':None,'bonus6':None,
 # Trust-badge / guarantee-seal / payment-icon slots — a design's own
 # scraped versions of these are classified "keep" and previously always
 # auto-downloaded from the original site regardless of what the publisher
 # uploaded, so a manually supplied badge-fda.png etc. was silently ignored.
 'badge-fda':None,'badge-gmp':None,'badge-usa':None,'badge-natural':None,
 'guarantee':None,'credit-cards':None,'stars':None,
 # Optional — a checkout-page screenshot or a supplement-facts/dosage label
 # has no safe generic substitute, so these slots stay empty unless a
 # publisher uploads something specifically named for them.
 'checkout':None,'supplement-facts':None}

# A stem naming an actual bottle count (e.g. "breathizen-6-bottles-guarantee")
# is real product packaging photography, even when it also carries a
# generic-sounding keyword like "guarantee" (a badge seal graphic wouldn't
# also mention a bottle count) — never auto-reuse those, regardless of
# which per-design/keyword list they'd otherwise match.
_BOTTLE_PHOTO_PAT=re.compile(r'\d+[-_]?bottles?\b',re.I)
# Design 5/6's own scraped photos aren't named descriptively at all — their
# source hosts (an asset-bucket CDN) give every image a random UUID
# filename like "b33bfdaf-37ab-4561-a74f-63100207a4de". A plain substring
# check against GENERIC_KEEP_KW below is fine for a real descriptive stem
# ("jellytide-fda-approved") but unsafe here: hex digits alone can spell out
# a keyword by pure chance — that exact UUID contains "fda" — misclassifying
# an ordinary scraped PRODUCT PHOTO as a keep-worthy badge/trust-seal graphic,
# which then gets live-downloaded and shown as-is (the original, different
# product's own packaging) instead of being replaced by the publisher's
# upload. Treat anything shaped like a UUID as never keyword-matchable.
_RANDOM_ID_PAT=re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$',re.I)

def _is_keep(stem,design):
 d=str(design)
 if _BOTTLE_PHOTO_PAT.search(stem):return False
 if stem in KEEP_IMG_STEMS.get(d,set()):return True
 if not _RANDOM_ID_PAT.match(stem) and any(k in stem for k in GENERIC_KEEP_KW):return True
 return False

def _classify(stem,design):
 d=str(design)
 if not _BOTTLE_PHOTO_PAT.search(stem):
  if stem in KEEP_IMG_STEMS.get(d,set()):return 'keep'
  if not _RANDOM_ID_PAT.match(stem) and any(k in stem for k in GENERIC_KEEP_KW):return 'keep'
 if stem in HERO_STEMS.get(d,set()):return 'hero'
 if stem in BOTTLE_STEMS.get(d,set()):return 'bottle'
 return 'product'

SCHEMA={'type':'object','properties':{
 'product_name':{'type':'string'},'brand':{'type':'string'},'tagline':{'type':'string'},'category':{'type':'string'},'description':{'type':'string'},
 'ingredients':{'type':'array','items':{'type':'object','properties':{'name':{'type':'string'},'role':{'type':'string'},'description':{'type':'string'}},'required':['name','role','description'],'additionalProperties':False}},
 'benefits':{'type':'array','items':{'type':'string'},'description':'Each string MUST be in the exact format "Title — Description" (em-dash separator). Never return just a bare title with no description half.'},
 'how_it_works':{'type':'array','items':{'type':'object','properties':{'title':{'type':'string'},'text':{'type':'string'}},'required':['title','text'],'additionalProperties':False}},
 'faqs':{'type':'array','items':{'type':'object','properties':{'q':{'type':'string'},'a':{'type':'string'}},'required':['q','a'],'additionalProperties':False},'description':'If any FAQ answer states how much/how often to take this product, it MUST quote the exact same number as serving_info.daily_serving below — never a different capsule/serving count than that field.'},
 'pricing':{'type':'array','items':{'type':'object','properties':{'bottles':{'type':'integer'},'price_per_bottle':{'type':'string'},'total':{'type':'string'},'shipping':{'type':'string'},'label':{'type':'string'}},'required':['bottles','price_per_bottle','total','shipping','label'],'additionalProperties':False}},
 'seo':{'type':'object','properties':{'title':{'type':'string'},'description':{'type':'string'},'keywords':{'type':'array','items':{'type':'string'}}},'required':['title','description','keywords'],'additionalProperties':False},
 'reviews_note':{'type':'string','description':'A short, generic, public-safe disclaimer shown directly on the live site under the reviews section (e.g. "Individual experiences vary. These reflect personal opinions, not guaranteed outcomes."). This is READ BY SITE VISITORS — never mention that the reviews are placeholders, fictional, or need to be replaced; that reminder belongs in source_notes instead.'},
 'sample_reviews':{'type':'array','items':{'type':'string'},'description':'3 short, varied, plausible customer review sentences (fictional placeholder style, each different)'},
 'reviewer_names':{'type':'array','items':{'type':'string'},'description':'3 plausible first names for reviewers, demographically appropriate for who actually buys/uses this specific product (e.g. mostly male names for a male-targeted product, mostly female for a female-targeted product, mixed for general wellness)'},
 'bonuses':{'type':'array','items':{'type':'object','properties':{'title':{'type':'string'},'description':{'type':'string'}},'required':['title','description'],'additionalProperties':False},'description':'Any free bonus items, guides or extras that come with larger orders of this product, if genuinely offered. Return an empty array if the product has no known bonus offers — never invent fake bonuses.'},
 'whatis_callout':{'type':'string','description':'One sentence of straight-talk context about this specific product — e.g. what it is NOT, or an honest caveat. Must be specific to this product, not generic supplement boilerplate.'},
 'how_it_works_intro':{'type':'string','description':'One sentence summarizing the overall mechanism/approach of how this product works, specific to its actual ingredients and category — not a generic "combines ingredients" statement.'},
 'pricing_note':{'type':'string','description':'One sentence of honest guidance about choosing a package size for this product, referencing its actual bundle structure.'},
 'guarantee_text':{'type':'string','description':'One to two sentences describing the refund guarantee experience for this product in natural, varied phrasing — avoid generic boilerplate.'},
 'final_cta_text':{'type':'string','description':'One short, punchy closing sentence encouraging the reader to try this specific product, phrased uniquely each time — not a repeated template line.'},
 'symptoms':{'type':'array','items':{'type':'object','properties':{'title':{'type':'string'},'text':{'type':'string'}},'required':['title','text'],'additionalProperties':False},'description':'5 to 6 short problem/symptom-recognition statements that someone who needs this specific product would relate to — each a short title (2-4 words) plus one sentence describing what that problem actually feels like day-to-day. Must be specific to this product\'s real category (e.g. for a joint supplement: stiffness, reduced range of motion; for a sleep aid: trouble falling asleep, restless nights; for a digestive product: bloating, irregularity). Never reuse symptoms from an unrelated category.'},
 'serving_info':{'type':'object','properties':{
   'daily_serving':{'type':'string','description':'Typical daily serving for this category of product, e.g. "1 capsule" or "2 capsules" — a plausible, typical-for-category value, not a verified fact about this specific unverified product.'},
   'per_bottle':{'type':'string','description':'Typical capsule count per bottle for this category, consistent with the product\'s stated supply-length claims elsewhere (e.g. a 30-day supply at 1/day is "30 capsules"). Typical/plausible, not verified.'},
   'doses_published':{'type':'string','description':'Whether individual ingredient amounts are typically disclosed on the label for this category of product — usually "Yes, per label" for a simple named-ingredient formula, or "Proprietary blend" if the category commonly hides exact per-ingredient amounts behind a blend total. A plausible typical answer, not a verified fact.'}
  },'required':['daily_serving','per_bottle','doses_published'],'additionalProperties':False,'description':'Typical-for-category serving specs, same spirit as the pricing field — your best plausible estimate when the exact verified figure is not available, never a specific number left blank or evasive. This daily_serving value is the single source of truth for how often/how much to take this product — description, how_it_works_intro, sample_reviews and faqs must never state a different serving count.'},
 'source_notes':{'type':'array','items':{'type':'string'}}
},'required':['product_name','brand','tagline','category','description','ingredients','benefits','how_it_works','faqs','pricing','seo','reviews_note','sample_reviews','reviewer_names','bonuses','whatis_callout','how_it_works_intro','pricing_note','guarantee_text','final_cta_text','symptoms','serving_info','source_notes'],'additionalProperties':False}

def clean_url(u):
 u=(u or '').strip()
 if not u:return ''
 return u if re.match(r'^https?://',u,re.I) else 'https://'+u

def slugify(s):return re.sub(r'[^a-z0-9]+','-',s.lower()).strip('-') or 'product'

_LABEL_PAT=re.compile(
 r'^\s*(?:SCHEMA\b|NAVBAR\b|SYMPTOMS\b|HERO\b|PRICING\b|INGREDIENTS\b|BENEFITS\b|'
 r'REVIEWS\b|HOW IT WORKS\b|FAQ\b|TESTIMONIALS\b|ORDER\b|GUARANTEE\b|BONUS\b|'
 r'CERTIFICATIONS\b|FEATURES\b|FOOTER\b|NAVIGATION\b|CTA\b|INTRO\b|WHAT IS\b|'
 r'NEW SECTION\b|PRICING BAND\b|PRICING DETAILS\b|HERO —|SYMPTOMS —|SCHEMA —|'
 r'NEW SECTION \().*$',re.I)

def normalize_source(raw):
 lines=[]
 for ln in raw.splitlines():
  if ln.startswith('|') and ln.endswith('|'):ln=ln[1:-1]
  if ln.startswith('| '):ln=ln[2:]
  if ln.endswith(' |'):ln=ln[:-2]
  # Markdown tables pad every cell with spaces to match the widest row in
  # the table — without stripping that, every generated page carries
  # megabytes of dead trailing whitespace copied straight into the HTML.
  lines.append(ln.rstrip())
 s='\n'.join(lines)
 s=re.sub(r'\\([\\`\*\_\{\}\[\]\(\)\#+\.!\|<>:&=?/\-@])',r'\1',s)
 s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',lambda m:m.group(2),s)
 s='\n'.join(ln for ln in s.splitlines() if not re.fullmatch(r'\s*\|?\s*:?-{3,}:?\s*(?:\|\s*)?',ln))
 s=re.sub(r'(?is)(<!doctype[^>]*>)\s*html\s*',r'\1\n',s,count=1)
 s=re.sub(r'(?im)^\s*html\s*[-_]{3,}\s*$','',s)
 s=re.sub(r'={3,}[^\n<>\'"();]*={3,}','',s)
 out=[]
 for ln in s.splitlines():
  stripped=ln.strip()
  if not stripped:out.append(ln);continue
  if re.fullmatch(r'=+',stripped):continue
  if re.fullmatch(r'<br\s*/?>',stripped,re.I):continue
  # Only treat this as a leaked "<!-- FOOTER SECTION -->"-style scrape
  # comment (safe to drop) when it's genuinely shouting ALL-CAPS with no
  # markup in it — the same signal used for the second-pass check below.
  # Without the uppercase/no-tag guard, this also matched ordinary
  # lowercase body copy that merely *starts* with one of these common
  # words — e.g. a wrapped footer link line "guarantee on every
  # order</a></li>" (starts with "guarantee") — and silently deleted it,
  # taking its closing </a></li> with it and corrupting every page's
  # footer nav on every generated site.
  if _LABEL_PAT.match(stripped) and '<' not in stripped and stripped==stripped.upper():continue
  out.append(ln)
 s='\n'.join(out)
 soup=BeautifulSoup(s,'html.parser')
 for t in list(soup.find_all(string=True)):
  if not isinstance(t,NavigableString):continue
  # Real <a> link text ("How It Works", "Ingredients", "Order Now"...) very
  # often is exactly one of the section-label keywords below — stripping it
  # here as if it were a leaked "HOW IT WORKS —" scrape comment silently
  # empties out real navigation links and buttons, which then either show
  # up blank or get deleted outright later (empty CTAs get decomposed).
  if t.parent.name in ('script','style','noscript','meta','link','title','a','button'):continue
  txt=str(t).strip()
  if not txt:continue
  if re.fullmatch(r'\s*html\s*',txt,re.I):t.extract();continue
  if '=====' in txt:
   cleaned=re.sub(r'={3,}[^\n\'"();]*={3,}','',txt)
   if cleaned!=txt:t.replace_with(cleaned);continue
  if _LABEL_PAT.match(txt) and len(txt)<150:
   # A short numbered tag like "BONUS 1"/"BONUS 2" is genuine visible card
   # copy (the small tag label on a bonus card), not a leaked scrape-artifact
   # section marker — real markers in this same list always pair with an em
   # dash elsewhere ("HERO —", "SYMPTOMS —"), never just a bare number.
   # Stripping it here silently emptied that tag on every generated site.
   if re.fullmatch(r'[A-Z][A-Z ]*\s*#?\d+',txt):continue
   # A bare keyword with nothing else — no number, no dash — is genuinely
   # ambiguous: e.g. design 4's trust-bar badge is a "60-Day" line followed
   # by a plain "Guarantee" text node (split across a <br>), which starts
   # with the GUARANTEE\b keyword and used to get silently deleted here,
   # leaving the badge's second line blank on every generated site. Every
   # confirmed real leaked-comment artifact in this format — every example
   # in _LABEL_PAT itself, "HERO —"/"SYMPTOMS —"/"SCHEMA —", the "BONUS 1"
   # style tags above — is ALL-CAPS, because it's converted straight from an
   # "<!-- HERO SECTION -->"-style HTML comment. Real visible UI copy that
   # merely happens to start with one of these keywords ("Guarantee",
   # "Bonus included", "Order today") is normal/title case. Only extract
   # when the text is actually shouting like a real artifact label.
   if txt==txt.upper():t.extract()
   continue
 return soup

def source_for(design):
 return normalize_source((TEMPLATE_DIR/TEMPLATES[design]['source']).read_text(encoding='utf-8',errors='ignore'))

def safe_rel(path):return path.lstrip('/')

# ── Responsive <img> sizing: real pixel width/height (PIL), eager/lazy
# loading, and consistent badge/guarantee/credit-card display widths —
# applied once, after each design's own DOM/template work is finished, as a
# single shared pass rather than per-design markup (most designs never set
# any of this themselves; a couple, e.g. design 13, already hardcode their
# own width/height/loading and are left alone below). ──
_IMG_CSS_BLOCK=('img{max-width:100%;height:auto}'
 '.auto-badge-img{width:100%;max-width:160px;height:auto}'
 '.auto-guarantee-img{width:100%;max-width:220px;height:auto}'
 '.auto-cc-img{width:100%;max-width:320px;height:auto}'
 '@media(max-width:480px){.auto-cc-img{max-width:260px}}'
 '.auto-authority-links a{color:var(--accent,#2563EB);text-decoration:none}'
 '.auto-authority-links a:hover{text-decoration:underline}')
_BADGE_IMG_STEMS={'badge-usa','badge-fda','badge-gmp','badge-natural','stars'}
_LOW_RES_DISPLAY_PX={'badge':160,'guarantee':220,'cc':320}
_LOW_RES_WARNINGS=[]  # reset per /api/generate request; (src,source_width,display_width)
_HIW_IMG_WARNINGS=[]  # reset per /api/generate request; design id, once per how-it-works image removed for lack of an upload

def _img_role(stem):
 if stem in _BADGE_IMG_STEMS:return 'badge'
 if stem=='guarantee':return 'guarantee'
 if stem=='credit-cards':return 'cc'
 return None

def real_image_size(rel_src,site_root):
 """(width,height) of the actual image file a page's <img src> points to,
 resolved against the output site root — or None when it can't be read
 (external URL, data: URI, or a placeholder path nothing was ever saved to)."""
 if not rel_src or not site_root:return None
 rel_src=str(rel_src)
 if rel_src.startswith(('data:','http:','https:')):return None
 p=Path(site_root)/rel_src.split('?',1)[0].split('#',1)[0]
 if not p.exists():return None
 try:
  from PIL import Image
  with Image.open(p) as im:return im.size
 except Exception:return None

def apply_img_sizing(soup,site_root,brand='',category=''):
 """Set real pixel width/height on every <img> (never a guessed fixed
 size); fetchpriority="high"+loading="eager" on the hero photo, loading="lazy"
 decoding="async" on everything else; a shared max-width class on badge/
 guarantee/credit-card images; and a brand+category hero alt instead of a
 bare "{brand} product". Returns a list of (src,source_width,display_width)
 for images displayed noticeably larger than their real resolution."""
 low_res=[]
 for img in soup.find_all('img'):
  src=img.get('src') or ''
  if not src or src.startswith('data:'):continue
  stem=Path(src).stem.lower()
  is_hero=stem=='hero' or img.get('id')=='hero-img'
  dims=real_image_size(src,site_root)
  if dims and (not img.get('width') or not img.get('height') or is_hero or _img_role(stem)):
   img['width']=str(dims[0]);img['height']=str(dims[1])
  role=_img_role(stem)
  if role:
   cls=img.get('class') or []
   if isinstance(cls,str):cls=cls.split()
   extra=f'auto-{role}-img' if role!='cc' else 'auto-cc-img'
   if role=='badge':extra='auto-badge-img'
   elif role=='guarantee':extra='auto-guarantee-img'
   if extra not in cls:cls=cls+[extra]
   img['class']=cls
   if dims and dims[0]<300 and _LOW_RES_DISPLAY_PX[role]>150:
    low_res.append((src,dims[0],_LOW_RES_DISPLAY_PX[role]))
    _LOW_RES_WARNINGS.append((src,dims[0],_LOW_RES_DISPLAY_PX[role]))
  if is_hero:
   img['fetchpriority']='high'
   img['loading']='eager'
   alt=(img.get('alt') or '').strip()
   if not alt or alt.lower() in ('',f'{brand} product'.lower(),(brand or '').lower()):
    # category is normally a full label like "respiratory wellness
    # supplement" — appending " supplement bottle" to that verbatim doubles
    # up the word ("...wellness supplement supplement bottle"); strip a
    # trailing generic product-type word first, same as _support_phrase().
    cat_clean=category
    for suffix in (' supplement',' formula',' product'):
     if cat_clean.lower().endswith(suffix):cat_clean=cat_clean[:-len(suffix)];break
    img['alt']=f'{brand} {cat_clean} supplement bottle'.strip() if cat_clean else (alt or f'{brand} supplement bottle')
   if soup.head and not soup.head.find('link',attrs={'rel':'preload','href':src}):
    link=soup.new_tag('link',rel='preload',href=src)
    link['as']='image'
    link['fetchpriority']='high'
    soup.head.append(link)
  else:
   if not img.get('loading'):img['loading']='lazy'
   if not img.get('decoding'):img['decoding']='async'
 return low_res

def inject_img_css(soup):
 style=soup.new_tag('style')
 style.string=_IMG_CSS_BLOCK
 if soup.head:soup.head.append(style)
 elif soup.body:soup.body.insert(0,style)

# ── CTA system: shared copy per slot, a trust line under primary CTAs, and a
# mobile sticky bottom bar — applied as a final pass over the finished DOM so
# it works identically across every design (native and reference) without
# hand-editing 13 different template files. ──
GUARANTEE_DAYS=60

def cta_texts(brand,category=''):
 cat=(category or '').lower()
 breathing=any(k in cat for k in ('respiratory','breath','lung','sinus','nasal','airway'))
 return {
  'header':f'Get {brand} →',
  'hero':'Yes, I Want Easier Breathing – Get Mine →' if breathing else 'Get Mine →',
  'mid':"See Today's Best Price →",
  'pack2':'Try 2 Bottles →','pack3':'Get My 3 Bottles + Free Shipping →',
  'pack6':'Claim 6 Bottles – Lowest Price Per Bottle →',
  'bonus':'Grab My Free Bonuses With This Order →',
  'afterReviews':'Join Customers Who Made It Part of Their Day →',
  'afterFaq':f'Still Thinking? Try It Risk-Free for {GUARANTEE_DAYS} Days →',
  'closing':f'Start Today – Order {brand} →',
 }

def cta_trust_line_html():
 return (f'<div class="auto-cta-trust">{GUARANTEE_DAYS}-Day Money-Back Guarantee '
         '&middot; Secure Checkout</div>')

_CTA_CSS=('.auto-cta-trust{display:block;text-align:center;font-size:.78rem;'
 'color:#6b7280;margin:8px 0 0;font-weight:500}'
 '.auto-sticky-cta{position:fixed;left:0;right:0;bottom:0;z-index:9999;display:none;'
 'background:#fff;padding:10px 16px;box-shadow:0 -6px 20px rgba(0,0,0,.15)}'
 '.auto-sticky-cta-btn{display:block;width:100%;box-sizing:border-box;text-align:center;'
 'color:#fff!important;font-weight:700;padding:14px 18px;border-radius:10px;'
 'text-decoration:none;min-height:48px;line-height:1.2}'
 '@media(max-width:640px){.auto-sticky-cta{display:block}body{padding-bottom:84px}}'
 '.btn,.nav-btn,a.btn,button.btn{min-height:48px;transition:transform .15s ease,box-shadow .15s ease}'
 '.btn:hover,a.btn:hover,button.btn:hover{transform:translateY(-2px);box-shadow:0 10px 24px rgba(0,0,0,.18)}')

def inject_cta_extras(soup,brand,affiliate):
 """Mobile sticky bottom CTA bar + shared button hover/tap-target CSS. Every
 native design (6,8-13) already ships its own working `.sticky-bar`, and so
 do reference designs 1 (.bpo-sticky), 5 (.ge-sticky) and 7 (.mv-sticky) —
 skip adding a second, competing one on any of those and only add it where
 none exists (reference designs 2, 3, 4; design 3's own "sticky-top" is
 just a sticky NAV header, not a bottom CTA bar, so it still gets one).
 Never touches the affiliate link's own rel/target attributes beyond what
 every other generated CTA already uses (nofollow sponsored noopener)."""
 if not soup.find(class_=re.compile(r'\bsticky-bar\b|\bbpo-sticky\b|\bge-sticky\b|\bmv-sticky\b|\bauto-sticky-cta\b')):
  bar=BeautifulSoup(
   f'<div class="auto-sticky-cta"><a class="auto-sticky-cta-btn" style="background:var(--primary,#2563EB)" '
   f'href="{html.escape(affiliate)}" target="_blank" rel="nofollow sponsored noopener">'
   f'Get {html.escape(brand)} – {GUARANTEE_DAYS}-Day Guarantee &rarr;</a></div>','html.parser')
  if soup.body:soup.body.append(bar)
 style=soup.new_tag('style');style.string=_CTA_CSS
 if soup.head:soup.head.append(style)

# ── External authority links (NIH Office of Dietary Supplements) — only for
# ingredient names that actually match this curated, individually-verified
# list (confirmed live at ods.od.nih.gov/factsheets/{slug}/ before being
# added here); anything that doesn't match gets no link at all rather than
# a guessed URL. ──
_INGREDIENT_AUTHORITY_LINKS={
 'vitamin a':'VitaminA-Consumer','vitamin c':'VitaminC-Consumer','ascorbic acid':'VitaminC-Consumer',
 'vitamin d':'VitaminD-Consumer','vitamin d3':'VitaminD-Consumer','cholecalciferol':'VitaminD-Consumer',
 'vitamin e':'VitaminE-Consumer','vitamin k':'VitaminK-Consumer',
 'vitamin b6':'VitaminB6-Consumer','vitamin b12':'VitaminB12-Consumer','cobalamin':'VitaminB12-Consumer',
 'folate':'Folate-Consumer','folic acid':'Folate-Consumer','biotin':'Biotin-Consumer',
 'calcium':'Calcium-Consumer','magnesium':'Magnesium-Consumer','zinc':'Zinc-Consumer',
 'iron':'Iron-Consumer','potassium':'Potassium-Consumer',
 'omega-3':'Omega3FattyAcids-Consumer','omega 3':'Omega3FattyAcids-Consumer','fish oil':'Omega3FattyAcids-Consumer',
}

def _match_ingredient_authority_links(ingredients,limit=3):
 """Up to `limit` (name, url) pairs for ingredients that match the curated
 list above — substring match on the ingredient's own name, longest key
 first so e.g. "vitamin b12" wins over a looser "vitamin" false match."""
 out=[]
 seen_urls=set()
 for ing in ingredients or []:
  name=str(ing.get('name','')).lower()
  if not name:continue
  for key in sorted(_INGREDIENT_AUTHORITY_LINKS,key=len,reverse=True):
   if key in name:
    slug=_INGREDIENT_AUTHORITY_LINKS[key]
    url=f'https://ods.od.nih.gov/factsheets/{slug}/'
    if url in seen_urls:break
    seen_urls.add(url)
    out.append((ing.get('name',''),url))
    break
  if len(out)>=limit:break
 return out

_EYEBROW_CLASS_RE=re.compile(r'eyebrow',re.I)

def _reuse_eyebrow_class(container):
 """An existing small-label/"eyebrow" element's class list (e.g. the
 "What Is VapoCept" / "Inside Every Capsule" tag above a section heading),
 reused for a new sub-heading instead of a plain, unstyled one."""
 el=container.find(class_=_EYEBROW_CLASS_RE) if container else None
 if not el:return []
 cls=el.get('class') or []
 if isinstance(cls,str):cls=cls.split()
 return [c for c in cls if c]

def ingredient_authority_links_html(links,eyebrow_classes=None):
 """`links` is the already-matched (name,url) list — the SAME list the
 References/Evidence section (when a design has one) also renders, so the
 two locations never independently compute and risk disagreeing: one
 compact per-ingredient mention here, the full list there."""
 if not links:return ''
 items=''.join(
  f'<li style="margin-bottom:4px"><a href="{html.escape(url)}" rel="noopener" target="_blank">'
  f'{html.escape(name)} — NIH Office of Dietary Supplements ↗</a></li>'
  for name,url in links)
 if eyebrow_classes:
  heading=f'<span class="{" ".join(eyebrow_classes)}">Sources &amp; Further Reading</span>'
 else:
  heading='<h4 style="margin:0 0 8px">Sources &amp; Further Reading</h4>'
 return (f'<div class="auto-authority-links" style="margin-top:32px;padding-top:16px;'
         f'border-top:1px solid #e5e7eb;font-size:.85rem">'
         f'{heading}<ul style="list-style:none;padding:0;margin-top:8px">{items}</ul></div>')

def ensure_core_faqs(data):
 """Append 3 AEO-recommended FAQ entries (safety, bottle duration, who
 should avoid it) when the AI's own FAQ list doesn't already cover them —
 reuses the existing FAQ accordion/JSON-LD rendering rather than adding any
 new page markup, so it works identically across every design."""
 brand=data.get('brand','')
 faqs=list(data.get('faqs') or [])
 existing=' '.join(f.get('q','').lower() for f in faqs)
 serving=data.get('serving_info',{}) or {}
 guarantee=data.get('guarantee_text') or f'{brand} is backed by a {GUARANTEE_DAYS}-day money-back guarantee.'
 n_ing=len(data.get('ingredients') or [])
 additions=[]
 if not any(w in existing for w in ('safe','safety')):
  additions.append({'q':f'Is {brand} safe?',
   'a':(f'{brand} is formulated with {n_ing} named ingredient{"s" if n_ing!=1 else ""} and is intended for healthy adults '
        f'following the label\'s serving directions. As with any supplement, check with a healthcare provider first if '
        f'you are pregnant, nursing, taking medication, or managing a medical condition.')})
 if not any(w in existing for w in ('how long','last','supply','duration')):
  per_bottle=serving.get('per_bottle','');daily=serving.get('daily_serving','')
  additions.append({'q':f'How long does one bottle of {brand} last?',
   'a':(f'Each bottle contains {per_bottle or "the serving count printed on the label"}, and the label calls for '
        f'{daily or "the listed serving"} per day — for most people that works out to roughly a month per bottle, '
        f'though actual use may vary.')})
 if not any(w in existing for w in ('avoid','skip','should not','contraindicat')):
  additions.append({'q':f'Who should avoid {brand}?',
   'a':(f'{brand} is not intended for children, and anyone pregnant, nursing, taking medication, or managing a medical '
        f'condition should talk to a healthcare provider before use. {guarantee}')})
 if additions:
  data['faqs']=faqs+additions
 return data

_PANEL_CLASS_RE=re.compile(r'callout|flag|info-box|notice|panel|alert',re.I)

def _section_wrap(sec):
 """The section's own inner content wrapper (.bpo-wrap/.ge-wrap/.wrap/...)
 — every design names it differently, but all of them put exactly one
 class containing "wrap" on it. Auto-inserted boxes belong INSIDE this,
 never as a sibling of the <section> itself (full body width, no padding,
 sticking to the left edge) and never even as a direct child of <section>
 outside the wrap (same problem — the wrap is what carries the centering/
 max-width/padding that makes content line up with everything else)."""
 if sec is None:return None
 # "wrap" covers every reference design (bpo-wrap/ge-wrap/mv-wrap/...) and
 # most native ones; design 13 uses Bootstrap's own ".container" instead.
 return sec.find(class_=re.compile(r'\bwrap\b|\bcontainer\b',re.I)) or sec

def _reuse_panel_class(container):
 """An existing callout/info-box element's class list within this
 container, so a new box can borrow the design's OWN panel styling
 (background/border/radius/padding/shadow) instead of inventing separate
 CSS that won't match the rest of the page."""
 el=container.find(class_=_PANEL_CLASS_RE) if container else None
 if not el:return []
 cls=el.get('class') or []
 if isinstance(cls,str):cls=cls.split()
 return [c for c in cls if c]

def _serving_per_day_label(serving_info):
 """'2 capsules' -> '2/day', '1-2 capsules' -> '1-2/day' — the short numeric
 form used in hero stat strips. Derived from the SAME serving_info.daily_serving
 value every other on-page serving mention (Quick Facts, FAQ, schema, blog)
 reads, instead of a separately hardcoded number that can silently disagree
 with it (e.g. a stat strip claiming "2/day" while Quick Facts says "1 capsule")."""
 ds=((serving_info or {}).get('daily_serving') or '1-2 capsules').strip()
 m=re.match(r'^\d+(?:\s*[-–]\s*\d+)?',ds)
 return (m.group().replace(' ','')+'/day') if m else ds

def quick_facts_html(data,panel_classes=None):
 """Home-page-only "Quick Facts" box — name/category/ingredient count/daily
 serving/guarantee/price range, all read straight from the same data used
 to build the rest of the page (and its JSON-LD), so nothing here can ever
 disagree with the visible content elsewhere. `panel_classes`, when given
 (an existing callout/info-box class found on the page), is reused as-is
 for the box's visual styling instead of a separate hardcoded look."""
 brand=data.get('brand','');category=data.get('category','')
 n_ing=len(data.get('ingredients',[]))
 serving=data.get('serving_info',{}).get('daily_serving','') or 'See label'
 pricing=data.get('pricing',[])
 prices=[]
 for p in pricing:
  try:
   v=float(re.sub(r'[^0-9.]','',str(p.get('price_per_bottle','')) or '0') or 0)
   if v:prices.append(v)
  except Exception:pass
 price_range=f'${min(prices):g}–${max(prices):g} per bottle' if prices else 'See pricing'
 rows=[('Product',brand),('Category',category),
       ('Ingredients',f'{n_ing} named ingredient{"s" if n_ing!=1 else ""}'),
       ('Daily Serving',serving),('Guarantee',f'{GUARANTEE_DAYS} days'),('Price Range',price_range)]
 items=''.join(f'<tr><th scope="row" style="text-align:left;padding:6px 12px 6px 0;color:#6b7280;'
               f'font-weight:600;white-space:nowrap">{html.escape(k)}</th>'
               f'<td style="padding:6px 0">{html.escape(str(v))}</td></tr>' for k,v in rows)
 cls_attr=' '+' '.join(panel_classes) if panel_classes else ''
 own_style='margin-top:32px' if panel_classes else ('margin-top:32px;padding:20px 24px;background:#f8fafc;'
           'border:1px solid #e5e7eb;border-radius:10px')
 return (f'<div class="auto-quick-facts{cls_attr}" style="{own_style}">'
         f'<h3 style="margin:0 0 12px">Quick Facts</h3>'
         f'<table style="width:100%;border-collapse:collapse;font-size:.92rem">{items}</table></div>')

def ensure_social_meta(soup,domain,images):
 """og:locale + twitter:image on every page — previously only ever set for
 the homepage/subpage metadata pass (rebuild_metadata/build_native_page's
 own og/twitter block), never for blog articles or legal pages, and
 og:locale was never set anywhere at all."""
 if not soup.find('meta',attrs={'property':'og:locale'}):
  set_or_add_meta(soup,'og:locale','en_US','property')
 twitter_img=_find_meta(soup,'twitter:image')
 if not twitter_img or not (twitter_img.get('content') or '').strip():
  og_img_tag=soup.find('meta',attrs={'property':'og:image'})
  img_url=og_img_tag.get('content') if og_img_tag else None
  if not img_url:
   og_imgs=seo_images(images) if images else []
   if og_imgs:img_url=current_domain_url(domain,og_imgs[0])
  if img_url:set_or_add_meta(soup,'twitter:image',img_url,'property')

# ── Favicon: a user-supplied favicon image (named "favicon.*", excluded from
# seo_images()/product-photo pools already) wins; otherwise a generated
# rounded-square brand-initial icon. Every scraped reference template (1-5,7)
# ships its own <link rel="icon"> pointing at the ORIGINAL site's favicon —
# apply_favicon_links() strips those (and any apple-touch-icon/mask-icon
# link) before inserting the generated set, so the old brand's icon is never
# linked (and unreferenced_images() then drops it from the zip on its own). ──
def generate_favicon_files(site,images,brand,primary_hex='#2563EB'):
 from PIL import Image,ImageDraw,ImageFont
 fav_src=next((p for p in images if Path(p).stem.lower()=='favicon'),None)
 base=None
 if fav_src:
  cand=Path(fav_src)
  if not cand.is_absolute():cand=site/fav_src
  if cand.exists():
   try:base=Image.open(cand).convert('RGBA')
   except Exception:base=None
 if base is not None:
  w,h=base.size
  if w!=h:
   m=min(w,h);left=(w-m)//2;top=(h-m)//2
   base=base.crop((left,top,left+m,top+m))
 else:
  size=512
  hexv=(primary_hex or '#2563EB').lstrip('#')
  if len(hexv)!=6:hexv='2563EB'
  bg=tuple(int(hexv[i:i+2],16) for i in (0,2,4))+(255,)
  base=Image.new('RGBA',(size,size),(0,0,0,0))
  d=ImageDraw.Draw(base)
  d.rounded_rectangle((0,0,size,size),radius=size*0.18,fill=bg)
  letter=(brand.strip()[:1] or '?').upper()
  font=None
  for f in ('DejaVuSans-Bold.ttf','arialbd.ttf','Arial Bold.ttf'):
   try:font=ImageFont.truetype(f,int(size*0.56));break
   except Exception:pass
  if font is None:font=ImageFont.load_default()
  bbox=d.textbbox((0,0),letter,font=font)
  tw=bbox[2]-bbox[0];th=bbox[3]-bbox[1]
  d.text(((size-tw)/2-bbox[0],(size-th)/2-bbox[1]),letter,font=font,fill=(255,255,255,255))
 base.resize((192,192),Image.LANCZOS).save(site/'icon-192.png')
 base.resize((512,512),Image.LANCZOS).save(site/'icon-512.png')
 # apple-touch-icon must be opaque. Converting a transparent icon straight to
 # RGB turns its transparent pixels BLACK (a round logo ended up on a black
 # square), so flatten it onto white first — the other sizes keep transparency.
 _flat=Image.new('RGBA',base.size,(255,255,255,255));_flat.alpha_composite(base)
 _flat.resize((180,180),Image.LANCZOS).convert('RGB').save(site/'apple-touch-icon.png')
 base.resize((32,32),Image.LANCZOS).save(site/'favicon-32.png')
 base.resize((16,16),Image.LANCZOS).save(site/'favicon-16.png')
 base.save(site/'favicon.ico',format='ICO',sizes=[(16,16),(32,32),(48,48)])

def apply_favicon_links(site,theme_color='#2563EB'):
 for p in site.rglob('*.html'):
  try:soup=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
  except Exception:continue
  if not soup.head:continue
  for tag in list(soup.head.find_all('link')):
   rel=tag.get('rel') or []
   if isinstance(rel,str):rel=[rel]
   if any('icon' in tok.lower() for tok in rel):tag.decompose()
  for tag in list(soup.head.find_all('meta',attrs={'name':'theme-color'})):tag.decompose()
  depth=len(p.relative_to(site).parts)-1
  prefix='../'*depth
  new_tags=BeautifulSoup(
   f'<link rel="icon" href="{prefix}favicon.ico" sizes="any">'
   f'<link rel="icon" type="image/png" sizes="32x32" href="{prefix}favicon-32.png">'
   f'<link rel="apple-touch-icon" href="{prefix}apple-touch-icon.png">'
   f'<meta name="theme-color" content="{theme_color}">','html.parser')
  soup.head.append(new_tags)
  p.write_text(str(soup),encoding='utf-8')

def generate_how_it_works_image(path,steps,brand,primary_hex='#2563EB'):
 """A clean, numbered-steps infographic built from this product's own real
 how_it_works data (title+text per step) — used only as a fallback when the
 publisher hasn't uploaded their own how-it-works.* image. Saved under that
 same slot name, so localize_images()/build_native_page() treat it exactly
 like a real upload — never the ORIGINAL scraped template's own mechanism
 graphic (see the wrong-brand-image-leak fix elsewhere in this file)."""
 from PIL import Image,ImageDraw,ImageFont
 steps=[s for s in (steps or []) if (s.get('title') or s.get('text'))][:4]
 if not steps:return False
 hexv=(primary_hex or '#2563EB').lstrip('#')
 if len(hexv)!=6:hexv='2563EB'
 primary=tuple(int(hexv[i:i+2],16) for i in (0,2,4))
 light=_lighten(primary,0.94)
 def font(px,bold=True):
  names=('DejaVuSans-Bold.ttf','arialbd.ttf','Arial Bold.ttf') if bold else ('DejaVuSans.ttf','arial.ttf','Arial.ttf')
  for f in names:
   try:return ImageFont.truetype(f,px)
   except Exception:pass
  return ImageFont.load_default()
 f_head=font(30,True);f_title=font(24,True);f_body=font(18,False)
 def wrap(draw,text,fnt,max_w):
  words=text.split();lines=[];cur=''
  for w in words:
   trial=(cur+' '+w).strip()
   if draw.textlength(trial,font=fnt)<=max_w:cur=trial
   else:
    if cur:lines.append(cur)
    cur=w
  if cur:lines.append(cur)
  return lines or ['']
 W=900;pad=40;circle_d=56;row_gap=26;head_h=70
 tmp=Image.new('RGB',(10,10));d=ImageDraw.Draw(tmp)
 text_w=W-pad*2-circle_d-24
 rows=[]
 for s in steps:
  tlines=wrap(d,s.get('title',''),f_title,text_w)
  blines=wrap(d,s.get('text',''),f_body,text_w)
  rows.append((tlines,blines,max(circle_d,len(tlines)*30+len(blines)*24+10)))
 total_h=head_h+sum(r[2] for r in rows)+row_gap*(len(rows)-1)+pad*2
 im=Image.new('RGB',(W,total_h),(255,255,255))
 d=ImageDraw.Draw(im)
 d.text((pad,pad-6),f'How {brand} Works',font=f_head,fill=primary)
 y=pad+head_h
 for i,(tlines,blines,rh) in enumerate(rows):
  d.ellipse((pad,y,pad+circle_d,y+circle_d),fill=primary)
  num=str(i+1)
  nb=d.textbbox((0,0),num,font=f_title);nw=nb[2]-nb[0];nh=nb[3]-nb[1]
  d.text((pad+circle_d/2-nw/2-nb[0],y+circle_d/2-nh/2-nb[1]),num,font=f_title,fill=(255,255,255))
  tx=pad+circle_d+24;ty=y
  for ln in tlines:d.text((tx,ty),ln,font=f_title,fill=(20,24,34));ty+=30
  for ln in blines:d.text((tx,ty),ln,font=f_body,fill=(90,98,115));ty+=24
  if i<len(rows)-1:
   d.line((pad+circle_d/2,y+circle_d,pad+circle_d/2,y+rh+row_gap),fill=light,width=3)
  y+=rh+row_gap
 im.save(path)
 return True

def _clean_total_value(v):
 """Strip a leading "Total:"/"Total" label the AI occasionally bakes into
 the pricing.total field itself despite the prompt's instructions — every
 template that displays this value already prepends its own "Total: "
 label, so an unstripped value here shows up on the page as literal
 "Total: Total: $158"."""
 return re.sub(r'(?i)^\s*total\s*:?\s*','',str(v))

def extract_brand_color(image_path):
 """Extract a vibrant dominant color from a product image (e.g. bottle label)
 for use as the theme's primary accent color. Returns (r,g,b) or None."""
 try:
  from PIL import Image
  import colorsys
  img=Image.open(image_path).convert('RGB')
  img.thumbnail((150,150))
  pixels=list(img.getdata())
  # Filter out near-white/near-black/near-gray pixels (backgrounds, shadows)
  vibrant=[]
  for r,g,b in pixels:
   mx,mn=max(r,g,b),min(r,g,b)
   sat=(mx-mn)
   brightness=(r+g+b)/3
   if sat>25 and 30<brightness<225:
    vibrant.append((r,g,b))
  if not vibrant:vibrant=pixels
  # Bucket by hue (30°-wide buckets) and average only the largest bucket,
  # rather than averaging every vibrant pixel directly — a photo commonly
  # has more than one distinct vibrant color (the bottle itself, a leaf/
  # herbal graphic, label text, a gold badge...), and averaging RGB across
  # genuinely different hues blends them into a color that may not appear
  # anywhere in the image at all (e.g. a purple bottle + green graphic
  # averaging toward an unrelated muddy hue) — bucketing first and picking
  # the most common one keeps the result anchored to one real, dominant hue.
  buckets={}
  for r,g,b in vibrant:
   h,_,_=colorsys.rgb_to_hsv(r/255,g/255,b/255)
   bucket=int(h*12)%12
   buckets.setdefault(bucket,[]).append((r,g,b))
  dominant=max(buckets.values(),key=len)
  n=len(dominant)
  r=sum(p[0] for p in dominant)//n
  g=sum(p[1] for p in dominant)//n
  b=sum(p[2] for p in dominant)//n
  return (r,g,b)
 except Exception:
  return None

def _rgb_to_hex(rgb):return '#%02x%02x%02x' % rgb

def _darken(rgb,factor=0.7):return tuple(max(0,int(c*factor)) for c in rgb)

def _lighten(rgb,factor=0.85):return tuple(min(255,int(c+(255-c)*factor)) for c in rgb)

def _relative_luminance(rgb):
 r,g,b=[c/255 for c in rgb]
 return 0.2126*r+0.7152*g+0.0722*b

def build_theme_palette(rgb):
 """Build a full color palette (primary, dark, light, text-on-primary) from one seed color."""
 if not rgb:rgb=(30,80,150)  # sensible default blue
 primary=rgb
 dark=_darken(rgb,0.55)
 light=_lighten(rgb,0.92)
 accent=_darken(rgb,0.8)
 on_primary='#ffffff' if _relative_luminance(rgb)<0.55 else '#12213a'
 return {
  'primary':_rgb_to_hex(primary),
  'primary_dark':_rgb_to_hex(dark),
  'primary_light':_rgb_to_hex(light),
  'accent':_rgb_to_hex(accent),
  'on_primary':on_primary,
 }

# ── Dynamic accent re-theming for designs 1-7 ──
# Designs 8/9/10 already auto-theme to the product's own color (see
# build_theme_palette above). Designs 1-7 are reskinned scraped templates —
# each one ships with its own hand-picked CSS custom properties (or, for
# design 6, a Tailwind config color object) controlling its accent/button
# color. Rather than repainting the whole page (which risks wrecking a
# design's own crafted contrast/dark-mode structure if the product photo's
# color is very different from the template's original palette), this only
# hue-rotates the ACCENT/BRAND-identity variables — buttons, CTAs, badges,
# highlight tints — by the same delta for every variable in a design, which
# preserves each design's internal color relationships (e.g. design 3's
# teal+amber contrast) while shifting them to align with the product photo.
# Structural colors (backgrounds, body text, borders) are deliberately left
# untouched for guaranteed readability.
# "canonical" maps the design-neutral names --primary/--primary-dark/--accent
# (used by shared, cross-design generated markup like the bonus section)
# onto whichever of this design's OWN var names plays that role — every
# design's palette already has a "main" hue and a complementary/darker one,
# just under different names.
DESIGN_ACCENT_VARS={
 '1':{'anchor':'copper','vars':{'copper':'#C1702E','copper-dk':'#98551F'},
      'canonical':{'primary':'copper','primary-dark':'copper-dk','accent':'copper'}},
 '2':{'anchor':'accent','vars':{'primary':'#2D1B4E','primary-light':'#3D2A66','accent':'#5B2E9E','accent-hover':'#4A2583','accent-light':'#7B4EC4','accent-bg':'#F6F1FC'},
      'canonical':{'primary':'primary','primary-dark':'accent-hover','accent':'accent'}},
 '3':{'anchor':'vc-teal','vars':{'vc-teal':'#2C82A4','vc-teal-l':'#5CBADC','vc-teal-d':'#1A5E7C','vc-amber':'#DA9838','vc-amber-l':'#F0C060','vc-amber-d':'#B07828'},
      'canonical':{'primary':'vc-teal','primary-dark':'vc-teal-d','accent':'vc-amber'}},
 '4':{'anchor':'coral','vars':{'coral':'#E8704A','coral-hover':'#C85A38','coral-pale':'#FDF2EE','mint':'#34A882','mint-light':'#4CC9A0','mint-pale':'#F0FBF7'},
      'canonical':{'primary':'coral','primary-dark':'coral-hover','accent':'mint'}},
 '5':{'anchor':'rose','vars':{'rose':'#D88A93','rose-dk':'#B5636D','gold':'#A67C3D','gold-dk':'#8A6528'},
      'canonical':{'primary':'rose','primary-dark':'rose-dk','accent':'gold'}},
 '7':{'anchor':'steel','vars':{'steel':'#E8A23D','steel-dk':'#B87A22','sage':'#F0C066'},
      'canonical':{'primary':'steel','primary-dark':'steel-dk','accent':'sage'}},
}
DESIGN6_ACCENT_VARS={'anchor':'primary','vars':{'primary':'#B0233F','primary-dark':'#8B1A33','gold':'#C6A15B'},
                     'canonical':{'primary':'primary','primary-dark':'primary-dark','accent':'gold'}}

def _hex_to_hsl(hexcolor):
 hx=hexcolor.lstrip('#')
 r,g,b=[int(hx[i:i+2],16)/255 for i in (0,2,4)]
 mx,mn=max(r,g,b),min(r,g,b)
 l=(mx+mn)/2
 if mx==mn:
  return 0.0,0.0,l
 d=mx-mn
 s=d/(2-mx-mn) if l>0.5 else d/(mx+mn)
 if mx==r:hue=((g-b)/d)%6
 elif mx==g:hue=(b-r)/d+2
 else:hue=(r-g)/d+4
 return hue*60,s,l

def _hsl_to_hex(h,s,l):
 h=h%360
 c=(1-abs(2*l-1))*s
 x=c*(1-abs((h/60)%2-1))
 m=l-c/2
 if h<60:r,g,b=c,x,0
 elif h<120:r,g,b=x,c,0
 elif h<180:r,g,b=0,c,x
 elif h<240:r,g,b=0,x,c
 elif h<300:r,g,b=x,0,c
 else:r,g,b=c,0,x
 r,g,b=(round((v+m)*255) for v in (r,g,b))
 return '#%02x%02x%02x'%(max(0,min(255,r)),max(0,min(255,g)),max(0,min(255,b)))

def _rotate_hex_hue(hexcolor,delta):
 h,s,l=_hex_to_hsl(hexcolor)
 return _hsl_to_hex(h+delta,s,l)

def _theme_delta(cfg,seed_rgb):
 """Hue shift (degrees) between the product's extracted color and this
 design's own current accent hue — None if the product photo's color is
 too close to gray/white/black to give a reliable hue to rotate toward."""
 if not seed_rgb:return None
 seed_hue,seed_s,seed_l=_hex_to_hsl(_rgb_to_hex(seed_rgb))
 if seed_s<0.12 or seed_l<0.08 or seed_l>0.93:return None
 anchor_hue,_,_=_hex_to_hsl(cfg['vars'][cfg['anchor']])
 return seed_hue-anchor_hue

def apply_dynamic_accent_theme(soup,design,images,site_root):
 """Re-tint a design's own accent/button colors toward the uploaded
 product photo's dominant color (no-op for designs that already self-theme
 — 8/9/10 — or ones with no defined accent palette). Regardless of whether
 a usable product photo is available to re-tint from, this always defines
 the canonical --primary/--primary-dark/--accent aliases (pointing at
 whichever of the design's own vars play that role, rotated if a re-tint
 happened, or the design's base palette otherwise) — shared, cross-design
 generated markup like the bonus section relies on these three names
 existing under every design's own native color scheme."""
 d=str(design)
 cfg=DESIGN6_ACCENT_VARS if d=='6' else DESIGN_ACCENT_VARS.get(d)
 if not cfg:return
 seed_rgb=None
 if images and site_root:
  seed_path=next((p for p in images if Path(p).stem.lower()=='hero'),None) or images[0]
  try:
   seed_rgb=extract_brand_color(Path(site_root)/seed_path)
  except Exception:
   seed_rgb=None
 delta=_theme_delta(cfg,seed_rgb)
 resolved=({name:_rotate_hex_hue(hexval,delta) for name,hexval in cfg['vars'].items()}
           if delta is not None else dict(cfg['vars']))
 if d=='6':
  if delta is not None:
   script=None
   for sc in soup.find_all('script'):
    if sc.string and 'tailwind.config' in sc.string:script=sc;break
   if script:
    text=str(script.string)
    for name,hexval in cfg['vars'].items():
     text=re.sub(re.escape(hexval),resolved[name],text,flags=re.I)
    script.string=text
  decls=''
 else:
  decls=''.join(f'--{name}:{hexval};' for name,hexval in resolved.items()) if delta is not None else ''
 canon_decls=''.join(f'--{alias}:{resolved.get(varname,"#000")};' for alias,varname in cfg.get('canonical',{}).items())
 style_tag=soup.new_tag('style')
 style_tag.string=f':root{{{decls}{canon_decls}}}'
 head=soup.find('head')
 if head:head.append(style_tag)

# A few designs' scraped source carries bespoke, seemingly hand-authored
# blocks (an "Is My Payment Safe?" panel, a "Scientifically Formulated"
# strip) whose inline style="" attributes hardcode the ORIGINAL brand's own
# hex values directly, instead of referencing that design's CSS custom
# properties — apply_dynamic_accent_theme() has nothing to rotate there, so
# these specific elements stay frozen at the scraped brand's color
# regardless of the product photo. Extra shades that appear in these blocks
# but aren't literally one of a design's own named vars (e.g. a gradient's
# lighter end-stop) are mapped to the closest existing canonical alias here.
_EXTRA_HEX_ALIASES={'2':{'#8B5EC8':'accent-light'}}

def dehardcode_inline_accent_colors(soup,design):
 """Rewrite literal occurrences of this design's own base palette hex
 inside inline style="" attributes to the matching var(--name,fallback)
 reference, so those elements follow the same product-photo re-tint as
 everything else on the page instead of staying stuck at the original
 scraped brand's fixed color."""
 d=str(design)
 cfg=DESIGN6_ACCENT_VARS if d=='6' else DESIGN_ACCENT_VARS.get(d)
 if not cfg:return
 canon_by_var={v:k for k,v in cfg.get('canonical',{}).items()}
 subs={}
 for varname,hexval in cfg['vars'].items():
  name=canon_by_var.get(varname,varname)
  subs[hexval.lower()]=f'var(--{name},{hexval})'
 for hexval,alias in _EXTRA_HEX_ALIASES.get(d,{}).items():
  subs.setdefault(hexval.lower(),f'var(--{alias},{hexval})')
 if not subs:return
 pattern=re.compile('|'.join(re.escape(h) for h in subs),re.I)
 for el in soup.find_all(style=True):
  style=el['style']
  new_style=pattern.sub(lambda m:subs[m.group(0).lower()],style)
  if new_style!=style:el['style']=new_style

# Accept whichever bottle-count naming a user actually types — the web
# form's on-screen hint says "1-bottles.jpg"/"3-bottles.jpg"/"6-bottles.jpg"
# while the slot-matching logic elsewhere keys off "bottle-N" — normalize to
# the canonical "bottle-N" form once, here, so every downstream consumer
# (localize_images, _get_product_img, MANUAL_SLOTS lookups) just works.
_SLOT_NAME_ALIASES={'1-bottle':'bottle-1','1-bottles':'bottle-1','bottle1':'bottle-1',
 '2-bottle':'bottle-2','2-bottles':'bottle-2','bottle2':'bottle-2',
 '3-bottle':'bottle-3','3-bottles':'bottle-3','bottle3':'bottle-3',
 '6-bottle':'bottle-6','6-bottles':'bottle-6','bottle6':'bottle-6',
 'reviewer1':'reviewer-1','reviewer2':'reviewer-2','reviewer3':'reviewer-3','reviewer4':'reviewer-4',
 'fda-badge':'badge-fda','fda-approved':'badge-fda','fda':'badge-fda',
 'gmp-badge':'badge-gmp','gmp-certified':'badge-gmp','gmp':'badge-gmp',
 'usa-badge':'badge-usa','made-in-usa':'badge-usa','usa':'badge-usa',
 'natural-badge':'badge-natural','all-natural':'badge-natural','all-natural-ingredients':'badge-natural','natural-ingredients':'badge-natural','natural':'badge-natural',
 'guarantee-seal':'guarantee','guarantee-badge':'guarantee','money-back':'guarantee','money-back-guarantee':'guarantee','60-days':'guarantee','60_days':'guarantee',
 'credit-card':'credit-cards','payment-methods':'credit-cards','cards':'credit-cards',
 'star-rating':'stars','5-star':'stars','rating':'stars',
 # Bare "payment" is ambiguous — could mean the payment-method icon strip
 # or an order/checkout-page screenshot — left unaliased so it doesn't
 # collide with either; use "credit-cards.png" or "checkout.png" explicitly.
 'description':'supplement-facts','supplement_facts':'supplement-facts'}

# Badge/guarantee/payment-icon slots carry small text (GMP CERTIFIED, FDA
# REGISTERED, card logos) that visibly blurs under lossy WebP compression at
# photo-appropriate quality levels — these get lossless WebP instead.
_TEXT_IMAGE_SLOTS={'badge-usa','badge-fda','badge-gmp','badge-natural','guarantee','credit-cards','stars'}

_IMG_EXTS=('.jpg','.jpeg','.png','.webp','.gif','.bmp','.tif','.tiff')

def _clean_img_stem(name):
 """Strip every trailing recognized image extension from a filename, not
 just the last one the way Path.stem/with_suffix() do — a name that
 already carries more than one (someone's local "hero.jpg.png", or a file
 that landed on disk as "hero.png.webp" from an earlier naming slip) needs
 all of them gone, or the leftover one ends up baked into what should be
 the bare stem. Shared by _to_webp() (so its output is always a clean
 "X.webp") and save_uploaded() (so its collision check predicts that same
 final name up front, before two differently-named uploads that converge
 on it silently overwrite each other on disk)."""
 name=Path(name).name
 while Path(name).suffix.lower() in _IMG_EXTS:
  new=Path(name).stem
  if new==name:break
  name=new
 return name

def _to_webp(path,quality=80,lossless=False):
 """Convert an already-saved image file to WebP in place (same directory,
 new extension) and delete the original, returning the new Path. Every
 downstream consumer (image lists, <img src>) reads the real file that ends
 up on disk, so this one conversion point is enough to make every generated
 site ship WebP instead of PNG/JPEG — no per-design template changes needed
 for the images that were already resolved dynamically (hero, bottle packs,
 reviewer photos, bonus images). Falls back to leaving the original file
 untouched if Pillow can't decode/encode it, rather than losing the upload.

 A file already named ".webp" is only trusted as a fast-path skip once its
 real, Pillow-decoded format is confirmed to actually be WebP — a bundled
 template asset saved under a ".webp" filename despite holding PNG/JPEG
 bytes, or a scraped source server that sends the wrong Content-Type for a
 ".webp"-named URL, would otherwise sail through unlabeled-but-wrong
 forever, since nothing downstream ever re-opens the file to check.

 The new name is built by stripping EVERY trailing recognized image
 extension, not just the last one via Path.with_suffix() (which only ever
 touches the final suffix) — an upload whose own original filename already
 carried two (e.g. someone's local "hero.jpg.png"), or a file that landed
 on disk as "hero.png.webp" from some earlier naming slip, would otherwise
 end up renamed to "hero.png.webp"/"hero.jpg.webp" instead of a clean
 "hero.webp". That leftover extension breaks every stem-based lookup
 downstream (Path(...).stem-keyed hero/bottle/badge slot detection,
 seo_images()/og:image/JSON-LD) since none of them expect a dot still
 sitting in what should be the bare stem."""
 path=Path(path)
 try:
  from PIL import Image
  img=Image.open(path)
  img.load()
  if path.suffix.lower()=='.webp' and img.format=='WEBP':
   return path
  if img.mode not in ('RGB','RGBA'):
   img=img.convert('RGBA' if img.mode in ('P','LA') and 'transparency' in img.info else 'RGB')
  dest=path.with_name(_clean_img_stem(path.name)+'.webp')
  save_kwargs={'lossless':True,'quality':100} if lossless else {'quality':quality}
  img.save(dest,'WEBP',**save_kwargs)
  if dest!=path:path.unlink()
  return dest
 except Exception:
  return path

def minify_css(text):
 """Single CSS-minification chokepoint for every design — the reference
 pipeline's external assets/css/*.css files (see _localize_one_asset) and
 the native pipeline's inline <style> block (see build_native_page) both
 go through this, so a new design never has to remember to wire this up
 separately. Falls back to the original text if minification ever throws
 on some unusual input, rather than losing the stylesheet."""
 try:return rcssmin.cssmin(text)
 except Exception:return text

def minify_js(text):
 """JS counterpart to minify_css — same two call sites, same fallback."""
 try:return rjsmin.jsmin(text)
 except Exception:return text

def save_uploaded(files,dest):
 out=[];dest.mkdir(parents=True,exist_ok=True);seen=set()
 for f in files:
  if not f or not f.filename:continue
  ext=Path(f.filename).suffix.lower()
  if ext not in {'.jpg','.jpeg','.png','.webp','.gif'}:continue
  stem=re.sub(r'[^a-zA-Z0-9._-]+','-',Path(f.filename).stem).strip('-').lower() or 'image'
  stem=_SLOT_NAME_ALIASES.get(stem,stem)
  # Collision-check the name _to_webp() below will actually end up
  # producing (it collapses every trailing image extension, not just this
  # upload's immediate one) — checking only the pre-conversion name missed
  # the case where two differently-named uploads in the same batch (e.g.
  # "hero.png" and someone's stray local "hero.jpg.png") converge on the
  # identical final "hero.webp", and the second one's conversion silently
  # overwrote the first's file on disk with no collision ever detected.
  use_stem=stem;final_name=_clean_img_stem(use_stem+ext)+'.webp';i=2
  while final_name in seen:
   use_stem=f'{stem}-{i}';final_name=_clean_img_stem(use_stem+ext)+'.webp';i+=1
  seen.add(final_name)
  name=use_stem+ext
  while (dest/name).exists():name=f'{use_stem}-{i}{ext}';i+=1
  f.save(dest/name)
  saved=_to_webp(dest/name,quality=80,lossless=stem in _TEXT_IMAGE_SLOTS)
  out.append('assets/images/'+saved.name)
 return out

def serp_images(product,key,num=20):
 if not key:return []
 try:
  out=[]
  queries=[f'"{product}" supplement bottle official',f'{product} bottle supplement',f'{product} official product']
  pwords=[w.lower() for w in re.findall(r'[a-zA-Z]+',product) if len(w)>2]
  for q in queries:
   try:
    r=requests.get('https://serpapi.com/search.json',params={'engine':'google_images','q':q,'api_key':key,'num':10},timeout=20)
    r.raise_for_status();d=r.json()
    for x in d.get('images_results',[]):
     title=(x.get('title') or '').lower()
     # Whole-word match, not a bare substring — a raw "w in title" check lets
     # a short product-name fragment match inside an unrelated word (and,
     # more importantly, matches keyword-stuffed titles from spun/aggregator
     # "reviews" pages that name-drop the product next to a generic stock
     # photo of some other product entirely). Whole-word matching alone
     # can't verify the photo is really this product — Google's title text
     # is the only signal available here — so a wrong image can still slip
     # through; treat auto-fetched images as a best-effort default, not a
     # verified match, and prefer manually-supplied photos when accuracy matters.
     if pwords and not any(re.search(r'\b'+re.escape(w)+r'\b',title) for w in pwords):continue
     u=x.get('original') or x.get('thumbnail')
     if u and u.startswith('http') and u not in out:out.append(u)
     if len(out)>=num:break
    if len(out)>=5:break
   except Exception:continue
  return out
 except Exception:return []

def download_images(urls,dest):
 dest.mkdir(parents=True,exist_ok=True);saved=[]
 for idx,u in enumerate(urls,1):
  try:
   r=requests.get(u,timeout=20,headers={'User-Agent':'Mozilla/5.0'},stream=True)
   if r.status_code!=200:continue
   ct=r.headers.get('content-type','').split(';')[0].lower()
   ext={'image/jpeg':'.jpg','image/png':'.png','image/webp':'.webp','image/gif':'.gif'}.get(ct)
   if not ext:continue
   data=b''.join(r.iter_content(65536))
   if len(data)<1500 or len(data)>3*1024*1024:continue
   digest=hashlib.sha1(data).hexdigest()[:10]
   p=dest/f'serp-{idx}-{digest}{ext}';p.write_bytes(data)
   webp_p=_to_webp(p,quality=80)
   saved.append('assets/images/'+webp_p.name)
  except Exception:continue
 return saved

def _extract_json(text):
 text=(text or '').strip()
 if text.startswith('```'):
  text=re.sub(r'^```(?:json)?\s*','',text,flags=re.I)
  text=re.sub(r'\s*```$','',text)
 try:return json.loads(text)
 except Exception:
  m=re.search(r'\{.*\}',text,re.S)
  if m:return json.loads(m.group(0))
  raise ValueError('Invalid JSON from AI provider.')

def _content_prompt(product,affiliate,domain,product_hint=''):
 schema_json=json.dumps(SCHEMA,ensure_ascii=False,separators=(',',':'))
 hint_block=''
 if product_hint.strip():
  hint_block=f"""
IMPORTANT — Publisher-provided product description (use this as ground truth, it overrides any assumption from the name alone):
"{product_hint.strip()}"
Base the category, ingredients, benefits and all content strictly on this description.
"""
 return f"""Create a factual content pack for an affiliate/product information website.
Product: {product}
Target domain: {domain}
Affiliate URL: {affiliate}
{hint_block}
CRITICAL: Generate content ONLY for "{product}". Do NOT use content from other products.
- Research "{product}" specifically — its actual ingredients, benefits, category and use case
- The product name alone can be misleading (e.g. a name mentioning wood/plants doesn't imply a digestive or dental product) — verify the actual category from search results or the publisher's description above before writing content
- If uncertain of the category from the name, prioritize the publisher-provided description block above
- Match the product category exactly to what "{product}" actually is; do not default to a generic "digestive health" or "gut wellness" framing unless that is confirmed

Use web research when available. Never invent prices, ingredients, guarantees, certifications, or reviewer identities/names tied to real people. Do not claim FDA approval unless explicitly verified. Use careful general wellness language; avoid disease treatment/cure claims.

For sample_reviews: write 3 short (15-25 word), DIFFERENT FROM EACH OTHER, plausible-sounding customer review sentences about using {product} day-to-day. Each must be genuinely distinct in wording, focus and tone (not variations of the same sentence). These are placeholder review text for the publisher to replace with real testimonials before launch — put that reminder in source_notes, NOT in reviews_note. reviews_note is rendered directly on the live public page under the reviews section, so it must be a short, generic, honest disclaimer only (e.g. "Individual experiences vary. These reflect personal opinions, not guaranteed outcomes.") — it must never tell site visitors that the reviews are placeholders, fictional, or unverified.

For reviewer_names: provide 3 common first names that match who would realistically buy/use {product} (e.g. if it's a men's product, use typical male first names; if women's, typical female first names; if unisex/general wellness, a natural mix).

For ingredients: the "ingredients" array MUST contain one entry PER INDIVIDUAL ingredient actually found in or associated with {product} specifically — never a single summary/grouped entry like "Botanical Blend (7 ingredients)". If {product} has N named ingredients according to your research, the array must have exactly N entries, each with that specific ingredient's own real name and its own description. Do not reuse example ingredient names from generic wellness categories — research and use the names that are actually associated with {product}. Never use generic placeholder names like "Botanical Ingredient 1" or "Ingredient A". Most supplement products have between 3 and 20 distinct ingredients — if your research suggests more than 20, you are likely over-splitting single ingredients into multiple entries (e.g. splitting "Vitamin B6" into separate rows for its form and dosage) or including non-ingredient filler/inactive items; consolidate to genuinely distinct active ingredients only.

For benefits: EVERY benefit MUST use "Title — Description" format (an em dash or hyphen surrounded by spaces separating the two halves — every entry needs both halves, never just a title alone). WRONG: "Supports digestive health". CORRECT: "Supports digestive health — helps break down food more efficiently." If the em-dash description is missing, the page will show generic repeated filler text instead of real content. The description half must be a real, specific claim grounded in {product}'s actual ingredients/category — never a generic filler line like "Supports your daily wellness routine" repeated across entries, and never hedged meta-commentary about uncertainty, alternate formulas or "if a different version ships" — commit to one confident description per benefit, the same way a real product page would.

For pricing: always provide a specific price_per_bottle and total value for each tier (e.g. price_per_bottle "$79", total "$158" — total is the bare dollar amount only, never prefixed with the word "Total:", since the page template already adds that label when it displays the value) based on typical pricing for this type of product if the exact current price cannot be verified — do not write vague text like "Check official page" in these numeric fields; note any uncertainty in source_notes instead.

For faqs: provide AT LEAST 8 question/answer pairs covering common buyer questions specific to {product} — what's in it, how it's used, timeline for results, safety/side effects, cost, guarantee, FDA status, and who should avoid it. Do not reuse questions from unrelated product categories. The cost/pricing FAQ answer MUST match the exact bottle-count tiers and per-bottle prices you provide in the `pricing` field below — never mention a "single bottle" or any bottle count that is not one of the `pricing` tiers.

For bonuses: this is a common industry practice — most supplement/wellness affiliate products sold via 3/6-bottle bundles DO include free bonus guides or digital extras. Check the official order page at {affiliate} directly — bonuses are typically listed right next to the 3/6-bottle package tiers there — in addition to searching "{product} bonus", "{product} free guide", "{product} bonuses included". If official/review sources mention specific bonus names, descriptions or values, include them (2-3 bonuses is typical). Only return an empty array if you genuinely find no evidence after searching — do not skip this research step just because the product name alone doesn't suggest bonuses. Never invent fake bonus names if none can be verified.

For pricing: research the ACTUAL package tiers this product is sold in (check the official order page). Most supplement brands sell in 2, 3, and 6-bottle bundles — a single "1 bottle" tier is uncommon and usually incorrect unless you have specifically verified the official page truly offers a 1-bottle option. If unsure, use 2/3/6 as the three tiers.

For serving_info: same spirit as pricing — give a specific, typical-for-category value in every field rather than leaving it vague. daily_serving and per_bottle must be internally consistent with each other and with any supply-length claims made elsewhere (e.g. a "60-day supply" bottle at 1 capsule/day implies "60 capsules" per bottle, not 30). Most simple named-ingredient capsule formulas list per-ingredient amounts on the label ("Yes, per label"); only use "Proprietary blend" for doses_published if that is genuinely typical for this specific category.

For seo.title: follow the proven high-CTR title style used by top-ranking supplement/affiliate pages. The brand name always leads (optionally with ™ or ®). After that, use ONE of these proven structures, varying which one you pick each time:
(a) Brand + "Official Website"/"Official Site" + separator (| or —) + a short category-benefit phrase — e.g. "MindTrex™ Official Site | Ingredients, Benefits & Reviews", "MindTrex® | Official Site | Cognitive Support Powder"
(b) Brand + separator + power-word benefit phrase with NO "Official" — e.g. "MindTrex - Unleash Peak Mental Performance, Focus & Memory Power"
(c) Brand + "Official Website"/"Official Site" as a middle clause between two pipes + product-form/category — e.g. "Mind Trex™ | Official Website | Brain Health Supplement"

CRITICAL — the benefit phrase must match THIS product's actual category, not a generic template. Pull real keywords people search for in that category:
- Cognitive/focus products → "Brain Health", "Memory & Focus Support", "Cognitive Support Powder/Capsules"
- Digestive/gut products → "Gut Health Support", "Digestive Wellness Formula", "Bloating & Regularity Relief"
- Weight loss/metabolism products → "Fat Burning Support", "Metabolism Booster", "Weight Loss Formula"
- Blood sugar products → "Blood Sugar Support", "Glucose Control Formula", "Healthy Blood Sugar Levels"
- Joint/mobility products → "Joint Pain Relief", "Mobility & Flexibility Support"
- (apply the same real-keyword logic to whatever category this product actually is)

Keep the full title under 65 characters. Mention the product form (capsules, powder, gummies, drops) when it fits naturally and you know it. Vary structure, separator (| vs —) and exact phrasing each time you generate — never repeat the same template mechanically.

For symptoms: list the real, specific problems/discomforts someone who needs {product} would recognize in themselves, grounded in its actual category — not a generic wellness checklist and never symptoms borrowed from a different category of product.

For whatis_callout, how_it_works_intro, pricing_note, guarantee_text, final_cta_text: write these fresh, in your own natural phrasing, specific to {product}'s actual ingredients/category. Do not reuse stock phrases like "combines its ingredients to work together" or "join thousands who have already added" — write like a different person wrote it each time.

IMPORTANT — VARY YOUR WRITING: if this exact product has been described before, do not reuse the same sentence structures, opening phrases, or paragraph order. Vary word choice, sentence length and which details you lead with, so that two content packs for the same product never read identically. Keep facts accurate but express them freshly.

Return ONLY one valid JSON object matching this schema exactly (no markdown, no commentary):
{schema_json}"""

def _call_anthropic(prompt,key):
 headers={'x-api-key':key,'anthropic-version':'2023-06-01','content-type':'application/json'}
 body={'model':os.getenv('ANTHROPIC_MODEL','claude-sonnet-4-6'),'max_tokens':4096,'messages':[{'role':'user','content':prompt}]}
 r=requests.post('https://api.anthropic.com/v1/messages',headers=headers,json=body,timeout=120)
 r.raise_for_status()
 return _extract_json(r.json()['content'][0]['text'])

def _openai_content(prompt,key):
 c=OpenAI(api_key=key)
 try:
  r=c.responses.create(model=os.getenv('OPENAI_MODEL','gpt-4o'),tools=[{'type':'web_search'}],input=prompt,text={'format':{'type':'json_schema','name':'site_content','strict':True,'schema':SCHEMA}},store=False)
  return json.loads(r.output_text)
 except Exception:
  r=c.chat.completions.create(model=os.getenv('OPENAI_MODEL','gpt-4o'),messages=[{'role':'system','content':'Factual product research writer. Output valid JSON only.'},{'role':'user','content':prompt}],response_format={'type':'json_object'},temperature=0.9)
  return _extract_json(r.choices[0].message.content)

def _deepseek_content(prompt,key):
 c=OpenAI(api_key=key,base_url=os.getenv('DEEPSEEK_BASE_URL','https://api.deepseek.com'))
 r=c.chat.completions.create(model=os.getenv('DEEPSEEK_MODEL','deepseek-chat'),messages=[{'role':'system','content':'Factual product research writer. Output valid JSON only.'},{'role':'user','content':prompt}],response_format={'type':'json_object'},temperature=0.9)
 return _extract_json(r.choices[0].message.content)

def _extract_bonuses_from_text(data):
 """If the AI wrote bonus names into description/tagline text but left the
 structured 'bonuses' array empty, parse them out directly — this is more
 reliable than hoping a retry call fills the field correctly."""
 if data.get('bonuses'):return data.get('bonuses')
 text=' '.join([str(data.get('description','')),str(data.get('tagline',''))])
 # Look for pattern like: "...guides: Name One, Name Two, and Name Three."
 m=re.search(r'(?:bonus(?:es)?|guides?|extras?)[^:.]{0,40}:\s*([A-Z][^.]{5,220})',text)
 if not m:return []
 chunk=m.group(1)
 # Split on commas / "and" while keeping Title Case phrases
 parts=re.split(r',\s*(?:and\s+)?|\s+and\s+',chunk)
 names=[]
 for p in parts:
  p=p.strip().strip('.').strip()
  # Must look like a title (starts capital, 2-6 words, no stray punctuation)
  if p and re.match(r'^[A-Z][A-Za-z0-9\'\-\s]{2,60}$',p) and 1<len(p.split())<=6:
   names.append(p)
 if not names:return []
 return [{'title':n,'description':f'A free digital bonus guide included with qualifying {data.get("brand","")} orders.'} for n in names[:3]]

_SPELLED_NUMBERS={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,
 'nine':9,'ten':10,'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,
 'sixteen':16,'seventeen':17,'eighteen':18,'nineteen':19,'twenty':20}

def _ingredients_look_weak(data):
 """Detect generic/placeholder ingredient names or count mismatch with description text."""
 ingredients=data.get('ingredients',[])
 if not ingredients:return True
 # A single entry standing in for a whole formula (e.g. "Botanical Vitality
 # Complex (7-herb blend)") is exactly the ungrouped-array violation the
 # prompt explicitly forbids — catch the "(N-herb/ingredient blend)"
 # giveaway pattern specifically, not just the older generic-placeholder
 # names, since this one reads like a real (if vague) ingredient name.
 generic_pattern=re.compile(r'\b(botanical ingredient \d|generic ingredient|ingredient [a-z]\b|ingredient #?\d+\s*\(|component \d+|blend \(\d+|\(\d+[- ](?:herb|ingredient|botanical)s?\s*blend\)|\bcomplex\s*\(\d+)',re.I)
 for ing in ingredients:
  name=str(ing.get('name',''))
  if generic_pattern.search(name):return True
 # Check if description/benefits mention a specific ingredient count that doesn't match array length
 desc_text=' '.join([str(data.get('description','')),' '.join(data.get('benefits',[]))])
 count_match=re.search(r'\b(\d+)\s*(?:named\s+)?(?:botanical|plant-based|active)?\s*ingredients?\b',desc_text,re.I)
 mentioned_count=None
 if count_match:
  mentioned_count=int(count_match.group(1))
 else:
  # The count is often spelled out in prose ("seven botanical
  # ingredients") rather than given as a digit — a purely numeric check
  # misses this entirely, letting a 1-entry array through unnoticed
  # alongside a description that plainly says otherwise.
  word_match=re.search(r'\b('+'|'.join(_SPELLED_NUMBERS)+r')\s+(?:named\s+)?(?:botanical|plant-based|active|herbal)?\s*(?:ingredients?|herbs?|botanicals?)\b',desc_text,re.I)
  if word_match:mentioned_count=_SPELLED_NUMBERS[word_match.group(1).lower()]
 if mentioned_count and mentioned_count>=4 and len(ingredients)<mentioned_count:return True
 return False

def _bonus_focused_prompt(product,affiliate='',product_hint=''):
 hint_line=f'\nPublisher-provided context: "{product_hint.strip()}"\nUse this directly if it already describes bonus offers.\n' if product_hint.strip() else ''
 link_line=(f'\nThe official order page for this exact product is: {affiliate}\n'
            f'Check that specific page directly (it typically lists any free bonuses next to the 3/6-bottle package tiers) '
            f'before falling back to a general web search.\n') if affiliate.strip() else ''
 return f"""Search specifically for "{product} bonus", "{product} free guide", "{product} bonuses included with order" and similar. Many supplement/wellness products sold in bulk (3 or 6-bottle) bundles include free digital bonus guides — check official product pages and reviews for this product specifically.
{link_line}{hint_line}
Return ONLY compact JSON, no markdown:
{{"bonuses":[{{"title":"exact bonus name if found","description":"what it covers, one sentence"}}]}}

If you find genuine evidence of bonus offers, list up to 3. If none can be found after searching, return {{"bonuses":[]}}. Do not invent bonus names."""

def _bonus_focused_call(product,provider,openai_key,deepseek_key,anthropic_key,affiliate='',product_hint=''):
 prompt=_bonus_focused_prompt(product,affiliate,product_hint)
 try:
  if provider in ('anthropic','auto') and anthropic_key:
   return _call_anthropic(prompt,anthropic_key)
 except Exception:pass
 try:
  if provider in ('openai','auto') and openai_key:
   return _openai_content(prompt,openai_key)
 except Exception:pass
 try:
  if provider in ('deepseek','auto') and deepseek_key:
   return _deepseek_content(prompt,deepseek_key)
 except Exception:pass
 return None

_IMG_MIME={'jpg':'image/jpeg','jpeg':'image/jpeg','png':'image/png','webp':'image/webp','gif':'image/gif'}

def _detect_photo_gender(image_path,openai_key='',anthropic_key=''):
 """Best-effort vision gender check for one reviewer photo, used so a
 review card's name can be generated to actually match who's in the
 photo instead of just trusting upload order. DeepSeek has no vision
 model available here, so only Anthropic/OpenAI are tried. Returns
 'male', 'female', or 'unclear' — 'unclear' covers no vision key
 configured, an unreadable image, or an ambiguous/failed API response,
 and callers must treat it as "do not risk a gendered name here", never
 as a coin-flip default."""
 try:
  img_bytes=Path(image_path).read_bytes()
 except Exception:
  return 'unclear'
 if len(img_bytes)<100:return 'unclear'
 b64=base64.b64encode(img_bytes).decode('ascii')
 mime=_IMG_MIME.get(Path(image_path).suffix.lower().lstrip('.'),'image/jpeg')
 prompt_text=('Look at this photo of a person. Reply with exactly one word — '
              '"male", "female", or "unclear" if the photo does not clearly show '
              'one person\'s apparent gender. No other text.')
 ans=''
 try:
  if anthropic_key:
   headers={'x-api-key':anthropic_key,'anthropic-version':'2023-06-01','content-type':'application/json'}
   body={'model':os.getenv('ANTHROPIC_MODEL','claude-sonnet-4-6'),'max_tokens':10,
         'messages':[{'role':'user','content':[
          {'type':'image','source':{'type':'base64','media_type':mime,'data':b64}},
          {'type':'text','text':prompt_text}]}]}
   r=requests.post('https://api.anthropic.com/v1/messages',headers=headers,json=body,timeout=30)
   r.raise_for_status()
   ans=r.json()['content'][0]['text'].strip().lower()
  elif openai_key:
   c=OpenAI(api_key=openai_key)
   r=c.chat.completions.create(
    model=os.getenv('OPENAI_VISION_MODEL','gpt-4o-mini'),
    messages=[{'role':'user','content':[
     {'type':'text','text':prompt_text},
     {'type':'image_url','image_url':{'url':f'data:{mime};base64,{b64}'}}]}],
    max_tokens=10,temperature=0)
   ans=(r.choices[0].message.content or '').strip().lower()
  else:
   return 'unclear'
 except Exception:
  return 'unclear'
 if 'female' in ans:return 'female'
 if 'male' in ans:return 'male'
 return 'unclear'

_NEUTRAL_US_REVIEWER_NAMES=['M. Johnson','C. Miller','A. Davis','J. Thompson','R. Anderson','T. Clark']

def _gendered_names_prompt(slot_genders,product):
 lines=[]
 for i,g in enumerate(slot_genders):
  slot=i+1
  if g=='male':
   lines.append(f'- Reviewer {slot}\'s photo is MALE — give a common MALE American first name (plus last initial, e.g. "Michael T.").')
  elif g=='female':
   lines.append(f'- Reviewer {slot}\'s photo is FEMALE — give a common FEMALE American first name (plus last initial, e.g. "Jennifer T.").')
  else:
   lines.append(f'- Reviewer {slot}\'s photo gender could not be reliably determined — give a gender-neutral name in the style "M. Johnson"/"C. Miller"/"A. Davis"/"J. Thompson" (first initial + common American surname) so it never reads as clearly male or female.')
 joined='\n'.join(lines)
 return f"""Generate exactly {len(slot_genders)} realistic customer review names for {product}, a product sold to US customers (the site uses US city/state locations like Seattle WA, Nashville TN, Las Vegas NV).

Each name MUST match the instruction for that exact slot, in order — this is critical, a mismatched name next to a real customer photo is not acceptable:
{joined}

Return ONLY compact JSON, no markdown: {{"reviewer_names":["name for slot 1","name for slot 2",...]}} — exactly {len(slot_genders)} names in slot order."""

def _reviewer_gender_match_call(product,slot_genders,provider,openai_key,deepseek_key,anthropic_key):
 """Text-only follow-up call (no vision needed here — _detect_photo_gender
 already did that) that asks the AI for names matching each slot's detected
 gender. Returns a list the same length as slot_genders, or None if every
 provider attempt failed (caller falls back to _NEUTRAL_US_REVIEWER_NAMES)."""
 prompt=_gendered_names_prompt(slot_genders,product)
 for fn,key in ((_call_anthropic,anthropic_key),(_openai_content,openai_key),(_deepseek_content,deepseek_key)):
  prov_name={_call_anthropic:'anthropic',_openai_content:'openai',_deepseek_content:'deepseek'}[fn]
  if provider not in (prov_name,'auto') or not key:continue
  try:
   result=fn(prompt,key)
   names=result.get('reviewer_names') if isinstance(result,dict) else None
   if isinstance(names,list) and len(names)>=len(slot_genders):
    return [str(n) for n in names[:len(slot_genders)]]
  except Exception:continue
 return None

def gender_match_reviewer_names(images,site_root,reviewer_names,product,provider='auto',openai_key='',deepseek_key='',anthropic_key=''):
 """Single shared step (both pipelines read data['reviewer_names'] the same
 way, so fixing it once here — before either build_native_page() or
 make_page()/page_variant() ever runs — covers all 13 designs with no
 per-design wiring needed): for every reviewer slot that actually has an
 uploaded photo, detect that photo's real gender and replace the AI's
 originally-generated name with one that matches it (or a gender-neutral
 US-style name if detection is unreliable). Slots with no uploaded photo
 keep their original name untouched — no photo is ever shown for those
 (see _get_reviewer_img/_initials_avatar_data_uri), so there is no
 mismatch risk to correct there."""
 reviewer_names=list(reviewer_names or [])
 n=max(len(reviewer_names),3)
 slots=[]  # (index, disk_path) for every slot that has a real uploaded photo
 for i in range(n):
  rel=_get_reviewer_img(images,i)
  if not rel:continue
  disk=Path(site_root)/rel if site_root else Path(rel)
  if disk.exists():slots.append((i,disk))
 if not slots:return reviewer_names
 genders=[_detect_photo_gender(disk,openai_key,anthropic_key) for _,disk in slots]
 matched=_reviewer_gender_match_call(product,genders,provider,openai_key,deepseek_key,anthropic_key)
 while len(reviewer_names)<n:reviewer_names.append(f'Verified Buyer {len(reviewer_names)+1}')
 for slot_pos,(i,_) in enumerate(slots):
  if matched and slot_pos<len(matched) and matched[slot_pos].strip():
   reviewer_names[i]=matched[slot_pos].strip()
  else:
   # Every provider attempt failed outright (no keys, or all calls errored)
   # — never leave the original, possibly wrong-gender name sitting next
   # to a real uploaded photo; fall back to a gender-neutral one instead.
   reviewer_names[i]=_NEUTRAL_US_REVIEWER_NAMES[i%len(_NEUTRAL_US_REVIEWER_NAMES)]
 return reviewer_names

def get_content(product,affiliate,domain,provider='auto',openai_key='',deepseek_key='',anthropic_key='',product_hint=''):
 prompt=_content_prompt(product,affiliate,domain,product_hint)
 provider=(provider or 'auto').lower()
 openai_key=(openai_key or os.getenv('OPENAI_API_KEY','')).strip()
 deepseek_key=(deepseek_key or os.getenv('DEEPSEEK_API_KEY','')).strip()
 anthropic_key=(anthropic_key or os.getenv('ANTHROPIC_API_KEY','')).strip()

 def _attempt():
  errors=[]
  if provider in ('anthropic','auto') and anthropic_key:
   try:return _call_anthropic(prompt,anthropic_key)
   except Exception as e:errors.append(f'Anthropic: {e}')
  if provider in ('openai','auto') and openai_key:
   try:return _openai_content(prompt,openai_key)
   except Exception as e:errors.append(f'OpenAI: {e}')
  if provider in ('deepseek','auto') and deepseek_key:
   try:return _deepseek_content(prompt,deepseek_key)
   except Exception as e:errors.append(f'DeepSeek: {e}')
  if not errors:errors.append('No API key provided.')
  raise RuntimeError('AI generation failed.\n- '+'\n- '.join(errors))

 result=_attempt()
 # If ingredients look generic/placeholder or count doesn't match, retry up to 2 more times
 for _ in range(2):
  if not _ingredients_look_weak(result):break
  try:
   retry=_attempt()
   if not _ingredients_look_weak(retry):result=retry;break
   if len(retry.get('ingredients',[]))>len(result.get('ingredients',[])):result=retry
  except Exception:break
 # Safety cap — if the AI over-split ingredients into an unreasonably long list
 # (a real product almost never has 25+ distinct active ingredients), trim to
 # the first 20 rather than shipping a broken-looking, oversized page.
 if len(result.get('ingredients',[]))>20:
  result['ingredients']=result['ingredients'][:20]
 # Final guarantee: sync any stated ingredient count in text fields to the ACTUAL
 # array length, so the page never claims a number that doesn't match what's shown.
 actual_count=len(result.get('ingredients',[]))
 if actual_count>0:
  count_pat=re.compile(r'\b\d+\s*(?:named\s+)?(botanical|plant-based|active)?\s*ingredients?\b',re.I)
  def _fix_count(txt):
   if not isinstance(txt,str):return txt
   def _repl(m):
    kind=(m.group(1)+' ' if m.group(1) else '')
    return f'{actual_count} {kind}ingredients' if actual_count!=1 else f'{actual_count} {kind}ingredient'
   return count_pat.sub(_repl,txt)
  result['description']=_fix_count(result.get('description',''))
  result['tagline']=_fix_count(result.get('tagline',''))
  result['benefits']=[_fix_count(b) for b in result.get('benefits',[])]
  if isinstance(result.get('seo'),dict):
   result['seo']['title']=_fix_count(result['seo'].get('title',''))
   result['seo']['description']=_fix_count(result['seo'].get('description',''))

 # If bonuses came back empty, first try extracting them directly from text
 # the AI already wrote (fast, free, and most reliable — the info is often
 # already there, just not placed in the structured field). Only fall back
 # to an extra API call if that fails too.
 if not result.get('bonuses'):
  extracted=_extract_bonuses_from_text(result)
  if extracted:
   result['bonuses']=extracted
 if not result.get('bonuses'):
  try:
   bonus_result=_bonus_focused_call(product,provider,openai_key,deepseek_key,anthropic_key,affiliate,product_hint)
   if bonus_result and bonus_result.get('bonuses'):
    result['bonuses']=bonus_result['bonuses'][:3]
  except Exception:pass

 # Guard against a bonus item that came back with a real title but a blank
 # description (seen from both the main call and _bonus_focused_call) —
 # unlike _extract_bonuses_from_text() above, neither of those paths
 # synthesizes fallback text, so an empty string here rendered as a visibly
 # blank paragraph under a real bonus heading on the page.
 brand_name=result.get('brand','')
 for b in result.get('bonuses',[]) or []:
  if isinstance(b,dict) and not str(b.get('description','')).strip():
   b['description']=f'A free digital bonus guide included with qualifying {brand_name} orders.'

 return result

def current_domain_url(domain,path=''):
 return domain.rstrip('/')+('/'+path.lstrip('/') if path else '/')

def set_or_add_meta(soup,key,value,kind='name'):
 # Twitter Card tags are specified with name=, never property= — og: tags
 # are the ones that need property=. A caller passing kind='property' for
 # convenience (looping og: and twitter: keys together) used to put BOTH
 # under property=, which most parsers tolerate but isn't spec-correct;
 # force twitter: keys to name= here regardless of what the caller passed.
 attr='name' if key.startswith('twitter:') else ('property' if kind=='property' else 'name')
 tag=soup.find('meta',attrs={attr:key})
 if not tag:tag=soup.new_tag('meta');tag[attr]=key;soup.head.append(tag)
 tag['content']=value

def _find_meta(soup,key):
 """Look up a meta tag the same way set_or_add_meta() would have written
 it — name= for twitter:, property= for everything else (og:, etc.) —
 so a caller updating an existing tag's content doesn't silently miss it
 by searching under the wrong attribute."""
 attr='name' if key.startswith('twitter:') else 'property'
 return soup.find('meta',attrs={attr:key})

def canonical_links(soup):
 out=[]
 for l in soup.find_all('link'):
  rel=l.get('rel') or []
  if isinstance(rel,str):rel=rel.split()
  if any(str(x).lower()=='canonical' for x in rel):out.append(l)
 return out

FOREIGN_VERIFICATION_META={'google-site-verification','msvalidate.01','yandex-verification',
 'p:domain_verify','facebook-domain-verification','norton-safeweb-site-verification','alexaverifyid'}

def rebuild_metadata(soup,data,canonical,images,domain):
 if not soup.head:soup.insert(0,soup.new_tag('head'))
 for m in soup.find_all('meta'):
  n=(m.get('name') or '').lower();p=(m.get('property') or '').lower()
  if n in {'description','keywords','author'} or n in FOREIGN_VERIFICATION_META or n.startswith('twitter:') or p.startswith('og:') or p.startswith('twitter:'):m.decompose()
 for l in list(soup.find_all('link')):
  rel=[x.lower() for x in (l.get('rel') or [])]
  if 'canonical' in rel or l.get('property','').lower().startswith('og:') or any(x in rel for x in ('icon','apple-touch-icon','manifest')):l.decompose()
 for sc in list(soup.find_all('script',type=lambda x:x and 'ld+json' in x)):sc.decompose()
 for sc in list(soup.find_all('script',src=lambda x:x and 'googletagmanager.com/gtag/js' in x)):
  nxt=sc.find_next_sibling('script')
  if nxt and not nxt.get('src') and nxt.string and 'gtag(' in nxt.string:nxt.decompose()
  sc.decompose()
 if soup.title:soup.title.string=data['seo']['title']
 else:
  t=soup.new_tag('title');t.string=data['seo']['title'];soup.head.append(t)
 set_or_add_meta(soup,'description',data['seo']['description'])
 set_or_add_meta(soup,'keywords',', '.join(data['seo'].get('keywords',[])))
 for p,v in [('og:title',data['seo']['title']),('og:description',data['seo']['description']),('og:url',canonical),('og:type','website'),('og:site_name',data['brand']),('twitter:card','summary_large_image'),('twitter:title',data['seo']['title']),('twitter:description',data['seo']['description'])]:
  set_or_add_meta(soup,p,v,'property')
 og_imgs=seo_images(images) if images else []
 if og_imgs:
  og_img=og_imgs[0]
  set_or_add_meta(soup,'og:image',current_domain_url(domain,og_img),'property')
  set_or_add_meta(soup,'twitter:image',current_domain_url(domain,og_img),'property')
 tracking=data.get('tracking') or {}
 if tracking.get('gsc_verify'):
  tag=soup.new_tag('meta');tag['name']='google-site-verification';tag['content']=tracking['gsc_verify'];soup.head.append(tag)
 if tracking.get('bing_verify'):
  tag=soup.new_tag('meta');tag['name']='msvalidate.01';tag['content']=tracking['bing_verify'];soup.head.append(tag)
 if tracking.get('ga_id'):
  ga_id=tracking['ga_id']
  s1=soup.new_tag('script',src=f'https://www.googletagmanager.com/gtag/js?id={ga_id}');s1['async']=True
  soup.head.append(s1)
  s2=soup.new_tag('script')
  s2.string=f"window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','{ga_id}');"
  soup.head.append(s2)
 for l in canonical_links(soup):l.decompose()
 c=soup.new_tag('link');c['rel']=['canonical'];c['href']=canonical;soup.head.append(c)

def _replace_brand_in_attrs(tag,brand):
 for attr in ('alt','title','aria-label','placeholder'):
  if not tag.has_attr(attr):continue
  v=str(tag[attr])
  for old in ALL_OLD_BRANDS:
   if old.lower() in v.lower():v=re.sub(re.escape(old),brand,v,flags=re.I)
  tag[attr]=v

# Template-specific phrases to clean up
TEMPLATE_SPECIFIC_PHRASES=[
 (r'Nitric Oxide[^<]{0,50}Blood Pressure','{brand} Product Guide'),
 (r'Independent Product Guide[^<]{0,80}Nitric Oxide[^<]{0,50}Blood Pressure','{brand} Independent Product Guide'),
 (r'Amino Acids Feed The Nitric[^<]{0,50}','{brand} Daily Formula'),
 (r'3-Ingredient Amino Acid Formula[^<]{0,50}','{brand} Formula'),
 (r'\d+-Ingredient Amino Acid[^<]{0,50}','{brand} Formula'),
 (r'Nitric Oxide: The Molecule[^<]{0,80}','How {brand} Works'),
 (r'Established physiology, not invented science','Evidence-Based Formula'),
 # Design 5/6 (Gelagen) were scraped from a skin/hair/nail beauty gummy
 # product — their "ge-strip" credibility banner and footer copyright line
 # hardcode that original product's own category words. Brand-name
 # substitution above only swaps "Gelagen" for the new brand, so every
 # generated site regardless of category (a digestive-health capsule, a
 # blood-pressure formula, etc.) still literally said "{Brand} Beauty Desk"
 # and "the {Brand} skin, hair and nail support gummies" — both false and
 # niche-inappropriate claims about the actual product being described.
 (r'\bBeauty Desk\b','Research Desk'),
 (r'skin,\s*hair\s*and\s*nail\s*support\s*gummies','supplement'),
]

def _fix_spaced_email_domains(s):
 """The old-brand word-boundary swap in replace_all_brand_refs() runs on
 plain body text, including a template's own hardcoded "support@oldbrand.com"
 line — it has no idea that particular occurrence sits inside an email
 address, so a multi-word new brand name ("Gut Save") lands in the domain
 verbatim and produces an invalid "support@Gut Save.com". Collapse any
 spaces found between the "@" and the ".tld" of what looks like an email
 address, after all brand substitution has already run."""
 return re.sub(r'@([A-Za-z0-9](?:[A-Za-z0-9 ]*[A-Za-z0-9])?)(\.[A-Za-z]{2,})\b',
               lambda m:'@'+re.sub(r'\s+','',m.group(1))+m.group(2),s)

def replace_all_brand_refs(soup,brand):
 """Replace old brand names + template-specific phrases everywhere."""
 # Text nodes
 for t in list(soup.find_all(string=True)):
  if not isinstance(t,NavigableString):continue
  # Comment IS-A NavigableString, so find_all(string=True) matches it too.
  # t.replace_with(plain_str) below would silently turn a hidden
  # <!-- SEO PLACEHOLDER FIELDS ... --> comment (which names the old
  # brand, e.g. "Gelagen") into a real, VISIBLE text node once the brand
  # name inside it gets swapped — leaking raw internal notes onto every
  # generated page. Comments carry no visible brand text to begin with,
  # so just leave them untouched.
  if isinstance(t,Comment):continue
  if t.parent.name in ('style','noscript'):continue
  s=str(t)
  # Inline scripts — replace brand but keep script intact
  if t.parent.name=='script':
   changed=False
   for old in ALL_OLD_BRANDS:
    new_s=re.sub(re.escape(old),brand,s,flags=re.I)
    if new_s!=s:s=new_s;changed=True
   new_s=_fix_spaced_email_domains(s)
   if new_s!=s:s=new_s;changed=True
   if changed:t.replace_with(s)
   continue
  for old in ALL_OLD_BRANDS:s=re.sub(r'\b'+re.escape(old)+r'\b',brand,s,flags=re.I)
  for old in OLD_REVIEWER_NAMES:s=s.replace(old,'Verified Buyer')
  # Clean template-specific phrases
  for pat,repl in TEMPLATE_SPECIFIC_PHRASES:
   s=re.sub(pat,repl.replace('{brand}',brand),s,flags=re.I)
  s=_fix_spaced_email_domains(s)
  if s!=str(t):t.replace_with(s)
 # id attributes (e.g. id="which-vapocept") can also carry the old brand
 # name baked into the slug — rename them and fix up any same-page
 # references (href="#which-vapocept", aria-controls, data-bs-target...)
 # so nothing points at a now-renamed id.
 id_renames={}
 for tag in soup.find_all(id=True):
  old_id=str(tag['id']);new_id=old_id
  for old in ALL_OLD_BRANDS:
   new_id=re.sub(re.escape(old.lower()),slugify(brand),new_id,flags=re.I)
  if new_id!=old_id:
   tag['id']=new_id;id_renames[old_id]=new_id
 if id_renames:
  for tag in soup.find_all(True):
   for attr in ('href','aria-controls','aria-labelledby','data-bs-target','data-bs-parent'):
    if not tag.has_attr(attr):continue
    v=str(tag[attr])
    frag=v[1:] if v.startswith('#') else v
    if frag in id_renames:
     tag[attr]=('#' if v.startswith('#') else '')+id_renames[frag]
 # Attributes on every tag
 for tag in soup.find_all(True):
  _replace_brand_in_attrs(tag,brand)
  for attr in ('href','src','content','value','data-src','data-href'):
   if not tag.has_attr(attr):continue
   v=str(tag[attr])
   if v.startswith(('http','/','.','#','data:')):continue
   # A path under assets/ is a reference to a file this generator already
   # wrote to disk under its ORIGINAL stem (e.g. "jellytide-made-in-usa.webp",
   # downloaded/copied by localize_reference_assets/localize_images before
   # this step runs) — renaming the brand token in the string here doesn't
   # rename the actual file, so the <img>/<link> ends up pointing at a
   # filename that was never created and 404s. Only text content (not our
   # own generated local paths) should get the brand swap.
   if v.startswith('assets/'):continue
   for old in ALL_OLD_BRANDS:
    if old.lower() in v.lower():v=re.sub(re.escape(old),brand,v,flags=re.I)
   tag[attr]=v

def sanitize_urls(soup,old_domains,new_domain,affiliate):
 ods=[d.lower() for d in old_domains]
 replace_domains=['mwebtracepoint.com','mwebauditly.com','alikoo.com']
 for tag in soup.find_all(True):
  for attr in ('href','src','action','poster','data-src','data-href'):
   if not tag.has_attr(attr):continue
   v=str(tag[attr])
   vl=v.lower()
   for od in ods:
    if od in vl:
     if any(rd in od for rd in replace_domains):
      v=re.sub(r'https?://(?:www\.)?'+re.escape(od)+r'[^\s"\']*',affiliate,v,flags=re.I)
     else:
      v=re.sub(r'https?://(?:www\.)?'+re.escape(od),new_domain.rstrip('/'),v,flags=re.I)
   tag[attr]=v

def rebase_relative_assets(soup,prefix):
 """Every generated page except blog/index.html sits at the site root, so
 "assets/css/..."-style relative paths (no leading slash, no domain) resolve
 correctly there. blog/index.html is one directory deeper — the exact same
 relative paths would then resolve to a nonexistent "blog/assets/..." and
 404 for every stylesheet, script and inline image (e.g. a header trust-badge
 strip) that isn't already using the appropriate full https://domain URL.
 Called only for that nested page, to prepend the '../' needed to reach the
 real assets/ folder one level up."""
 for tag in soup.find_all(True):
  for attr in ('src','href','poster','data-src'):
   if tag.has_attr(attr) and str(tag[attr]).startswith('assets/'):
    tag[attr]=prefix+str(tag[attr])
  if tag.has_attr('style') and 'assets/' in tag['style']:
   tag['style']=re.sub(r'url\((["\']?)assets/',lambda m:f'url({m.group(1)}{prefix}assets/',tag['style'])

def rebase_internal_page_links(soup,prefix):
 """Same problem as rebase_relative_assets() above, but for the nav/footer's
 own <a href="about.html">-style page links instead of assets — those are
 root-relative filenames literally baked into the design templates (e.g.
 design-13.source.md's nav: href="how-it-works.html", href="ingredients.html",
 footer: href="terms.html", href="contact.html", plus the logo's own
 href="index.html"). They resolve fine on every normal page, which all sit at
 the site root, but blog/index.html sits one directory deeper — the exact
 same links then resolve to nonexistent pages like "blog/about.html" and 404.
 Called only for that nested page, to prepend the '../' needed to reach the
 real page one level up. External links, in-page "#anchor" links, mailto:/tel:
 links and asset paths (already handled by rebase_relative_assets) are left
 untouched."""
 for a in soup.find_all('a',href=True):
  href=str(a['href']).strip()
  if not href or href.startswith(('http://','https://','//','#','mailto:','tel:','javascript:','assets/',prefix)):
   continue
  a['href']=prefix+href

def sanitize_text_domains(soup,old_domains,new_domain):
 """sanitize_urls() only rewrites href/src/etc. attributes. A scraped page's
 own body copy can also name its old domain directly as plain text — a
 shipping-policy paragraph mentioning "support@getgelagen.com", or a
 tracking URL like "https://alikoo.com/DMthegelagen.com/" pasted into a
 disclaimer. replace_all_brand_refs()'s word-boundary brand-name swap never
 catches these, since the old brand there is embedded as a bare substring
 with no word boundary around it (getgelagen.com, thegelagen.com) — clean
 them up here as plain text instead."""
 ods=[d for d in old_domains if d]
 if not ods:return
 new_host=re.sub(r'^https?://(?:www\.)?','',new_domain.rstrip('/')).rstrip('/')
 pattern=re.compile('|'.join(re.escape(d) for d in ods),re.I)
 for t in list(soup.find_all(string=True)):
  if not isinstance(t,NavigableString):continue
  if isinstance(t,Comment):continue  # don't unwrap a comment into visible text
  if t.parent.name in ('style','script','noscript'):continue
  s=str(t)
  new_s=pattern.sub(new_host,s)
  if new_s!=s:t.replace_with(new_s)

def strip_old_product_images(soup,old_domains,design='1'):
 ods=[d.lower() for d in old_domains]
 for img in soup.find_all('img'):
  isrc=str(img.get('src','')).lower()
  if not any(d in isrc for d in ods):continue
  # Decode URL-encoded filename
  raw_fname=isrc.split('/')[-1].split('?')[0]
  try:fname=unquote(raw_fname).lower()
  except Exception:fname=raw_fname.lower()
  stem=Path(fname).stem.lower()
  img['data-orig-stem']=stem
  img['data-download-url']=img.get('src','')
  img['src']=''
  if img.has_attr('srcset'):del img['srcset']

def _build_token(site_root):
 """Short per-generation token so asset filenames/content differ on every
 build — avoids every generated site sharing byte-identical CSS/JS fingerprints."""
 return hashlib.sha1(str(site_root).encode('utf-8')).hexdigest()[:8]

def _localize_one_asset(href,dest_dir,design,kind,bundled_dir,token,target_rgb=None):
 """Resolve one CSS/JS asset: prefer a locally bundled copy (fast, works
 offline, never breaks if the original scraped site goes down); fall back to
 fetching it live only when no bundled copy exists. Returns
 (new relative src/href or None, original un-retouched CSS text or None) —
 for kind='css' with a target_rgb, the file actually written to disk has
 the template's own brand-colour family hue-rotated toward the product
 photo's colour first (class-level rules in the stylesheet itself are
 otherwise never touched by the :root CSS-variable theming layer); the
 original text is still returned so the caller can later hue-rotate the
 handful of literal hex colors baked into the final HTML's own inline
 style="" attributes using the same base-hue detection."""
 basename=Path(urlparse(href).path).name or ('style.css' if kind=='css' else 'script.js')
 stem,ext=os.path.splitext(basename)
 if not ext:ext='.css' if kind=='css' else '.js'
 name=f'ref-{design}-{stem}-{token}{ext}'
 bundled=(bundled_dir/kind/basename) if bundled_dir else None
 comment=f'/* build:{token} */\n' if kind=='css' else f'/* build:{token} */\n'
 try:
  if bundled and bundled.exists():
   content=bundled.read_bytes()
  else:
   r=requests.get(href,timeout=20,headers={'User-Agent':'Mozilla/5.0'});r.raise_for_status()
   content=r.content
  original_text=None
  if kind=='css':
   original_text=content.decode('utf-8',errors='ignore')
   css_text=retheme_reference_css(original_text,target_rgb) if target_rgb else original_text
   content=minify_css(css_text).encode('utf-8')
  else:
   content=minify_js(content.decode('utf-8',errors='ignore')).encode('utf-8')
  (dest_dir/name).write_bytes(comment.encode('utf-8')+content)
  return f'assets/{kind}/{name}',original_text
 except Exception:
  return None,None

def _get_reviewer_img(images,i):
 """Single shared lookup (native + reference pipelines both use this) for
 slot i's reviewer photo: only an actual uploaded reviewer-N image counts —
 never a random product/SERP photo or an original scraped template photo,
 either of which guarantees a gender/identity mismatch with the AI-
 generated reviewer name. Returns None when no matching upload exists, so
 callers fall back to a neutral avatar (_initials_avatar_data_uri) instead
 of risking a mismatch."""
 slot=f'reviewer-{i+1}'
 for p in (images or []):
  if Path(p).stem.lower() in (slot,f'reviewer{i+1}',f'reviewer_{i+1}'):return safe_rel(p)
 # Custom-named uploads ("vapocept-customer-1", "testimonial_2") are
 # reviewer photos too: a trailing number claims that slot; un-numbered ones
 # fill slots in upload order, but only when no numbered ones exist (so the
 # two schemes never hand the same photo to two slots).
 custom=[(reviewer_photo_slot(p),p) for p in (images or [])]
 custom=[(n,p) for n,p in custom if n is not None]
 for n,p in custom:
  if n==i+1:return safe_rel(p)
 unnumbered=[p for n,p in custom if n==0]
 if unnumbered and not any(n for n,_ in custom) and i<len(unnumbered):return safe_rel(unnumbered[i])
 return None

def _initials_avatar_data_uri(name):
 """Shared reviewer-photo fallback for every reference design (1-5,7) and
 the native pipeline: a neutral initials avatar with no depicted gender,
 used whenever no gender-matched reviewer photo was uploaded for a slot.
 The alternative — keeping an original scraped template's own reviewer
 photo (a real, specifically-gendered person) next to a freshly AI-
 generated name with no relation to that photo — is what produced the
 reported "Melissa" shown with an elderly man's photo. An unverified photo
 is never worth the mismatch risk, so this is the only fallback used."""
 initials=''.join(w[:1] for w in re.split(r'\s+',(name or '').strip()) if w)[:2].upper() or '?'
 hues=('#6b7280','#64748b','#78716c','#737373','#6d6875','#5b6472')
 bg=hues[sum(ord(c) for c in initials)%len(hues)]
 svg=(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 96 96">'
      f'<rect width="96" height="96" rx="48" fill="{bg}"/>'
      f'<text x="48" y="48" font-family="Arial,Helvetica,sans-serif" font-size="36" '
      f'font-weight="700" fill="#ffffff" text-anchor="middle" dominant-baseline="central">{html.escape(initials)}</text></svg>')
 return 'data:image/svg+xml;base64,'+base64.b64encode(svg.encode('utf-8')).decode('ascii')

def _keep_role(stem):
 """Map a 'keep'-classified image's ORIGINAL scraped stem to the generic
 slot name a publisher would use to manually override it (matching the
 MANUAL_SLOTS keys above) — e.g. "jellytide-fda-approved" and
 "breathizen-guarantee" both describe the same kind of asset (an FDA badge,
 a guarantee seal) despite every design/scrape naming it differently."""
 s=stem.lower()
 # A stem naming an actual bottle count is real packaging photography (e.g.
 # design 4's "breathizen-6-bottles-guarantee") — never treat that as a
 # generic guarantee-seal/badge slot just because it also contains one of
 # those words; it belongs to the bottle-count photo slots instead.
 if _BOTTLE_PHOTO_PAT.search(s):return None
 if any(x in s for x in ('how-it-works','how_it_works','howitworks','how-it-work')):return 'how-it-works'
 # "member-N" (designs 5 and 7's own scraped stem for this exact slot) is
 # just that scraped template's word for the same reviewer-headshot photo —
 # without matching it here, a manually uploaded reviewer-N.png was never
 # even checked, so this fell straight through to a live download of the
 # ORIGINAL scraped product's own real customer photo from its old domain.
 m=re.search(r'review(?:er)?[-_]?(\d)|member[-_]?(\d)',s)
 if m:return f'reviewer-{m.group(1) or m.group(2)}'
 if 'fda' in s:return 'badge-fda'
 if 'gmp' in s:return 'badge-gmp'
 if 'natural' in s:return 'badge-natural'
 if 'usa' in s:return 'badge-usa'
 # 'gurantee' (missing the 'a') is how design 3's own scraped asset is
 # actually spelled ("money-back-gurantee") — matching only the correct
 # spelling meant this branch silently never fired for it, so a manual
 # guarantee-image upload was never checked and the bundled VapoCept
 # asset always won by default.
 if 'guarantee' in s or 'gurantee' in s or 'money-back' in s or 'money_back' in s or 'moneyback' in s or re.search(r'\b60[-_]?days?\b',s):return 'guarantee'
 if 'credit' in s or 'card' in s:return 'credit-cards'
 if re.search(r'\bstars?\b',s):return 'stars'
 # A checkout-page screenshot or a supplement-facts/dosage-label graphic
 # (design 2's jellytide_checkout.webp, jellytide_description.webp; design
 # 4's breathizen-payment.webp) has no safe generic substitute — treat it
 # as its own single-purpose slot: use an exact manual upload if one
 # exists, otherwise remove it rather than filling it with an unrelated
 # image (see localize_images' role-aware fallback).
 # Design 4's own scraped "order page" screenshot slot is literally named
 # "breathizen-order-page" — no "checkout"/"payment" substring at all —
 # so without this it fell straight through to the generic product-photo
 # fallback (once no longer misclassified as a hero-slot alias above).
 if 'checkout' in s or 'payment' in s or 'order-page' in s or 'order_page' in s or 'orderpage' in s:return 'checkout'
 if 'description' in s or 'supplement' in s or 'facts' in s or 'dosage' in s or 'label' in s:return 'supplement-facts'
 return None

def localize_reference_assets(soup,site_root,design,old_domains,brand='',images=None,reviewer_names=None):
 """Returns (target_rgb, base_css_text) so the caller can later apply
 retheme_html_inline() to the final serialized HTML — target_rgb is the
 color extracted from the product photo (None if no usable photo/hero was
 provided), base_css_text is the ORIGINAL un-retouched stylesheet text (used
 only to detect the template's own base accent hue to rotate away from)."""
 reviewer_names=reviewer_names or []
 cssdir=site_root/'assets/css';jsdir=site_root/'assets/js';imgdir=site_root/'assets/images'
 cssdir.mkdir(parents=True,exist_ok=True);jsdir.mkdir(parents=True,exist_ok=True);imgdir.mkdir(parents=True,exist_ok=True)
 ods=[d.lower() for d in old_domains]
 bundled_dir=BUNDLED_ASSETS_DIR/f'design-{design}'
 token=_build_token(site_root)
 target_rgb=None
 if images and site_root:
  seed_path=next((p for p in images if Path(p).stem.lower()=='hero'),None) or images[0]
  try:target_rgb=extract_brand_color(Path(site_root)/seed_path)
  except Exception:target_rgb=None
 base_css_text=None
 for tag in list(soup.find_all('link',href=True)):
  href=str(tag['href']);host=urlparse(href).netloc.lower()
  if host and any(d in host for d in ods) and 'stylesheet' in [x.lower() for x in (tag.get('rel') or [])]:
   new_href,css_text=_localize_one_asset(href,cssdir,design,'css',bundled_dir,token,target_rgb)
   if css_text and base_css_text is None:base_css_text=css_text
   if new_href:tag['href']=new_href
   else:tag.decompose()
 for tag in list(soup.find_all('script',src=True)):
  href=str(tag['src']);host=urlparse(href).netloc.lower()
  if host and any(d in host for d in ods):
   new_src,_=_localize_one_asset(href,jsdir,design,'js',bundled_dir,token)
   if new_src:tag['src']=new_src
   else:tag.decompose()
 # Download keep images (badges, reviews, guarantee etc)
 bundled_dir=BUNDLED_ASSETS_DIR/f'design-{design}'
 for img in soup.find_all('img'):
  stem=img.get('data-orig-stem','')
  if not stem:continue
  cls=_classify(stem,design)
  if cls!='keep':continue
  # The stem used to LOOK UP a source file/URL must stay the original
  # scraped name (that's what's bundled/hosted under) — but the name we
  # actually SAVE it as should carry the new brand, not the old one, so
  # the ZIP a publisher downloads doesn't have the previous product's
  # name baked into its own asset filenames.
  save_stem=stem
  if brand:
   for old in ALL_OLD_BRANDS:
    save_stem=re.sub(re.escape(old.lower()),slugify(brand),save_stem,flags=re.I)
  # Manual-upload override — a publisher who uploaded their own badge/
  # guarantee-seal/reviewer-photo/etc. expects THAT to appear, not the
  # original scraped product's version. save_uploaded() already wrote any
  # matching upload straight into this site's assets/images/ under its
  # canonical slot name (e.g. "badge-fda.png") before this function runs,
  # so it's enough to check whether a file with that name exists here.
  role=_keep_role(stem)
  if role=='badge-fda':
   # Supplements are never FDA "approved" — the scraped template's own badge
   # (and, potentially, a publisher's manually uploaded replacement) can say
   # otherwise. Generate the compliant "FDA REGISTERED FACILITY" badge here
   # unconditionally, every generate, ahead of the manual-upload check and
   # the bundled/downloaded fallbacks below, so it always wins regardless of
   # what else exists for this slot.
   try:
    make_fda_registered_badge(imgdir/'badge-fda.webp')
    img['src']='assets/images/badge-fda.webp'
    img.attrs.pop('data-orig-stem',None);img.attrs.pop('data-download-url',None)
    continue
   except Exception:pass
  if role:
   found=False
   for ext2 in ('.jpg','.jpeg','.png','.webp','.gif'):
    cand=imgdir/(role+ext2)
    if cand.exists():
     img['src']=f'assets/images/{role+ext2}'
     img.attrs.pop('data-orig-stem',None);img.attrs.pop('data-download-url',None)
     found=True;break
   if found:continue
  # No manually-uploaded, gender-matched photo for this reviewer slot —
  # never fall through to the bundled/downloaded branches below for a
  # reviewer-N role, since those would pull in the ORIGINAL scraped
  # template's own photo of a real, specifically-gendered person who has
  # no connection to the freshly AI-generated reviewer name now sitting
  # next to it (the exact "Melissa" + elderly-man-photo bug). Use a
  # neutral initials avatar instead — see _initials_avatar_data_uri.
  if role and role.startswith('reviewer-'):
   try:idx=int(role.split('-',1)[1])-1
   except Exception:idx=-1
   rname=reviewer_names[idx] if 0<=idx<len(reviewer_names) else ''
   img['src']=_initials_avatar_data_uri(rname)
   img.attrs.pop('data-orig-stem',None);img.attrs.pop('data-download-url',None)
   continue
  # ── Bundled assets first (no internet needed) ──
  # Small chrome graphics (badges, guarantee seals, star-rating icons) carry
  # text/fine detail that visibly blurs under lossy compression; only the
  # large full-page screenshots (checkout, supplement-facts label) get lossy
  # compression instead, since lossless would bloat those far more than it's
  # worth.
  keep_lossless=role not in ('checkout','supplement-facts')
  bundled_found=False
  if bundled_dir.exists():
   for ext2 in ('.png','.webp','.jpg','.jpeg'):
    cand=bundled_dir/(stem+ext2)
    if cand.exists():
     import shutil as _sh
     dest=imgdir/(save_stem+ext2)
     _sh.copy2(str(cand),str(dest))
     webp_dest=_to_webp(dest,quality=90,lossless=keep_lossless)
     img['src']=f'assets/images/{webp_dest.name}'
     img.attrs.pop('data-orig-stem',None);img.attrs.pop('data-download-url',None)
     bundled_found=True;break
  if bundled_found:continue
  # Download from original domain
  dl_url=img.get('data-download-url','')
  if not dl_url:
   # Try common extensions
   for od in old_domains:
    dl_url=f'https://{od}/assets/images/{stem}.webp'
    break
  # Try download with multiple extensions
  downloaded=False
  urls_to_try=[dl_url]
  # Add alternate extensions
  base_url=dl_url.rsplit('.',1)[0] if '.' in dl_url.split('/')[-1] else dl_url
  for ext2 in ('.webp','.png','.jpg','.jpeg','.gif'):
   alt=base_url+ext2
   if alt not in urls_to_try:urls_to_try.append(alt)
  for try_url in urls_to_try:
   try:
    r=requests.get(try_url,timeout=12,headers={'User-Agent':'Mozilla/5.0'})
    if r.status_code==200 and len(r.content)>500:
     # Trust the real Content-Type over the URL's own extension (or lack of
     # one) — guessing ".webp" whenever the URL has no suffix, as this used
     # to do, mislabeled non-WebP bytes as WebP without ever re-encoding
     # them, so a JPEG/PNG the source server returned ended up shipped
     # under a ".webp" filename with its original (non-WebP) bytes intact.
     # A non-".webp" placeholder here guarantees _to_webp() below always
     # actually inspects and (re-)encodes the real bytes.
     ct=r.headers.get('content-type','').split(';')[0].strip().lower()
     orig_ext={'image/jpeg':'.jpg','image/png':'.png','image/webp':'.webp','image/gif':'.gif'}.get(ct) \
      or Path(try_url.split('?')[0]).suffix or '.img'
     local_name=save_stem+orig_ext
     local_path=imgdir/local_name
     local_path.write_bytes(r.content)
     webp_path=_to_webp(local_path,quality=90,lossless=keep_lossless)
     img['src']=f'assets/images/{webp_path.name}'
     img.attrs.pop('data-orig-stem',None);img.attrs.pop('data-download-url',None)
     downloaded=True;break
   except Exception:continue
  if not downloaded:
   # All downloads failed — remove this img completely
   img.decompose()
 return target_rgb,base_css_text

def _get_product_img(image_paths,slot_key,fallback_idx=0):
 """Get best image for a slot — manual upload first, then serp, never hero.png as bottle fallback."""
 # 1. Exact slot match (e.g. user uploaded bottle-3.png)
 for p in image_paths:
  if Path(p).stem.lower()==slot_key:return p
 # 2. Non-manual (serp) images — safe fallback
 manual_stems=set(MANUAL_SLOTS.keys())
 serp_imgs=[p for p in image_paths if Path(p).stem.lower() not in manual_stems]
 if serp_imgs:return serp_imgs[min(fallback_idx,len(serp_imgs)-1)]
 # 3. Fallback to another bottle image (never hero)
 bottle_imgs=[p for p in image_paths if Path(p).stem.lower() in ('bottle-2','bottle-3','bottle-6','bottle2','bottle3','bottle6')]
 if bottle_imgs:return bottle_imgs[min(fallback_idx,len(bottle_imgs)-1)]
 # 4. Last resort — any image
 return image_paths[0] if image_paths else None

def localize_images(soup,image_paths,design='1'):
 if not image_paths:
  # Remove all blanked product image slots
  for img in soup.find_all('img'):
   if not img.get('src','') and img.get('data-orig-stem',''):img.decompose()
  return
 # Separate manual named vs serp vs how-it-works
 HOW_IT_WORKS_STEMS=('how-it-works','how_it_works','howitworks','how-it-work')
 manual={Path(p).stem.lower():p for p in image_paths if Path(p).stem.lower() in MANUAL_SLOTS
         and Path(p).stem.lower() not in HOW_IT_WORKS_STEMS}
 hiw_img=next((p for p in image_paths if Path(p).stem.lower() in HOW_IT_WORKS_STEMS),None)
 serp=[p for p in image_paths if Path(p).stem.lower() not in MANUAL_SLOTS
       and Path(p).stem.lower() not in HOW_IT_WORKS_STEMS]
 # all_prod = every non-how-it-works manual upload (hero/bottles AND
 # badges/guarantee/reviewer/bonus/cards) + serp images — NOT product
 # photos only, despite the name. product_only below is the actual
 # product-photo pool (hero + bottles) for "no idea what this image slot
 # is, just show a reasonable product photo" fallbacks — using all_prod
 # directly for those is how an unrelated badge or reviewer headshot ends
 # up filling e.g. a generic "benefits" illustration slot.
 all_prod=list(manual.values())+serp
 product_only=seo_images(image_paths) or all_prod

 def best(slot,idx=0):
  if slot in manual:return manual[slot]
  fallbacks=['hero','bottle-1','bottle1']
  for fb in fallbacks:
   if fb in manual:return manual[fb]
  if serp:return serp[min(idx,len(serp)-1)]
  if product_only:return product_only[min(idx,len(product_only)-1)]
  return None

 extra_idx=0
 for img in soup.find_all('img'):
  cur=str(img.get('src') or '').strip()
  stem=img.get('data-orig-stem','')
  # Skip images already correctly set by populate() (pricing cards etc)
  if img.get('data-populated'):
   img.attrs.pop('data-populated',None)
   img.attrs.pop('data-orig-stem',None)
   continue
  if not stem:
   # Already has local src or empty without stem
   if cur.startswith('assets/images/') and cur:continue
   # Skip failed keep-image downloads — remove broken img
   if img.get('data-keep-failed'):img.decompose();continue
   if not cur and not stem:
    # Empty blank slot with no info at all — a bottle-3/bottle-6 pack shot
    # reads better here than repeating the hero image, with its own alt.
    bottle_fallback=manual.get('bottle-3') or manual.get('bottle-6')
    if bottle_fallback:
     p=bottle_fallback
     p_alt='3 bottle package' if bottle_fallback==manual.get('bottle-3') else '6 bottle package'
    else:
     p=best('hero',extra_idx%max(len(all_prod),1));extra_idx+=1
     p_alt=None
    if p:img['src']=safe_rel(p);img['alt']=img.get('alt') or p_alt or 'Product image'
   continue
  cls=_classify(stem,design)
  if cls=='keep':
   img.attrs.pop('data-orig-stem',None);img.attrs.pop('data-download-url',None);continue
  # how-it-works slot — only ever shows the publisher's OWN uploaded image.
  # The ORIGINAL scraped template's own mechanism infographic is never used
  # as a fallback here (it's another product's graphic, possibly with that
  # brand's own text baked into the pixels) — with no upload, the image is
  # removed outright and a warning is recorded, leaving just the text steps.
  if any(x in stem for x in HOW_IT_WORKS_STEMS):
   if hiw_img:
    img['src']=safe_rel(hiw_img)
    img['alt']=img.get('alt') or 'How it works'
    img.attrs.pop('data-orig-stem',None);img.attrs.pop('data-download-url',None)
   else:
    parent=img.find_parent('figure')
    (parent or img).decompose()
    _HIW_IMG_WARNINGS.append(design)
   continue
  chosen=None
  fallback_alt=None
  # Design 1 special case: template's bottle-3 slot = hero image position
  if design=='1' and stem==DESIGN1_HERO_STEM:
   # Use hero.png if uploaded, else bottle-3.png
   chosen=best('hero',0)
   if not chosen:chosen=manual.get('bottle-3') or (serp[0] if serp else None)
  elif cls=='hero':
   chosen=best('hero',0)
  elif cls=='bottle':
   if any(x in stem for x in ('_2_','_2-','2-bottle','prod_2','-2-bottle','bottle-2')):chosen=best('bottle-2',0)
   elif any(x in stem for x in ('_6_','_6-','6-bottle','prod_6','-6-bottle','bottle-6')):chosen=best('bottle-6',2)
   elif any(x in stem for x in ('_3_','_3-','3-bottle','prod_3','-3-bottle','bottle-3')):chosen=best('bottle-3',1)
   else:chosen=best('hero',0)
  else:
   # A stem the "keep" pass already recognizes as a single-purpose slot
   # (checkout screenshot, bespoke description graphic, a badge/guarantee
   # variant that just wasn't classified "keep" for this design) has no
   # safe generic substitute — use an exact manual upload if the publisher
   # gave one, otherwise remove the tag. Falling through to "just grab the
   # next uploaded image" here is how a checkout-page slot ended up showing
   # an unrelated FDA badge photo.
   role=_keep_role(stem)
   if role and role in manual:
    chosen=manual[role]
   elif role:
    img.decompose();continue
   elif product_only:
    # No recognizable role for this slot either — a bottle-3/bottle-6
    # pack shot reads better here than repeating the hero image (which
    # already appears elsewhere on the page), and gets its own distinct
    # alt text instead of inheriting/duplicating the hero's.
    bottle_fallback=manual.get('bottle-3') or manual.get('bottle-6')
    if bottle_fallback:
     chosen=bottle_fallback
     fallback_alt='3 bottle package' if bottle_fallback==manual.get('bottle-3') else '6 bottle package'
    else:
     chosen=product_only[extra_idx%len(product_only)];extra_idx+=1
  if chosen:
   img['src']=safe_rel(chosen)
   img['alt']=img.get('alt') or fallback_alt or 'Product image'
  img.attrs.pop('data-orig-stem',None);img.attrs.pop('data-download-url',None)

def set_text(el,text):
 if el:el.string=str(text)

def clean_section_text(section_el):
 for el in section_el.find_all(['script','style','noscript']):el.decompose()

def section(soup,*ids):
 # Prefer an actual <section> tag over any other element. Some templates
 # keep a small heading-only "title band" <div id="benefits"> as a SIBLING
 # of the real content <section class="benefits-section"> (the id sits on
 # the div, not the section) — matching the div first via a plain
 # soup.find(id=i) silently rewrites only the heading text and leaves every
 # real card/paragraph inside the actual content section untouched.
 for i in ids:
  x=soup.find('section',id=i)
  if x:return x
 for i in ids:
  x=soup.find('section',class_=re.compile(re.escape(i),re.I))
  if x:return x
 for i in ids:
  x=soup.find(id=i)
  if x:return x
 # Not every template puts these markers on `id` — some only use a class
 # (e.g. <section class="faq-section">, no id at all), which would silently
 # skip that whole section's content rewrite. Fall back to a class-name
 # (and then id-substring) match before giving up.
 for i in ids:
  x=soup.find(['section','div'],class_=re.compile(re.escape(i),re.I))
  if x:return x
 for i in ids:
  x=soup.find(id=re.compile(re.escape(i),re.I))
  if x:return x
 return None

def _first_heading(sec):
 for tag in sec.find_all(['h1','h2','h3','h4'],recursive=True):return tag
 return None

def _replace_texts(nodes,values):
 vals=[str(x) for x in values if str(x).strip()]
 for i,node in enumerate(nodes):
  if i<len(vals):set_text(node,vals[i])

def _fill_existing_items(sec,values):
 vals=[str(x) for x in values if str(x).strip()]
 items=sec.find_all('li')
 if items:
  for i,v in enumerate(vals):
   if i<len(items):set_text(items[i],v)
  return
 cards=[]
 for el in sec.find_all(['article','div']):
  cls=' '.join(el.get('class') or []).lower()
  if any(k in cls for k in ('card','item','tile','feature','point','step','benefit','check')) and (el.find(['h3','h4','p','strong'])):cards.append(el)
 for i,v in enumerate(vals):
  if i>=len(cards):break
  target=cards[i].find(['p','li','strong','h3','h4'])
  if target:set_text(target,v)

def _set_section_text(sec, heading, paragraphs=None):
 """Set heading and optional paragraphs in a section."""
 h=sec.find(['h1','h2','h3','h4'])
 if h: h.string=heading
 if paragraphs:
  ps=sec.find_all('p')
  for i,txt in enumerate(paragraphs):
   if i<len(ps): ps[i].string=txt

_ICON_KEYWORDS=[
 (r'\bheartburn|\bindigestion|\breflux','🔥'),
 (r'\bfood sensitiv|\ballerg|\bintoleran','🍽️'),
 (r'\bbloat','🎈'),
 (r'\bregular','🔄'),
 (r'\bnutrient|\babsorption|\bappetite','🥗'),
 (r'\bflora|\bmicrobiome|\bprobiotic|\bbacteria','🌱'),
 (r'\bsleep|\bnight|\binsomnia|\brest\b','🌙'),
 (r'\benergy|\bfatigue|\btired|\bstamina|\bvitality','⚡'),
 (r'\bimmun','🛡️'),
 (r'\bjoint|\bmobility|\bflexib|\bmuscle','🦴'),
 (r'\bheart|\bcardio|\bcirculat|\bblood pressure','❤️'),
 (r'\bbrain|\bfocus|\bmental|\bcognit|\bmemory|\bclarity','🧠'),
 (r'\bskin|\bcomplexion|\bwrinkle','✨'),
 (r'\bweight|\bmetaboli|\bfat burn','⚖️'),
 (r'\bstress|\banxiet|\bcalm|\bmood','😌'),
 (r'\bhormon','⚖️'),
 (r'\bdetox|\bcleanse|\btoxin','🌿'),
 (r'\binflam','🔥'),
 (r'\bblood sugar|\bglucose|\binsulin','🩸'),
 (r'\bhair','💇'),
 (r'\bvision|\beye\b','👁️'),
 (r'\bpain|\bache|\bsore','💢'),
 (r'\bliver|\bkidney|\bdetox','🫘'),
 (r'\bcramp|\bgas\b|\bflatul','💨'),
 (r'\bcomfort|\bsooth|\bease\b','🍃'),
 (r'\bconfiden|\bself[- ]esteem','💪'),
 # Broad/generic — checked last so a digestive-health product's benefit
 # copy (which routinely contains "gut"/"digest" in nearly every line)
 # doesn't drown out the more specific matches above and repeat the same
 # icon across most of its benefit cards.
 (r'\bgut\b|\bdigest|\bstomach\b|\bbowel|\bintestin','🦠'),
]
def _pick_icon(*texts,fallback='✅'):
 """Design 4's symptom/benefit cards ship with a decorative emoji baked into
 the scraped template, one per card position — fine for the original
 product, meaningless once AI-generated text for a different category (or
 even a different benefit ordering) lands in that slot. Rather than leave a
 stale icon sitting next to unrelated text, match one to the actual title
 via keyword. Falls back to a neutral checkmark, never a random pick."""
 # Check each text in order (title before description) rather than pooling
 # them together, so a specific word in the title isn't buried by a more
 # generic/earlier-listed keyword that happens to appear in the body text.
 for t in texts:
  low=(t or '').lower()
  for pat,emo in _ICON_KEYWORDS:
   if re.search(pat,low):return emo
 return fallback

_ING_ICON_KEYWORDS=[
 (r'\bginger|\bturmeric|\bginseng','🫚'),
 (r'\bpineapple|\bbromelain','🍍'),
 (r'\blemon|\blime\b|\bcitrus','🍋'),
 (r'\bapple\b(?!\s*cider)','🍎'),
 (r'\bapple cider|\bvinegar','🍏'),
 (r'\bwalnut|\balmond|\bnut\b','🌰'),
 (r'\baloe','🌵'),
 (r'\bprune|\bplum','🍑'),
 (r'\bpapaya|\bmango','🍈'),
 (r'\bcoconut','🥥'),
 (r'\bavocado','🥑'),
 (r'\bgrape\b','🍇'),
 (r'\bberry|\bberries|\bacai|\belderberry','🫐'),
 (r'\bflax|\bchia|\bseed\b','🌱'),
 (r'\boat|\bwheat|\bbran|\bgrain|\bhusk|\bpsyllium','🌾'),
 (r'\bgarlic','🧄'),
 (r'\bclay|\bcharcoal|\bbentonite','🪨'),
 (r'\bprobiotic|\blactobacillus|\bbifidobacter|\bacidophilus|\bbacteria|\bmicrobiome','🦠'),
 (r'\bmushroom|\breishi|\bfungal|\bfungi','🍄'),
 (r'\bhoney','🍯'),
 (r'\bmint|\bpeppermint|\bfennel|\blicorice|\bbasil|\bherb','🌿'),
 (r'\bmarshmallow|\belm|\bbark|\broot\b','🌳'),
 (r'\bgreen tea|\btea\b|\bcatechin','🍵'),
 (r'\bcayenne|\bchili|\bpepper\b(?!mint)|\bcapsaicin','🌶️'),
 (r'\bfiber|\bpectin|\bglucomannan|\binulin','🌾'),
 (r'\benzyme|\bpapain|\blipase|\bamylase','🧪'),
 (r'\bomega|\bfish oil|\bdha\b|\bepa\b','🐟'),
 (r'\bvitamin c|\bcamu|\bacerola','🍊'),
 (r'\bvitamin|\bmineral|\bzinc|\bmagnesium|\bcalcium|\bpotassium','🧂'),
 (r'\bantioxidant|\bpolyphenol','🍇'),
 (r'\bdetox|\bcleanse|\btoxin','🪨'),
 (r'\bsoothing|\bsooth|\bcalm|\bcomfort','🍃'),
 (r'\bantimicrobial|\bantibacterial|\bantiviral','🛡️'),
 (r'\blaxative|\bregular','🔄'),
 (r'\badaptogen','🌱'),
]
def _pick_ing_icon(*texts,fallback='🌿'):
 """Same problem as _pick_icon, one level down: design 4's ingredient rows
 (name/role/description) get fully rewritten with AI-generated content, but
 the decorative "ing-visual" emoji next to each row is never touched, so it
 keeps whichever unrelated icon happened to sit in that template slot (a
 ginger-root emoji next to "Oat Bran", a pineapple next to "Prune"...).
 Cloned rows (for ingredient counts beyond the template's own slots) had it
 worse — they just cycled a fixed pool with no relation to content at all.
 Match the ingredient's actual name first, then its role/description."""
 for t in texts:
  low=(t or '').lower()
  for pat,emo in _ING_ICON_KEYWORDS:
   if re.search(pat,low):return emo
 return fallback

def _support_phrase(category):
 """'category' is normally a full product-type label like 'Digestive Health
 Supplement' — natural on its own ("falls into the X category") but
 grammatically broken once substituted into a "...to support {category}"
 sentence ("support digestive health supplement"). Strip a trailing generic
 product-type word so these sentences read naturally, without touching the
 stored category value used everywhere else (JSON-LD, labels, etc.)."""
 c=(category or '').strip()
 low=c.lower()
 for suffix in (' supplement',' formula',' product'):
  if low.endswith(suffix):
   c=c[:-len(suffix)]
   break
 return (c or category or '').lower()

def _truncate_words(text,limit=100):
 """Plain text[:limit] cuts mid-word (e.g. "...certain compoun") which reads
 as a rendering glitch, not a deliberate teaser. Cut at the last whole word
 within the limit and mark it with an ellipsis instead."""
 text=text or ''
 if len(text)<=limit:return text
 cut=text[:limit].rsplit(' ',1)[0].rstrip('.,;: ')
 return (cut or text[:limit])+'…'

def _dedup_leaf_elements(els):
 """A wrapping/grid container's class often substring-matches the same
 keyword check used to find individual cards inside it (e.g.
 class="reviews-container" contains "review", same as the class="review"
 cards nested inside it) — that silently shifts every following index by
 one. Drop any candidate that itself contains another candidate, keeping
 only the actual leaf elements."""
 return [el for el in els if not any(el is not oel and oel in el.descendants for oel in els)]

def _replace_cards(sec, items):
 """Replace card items — handles div.bpo-card, li+b, and any heading+p structure."""
 if not items: return False
 # Try 1: div/article cards with heading
 cards=[]
 for el in sec.find_all(['article','div']):
  cls=' '.join(el.get('class') or []).lower()
  if any(k in cls for k in ('card','item','tile','point','step','feature','thing','badge')):
   if el.find(['h3','h4','h5','strong','b']): cards.append(('card',el))
 leaf=set(id(el) for el in _dedup_leaf_elements([el for _,el in cards]))
 cards=[(k,el) for k,el in cards if id(el) in leaf]
 # Try 2: li items with b/strong title (bpo-list style)
 if not cards:
  for li in sec.find_all('li'):
   cards.append(('li',li))
 # Try 3: any heading+p pairs
 if not cards:
  for h in sec.find_all(['h3','h4','h5']):
   cards.append(('h',h))
 if not cards: return False
 for i,(kind,el) in enumerate(cards):
  if i>=len(items): el.decompose() if kind!='h' else None; continue
  item=items[i]
  title=item.get('title','') if isinstance(item,dict) else str(item)
  text=item.get('text','') if isinstance(item,dict) else ''
  if kind=='card':
   h=el.find(['h3','h4','h5','strong','b'])
   ps=el.find_all('p')
   if h: h.string=title
   if ps:
    ps[0].string=text
    # A card with a second <p> (e.g. the source template's own bonus cards,
    # which pair a "was" summary <p> with a second, longer sales-copy <p>)
    # only ever had its first <p> filled here — the second one survived on
    # every generated site as the ORIGINAL scraped product's own unrelated
    # copy (e.g. a gut-health bonus card's second paragraph still pitching
    # "reduce the appearance of varicose veins"). There's no second real
    # value to put there, so drop it instead of leaving stale copy behind.
    for extra_p in ps[1:]:extra_p.decompose()
  elif kind=='li':
   b=el.find(['b','strong'])
   # Get text node after b
   if b:
    b.string=title
    # Replace text after b tag
    for child in list(el.children):
     if child!=b and hasattr(child,'replace_with') and str(child).strip():
      child.replace_with(text)
      break
   else:
    el.clear(); el.append(title)
  elif kind=='h':
   el.string=title
   p=el.find_next_sibling('p')
   if p: p.string=text
 # Remove extra items
 for kind,el in cards[len(items):]:
  try: el.decompose()
  except Exception: pass
 return True

# (keywords to match against a card's own icon alt-text/title, new title, new text)
_BADGE_ITEM_POOL=[
 (('usa','america','united states','domestic'),'Made In The USA',
  'Produced in the United States under standard manufacturing practices.'),
 (('fda','registered facility','facility'),'FDA-Registered Facility',
  '{brand} is produced in an FDA-registered facility.'),
 (('gmp','good manufacturing'),'GMP Manufacturing',
  'Manufactured under Good Manufacturing Practice guidelines for consistent quality.'),
 (('natural','plant','non-gmo','nongmo','organic'),'100% Natural Formula',
  'Made with natural, plant-based ingredients — no unnecessary fillers.'),
 (('guarantee','money-back','money back','refund','risk-free','risk free','quality'),'Satisfaction Guarantee',
  '{brand} is backed by a money-back guarantee — see the official site for current terms.'),
 (('ingredient','label','disclosed','named'),'{n} Named Ingredients',
  'A complete, clearly labeled formula — every ingredient disclosed on the official product label.'),
]

def _replace_badge_cards(sec,brand,ingredients):
 """Trust-badge/certification cards (USA-made, GMP, FDA facility, natural,
 guarantee...) can't just be filled positionally from a fixed 4-item list
 like _replace_cards does — a design's own badge ORDER varies (the
 USA-flag icon comes first in one template, the checkmark icon first in
 another), so pairing card[i] with a fixed items[i] regularly lands the
 wrong headline under the wrong icon. Instead, read each card's own
 original signal (its <img alt="">, or its own pre-existing title) to work
 out which real-world claim that icon actually represents, and assign
 matching content to it directly — the icon and the words under it can
 then never contradict each other."""
 cards=[]
 for el in sec.find_all(['article','div']):
  cls=' '.join(el.get('class') or []).lower()
  if any(k in cls for k in ('card','item','tile','point','step','feature','thing','badge')):
   if el.find(['h3','h4','h5','strong','b']):cards.append(el)
 leaf=set(id(el) for el in _dedup_leaf_elements(cards))
 cards=[el for el in cards if id(el) in leaf]
 if not cards:
  # No recognizable card structure — fall back to the old fixed-order
  # behavior rather than leaving the section completely untouched.
  return _replace_cards(sec,[
   {'title':f'{len(ingredients)} Named Ingredients','text':'A complete, clearly labeled formula — every ingredient disclosed on the official product label.'},
   {'title':'Made In The USA','text':'Produced in the United States under standard manufacturing practices.'},
   {'title':'GMP Manufacturing','text':'Manufactured under Good Manufacturing Practice guidelines for consistent quality.'},
   {'title':'Satisfaction Guarantee','text':f'{brand} is backed by a money-back guarantee — see the official site for current terms.'},
  ])
 pool=[{'keywords':kws,'title':title.format(n=len(ingredients)),'text':text.format(brand=brand)}
       for kws,title,text in _BADGE_ITEM_POOL]
 used=set();assignments={};unmatched=[]
 for el in cards:
  sig_parts=[]
  img=el.find('img')
  if img and img.get('alt'):sig_parts.append(str(img['alt']))
  # The image's own original filename (e.g. "jellytide-fda-approved.webp") is
  # a stronger signal than the alt/heading text for which real badge image
  # will actually end up here after localize_images runs later in the
  # pipeline — some scraped templates reuse a certification-shaped graphic
  # under vague copy ("Quality" / "TRUSTED QUALITY") for an image that is
  # unambiguously an FDA/GMP/USA/natural badge by filename. Without this, the
  # heading text ends up describing a different claim than the badge image
  # the visitor actually sees under it. This runs before strip_old_product_
  # images() sets data-orig-stem, so read the stem straight off the still-
  # original <img src> URL here instead.
  if img and img.get('src'):
   try:sig_parts.append(Path(str(img['src']).split('?')[0]).stem.lower())
   except Exception:pass
  h=el.find(['h3','h4','h5','strong','b'])
  if h:sig_parts.append(h.get_text())
  sig=' '.join(sig_parts).lower()
  matched=None
  for idx,item in enumerate(pool):
   if idx in used:continue
   if any(kw in sig for kw in item['keywords']):matched=idx;break
  if matched is not None:
   used.add(matched);assignments[id(el)]=pool[matched]
  else:
   unmatched.append(el)
 remaining=[item for idx,item in enumerate(pool) if idx not in used]
 for el in unmatched:
  assignments[id(el)]=remaining.pop(0) if remaining else None
 for el in cards:
  item=assignments.get(id(el))
  if item is None:
   el.decompose();continue
  h=el.find(['h3','h4','h5','strong','b'])
  p=el.find('p')
  if h:h.string=item['title']
  if p:p.string=item['text']
 return True

def _best_worst_pb(pricing):
 vals=[]
 for p in pricing:
  try:vals.append(float(re.sub(r'[^0-9.]','',str(p.get('price_per_bottle','')) or '0') or 0))
  except Exception:pass
 return (min(vals) if vals else 0),(max(vals) if vals else 0)

def _populate_design3_investigative(soup,data,brand):
 """Design 3's whole page is written as an investigative/comparison article
 about the ORIGINAL product specifically — two conflicting scam sites
 selling different formulas under the same name, specific drug-interaction
 claims (St. John's Wort/SSRIs), specific price discrepancies ($158 vs
 $207...). None of that is true of, or transfers to, an arbitrary new
 product — generic card/paragraph replacement elsewhere in populate() only
 catches headings, so this fills in the bespoke sections with an honest,
 generic equivalent that keeps the same investigative/editorial *design*
 (tables, checklists, safety boards) without the fabricated specifics."""
 ingredients=data.get('ingredients',[])
 benefits=data.get('benefits',[])
 how_it_works=data.get('how_it_works',[])
 pricing=data.get('pricing',[])
 category=data.get('category','wellness supplement')
 description=data.get('description','')
 guarantee_text=data.get('guarantee_text','') or f'{brand} is backed by a satisfaction guarantee — see the official product page for current terms.'
 best_pb,worst_pb=_best_worst_pb(pricing)

 # ── Hero spec sheet — was hard-coded "Doses published: None" etc (that
 # was the ORIGINAL scraped product's own specific numbers, not a verified
 # fact about this new product). Use the AI's typical-for-category
 # estimate from serving_info when available — same "plausible, not
 # copied from an unrelated product" spirit as the pricing field —
 # falling back to the safe placeholder only if that field is missing ──
 specs=soup.find('dl',class_=re.compile(r'\bvc-specs\b',re.I))
 if specs:
  dds=specs.find_all('dd')
  serving_info=data.get('serving_info') or {}
  vals=[serving_info.get('daily_serving') or 'See official label',
        serving_info.get('per_bottle') or 'See official label',
        serving_info.get('doses_published') or 'See official label',
        (f'${best_pb:g}/btl' if best_pb else 'See pricing')]
  for i,dd in enumerate(dds):
   if i<len(vals):dd.string=vals[i]

 # ── Mockery ticker ("Capsule or powder? Zero doses published…") → a
 # neutral trust strip using the same marquee markup ──
 ticker=soup.find(class_=re.compile(r'\bvc-ticker\b',re.I))
 if ticker:
  lis=ticker.find_all('li')
  trust=['Made In The USA','GMP Certified Facility',
         (f'{len(ingredients)} Named Ingredients' if ingredients else 'Quality Checked'),
         'Money-Back Guarantee']
  for i,li in enumerate(lis):
   if i<len(trust):li.string=trust[i]
   else:li.decompose()

 # ── "Before anything else" alert box in the what-is section ──
 alert=soup.find(class_=re.compile(r'\bvc-alert\b',re.I))
 if alert:
  p=alert.find('p')
  if p:
   p.clear()
   b=soup.new_tag('strong');b.string='Before you order: '
   p.append(b)
   p.append(f'confirm the current ingredient list, dosage and guarantee terms on the official '
            f'{brand} product page — these can change without notice.')

 # ── Second "what is" block — a distinct h2 + 4-paragraph analysis
 # ("Strip away the branding...") separate from the main intro answer,
 # built entirely around the original product's specific ingredient
 # critique and dual-identity problem ──
 what_is_sec=section(soup,'what-is')
 if what_is_sec:
  for h2 in what_is_sec.find_all('h2'):
   if 'named ingredients' in h2.get_text().lower() and h2.find_parent(class_=re.compile('col-lg-7|col-lg-6',re.I)):
    col=h2.find_parent(['div'])
    ps=[p for p in col.find_all('p',recursive=False)] if col else []
    if not ps and col:ps=col.find_all('p')
    lines=[
     f'{description}' if description else f'{brand} is formulated to support {_support_phrase(category)}.',
     (f'It contains {len(ingredients)} named ingredients, each disclosed on the official label.'
      if ingredients else f'Check the official label for the full, current ingredient list.'),
     f'{data.get("how_it_works_intro","") or "Individual results vary, and this is a dietary supplement, not a medical treatment."}',
     f'See the ingredients page for the full breakdown of what is in {brand} and why.',
    ]
    for i,p in enumerate(ps):
     for a in p.find_all('a'):a.decompose()
     if i<len(lines):p.string=lines[i]
     else:p.decompose()
    break

 # ── "Which <brand> are you buying" 3-card comparison → an honest
 # "what to verify" checklist using the same card markup ──
 compare_sec=next((s for s in soup.find_all('section') if (s.get('id') or '').startswith('which-')),None)
 if compare_sec:
  eyebrow=compare_sec.find(class_=re.compile(r'vc-eyebrow',re.I))
  if eyebrow:eyebrow.string='Worth checking before you buy'
  h2=compare_sec.find('h2')
  if h2:h2.string=f'What To Verify Before Ordering {brand}'
  lede=compare_sec.find(class_=re.compile(r'vc-lede',re.I))
  if lede:lede.string=f'A few quick checks that take under a minute and protect you either way.'
  # Restrict to the <article> tag with the *exact* "vc-siteca" class token
  # (\b-bounded) — an unbounded substring match also hits nested BEM child
  # classes (vc-siteca__tag, __claim, __note), turning one card into four
  # "cards" and cycling through the checklist once per sub-element instead
  # of once per actual card.
  cards=compare_sec.find_all('article',class_=re.compile(r'\bvc-siteca\b',re.I))
  checklist=[
   ('Check 1','Ingredient List','Make sure the ingredient list on the page you are ordering from matches what is printed on the product label when it arrives.'),
   ('Check 2','Guarantee Terms','Screenshot the refund window and any conditions before you pay — terms are easiest to verify while still on the order page.'),
   ('Check 3','Official Source','Buy only from the official website to make sure you get genuine product, current pricing and the full guarantee.'),
  ]
  for i,card in enumerate(cards):
   tag=card.find(class_=re.compile(r'vc-siteca__tag',re.I))
   h3=card.find('h3')
   claim=card.find(class_=re.compile(r'vc-siteca__claim',re.I))
   if i<len(checklist):
    if tag:tag.string=checklist[i][0]
    if h3:h3.string=checklist[i][1]
    if claim:claim.string=checklist[i][2]
   # The per-site comparison table and note don't have an honest
   # generic equivalent — drop them rather than show fabricated data.
   dl=card.find('dl')
   if dl:dl.decompose()
   note=card.find(class_=re.compile(r'vc-siteca__note',re.I))
   if note:note.decompose()
  note_box=compare_sec.find(class_=re.compile(r'\bvc-note\b',re.I))
  if note_box:
   ps=note_box.find_all('p')
   msgs=[f'These three checks take under a minute and cost nothing — worth doing before any online order, not just this one.',
         f'If anything on arrival does not match what the order page showed, you have a documented basis to request a refund.']
   for i,p in enumerate(ps):
    if i<len(msgs):
     b=p.find('strong')
     label=b.get_text() if b else ''
     p.clear()
     if label:
      nb=soup.new_tag('strong');nb.string=label;p.append(nb);p.append(' '+msgs[i])
     else:p.append(msgs[i])
    else:p.decompose()

 # ── How-it-works mechanism paragraphs (plain <p> sequence, no card
 # wrapper) — replace the fabricated "two are marketing" critique ──
 hiw_sec=section(soup,'how-it-works')
 if hiw_sec:
  mech_col=None
  for h2 in hiw_sec.find_all('h2'):
   if 'actually works' in h2.get_text().lower() or 'step by step' in h2.get_text().lower():
    mech_col=h2.find_parent(['div']);break
  if mech_col:
   ps=[p for p in mech_col.find_all('p') if not p.find('a')]
   lines=[x.get('text','') for x in how_it_works if x.get('text')]
   if not lines:lines=[f'{brand} is intended to support {_support_phrase(category)} through the combination of ingredients on its label.']
   for i,p in enumerate(ps):
    if i<len(lines):p.string=lines[i]
    else:p.decompose()

 # ── Refund "clock" — collapse the fabricated multi-site bar comparison
 # into the real guarantee text ──
 clock=soup.find(class_=re.compile(r'\bvc-clock\b',re.I))
 if clock:
  bars=clock.find(class_=re.compile(r'vc-clock__bars',re.I))
  if bars:bars.decompose()
  h3=clock.find('h3')
  if h3:h3.string='The guarantee, in plain terms'
  small_p=clock.find('p',class_=re.compile('vc-small',re.I))
  if small_p:small_p.string=guarantee_text

 # ── Ingredients dossier (.vc-doss <li>) — untouched by the generic
 # ingredients-card logic since these are <li>, not <div>, with a
 # subjective 0-100 "confidence" bar that can't be honestly replicated ──
 doss=soup.find('ul',class_=re.compile(r'\bvc-doss\b',re.I))
 if doss:
  items=doss.find_all('li',recursive=False) or doss.find_all('li')
  # The template only ships as many <li> dossier rows as its own original
  # ingredient list had — when the AI returns more ingredients than that,
  # the heading elsewhere on the page ("All N Ingredients, Explained")
  # still reports the full count N, but without cloning extra rows here
  # the list itself silently stops after the template's original row
  # count, so the page claims more ingredients than it actually shows.
  if items and len(ingredients)>len(items):
   template_li=items[-1]
   for _ in range(len(ingredients)-len(items)):
    new_li=BeautifulSoup(str(template_li),'html.parser').find('li')
    template_li.insert_after(new_li)
    template_li=new_li
    items.append(new_li)
  for i,li in enumerate(items):
   if i>=len(ingredients):li.decompose();continue
   ing=ingredients[i]
   name_el=li.find(class_=re.compile('vc-doss__name',re.I))
   chip_el=li.find(class_=re.compile('vc-doss__chip',re.I))
   pct_el=li.find(class_=re.compile('vc-doss__pct',re.I))
   desc_p=li.find('p')
   if name_el:name_el.string=ing.get('name','')
   if chip_el:chip_el.string=(ing.get('role','') or 'Named Ingredient')
   if pct_el:pct_el.string=''
   if desc_p:desc_p.string=ing.get('description','')
  note_box=doss.find_next_sibling(class_=re.compile(r'\bvc-note\b',re.I))
  if note_box:
   ps=note_box.find_all('p')
   if ps:
    ps[0].clear()
    ps[0].append(BeautifulSoup(
     f'Always check the official {html.escape(brand)} label for the current ingredient list and '
     f'serving directions. See our <a href="ingredients.html">ingredients page</a> for details.','html.parser'))
   if len(ps)>1:
    ps[1].string='If you have questions about a specific ingredient or amount, the manufacturer’s support line can usually confirm what is on the current label.'
   for p in ps[2:]:p.decompose()

 # ── Benefits list — plain <ul><li><strong>Title</strong> critique</li>,
 # no card wrapper, so the generic benefits-card logic never sees it ──
 ben_sec=section(soup,'benefits')
 if ben_sec:
  ben_ul=ben_sec.find('ul')
  if ben_ul and not ben_ul.find(class_=True):
   lis=ben_ul.find_all('li',recursive=False) or ben_ul.find_all('li')
   for i,li in enumerate(lis):
    if i>=len(benefits):li.decompose();continue
    parts=benefits[i].split(' — ',1) if ' — ' in benefits[i] else [benefits[i],f'Supports your daily {_support_phrase(category)} routine.']
    li.clear()
    b=soup.new_tag('strong');b.string=parts[0];li.append(b)
    li.append(' '+(parts[1] if len(parts)>1 else ''))
  lead_p=ben_sec.find('p')
  if lead_p and lead_p.find_parent('ul') is None and not lead_p.get('class'):
   lead_p.string=description

 # ── Interaction/safety board — specific drug names (St. John's Wort,
 # metformin…) replaced with standard, genuinely generic supplement
 # cautions that apply regardless of what's actually in this product ──
 board=soup.find('ul',class_=re.compile(r'\bvc-board\b',re.I))
 if board:
  items=board.find_all('li',recursive=False) or board.find_all('li')
  generic_cautions=[
   ('is-stop','See a doctor first','Any new or worsening symptom (unexplained weight change, persistent fatigue, unusual pain)','A supplement is not a substitute for a medical diagnosis. If something feels wrong, get it checked before assuming a supplement will fix it.'),
   ('is-stop','Ask your prescriber','Currently taking prescription medication','Some ingredients can interact with common medications. Check with your prescriber or pharmacist before starting, especially if you take medication daily.'),
   ('is-care','Ask first','Pregnant, nursing, or under 18','Not formulated or studied for these groups. The manufacturer states this too — check the official label.'),
   ('is-care','Caution','Known allergies or sensitivities','Review the full ingredient list on the official label before ordering, not just the marketing summary.'),
   ('is-care','Expect this','Mild digestive adjustment in the first week or two','Common with most new supplements, especially ones with fibre or botanical ingredients. Usually settles — stop if it does not.'),
   ('','Lower concern','Healthy adult, no medication, no known conditions','Interaction risk is generally lower. Still worth checking the label against your own situation before ordering.'),
  ]
  for i,li in enumerate(items):
   if i>=len(generic_cautions):li.decompose();continue
   cls,flag_label,title,body_text=generic_cautions[i]
   li['class']=[cls] if cls else []
   flag=li.find(class_=re.compile('vc-flag',re.I))
   if flag:
    flag.string=flag_label
    flag['class']=[c for c in (flag.get('class') or []) if 'vc-flag--' not in c]
    flag_variant={'is-stop':'vc-flag--stop','is-care':'vc-flag--care'}.get(cls,'vc-flag--ok')
    flag['class']=flag.get('class',[])+[flag_variant]
   b=li.find('b')
   if b:b.string=title
   p=li.find('p')
   if p:p.string=body_text
  cards_row=board.find_next_sibling(class_=re.compile('row',re.I))
  if cards_row:
   card_items=[
    (f'What {brand} Is Formulated For',description or f'{brand} is formulated to support {_support_phrase(category)} as part of a daily routine.'),
    (f'Who Should Consider {brand}',f'Adults looking for daily support for {_support_phrase(category)} as part of a healthy lifestyle. Individual results vary.'),
    (f'Getting {brand}',f'{brand} is sold through the official website only. See the pricing section above for current package options.'),
   ]
   cards=cards_row.find_all(class_=re.compile(r'\bvc-card\b',re.I))
   for i,card in enumerate(cards):
    h3=card.find('h3');p=card.find('p')
    if i<len(card_items):
     if h3:h3.string=card_items[i][0]
     if p:p.string=card_items[i][1]

 # ── Transparency scorecard — repurpose the table as a generic
 # "what to check" reference instead of fabricated per-site comparison ──
 trans_sec=section(soup,'transparency')
 if trans_sec:
  h2=trans_sec.find('h2')
  if h2:h2.string='What A Careful Buyer Should Check'
  head_row=trans_sec.find('thead')
  if head_row:
   ths=head_row.find_all('th')
   labels=['Buyer check','Where to look','Why it matters']
   for i,th in enumerate(ths):
    if i<len(labels):th.string=labels[i]
  rows_data=[
   ('Ingredient list','Official product label / page','Confirms exactly what you are taking'),
   ('Guarantee window','Order page, before you pay','Sets the deadline for any refund request'),
   ('Manufacturer contact','Official website footer','Needed if you have a question or a problem'),
   ('Return process','Refund policy page','Avoids surprises if you decide to send it back'),
   ('Official seller','URL in your browser bar','Protects you from lookalike or third-party listings'),
  ]
  tbody=trans_sec.find('tbody')
  if tbody:
   rows=tbody.find_all('tr')
   for i,tr in enumerate(rows):
    tds=tr.find_all('td')
    if i<len(rows_data):
     for j,td in enumerate(tds[:3]):
      b=td.find('strong')
      val=rows_data[i][j]
      if b and j==0:b.string=val
      elif j==0:
       td.clear();nb=soup.new_tag('strong');nb.string=val;td.append(nb)
      else:
       td.clear();td.append(val);td['class']=[]
    else:
     tr.decompose()
  closing_p=trans_sec.find(class_=re.compile('vc-small',re.I))
  if closing_p:closing_p.string=description

 # ── "Who checks this page" reviewer bios — headings already get the
 # generic Q&A fallback text from _rewrite_all_sections; the bio
 # paragraphs underneath (pharmacist/editor descriptions) are still the
 # original template's specific, invented credentials ──
 who_sec=section(soup,'who-checks')
 if who_sec:
  bios=who_sec.find_all(class_=re.compile(r'\bvc-card\b',re.I))
  bio_texts=[
   f'Reviewed for general accuracy against the manufacturer’s own published claims before this page goes live.',
   f'Verifies pricing, package options and guarantee terms against the official {brand} order page, and re-checks periodically as pages change.',
  ]
  for i,card in enumerate(bios):
   ps=card.find_all('p')
   bio_p=next((p for p in ps if not p.get('class')),None)
   if bio_p and i<len(bio_texts):
    for a in bio_p.find_all('a'):a.decompose()
    bio_p.string=bio_texts[i]

 # ── Pricing package cards — populate() only sets title/price/total/
 # shipping/image; the feature-bullet <li> list under each card
 # ("Site B adds six digital bonus guides", "$20 gap between pages"), the
 # section intro ("Both pages sell one, three and six bottles. Neither
 # agrees...") and the closing "the prices do not agree either" narrative
 # are all specific to the ORIGINAL scraped product's dual-site pricing
 # dispute — not true of this product. Replace them with an equivalent that
 # keeps the same numbers-driven, analytical voice but only makes claims
 # this product's own single set of pricing tiers actually supports. ──
 pricing_sec=section(soup,'pricing','order-bottle')
 if pricing_sec:
  lede=pricing_sec.find(class_=re.compile(r'\bvc-lede\b',re.I))
  if lede:
   lede.string=(f'Three tiers, priced by the bottle — here is what the numbers on each one actually work out to.'
                if len(pricing)>1 else 'Here is what this package actually works out to, per bottle.')
  pack_cards=pricing_sec.find_all(class_=re.compile(r'\bvc-pack\b',re.I))
  pack_cards=_dedup_leaf_elements(pack_cards)
  pricing_by_bottles={p.get('bottles'):p for p in pricing}
  per_bottle_by_bottles={}
  for p in pricing:
   try:per_bottle_by_bottles[p.get('bottles')]=float(re.sub(r'[^0-9.]','',str(p.get('price_per_bottle','')) or '0') or 0)
   except Exception:pass
  starter_bottles=min(per_bottle_by_bottles) if per_bottle_by_bottles else 0
  starter_pb=per_bottle_by_bottles.get(starter_bottles,0)
  highest_pb=max(per_bottle_by_bottles.values()) if per_bottle_by_bottles else 0
  # How many bottles actually get tried before a 60-day guarantee window
  # closes, at the ~30-day-per-bottle pace these templates already assume
  # elsewhere (their own "30-60/90/180-day supply" subtitles). Comparing a
  # tier's bottle count against this — instead of comparing "days of supply"
  # to "days of guarantee" — avoids ever claiming a >60-day supply is
  # "inside" the window, which isn't true once a tier has 3+ bottles.
  evaluable_bottles=max(1,60//30)
  for card in pack_cards:
   h3=card.find('h3')
   m=re.search(r'\d+',h3.get_text()) if h3 else None
   bottles=int(m.group(0)) if m else 0
   pkg=pricing_by_bottles.get(bottles,{})
   pb=per_bottle_by_bottles.get(bottles,0)
   supply_days=bottles*30
   ship_txt=str(pkg.get('shipping','')).strip()
   ship_bullet=('Free shipping included' if 'free' in ship_txt.lower()
                else (ship_txt or 'Confirm shipping cost at checkout'))
   is_best='best' in ' '.join(card.get('class') or []).lower()
   is_last=len(pack_cards)>1 and card is pack_cards[-1]
   gap=round(starter_pb-pb) if starter_pb and pb and pb<starter_pb else 0
   if bottles<=evaluable_bottles:
    guarantee_bullet=f'A {supply_days}-day supply that fits inside the 60-day guarantee window, so you can finish it before deciding'
   else:
    guarantee_bullet=f'Only about {evaluable_bottles} of the {bottles} bottles get used within the 60-day guarantee window — the rest sit unopened until you decide'
   if is_best:
    bullets=[
     'The tier most first-time buyers step up to',
     (f'${gap} cheaper per bottle than the starter size' if gap>0 else 'Priced the same per bottle as the starter size'),
     ship_bullet,
     guarantee_bullet,
    ]
   elif is_last:
    bullets=[
     (f'Lowest per-bottle price of the tiers — ${gap} less than the starter size' if gap>0 else 'Lowest per-bottle price of the tiers'),
     ship_bullet,
     guarantee_bullet,
     'Best once you already know the routine works for you',
    ]
   else:
    bullets=[
     'Smallest commitment if you are trying it for the first time',
     'Highest per-bottle price of the tiers' if highest_pb and pb>=highest_pb and len(per_bottle_by_bottles)>1 else 'Lower total commitment than the larger tiers',
     ship_bullet,
     guarantee_bullet,
    ]
   lis=card.find_all('li')
   for i,li in enumerate(lis):
    if i<len(bullets):li.string=bullets[i]
    else:li.decompose()
   # The CTA button text ("Check Starter Price" / "Check 3-Bottle Discount" /
   # "Check 6-Bottle Sale") is original scraped template copy that names a
   # SPECIFIC bottle count — since populate() reorders/relabels these cards
   # by tier (best value first, etc.), a card can end up correctly titled
   # "6 Bottles" while its leftover CTA still says "Check 3-Bottle Discount"
   # underneath. Re-derive the button label from this card's own <h3> so it
   # always names the package it is actually attached to.
   cta=card.find('a',class_=re.compile(r'\bvc-btn\b',re.I))
   if h3 and cta and m:
    cta.string=f'Check {m.group(0)}-Bottle Pricing'
  note_box=pricing_sec.find(class_=re.compile(r'\bvc-note\b',re.I))
  if note_box:
   ps=note_box.find_all('p')
   sorted_p=sorted(pricing,key=lambda p:p.get('bottles',0))
   msgs=None
   if sorted_p:
    checks=[]
    for p in sorted_p:
     b=p.get('bottles',0)
     try:
      pb=float(re.sub(r'[^0-9.]','',str(p.get('price_per_bottle','')) or '0') or 0)
      tot=float(re.sub(r'[^0-9.]','',str(p.get('total','')) or '0') or 0)
      if pb and b:checks.append(f'{b}×${pb:g} = ${round(pb*b)}')
     except Exception:pass
    lo=sorted_p[0];hi=sorted_p[-1]
    lo_b=lo.get('bottles',0);hi_b=hi.get('bottles',0)
    hi_supply=hi_b*30
    if checks and hi_b>lo_b:
     msgs=[
      (f"The math checks out — {', '.join(checks)} — matching the totals shown on each tier, so there is no hidden "
       f"per-bottle markup. The real trade-off is timing: the {hi_b}-bottle tier has the lowest cost per bottle, but "
       f"the standard 60-day guarantee window closes well before a {hi_supply}-day supply is used up if you are "
       f"taking it as directed."),
      (f"What we would do: if you are new to {brand}, the {lo_b}-bottle tier lets you judge results and still "
       f"request a refund inside the window; step up to a larger tier once you know it works for you."),
     ]
   if not msgs:
    msgs=[data.get('pricing_note') or f'Multi-bottle packages lower the per-bottle price — pick the size that matches how long you plan to use {brand}.',
          f'Confirm your final total, the ingredient list and the refund terms on the official order page before submitting your order.']
   for i,p in enumerate(ps):
    if i<len(msgs):p.string=msgs[i]
    else:p.decompose()
  # A separate small-print disclaimer below the trust badges ("Pricing on
  # both pages verified...") is the same fabricated dual-site framing as the
  # lede/note text above, just left untouched by the checks there since it
  # sits outside .vc-note. Replace it the same way.
  verify_note=pricing_sec.find('p',class_=re.compile(r'\bvc-small\b',re.I))
  if verify_note:
   verify_note.string=(f'Pricing verified {date.today().isoformat()} — confirm your final total, the ingredient '
                        f'list and the refund terms on the official order page before submitting your order.')

 # ── "How to protect yourself" guarantee tips — generic advice framing is
 # fine to keep, but one tip ("Diarise day 50") references the original
 # product's specific 180-vs-60-day contradiction ──
 guarantee_sec=section(soup,'guarantee')
 if guarantee_sec:
  tip_cards=_dedup_leaf_elements(guarantee_sec.find_all(class_=re.compile(r'\bvc-card\b',re.I)))
  tips=[
   ('Screenshot before you pay','Capture the guarantee text, the ingredient list and the price, with the date visible. Takes ten seconds and gives you a record if anything changes.'),
   ('Know your deadline','Note the exact guarantee window when you order, and mark the date it closes so you are not caught out.'),
   ('Ask before you need to','Confirm whether opened bottles are accepted and who pays return postage — most pages do not state this upfront.'),
   ('Check your statement','Make sure the billing descriptor matches what you expect, and watch for unexpected repeat charges.'),
  ]
  for i,card in enumerate(tip_cards):
   h3=card.find('h3');p=card.find('p')
   if i<len(tips):
    if h3:h3.string=tips[i][0]
    if p:p.string=tips[i][1]
   else:card.decompose()
  note_box=guarantee_sec.find(class_=re.compile(r'\bvc-note\b',re.I))
  if note_box:
   ps=note_box.find_all('p')
   if ps:
    ps[0].string=f'If what arrives does not match the official listing, you have a documented basis for a refund request.'
    for extra in ps[1:]:extra.decompose()

 # ── Review cards — reviewer name/star-rating/status tag aren't wired to
 # a ".rev-name"-style class the shared reviews step looks for, so they
 # keep the original placeholder names, a 2-star "Returned" status and
 # inconsistent star counts regardless of what data was provided ──
 reviewer_names=data.get('reviewer_names',[])
 rev_sec=section(soup,'reviews')
 if rev_sec:
  rev_cards=rev_sec.find_all('article',class_=re.compile(r'\bvc-rev\b',re.I))
  star_options=['★★★★★','★★★★★','★★★★☆']
  status_options=['Verified purchase · 2-bottle','Verified purchase · 3-bottle','Verified purchase · 6-bottle']
  for i,card in enumerate(rev_cards):
   star_el=card.find(class_=re.compile(r'vc-rev__st',re.I))
   if star_el:
    stars=star_options[i%len(star_options)]
    star_el.string=stars
    star_el['aria-label']=f'{stars.count("★")} out of 5 stars'
   by=card.find(class_=re.compile(r'vc-rev__by',re.I))
   if by:
    name_b=by.find('b')
    if name_b and i<len(reviewer_names):name_b.string=reviewer_names[i]
    status_span=by.find('span')
    if status_span:status_span.string=status_options[i%len(status_options)]

 # ── Stray figcaptions/alt text referencing the original dual-page
 # comparison or a wrong product category (memory/cognitive artwork
 # copy reused under a respiratory or other unrelated product) ──
 for fig in soup.find_all('figcaption'):
  txt=fig.get_text()
  if re.search(r'either page|60-day terms|composition built from the product artwork',txt,re.I):
   fig.string=f'Official {brand} product imagery.'
 hiw_img=soup.find('img',alt=re.compile(r'restores memory|boosts cognitive|clinical memory',re.I))
 if hiw_img:hiw_img['alt']=f'How {brand} works'
 ben_img=soup.find('img',alt=re.compile(r'appetite and portion support|steady daily energy',re.I))
 if ben_img:ben_img['alt']=f'{brand} benefits'

 # ── Footer blurb under the logo — summarizes the original product's
 # specific dual-identity/interaction complaints ──
 blurb=soup.find(class_=re.compile(r'vc-foot__blurb',re.I))
 if blurb:
  blurb.string=(f'An independent {brand} reference — ingredients, pricing, guarantee terms and '
                f'what to verify before you order, all in one place.')

def _populate_design4_supplement(soup,data,brand,images):
 """Design 4's real section content mostly lives in a plain
 <section class="X-section"> while the id + heading sit on a SIBLING
 "title band" <div id="X"> right before it — invisible to the numbered
 steps above, which look for a heading inside the section they matched.
 This handles the pieces those steps still can't reach: the title bands
 themselves, the respiratory-specific "symptoms" grid (not a concept any
 other design has), fabricated review-count/percentage-off stats, and the
 plain-text pricing/bonus list that has no card structure to hook into."""
 ingredients=data.get('ingredients',[])
 benefits=data.get('benefits',[])
 bonuses=data.get('bonuses',[])
 category=data.get('category','health supplement')

 # ── Title bands ──
 band=soup.find(id='symptoms')
 if band:
  sub=band.find('p')
  if sub:sub.string=f'If these sound familiar, {brand} was designed for exactly this'
 band=soup.find(id='about')
 if band:
  h2=band.find('h2')
  if h2:h2.string=f'What Is {brand}? {len(ingredients)} Named Ingredients.' if ingredients else f'What Is {brand}?'
  sub=band.find('p')
  if sub:sub.string=f'A closer look at what {brand} actually is'
 band=soup.find(id='reviews')
 if band:
  h2=band.find('h2')
  if h2:h2.string=f'What {brand} Users Are Saying'
  sub=band.find('p')
  if sub:sub.string='Real stories from real people who made the switch'
 band=soup.find(id='faqs')
 if band:
  # This band's own h2 was never set here, only by _rewrite_all_sections()'s
  # generic FAQ handler (~line 3199) — but that handler's `section(soup,'faq',
  # 'faqs')` lookup matches the real <section class="faq-section"> when it's
  # still on the page, and design 4's real FAQ section has no h2/h3 inside it
  # (the heading lives only on this sibling band), so on pages where FAQ IS
  # the kept section (index.html, faq.html) that handler's `if h:` finds
  # nothing and leaves this band's ORIGINAL scraped text in place. On every
  # OTHER subpage, the FAQ <section> was already stripped by page_variant()
  # before populate() runs, so that same lookup falls through to matching
  # this band <div> by id instead — and DOES find an h2 inside it, so it
  # overwrites this band with a different, generic phrase. Net effect: the
  # same logical heading read two different ways depending on which page you
  # were on. Set it here explicitly (this function runs after that generic
  # pass) so every page agrees, regardless of which section survived.
  h2=band.find('h2')
  if h2:h2.string=f'{brand} — Your Questions Answered'
  sub=band.find('p')
  if sub:sub.string='Everything you should know before placing your first order'
 band=soup.find(id='ingredients')
 if band:
  h2=band.find('h2')
  if h2:h2.string=f'What Are The Ingredients In {brand}?'
  sub=band.find('p')
  if sub:sub.string=f'Every ingredient in {brand} is listed here, individually explained'
 band=soup.find(id='benefits')
 if band:
  h2=band.find('h2')
  if h2:
   shown=min(len(benefits),8) if benefits else 0
   h2.string=f'{shown} Ways {brand} May Support You' if shown else f'How {brand} May Support You'
  sub=band.find('p')
  if sub:sub.string=f'The cumulative benefits that build with consistent {brand} use'
 band=soup.find(id='bonuses')
 if band:
  if bonuses:
   h2=band.find('h2')
   if h2:h2.string=f'Order More — {len(bonuses)} Free Bonus{"es" if len(bonuses)!=1 else ""} Unlocked'
   sub=band.find('p')
   if sub:sub.string='Digital guides included free with qualifying orders'
  else:
   band.decompose()
   # The footer's own "Bonuses" nav link is static template markup, never
   # conditioned on whether this product actually has any bonus data — so
   # with no bonuses (the band above just got decomposed), it's now a dead
   # link to a #bonuses anchor that no longer exists anywhere on the page.
   bonus_link=soup.find('a',href=re.compile(r'#bonuses'))
   if bonus_link:bonus_link.decompose()
 band=soup.find(id='order-breathizen')
 if band:
  h3=band.find('h3')
  if h3:h3.string='Special Pricing Active Now'
  h4=band.find('h4')
  if h4:h4.string=f'Lock In Your {brand} Supply Before Stock Runs Out'
 band=soup.find(id='buy-breathizen')
 if band:
  h3=band.find('h3')
  # "Stock Is Limited" is a fake scarcity claim — this generator has no real
  # inventory data to back it, so it never writes one.
  if h3:h3.string=f'Order Your {brand} Kit Today'
  h4=band.find('h4')
  if h4:
   bonus_txt=f' + All {len(bonuses)} Bonus{"es" if len(bonuses)!=1 else ""}' if bonuses else ''
   h4.string=f'6-Bottle Kit — Biggest Discount + Free Shipping{bonus_txt}'

 # ── Symptoms grid — a respiratory-specific concept ("Constant Congestion",
 # "Chest Tightness"...) with no equivalent field on other designs. Use the
 # AI's own category-matched symptom list; fall back to a short generic set
 # for any cached content generated before this field existed. ──
 sec=soup.find('section',class_=re.compile(r'\bsymptoms-section\b',re.I))
 if sec:
  if sec.has_attr('aria-label'):sec['aria-label']=f'Common {category} concerns'
  symptoms=data.get('symptoms') or [
   {'title':'Not Feeling Your Best','text':f'A general sense that your {_support_phrase(category)} could use more support.'},
   {'title':'Inconsistent Results','text':'Trying different approaches without a lasting improvement.'},
   {'title':'Looking For A Better Option','text':f'Wanting a straightforward, daily way to support {_support_phrase(category)}.'},
  ]
  for i,card in enumerate(sec.find_all('div',class_=re.compile(r'\bsymptom-card\b',re.I))):
   if i<len(symptoms):
    h3=card.find('h3');p=card.find('p')
    title=symptoms[i].get('title','');text=symptoms[i].get('text','')
    if h3:h3.string=title
    if p:p.string=text
    icon_el=card.find(class_=re.compile(r'icon',re.I))
    if icon_el:icon_el.string=_pick_icon(title,text)
   else:
    card.decompose()
  cta=sec.find(class_=re.compile(r'symptoms-cta',re.I))
  if cta:
   p=cta.find('p')
   if p:
    p.clear()
    p.append("These aren't just occasional annoyances — they can be signs your body needs targeted support. ")
    nb=soup.new_tag('b');nb.string=f'{brand} was formulated to help address these at the root level.'
    p.append(nb)
   a=cta.find('a')
   if a:a.string=f'See How {brand} Helps'

 # ── Hero trust-bar fabricated star-rating/review-count stat ──
 htb=soup.find(class_=re.compile(r'hero-trust-bar',re.I))
 if htb:
  for item in htb.find_all(class_=re.compile(r'\bhtb-item\b',re.I)):
   if re.search(r'\d[\d,]*\+?\s*(stars?|reviews?)',item.get_text(),re.I):
    spans=item.find_all('span')
    text_span=spans[-1] if spans else None
    if text_span:
     text_span.clear()
     text_span.append('Trusted Formula')
     text_span.append(soup.new_tag('br'))
     text_span.append('Real Customer Feedback')

 # ── Pricing-details plain-text tier list — no card structure, so Step 8's
 # pricing-card logic never sees it; this is the ONLY place real per-bottle
 # numbers show up as text anywhere on this template. ──
 pd=soup.find('section',class_=re.compile(r'\bpricing-details\b',re.I))
 if pd:
  ul=pd.find('ul')
  if ul:
   pricing=sorted(data.get('pricing',[]),key=lambda p:p.get('bottles',0),reverse=True)
   lis=ul.find_all('li')
   for i,li in enumerate(lis):
    if i<len(pricing):
     pkg=pricing[i]
     # Bonuses are only ever included with the 3- and 6-bottle packages
     # elsewhere on this page (the bonus band above, the bonus section) —
     # showing them on every tier here, including a 1/2-bottle starter
     # pack, contradicted that.
     n_bonus=len(bonuses) if bonuses and pkg.get('bottles',0) in (3,6) else 0
     bonus_txt=f' + {n_bonus} Bonus{"es" if n_bonus!=1 else ""}' if n_bonus else ''
     label=' — BEST VALUE' if i==0 and len(pricing)>1 else ''
     li.string=(f"{pkg.get('bottles','')} Bottles — {pkg.get('price_per_bottle','')}/bottle"
                f" + {pkg.get('shipping','Shipping')}{bonus_txt}{label}")
    else:
     li.decompose()

 # ── Final CTA — fabricated buyer-count stat + un-populated price spans ──
 ctaf=soup.find('section',class_=re.compile(r'\bcta-final\b',re.I))
 if ctaf:
  h2=ctaf.find('h2')
  if h2:h2.string=f'Your {brand} Journey Starts With One Decision'
  sub=ctaf.find(class_=re.compile(r'cta-subhead',re.I))
  if sub:sub.string=f'Ready to experience {brand} for yourself?'
  try:
   pbs=[float(re.sub(r'[^0-9.]','',str(p.get('price_per_bottle','')) or '0') or 0) for p in data.get('pricing',[]) if p.get('price_per_bottle')]
   best_pb=min(pbs) if pbs else 0
   worst_pb=max(pbs) if pbs else 0
  except Exception:
   best_pb=worst_pb=0
  reg=ctaf.find(class_=re.compile(r'cta-regular-price',re.I))
  if reg:
   if worst_pb:reg.string=f'Regular Price: ${worst_pb:g} per bottle'
   else:reg.decompose()
  cur=ctaf.find(class_=re.compile(r'cta-current-price',re.I))
  if cur:
   if best_pb:cur.string=f'Now From Just ${best_pb:g}/bottle'
   else:cur.decompose()
  perks=ctaf.find(class_=re.compile(r'cta-perks',re.I))
  if perks:
   for sp in perks.find_all('span'):
    if re.search(r'\d+\s*digital bonus',sp.get_text(),re.I):
     if bonuses:sp.string=f'{len(bonuses)} Digital Bonus Guides Included'
     else:sp.decompose()
  # Final CTA button text ("SAVE UP TO 65%") is the ORIGINAL BreathiZen
  # template's own fixed claim — compute this product's real max saving
  # (2-bottle vs 6-bottle per-bottle price) instead, or drop the phrase
  # entirely when those two tiers aren't both present/computable.
  cta_btn=ctaf.find('a',class_=re.compile(r'\bbtn-cta-final\b'))
  if cta_btn:
   pricing_map={p.get('bottles'):p for p in data.get('pricing',[])}
   p2=pricing_map.get(2);p6=pricing_map.get(6)
   pct=0
   if p2 and p6:
    try:
     pb2=float(re.sub(r'[^0-9.]','',str(p2.get('price_per_bottle','')) or '0') or 0)
     pb6=float(re.sub(r'[^0-9.]','',str(p6.get('price_per_bottle','')) or '0') or 0)
     if pb2>0 and pb6<pb2:pct=round((pb2-pb6)/pb2*100)
    except Exception:pct=0
   save_txt=f' — Save Up To {pct}%' if pct>0 else ''
   cta_btn.string=f'🛒 Order {brand} Now{save_txt}'

 # ── Pricing bands' own "price-img-section" — the original template shows
 # a single flat screenshot (checkout.png) here instead of real package
 # cards, on BOTH the "Special Pricing Active Now" band AND the "Stock Is
 # Limited — Order Your Kit Today" band further down. Without a
 # publisher-supplied checkout screenshot to match it, the normal image
 # pipeline just removes that <img> outright (it's a single-purpose
 # "checkout" slot, never auto-filled with an unrelated photo), leaving an
 # empty gap — and no visible price at all — right under BOTH bands.
 # Replace each with a real 2/3/6-bottle pricing-cards row instead. ──
 def _fill_price_img_section(price_sec):
  # Card layout/copy modeled on the official product page's own pricing
  # cards (per-bottle price, "YOU SAVE $X", guarantee checkmarks, payment
  # icons, a highlighted centered best-value card) — publishers expect this
  # to look like the official offer, not a generic 3-box grid.
  pricing=sorted(data.get('pricing',[]),key=lambda p:p.get('bottles',0))
  if not pricing:return
  def _num(s):
   try:return float(re.sub(r'[^0-9.]','',str(s) or '0') or 0)
   except Exception:return 0.0
  best_bottles=max(p.get('bottles',0) for p in pricing)
  # "Regular price" reference — the smallest bundle's own per-bottle rate,
  # same convention this template already uses in its final-CTA section
  # ("Regular Price: $X per bottle" = the smallest tier's rate). Comparing
  # larger bundles against a REAL tier's own price (not an invented
  # "was $179" figure) keeps every number here traceable back to data the
  # publisher actually entered, per this tool's own verify-before-publish
  # policy — no fabricated "compare at" price.
  base_rate=_num(min(pricing,key=lambda p:p.get('bottles',0)).get('price_per_bottle',0))
  ordered=pricing
  if len(pricing)==3:
   best=max(pricing,key=lambda p:p.get('bottles',0))
   others=[p for p in pricing if p is not best]
   ordered=[others[0],best,others[1]]
  payment_icons=(
   '<div style="display:flex;justify-content:center;gap:6px;margin:12px 0;flex-wrap:wrap;">'
   '<span style="background:#1a1f71;color:#fff;font-size:.62rem;font-weight:800;padding:4px 8px;border-radius:4px;font-style:italic;">VISA</span>'
   '<span style="background:#eb001b;color:#fff;font-size:.62rem;font-weight:800;padding:4px 8px;border-radius:4px;">MC</span>'
   '<span style="background:#ff6000;color:#fff;font-size:.62rem;font-weight:800;padding:4px 8px;border-radius:4px;">DISC</span>'
   '<span style="background:#2e77bc;color:#fff;font-size:.62rem;font-weight:800;padding:4px 8px;border-radius:4px;">AMEX</span></div>')
  cards_html=[]
  for p in ordered:
   bottles=p.get('bottles',0)
   is_best=bottles==best_bottles and len(pricing)>1
   is_middle=(not is_best) and len(pricing)==3 and p is ordered[2]
   img=_get_img(images,f'bottle-{bottles}')
   img_html=(f'<img src="{html.escape(safe_rel(img))}" alt="{html.escape(brand)} {bottles} bottle package" '
              'style="max-width:130px;max-height:160px;margin:14px auto;display:block;">') if img else ''
   rate=_num(p.get('price_per_bottle',0));total=_num(p.get('total',0)) or rate*bottles
   regular_total=base_rate*bottles;save=regular_total-total
   shipping_txt=str(p.get('shipping','') or '')
   is_free_ship='free' in shipping_txt.lower()
   price_num=re.sub(r'[^0-9.]','',str(p.get('price_per_bottle','')))
   if is_best:
    save_line=(f'<div style="color:#ffd75e;font-weight:800;font-size:.92rem;margin-bottom:10px;">✅ YOU SAVE ${save:,.0f}</div>' if save>0 else '')
    total_line=(f'<span style="text-decoration:line-through;color:#a9c6d8;">${regular_total:,.0f}</span> ' if save>0 else '')
    cards_html.append(
     '<div style="flex:1.12;min-width:250px;max-width:300px;background:linear-gradient(165deg,#3f85ad,#1a4b63);'
     'border-radius:20px;overflow:hidden;box-shadow:0 16px 36px rgba(0,0,0,.2);transform:translateY(-10px);'
     'border:2px solid #fff;align-self:flex-start;">'
     '<div style="background:#fff;color:var(--primary,#1a4b63);text-align:center;padding:12px 8px;'
     'font-weight:900;font-size:1.05rem;letter-spacing:.03em;">BEST OFFER!</div>'
     '<div style="padding:22px 20px 26px;text-align:center;">'
     f'<div style="font-size:2rem;font-weight:900;color:#fff;letter-spacing:.02em;">{bottles} BOTTLES</div>'
     f'<div style="color:#cfe4f2;font-size:.85rem;">{bottles*30} Day Supply</div>'
     +img_html+
     '<div style="display:flex;align-items:flex-end;justify-content:center;gap:3px;margin:4px 0 8px;">'
     '<span style="font-size:1.5rem;font-weight:800;color:#fff;margin-bottom:10px;">$</span>'
     f'<span style="font-size:3.6rem;font-weight:900;color:#fff;line-height:.85;">{price_num}</span>'
     '<span style="font-size:.82rem;font-weight:700;color:#e6f2fa;text-align:left;line-height:1.15;margin-bottom:6px;">Per<br/>Bottle</span></div>'
     +save_line+
     '<div style="border-top:1px dashed rgba(255,255,255,.4);margin:0 0 10px;"></div>'
     '<div style="color:#fff;font-weight:700;font-size:.85rem;margin-bottom:4px;">✅ BIGGEST DISCOUNT</div>'
     '<div style="color:#fff;font-weight:700;font-size:.85rem;margin-bottom:16px;">✅ 60 DAYS GUARANTEE</div>'
     f'<a href="#" class="btn-primary" rel="nofollow sponsored" target="_blank" style="display:block;'
     'background:linear-gradient(180deg,#ffd75e,#f2a900);color:#182236;padding:15px;border-radius:10px;'
     'font-weight:900;text-decoration:none;font-size:1.08rem;margin-bottom:12px;">🛒 BUY NOW!</a>'
     +payment_icons+
     f'<div style="font-size:.85rem;color:#fff;margin-top:8px;">TOTAL: {total_line}${total:,.0f}</div>'
     f'<div style="font-size:.85rem;font-weight:800;color:{"#ffd75e" if is_free_ship else "#e6f2fa"};">'
     f'+ {html.escape(shipping_txt.upper()) if shipping_txt else "SHIPPING VARIES"}</div>'
     '</div></div>')
   else:
    band_color='#1d6484' if is_middle else '#7fc4e0'
    band_label='Most Popular' if is_middle else 'Basic Offer'
    save_line=(f'<div style="color:#d98a1f;font-weight:700;font-size:.88rem;margin-bottom:12px;">✅ YOU SAVE ${save:,.0f}</div>' if save>0 else '<div style="margin-bottom:12px;"></div>')
    total_line=(f'<span style="text-decoration:line-through;color:#999;">${regular_total:,.0f}</span> ' if save>0 else '')
    cards_html.append(
     f'<div style="flex:1;min-width:220px;max-width:270px;background:#fff;border-radius:18px;overflow:hidden;'
     'box-shadow:0 8px 22px rgba(0,0,0,.10);border:2px solid #e8f3fa;">'
     f'<div style="background:{band_color};color:#fff;text-align:center;padding:11px 8px;font-weight:800;'
     f'font-size:.95rem;letter-spacing:.02em;">{band_label}</div>'
     '<div style="padding:22px 18px 24px;text-align:center;">'
     f'<div style="font-size:1.6rem;font-weight:900;color:#182236;letter-spacing:.02em;">{bottles} BOTTLES</div>'
     f'<div style="color:#888;font-size:.82rem;">{bottles*30} Day Supply</div>'
     +img_html+
     '<div style="display:flex;align-items:flex-end;justify-content:center;gap:2px;margin:2px 0 6px;">'
     '<span style="font-size:1.15rem;font-weight:800;color:#182236;margin-bottom:8px;">$</span>'
     f'<span style="font-size:2.8rem;font-weight:900;color:#182236;line-height:.85;">{price_num}</span>'
     '<span style="font-size:.75rem;font-weight:700;color:#555;text-align:left;line-height:1.1;margin-bottom:4px;">Per<br/>Bottle</span></div>'
     +save_line+
     '<div style="border-top:1px dashed #ddd;margin:0 0 10px;"></div>'
     '<div style="color:#333;font-weight:700;font-size:.82rem;margin-bottom:16px;">✅ 60 DAYS GUARANTEE</div>'
     f'<a href="#" class="btn-primary" rel="nofollow sponsored" target="_blank" style="display:block;'
     'background:#c9cdd2;color:#182236;padding:13px;border-radius:10px;font-weight:900;text-decoration:none;'
     'font-size:1rem;margin-bottom:12px;">🛒 BUY NOW!</a>'
     +payment_icons+
     f'<div style="font-size:.82rem;color:#333;margin-top:8px;">TOTAL: {total_line}${total:,.0f}</div>'
     f'<div style="font-size:.82rem;font-weight:{"800;color:#1d8a4a" if is_free_ship else "600;color:#333"};">'
     f'+ {html.escape(shipping_txt.upper()) if shipping_txt else "SHIPPING VARIES"}</div>'
     '</div></div>')
  cards_block=BeautifulSoup(
   '<div style="display:flex;gap:20px;flex-wrap:wrap;justify-content:center;align-items:flex-end;'
   'max-width:1040px;margin:0 auto;padding:20px 20px 44px;">'+''.join(cards_html)+'</div>','html.parser')
  price_sec.clear()
  price_sec.append(cards_block)

 for band_id in ('order-breathizen','buy-breathizen'):
  band_el=soup.find(id=band_id)
  price_sec=band_el.find_next_sibling('section',class_=re.compile(r'\bprice-img-section\b',re.I)) if band_el else None
  if price_sec:_fill_price_img_section(price_sec)

def _decompose_unused_qa_slots(sub_heads):
 """A source template's Q&A-style grid/step-list is often padded out to a
 fixed slot count (e.g. 6 cards) regardless of how many real qa_items exist
 to fill it — the unused slots carry no h3/h4/h5 of their own, so the fill
 loop just above this call (which only ever iterates the headings it
 actually found) never reaches them, and they survive on every generated
 site as bare empty cards/steps sitting in the same grid as the real ones
 (e.g. three empty <div class="ge-card"></div> next to three real ones, or
 three numbered-but-blank steps in a "6-step" checklist that only ever had
 3 real steps). Walk up from a real, surviving heading to find the level at
 which siblings share its class (the repeating "card"/"step" unit — this
 may be one level up for a flat card grid, or two for a step-list where the
 heading sits inside an extra wrapper div next to the step's number), then
 drop any sibling at that level that has no heading of its own."""
 if not sub_heads:return
 hop=sub_heads[0].parent
 for _ in range(3):
  if hop is None or hop.parent is None:break
  own_class=hop.get('class')
  siblings=hop.parent.find_all(hop.name,recursive=False)
  if len(siblings)>=2 and sum(1 for s in siblings if s.get('class')==own_class)>=2:
   for sib in list(siblings):
    if sib.get('class')==own_class and not sib.find(['h3','h4','h5']):
     sib.decompose()
   return
  hop=hop.parent

def _rewrite_all_sections(soup,data,brand,images=None,desc_used=None,blog_articles=None):
 """Rewrite ALL sections — named and unnamed — with actual product content.
 `desc_used` is the same single-element mutable flag populate() threads
 through its own hero/What-Is handling — see its definition there. Default
 to a fresh, unshared one when called standalone so this function still
 behaves sensibly outside populate()'s own call."""
 images=images or []
 if desc_used is None:desc_used=[False]
 ingredients=data.get('ingredients',[])
 benefits=data.get('benefits',[])
 how_it_works=data.get('how_it_works',[])
 description=data.get('description','')
 category=data.get('category','health supplement')
 serving=data.get('serving_info',{})

 # ── Category-specific claim baked into the top trust-strip (design 7's
 # ".mv-strip", sitting outside any <section> so nothing else in the
 # pipeline ever reaches it) — e.g. "🧠 Memory & Focus Support", a literal
 # promotional claim tied to the ORIGINAL scraped nootropic product. Nothing
 # else in populate() touches it, so every site generated from this
 # template kept advertising that specific, unrelated benefit regardless of
 # what the new product actually is (a digestive-health site literally
 # claiming "Memory & Focus Support" at the top of every page).
 strip_el=soup.find(class_=re.compile(r'-strip\b',re.I))
 if strip_el:
  for span in strip_el.find_all('span'):
   if re.search(r'memory\s*&?\s*focus|focus\s*&?\s*memory',span.get_text(),re.I):
    span.string=f'{_support_phrase(category).title()} Support'
    break

 # Some templates repeat the same heading pattern in two different places
 # (e.g. a real "How To Use {brand}" content block, plus an unrelated
 # footer-reminder block that happens to share a keyword like "routine").
 # Only the first match should be treated as the real section — every later
 # match for the same category is a ghost duplicate with no real content of
 # its own, so it gets removed outright instead of getting a heading
 # rewritten over an otherwise-empty section.
 handled_categories=set()

 # Process every section in the page
 for sec in soup.find_all('section'):
  sid=(sec.get('id') or '').lower()
  # Skip already-handled sections. "bonuses" is skipped too — that section
  # is fully built by _bonus_section_html() with its own "Bonus #N — Title"
  # headings, which otherwise trip the generic 'bonus' keyword branch below
  # and get their title/price-line text clobbered with different content.
  if sid in ('hero','home','what-is','benefits','ingredients','how-it-works',
             'reviews','pricing','faq','faqs','legal-content','bonuses'):continue
  sec_classes=' '.join(sec.get('class') or []).lower()
  # Design 4's "symptoms-section" carries no id of its own (the id sits on a
  # sibling title-band div instead, invisible to the sid check above), so it
  # falls through to this loop's generic "ANY other section with old brand
  # text" catch-all — which finds the old brand name mentioned somewhere in
  # the section's own text (the CTA blurb), then treats its 6 symptom-card
  # <h3>+<p> pairs as if they were generic 3-item Q&A content and decomposes
  # the "excess" 2 headings/paragraphs outright. _populate_design4_supplement
  # runs right after this function specifically to populate this section
  # correctly with the real AI-generated symptom list — it can't recover
  # cards whose <h3>/<p> this generic pass already destroyed, so skip it here.
  if 'symptoms-section' in sec_classes:continue

  # Get section heading text to identify it
  h_el=sec.find(['h1','h2','h3','h4'])
  heading_txt=(h_el.get_text() if h_el else '').strip().lower()
  all_text=sec.get_text().lower()

  # ── "Why Choose" / certifications / badges section ──
  # Heading-keyword matching alone misses designs whose actual "why..."
  # wording lives in a sibling <span class="eyebrow"> rather than the h_el
  # itself (h_el's own text ends up something generic like "Quality You Can
  # Verify" that matches none of these phrases) — leaving every badge on
  # that design 100% unchanged, original-brand copy on every generated
  # site. A design-spanning, content-based signal catches those too: 2+
  # child cards whose class literally contains "badge" (bpo-card-badge,
  # ge-card-badge, mv-card-badge...) is itself strong enough evidence this
  # is a trust-badge section, independent of the heading's exact wording.
  badge_card_count=sum(1 for c in sec.find_all(['div','article'])
                        if 'badge' in ' '.join(c.get('class') or []).lower() and c.find('img') and c.find(['h3','h4','h5']))
  if badge_card_count>=2 or any(w in heading_txt for w in ('why this','why choose','formula stays','stay narrow',
                                    'certifications','quality check','why people love',
                                    'people love','loved by','trusted by')):
   if h_el: h_el.string=f'Why People Choose {brand}'
   _replace_badge_cards(sec,brand,ingredients)
   continue

  # ── "Manufacturing / Quality Claims" section wrongly matching "What Is" —
  # design 5's source template reuses the exact "What Is {Brand}?" heading
  # text on this unrelated 3-card manufacturing-claims section (no img, just
  # h4+p per card) as well as on the real what-is section. Heading-only
  # matching below can't tell them apart, so this one used to fall into the
  # "What Is" branch instead: that branch pastes the full product description
  # into this section's first two cards' <p> tags (clobbering their real
  # copy) while never touching each card's own <h4> — leaving the original
  # scraped product's card headings (e.g. a literal "Korean Technology
  # Badge") on every generated site regardless of category. A real "what is"
  # section is prose (an image + paragraphs), never a grid of heading+text
  # cards, so use that shape — 3+ sibling cards, each with its own h4/h3 and
  # p, none of them a trust badge with an img — to route here instead.
  claim_cards=[c for c in sec.find_all(['div','article'])
               if c.find(['h3','h4','h5']) and c.find('p') and not c.find('img')]
  claim_cards=_dedup_leaf_elements(claim_cards)
  if len(claim_cards)>=3 and any(w in heading_txt for w in ('what is','about')):
   if h_el:h_el.string=f'{brand} Manufacturing & Quality Claims'
   items=[
    {'title':'FDA-Registered Facility','text':f'{brand} is produced in an FDA-registered facility.'},
    {'title':'GMP Manufacturing','text':'Manufactured under Good Manufacturing Practice guidelines for consistent quality.'},
    {'title':'No Harmful Additives','text':(f"The brand describes {brand} as using high-quality ingredients with no harmful "
                                             f"additives, a claim we could not independently verify beyond the brand's own pages.")},
   ]
   _replace_cards(sec,items)
   continue

  # ── "What Is" / "About" section ──
  if any(w in heading_txt for w in ('what is','about','deliberately narrow',
                                    'a deliberately','once-daily')):
   if h_el: h_el.string=f'What Is {brand}?'
   ps=sec.find_all('p')
   if ps:
    ps[0].string=description if not desc_used[0] else f'{brand} is a {category} formulated with {len(ingredients)} named ingredients.'
    if description:desc_used[0]=True
   if len(ps)>1:
    ps[1].string=(f'{brand} falls into the {category} category. '
                  f'As with any supplement, individual results vary.')
   # Remove pills/tags showing old product info
   for pill in sec.find_all(class_=re.compile('pill|tag|badge|chip',re.I)):
    txt=pill.get_text().strip()
    if any(w in txt.lower() for w in ['ingredient','amino','nitric','stimulant']):
     pill.decompose()
   continue

  # ── "Ten Things" / "Case For It" / "Before You Order" section ──
  if any(w in heading_txt for w in ('ten things','case for it','before you order',
                                    'worth knowing','things worth')):
   if h_el: h_el.string=f'Ten Things Worth Knowing About {brand}'
   # Build items from ingredients + benefits
   items=[]
   for ing in ingredients[:4]:
    items.append({'title':ing['name'],'text':_truncate_words(ing.get('description',''))})
   for ben in benefits[:6]:
    parts=ben.split(' — ',1) if ' — ' in ben else [ben,'']
    items.append({'title':parts[0],'text':parts[1] if len(parts)>1 else ''})
   _replace_cards(sec,items[:10])
   continue

  # ── How It Works (NO-ID version) ──
  if any(w in heading_txt for w in ('actually works','step by step','how it works',
                                    'the mechanism','mechanism')):
   if h_el: h_el.string=f'How {brand} Actually Works'
   ps=sec.find_all('p')
   if ps and how_it_works: ps[0].string=how_it_works[0].get('text','') if how_it_works else ''
   if len(ps)>1 and how_it_works and len(how_it_works)>1:
    ps[1].string=how_it_works[1].get('text','')
   hiw_items=[{'title':x.get('title',''),'text':x.get('text','')} for x in how_it_works]
   _replace_cards(sec,hiw_items)
   # Replace ALL callout boxes in this section
   for callout in sec.find_all(class_=re.compile('callout|flag|clever|genuine|note',re.I)):
    b=callout.find(['b','strong'])
    if b:b.string='How it works:'
    for t in list(callout.strings):
     if t.strip() and t!=b.string if b else True:
      cat=data.get('category','health')
      t.replace_with(f'{brand} is designed to support {cat} through its combination of ingredients working together.')
      break
   continue

  # ── Manufacturing / Quality Standards ──
  # This used to hardcode the exact same FDA-Registered Facility/GMP
  # Manufacturing/Money-Back Guarantee claims already used to fill the
  # trust-badge section above (_replace_badge_cards, matched on nearly
  # every design via its badge_card_count check) and the dedicated
  # Guarantee section handled further below — a design carrying this as
  # its own standalone card-grid section then showed the identical FDA/GMP
  # claims twice on the same page under two different headings. There's no
  # other honest, non-duplicate data source for these cards, so remove the
  # section rather than repeat claims already made elsewhere on the page.
  if any(w in heading_txt for w in ('manufacturing','quality','plainly stated',
                                    'production standards','made under')):
   sec.decompose()
   continue

  # ── Guarantee section ──
  # Some templates keep the guarantee heading in a sibling "title band"
  # outside the <section> entirely, leaving heading_txt empty here — the
  # section's own class name (e.g. class="guarantee-section") is a more
  # reliable signal than trying to keyword-match whatever marketing h3 the
  # template actually uses inside the section ("You Either Love The Results
  # — Or You Pay Nothing" mentions none of the guarantee keywords).
  sec_cls=' '.join(sec.get('class') or []).lower()
  if any(w in heading_txt for w in ('guarantee','money-back','refund','risk-free')) or 'guarantee' in sec_cls:
   if h_el: h_el.string=f'{brand} Money-Back Guarantee'
   ps=sec.find_all('p')
   guarantee_msg=data.get('guarantee_text') or (f'{brand} comes with a satisfaction guarantee. '
                         f'Visit the official site for current refund terms and conditions.')
   if ps: ps[0].string=guarantee_msg
   if len(ps)>1: ps[1].string='Contact customer support within the guarantee window for assistance.'
   if len(ps)>2: ps[2].string=f'{brand} orders are backed by a straightforward, hassle-free refund process.'
   for extra in ps[3:]:extra.decompose()
   continue

  # ── "X vs. A Competitor" comparison section (e.g. design 7's "MemoVolt
  # vs. A Caffeine-Based Focus Pill") — this framing (comparing against a
  # specific rival product category, like a stimulant-based focus pill) is
  # inherent to the ORIGINAL scraped product and its category; there's no
  # honest way to generalize a fabricated "X vs. Y" comparison to whatever
  # unrelated product this template gets reused for, and the section's own
  # two-column layout is <h4> followed by a <ul> of bullet claims, not the
  # <h4>+<p> shape the generic Q&A fallback below expects. Left to that
  # fallback, it only rewrites the two <h4> headings (with unrelated "What
  # Makes Different"/"Who Is For" filler) and leaves the <ul> — the original
  # competitor-specific bullet claims (caffeine, jitters, ingredient counts
  # that don't match this product) — completely untouched on every site.
  # Remove the section outright rather than fabricate or leave stale claims.
  compare_cols=_dedup_leaf_elements([c for c in sec.find_all(['div','article'])
                    if c.find(['h3','h4','h5'],recursive=False) and c.find('ul',recursive=False)])
  if len(compare_cols)>=2 and re.search(r'\bvs\.?\b',heading_txt):
   sec.decompose()
   continue

  # ── "What Makes Different" section ──
  # This used to refill the section's cards from the same `benefits` list
  # already used for the page's own dedicated Benefits section — whenever a
  # design also has one of these as a separate, standalone card-grid section
  # (not the 3-item Who-For/Different/How-To-Get Q&A pattern handled
  # elsewhere), the result was two sections on the SAME page showing
  # word-for-word identical card headings and copy under different
  # headings. There's no other honest, non-duplicate data source to fill an
  # arbitrary N-card grid here, so remove the section rather than repeat
  # content the reader already saw a few scrolls up.
  if any(w in heading_txt for w in ('what makes','different','the difference',
                                    'sets it apart')):
   sec.decompose()
   continue

  # ── "How To Use" section ──
  # 'routine' was removed from this list — it's broad enough to also match
  # an unrelated final discount-CTA banner's own heading ("Ready To Start
  # Your {brand} Routine?"), stealing that section away from the dedicated
  # "Ready To Start" handler below (which is the one that actually knows
  # how to populate its image/price/CTA button — this generic handler only
  # ever touches the heading and step cards).
  if any(w in heading_txt for w in ('how to use','how to take','usage','directions',
                                    'correctly','getting the most')):
   if 'how_to_use' in handled_categories:
    # A second section matching this same heading pattern is a ghost
    # duplicate — it has no content of its own, so give it real content
    # again would just repeat the first section verbatim; remove it.
    sec.decompose()
    continue
   handled_categories.add('how_to_use')
   if h_el: h_el.string=f'How To Use {brand}'
   # 'how_it_works' describes the MECHANISM (why the ingredients work) and
   # already has its own dedicated section elsewhere on this page — reusing
   # it here for actual usage/dosage instructions made two sections show
   # identical step content. A "how do I take it" FAQ answer already exists
   # for the exact dosage details, so this card points there instead of
   # repeating that answer's own sentence word-for-word (a second section
   # showing the FAQ's exact text back-to-back on the same page reads as
   # duplicated content, even though it's technically accurate either way).
   dosage_faq=next((f for f in data.get('faqs',[]) if any(w in f.get('q','').lower()
                    for w in ('how do i take','how to take','how do you take','dosage'))),None)
   items=[
    {'title':'Follow label directions','text':f'Take {brand} exactly as instructed on the product label — see the FAQ below for the full serving details.' if dosage_faq else f'Use {brand} as directed on the official product label.'},
    {'title':'Be consistent','text':'For best results, take daily as part of your regular wellness routine.'},
    {'title':'Consult your doctor','text':'If you have health conditions or take medications, consult a healthcare professional.'},
   ]
   _replace_cards(sec,items)
   alert_el=sec.find(class_=re.compile('alert',re.I))
   if alert_el:
    b=alert_el.find(['b','strong'])
    note=f'Do not exceed the recommended dose. Consult a healthcare professional before use if pregnant, nursing, or taking medication.'
    if b:b.string='Note: '
    for t in list(alert_el.strings):
     if t.strip() and (not b or t!=b.string):
      t.replace_with(note);break
    else:
     alert_el.append(note)
   continue

  # ── CTA / Ready To Start section ──
  if any(w in heading_txt for w in ('ready to start','ready to try','start your',
                                    'order now','get started','claim')):
   if h_el: h_el.string=f'Ready To Try {brand}?'
   ps=sec.find_all('p')
   if ps: ps[0].string=f'Visit the official {brand} website to see current pricing, packages and guarantee terms.'
   continue

  # ── References / Sources / Blog section ──
  if any(w in heading_txt for w in ('references','sources','evidence')):
   if h_el:h_el.string=f'{brand} — Evidence & References'
   # Remove old brand-specific research links (arginine/citrulline/blood pressure etc)
   refs_list=sec.find(['ul','ol'],class_=re.compile('refs|references|sources',re.I)) or sec.find(['ul','ol'])
   if refs_list:
    refs_list.clear()
    li=soup.new_tag('li')
    a=soup.new_tag('a',href='https://ods.od.nih.gov/factsheets/list-all/',
                    rel='noopener nofollow',target='_blank')
    a.string='Dietary Supplement Fact Sheets — NIH Office of Dietary Supplements'
    li.append(a)
    refs_list.append(li)
    # Same verified per-ingredient links the Ingredients section already
    # shows — merged in here too, so this is the one consolidated/complete
    # source list; the Ingredients section's own mention stays a compact,
    # contextual "see also" next to the ingredient cards, not a second,
    # independently-built list that could drift out of sync with this one.
    for name,url in _match_ingredient_authority_links(ingredients):
     li2=soup.new_tag('li')
     a2=soup.new_tag('a',href=url,rel='noopener',target='_blank')
     a2.string=f'{name} — NIH Office of Dietary Supplements'
     li2.append(a2)
     refs_list.append(li2)
   # Fix the callout referencing old ingredients
   for callout in sec.find_all(class_=re.compile('callout',re.I)):
    for a in callout.find_all('a'):a.decompose()
    note=(f'Always verify current ingredient research and clinical evidence directly from '
          f'the official {brand} product page. These statements have not been evaluated by the FDA.')
    callout.clear()
    nb=soup.new_tag('b');nb.string='Important context:';callout.append(nb)
    callout.append(' '+note)
   continue
  if 'bonus' in heading_txt or 'bonus' in ' '.join(sec.get('class') or []).lower():
   bonuses=data.get('bonuses',[])
   if bonuses:
    if h_el:h_el.string=f'Bonuses Included With {brand}'
    ps=sec.find_all('p')
    if ps:ps[0].string='Extras that may be included with qualifying orders — confirm current offer details at checkout.'
    _replace_cards(sec,[{'title':b.get('title',''),'text':b.get('description','')} for b in bonuses])
    # A fixed "$59 FREE" style value tag is the original scraped product's
    # own invented bonus pricing — never carry a fabricated dollar figure
    # over to a different product's bonus offer.
    for val in sec.find_all(class_=re.compile(r'bonus-value',re.I)):val.string='FREE'
    # _replace_cards() above only ever rewrites each card's heading/paragraph
    # text — it never touches <img> tags, so every bonus card's picture (and
    # its alt text, e.g. alt="Memory Shield Diet bonus") stayed exactly what
    # the ORIGINAL scraped product's own bonus graphics were, completely
    # disconnected from whatever new bonus title/description just got
    # written in next to it. Swap in a real uploaded "bonus-N"-slot image
    # when one exists (same matching the native pipeline's own bonus
    # builder uses); either way, always fix the alt text so it at least
    # stops describing a different product's bonus.
    resolved_bonus_imgs=_bonus_images(images,len(bonuses))
    for i,img_tag in enumerate(sec.find_all('img')):
     if i>=len(bonuses):break
     real_img=resolved_bonus_imgs[i] if i<len(resolved_bonus_imgs) else None
     alt_title=(_derive_bonus_title_from_filename(real_img) if real_img else None) or bonuses[i].get('title','')
     if real_img:img_tag['src']=safe_rel(real_img)
     if alt_title:img_tag['alt']=alt_title
   else:
    # No real bonus data — remove this section entirely rather than showing fake/generic bonus claims
    sec.decompose()
   continue
  if any(w in heading_txt for w in ('guides','blog','honest assessment')):
   if h_el:h_el.string=f'{brand} — Guides & Honest Assessment'
   # Link each teaser card to its REAL article under its real slug, using
   # that article's own title/description — previously every card here got
   # generic hardcoded title/description text (disconnected from the actual
   # generated blog/*.html pages) AND every card's href pointed at the same
   # "blog/index.html" regardless, so none of the 3 teasers actually linked
   # to the article it claimed to be. `blog_articles` is the SAME list the
   # real blog pages are built from, so a card here can never name/link an
   # article that doesn't exist.
   blog_links=sec.find_all('a',href=True)
   featured=(blog_articles or [])[:3]
   post_i=0
   for a in blog_links:
    cls=' '.join(a.get('class') or [])
    if 'ghost' in cls or 'btn' in cls:
     a.string=f'Visit The {brand} Blog';a['href']='blog/index.html';continue
    b=a.find(['b','strong']);span=a.find('span')
    if post_i<len(featured):
     art=featured[post_i]
     if b:b.string=art['h1']
     if span:span.string=_truncate_words(art['meta_desc'],140)
     a['href']=f'blog/{art["slug"]}.html'
     post_i+=1
    else:
     a.decompose()
   continue
  if any(w in heading_txt for w in ('research',)):
   continue  # Leave as-is or template handles

  # ── ANY other section with old brand text — generic rewrite ──
  # Previously this only swapped the brand token in the section heading and
  # left every paragraph underneath as the scraped original copy (with the
  # brand name substituted in later, but the actual claims — ingredient
  # names, product-type, specific figures — all unchanged). Rewrite the
  # actual content too: a leading intro paragraph, plus any Q&A-style
  # h3/h4 + following-<p> pairs (a very common pattern for "Who Is It For?"
  # / "What Makes It Special?" style blocks).
  if any(old.lower() in all_text for old in ['bloodpril','jellytide','vapocept',
                                              'breathizen','gelagen','memovolt']):
   if h_el:
    txt=h_el.get_text()
    for old in ['BloodPril','JellyTide','VapoCept','BreathiZen','Gelagen','MemoVolt']:
     txt=re.sub(re.escape(old),brand,txt,flags=re.I)
    h_el.string=txt
   combined=sec.find_all(['h3','h4','h5','p'])
   if combined and combined[0].name=='p' and combined[0] is not h_el:
    # This fallback has no idea what the section is actually about (its own
    # heading may live outside it entirely, e.g. design 4's "how to order"
    # title-band) — `description` is the only real product copy on hand,
    # but pasting it in again when some earlier section already used it
    # verbatim (hero, What-Is...) just repeats that same paragraph a second
    # or third time on the page. Drop the stale old-brand line instead of
    # guessing at unrelated filler text once the real description has
    # already been placed elsewhere.
    if not desc_used[0]:
     combined[0].string=description
     if description:desc_used[0]=True
    else:
     combined[0].decompose()
   sub_heads=[hh for hh in sec.find_all(['h3','h4','h5']) if hh is not h_el]
   if sub_heads:
    ing_names=', '.join(x['name'] for x in ingredients[:6]) if ingredients else ''
    qa_items=[
     (f'What Makes {brand} Different',
      (f'{brand} combines {len(ingredients)} named ingredients — {ing_names} — to support {_support_phrase(category)}.'
       if ing_names else f'{brand} is formulated to support {_support_phrase(category)} as part of a daily routine.')),
     (f'Who Is {brand} For?',
      f'Anyone looking for daily support for {_support_phrase(category)} as part of a healthy lifestyle. '
      f'As with any supplement, individual results vary.'),
     (f'How Do I Get {brand}?',
      f'{brand} is available through the official website. See the pricing section above for '
      f'current package options and the guarantee terms on the official product page.'),
    ]
    for i,h3 in enumerate(sub_heads):
     p=h3.find_next_sibling('p')
     if i<len(qa_items):
      h3.string=qa_items[i][0]
      if p:p.string=qa_items[i][1]
     else:
      h3.decompose()
      if p:p.decompose()
    _decompose_unused_qa_slots(sub_heads)
   continue

_PRODUCT_FORM_WORDS=(('gummy','gummies'),('capsule','capsules'),('tablet','tablets'),
 ('softgel','softgels'),('pill','pills'),('powder','powder'),('drop','drops'))
_GUMMY_WORD_RE=re.compile(r'\bgumm(?:y|ies)\b',re.I)

def _detect_product_form(data):
 """(singular,plural) word for this product's ACTUAL physical form, derived
 from serving_info/category/description — never assumed to be "gummy" just
 because a reference template's own scraped copy says so. Defaults to
 "capsule", the most common supplement format, when nothing else indicates
 the real form."""
 blob=' '.join(str(data.get('serving_info',{}).get(k,'')) for k in ('daily_serving','per_bottle'))
 blob+=' '+' '.join(str(data.get(k,'')) for k in ('category','description','tagline'))
 blob=blob.lower()
 for sing,plur in _PRODUCT_FORM_WORDS:
  if sing in blob or plur in blob:return sing,plur
 return 'capsule','capsules'

def _fix_product_form_words(soup,data):
 """Swap every stray "gummy"/"gummies" (visible text, meta content, alt
 text) for this product's real form word, case-preserved — left alone when
 the product genuinely is a gummy."""
 sing,plur=_detect_product_form(data)
 if sing=='gummy':return
 def repl(m):
  w=m.group(0)
  base=plur if w.lower()=='gummies' else sing
  if w.isupper():return base.upper()
  if w[0].isupper():return base[0].upper()+base[1:]
  return base
 for t in list(soup.find_all(string=True)):
  if not isinstance(t,NavigableString):continue
  if t.parent.name in ('script','style'):continue
  s=str(t)
  if _GUMMY_WORD_RE.search(s):t.replace_with(_GUMMY_WORD_RE.sub(repl,s))
 for tag in soup.find_all(attrs={'content':True}):
  if _GUMMY_WORD_RE.search(tag['content']):tag['content']=_GUMMY_WORD_RE.sub(repl,tag['content'])
 for tag in soup.find_all('img',alt=True):
  if _GUMMY_WORD_RE.search(tag['alt']):tag['alt']=_GUMMY_WORD_RE.sub(repl,tag['alt'])

def _populate_design5_fixes(soup,data,brand):
 """Design 5 (Gelagen)'s scraped template hardcodes its own product form
 and bonus count in a few spots _rewrite_all_sections' generic heading/card
 matching never reaches: the ingredients section's "Inside Every Gummy"
 eyebrow and every other stray "gummy"/"gummies" mention."""
 eyebrow=soup.find(class_=re.compile(r'\bge-eyebrow\b'),string=re.compile(r'Inside Every',re.I))
 if eyebrow:
  sing,_=_detect_product_form(data)
  eyebrow.string=f'Inside Every {sing.capitalize()}'
 _fix_product_form_words(soup,data)

def populate(soup,data,design='1',domain='',affiliate=''):
 brand=data['brand']
 slug=re.sub(r'[^a-z0-9]+','-',brand.lower()).strip('-')
 ingredients=data.get('ingredients',[])
 benefits=data.get('benefits',[])
 how_it_works=data.get('how_it_works',[])
 description=data.get('description','')
 category=data.get('category','health supplement')
 faqs=data.get('faqs',[])
 images=data.get('images',[])
 serving=data.get('serving_info',{}) or {}
 # A single-element list (not a bool) so it can be mutated in place from
 # every section handler below AND from _rewrite_all_sections() after it's
 # passed in — the raw `description` string is the ONE piece of real
 # product copy every section handler reaches for by default, so without
 # tracking whether it's already been placed somewhere on the page (usually
 # the hero), it ends up pasted verbatim into the hero, the What-Is section
 # AND whatever leftover section matches _rewrite_all_sections()'s generic
 # old-brand-name fallback — three near-identical paragraphs on one page.
 _desc_used=[False]

 # ── 1. Nav bar ──
 # Logo — search the whole page, not just inside <nav>, since it commonly
 # sits as a sibling of <nav> inside a shared header wrapper. Replace the
 # entire logo element's content in one go rather than only the first text
 # node — brand names are frequently split across nested tags for styling
 # (e.g. Jelly<span>Tide</span>®), and patching just the first fragment
 # left the rest of the old brand name showing right next to the new one.
 # Word-bounded so "brand" doesn't also match e.g. FontAwesome's
 # "fa-brands" icon-set class prefix (fa-brands, fa-cc-visa...) — an
 # unbounded substring match grabs whichever payment/social icon happens
 # to come first in the document and stuffs the brand name as literal
 # text into it, while the real logo elsewhere is left untouched.
 logo=soup.find(class_=re.compile(r'\blogo\b|\bbrand\b',re.I))
 if logo:
  full_txt=logo.get_text()
  trademark='®' if '®' in full_txt else ('™' if '™' in full_txt else '')
  logo_target=logo.find(['h1','h2','h3','h4','h5'])
  if logo_target is None:
   # Some logos pair a decorative icon (<svg>/<img>) with the actual brand
   # text in its own styled wrapper (e.g. <svg>...</svg><span
   # class="vc-brandtype">Vapo<em>Cept</em></span>) — clearing the whole
   # logo element in that case deletes the icon AND loses the wrapper's
   # own text-color rule, leaving unstyled plain text that can vanish
   # against a dark navbar. Only narrow the target to that wrapper when
   # ALL of the logo's own visible text lives inside it (nothing directly
   # in the logo element itself) — otherwise (e.g. "Jelly<span>Tide</span>",
   # where "Jelly" sits outside the span) clearing just the wrapper would
   # leave that outer fragment behind, so keep clearing the whole logo.
   own_text=''.join(str(c) for c in logo.contents if isinstance(c,NavigableString)).strip()
   if not own_text:
    candidates=[c for c in logo.contents if getattr(c,'name',None) not in (None,'svg','img') and c.get_text(strip=True)]
    if len(candidates)==1:logo_target=candidates[0]
  if logo_target is None:logo_target=logo
  logo_target.clear()
  logo_target.append(brand+trademark)
 # Nav links — update text AND href. A page can have more than one <nav>
 # (a desktop menu plus a separate mobile/sidebar menu) — only fixing the
 # first left every other one showing stale/blank old-template link text.
 nav_map=[
  ('how','How It Works','how-it-works.html'),
  ('ingredient','Ingredients','ingredients.html'),
  ('benefit','Benefits','benefits.html'),
  ('review','Reviews','reviews.html'),
  ('blog','Blog','blog/index.html'),
  ('pricing','Pricing','index.html#pricing'),
 ]
 for nav in soup.find_all('nav'):
  for a in nav.find_all('a'):
   txt=a.get_text().strip().lower()
   href=str(a.get('href','')).lower()
   cls=' '.join(a.get('class') or [])
   if 'logo' in cls or 'brand' in cls:continue
   if 'btn' in cls or 'order' in txt:
    a.string='Order Now';a['href']='index.html#pricing';continue
   for key,label,new_href in nav_map:
    if key in txt or key in href:
     a.string=label;a['href']=new_href;break

 # ── 2. Hero section ──
 # Prefer an element whose class actually says "hero" (many templates keep
 # <header> as nav-only chrome and put the real hero content in a sibling
 # <section class="hero-section">) — falling straight to soup.find('header')
 # first, as this used to, grabs the nav bar instead and leaves the real
 # hero title/description/benefits completely unrewritten.
 hero=soup.find(class_=re.compile(r'\bhero\b',re.I)) or section(soup,'hero','home') or soup.find('header')
 if not hero:
  for h in soup.find_all(['header','div']):
   if 'hero' in ' '.join(h.get('class') or []).lower():hero=h;break
 # The primary page <h1> sometimes sits outside the hero container entirely
 # (a sibling between the nav header and the hero section) — always rewrite
 # it regardless of where it lives, since it's the single most visible line
 # of old-brand copy on the page. On subpages, the stray product-title h1 is
 # decomposed outright by page_variant()/legal_page() (a page should only
 # ever have one h1 — their own compact banner/legal-content title), so the
 # fallback here must never grab that banner h1 and overwrite its text; skip
 # anything marked "page-banner-h1".
 page_h1=soup.find('h1',class_='product-title') or soup.find(
  lambda t:t.name=='h1' and 'page-banner-h1' not in (t.get('class') or []))
 if page_h1:
  _tagline=data.get('tagline',category)
  # The AI sometimes already writes the brand name into the tagline itself
  # (e.g. "Synogut — Natural Digestive Support...") — prepending "{brand} — "
  # unconditionally then produced a doubled "Synogut — Synogut — ..." H1.
  page_h1.string=_tagline if _tagline.strip().lower().startswith(brand.strip().lower()) else f"{brand} — {_tagline}"
 if hero:
  # H1/H2 tagline inside the hero block itself (skip if it's the same node
  # as page_h1, already handled above)
  h1=hero.find('h1') or hero.find(['h2','h3'])
  if h1 and h1 is not page_h1:h1.string=data.get('tagline',f'{brand} — Daily {category}')
  # Small uppercase "kicker" pill sitting just above the H1 (e.g. design 6's
  # <span class="... rounded-full ... uppercase ...">Daily Biotin Gummy
  # </span>) names the ORIGINAL scraped product's own specific format —
  # nothing above rewrites it, so every generated site kept advertising a
  # gummy/biotin format regardless of what this product actually is.
  kicker=hero.find('span',class_=re.compile(r'rounded-full',re.I))
  if kicker and kicker.find_previous_sibling() is None and (kicker.find_next_sibling() is h1 or kicker.find_next_sibling(['h1','h2','h3']) is h1):
   kicker.string=category.title()
  # Promo / savings banner — never keep a fabricated dollar figure from the
  # original template; keep it brand-specific but numerically honest.
  for banner in hero.find_all(class_=re.compile(r'sale-banner|promo-banner|\bbanner\b',re.I)):
   banner.string=f'Save More With Multi-Bottle {brand} Bundles — Free Shipping Included'
  # Description paragraph(s) — a template may have more than one; the first
  # becomes the real product description, the second (if present) gets a
  # second distinct AI-written line, any further ones are dropped rather
  # than left as stale copy. A paragraph that reads like a fabricated
  # rating/customer-count claim ("★★★★★ 4.9/5 — 25,000+ Happy Customers")
  # is removed outright since we have no real number to put there.
  desc_lines=[l for l in (description,data.get('how_it_works_intro','')) if l]
  di=0
  for p in hero.find_all('p'):
   if p.find_parent(class_=re.compile('rating|stat|strip|chip|check',re.I)):continue
   ptxt=p.get_text()
   if re.search(r'★|\d[\d,]*\+?\s*(happy customers|reviews|verified buyers|5[- ]star)',ptxt,re.I):
    p.decompose();continue
   if di<len(desc_lines):
    p.string=desc_lines[di];di+=1
   else:
    p.decompose()
  if di>0 and desc_lines[0]==description:_desc_used[0]=True
  # Benefit bullet list (e.g. <ul class="benefits-lists"><li><b>Title</b> — text</li></ul>)
  # not already covered by the chip/check/facts patterns below.
  for ul in hero.find_all('ul'):
   if ul.find_parent(class_=re.compile('chip|check|facts|pills|tags',re.I)):continue
   lis=ul.find_all('li')
   if not lis or not any(li.find(['b','strong']) for li in lis):continue
   for i,li in enumerate(lis):
    if i>=len(benefits):li.decompose();continue
    parts=benefits[i].split(' — ',1) if ' — ' in benefits[i] else [benefits[i],'']
    b=li.find(['b','strong'])
    if b:
     b.string=parts[0]
     rest=parts[1] if len(parts)>1 else ''
     for child in list(li.children):
      if child is not b and str(child).strip():child.replace_with(' — '+rest if rest else '');break
     else:
      if rest:li.append(' — '+rest)
    else:
     li.string=benefits[i]
  # Pill/tag
  for pill in hero.find_all(class_=re.compile('pill|tag|chip-label',re.I)):
   n=len(ingredients)
   pill.string=f'{n} Named Ingredients — {category}'
  # Stat strip
  # "figures" added: design 5's hero has a <div class="ge-figures"> stat
  # block (Ingredients / daily serving / guarantee) that this regex never
  # matched — it was never in this handler's class list at all — so every
  # generated site kept the ORIGINAL scraped product's own numbers verbatim
  # (literally "5 Ingredients" and "2 Gummies daily" on every site regardless
  # of this product's real ingredient count or capsule/gummy form).
  stat=hero.find(class_=re.compile('stat.strip|stat-strip|stats-row|figures',re.I))
  if stat:
   divs=[d for d in stat.find_all('div') if not d.find('div')]
   stat_vals=[(str(len(ingredients)),'Ingredients'),(_serving_per_day_label(serving),'Capsules'),('60-Day','Guarantee'),('USA','Made In')]
   for i,div in enumerate(divs[:4]):
    if i<len(stat_vals):
     b=div.find(['b','strong'])
     span=div.find('span')
     if b:b.string=stat_vals[i][0]
     if span:span.string=stat_vals[i][1]
  # Chip grid — replace with actual benefits
  chip=hero.find(class_=re.compile('chip.grid|chip-grid',re.I))
  if chip:
   chip_divs=chip.find_all('div',recursive=False) or chip.find_all(['div','span','li'])
   for i,div in enumerate(chip_divs):
    if i<len(benefits):div.string='✔ '+benefits[i]
    else:div.decompose()
  # Check list (bpo-check ul li)
  check=hero.find(class_=re.compile('check|checklist',re.I))
  if check:
   lis=check.find_all('li')
   for i,li in enumerate(lis):
    if i<len(benefits):li.string=benefits[i]
    else:li.decompose()
  # Facts list (pills/tags in facts ul)
  facts=hero.find(class_=re.compile('facts|pills|tags',re.I))
  if facts:
   items=[f'{len(ingredients)} ingredients',f'{serving.get("daily_serving") or "1-2 capsules"} daily','60-day guarantee','Made in USA']
   for i,li in enumerate(facts.find_all('li')):
    if i<len(items):li.string=items[i]
    else:li.decompose()
  # Two hero buttons
  btns=hero.find_all('a')
  main_btn=next((a for a in btns if 'btn' in ' '.join(a.get('class') or []) and 'ghost' not in ' '.join(a.get('class') or [])),None)
  ghost_btn=next((a for a in btns if 'ghost' in ' '.join(a.get('class') or [])),None)
  if main_btn:
   # This was a bare "From $49" regardless of the product's actual pricing
   # data — a stale figure carried over from whichever template product
   # originally had that price, left mismatched with this product's real
   # cheapest tier (e.g. still showing $49 when the lowest tier here is $59).
   _hero_pbs=[float(re.sub(r'[^0-9.]','',str(p.get('price_per_bottle','')) or '0') or 0) for p in data.get('pricing',[]) if p.get('price_per_bottle')]
   _hero_best_pb=min(_hero_pbs) if _hero_pbs else 0
   main_btn.string=f'Get {brand} — From ${_hero_best_pb:g}' if _hero_best_pb else f'Get {brand} — From $49'
   main_btn['href']='index.html#pricing'
  if ghost_btn:ghost_btn.string=f'What Is {brand}?';ghost_btn['href']=f'what-is-{slug}.html'
  # Callout boxes in hero — replace BloodPril-specific text
  for callout in hero.find_all(class_=re.compile('callout|flag|note',re.I)):
   b=callout.find(['b','strong'])
   if b:b.string='Good to know:'
   for t in list(callout.strings):
    if t.strip() and (not b or t!=b.string):
     t.replace_with(f'{brand} contains {len(ingredients)} named ingredients. See the official label for full ingredient and serving details.')
     break
  # Hero image
  if images:
   hero_img=next((p for p in images if Path(p).stem.lower()=='hero'),None) or images[0]
   for img in hero.find_all('img'):
    stem=(img.get('data-orig-stem') or Path(img.get('src','') or '').stem).lower()
    if not _is_keep(stem,design):
     img['src']=safe_rel(hero_img);img['alt']=f'{brand} product';img['data-populated']='1'
     # title="" isn't alt — scrub_image_alts() only ever rewrites alt, so a
     # scraped template's own image tooltip (e.g. "Rediscover What It Feels
     # Like to Breathe" on the respiratory-spray template) survives verbatim
     # under every unrelated product this template gets reused for, with
     # only the brand name swapped out by the brand-refs pass. Since we're
     # already replacing this image's identity, drop the stale tooltip too.
     if img.has_attr('title'):img['title']=img['alt']
     break

 # ── 3. What-is section ──
 sec=section(soup,'what-is','about')
 if sec:
  h=sec.find(['h2','h3'])
  if h:h.string=f'What Is {brand}? {len(ingredients)} Named Ingredients.'
  # Some templates put a simple intro + second paragraph directly under the
  # section; others structure it as an intro paragraph followed by several
  # h3-headed Q&A blocks ("Who Is It For?", "What Makes It Special?", "How
  # Do I Get It?") — each needs its own real content, not just the first
  # two <p> tags in document order (which may both land inside/after the
  # first Q&A pair and leave the rest as the original scraped copy).
  sub_heads=[hh for hh in sec.find_all(['h3','h4']) if hh is not h]
  # The hero above already pastes `description` in verbatim as its own lead
  # paragraph — reusing the exact same sentence again here reads as the
  # same paragraph shown twice in two different sections. Only the FIRST
  # section on the page to reach for `description` gets the real text;
  # every later one gets a short, distinct line instead.
  whatis_lead=description if not _desc_used[0] else f'{brand} is a {category} formulated with {len(ingredients)} named ingredients.'
  if description:_desc_used[0]=True
  if sub_heads:
   combined=sec.find_all(['h3','h4','p'])
   # There may be more than one leading <p> before the first sub-heading —
   # this used to also fill a second paragraph with how_it_works_intro, but
   # that field is mechanism-focused just like description, so the two
   # paragraphs routinely ended up saying the same thing in different words
   # (and how_it_works_intro is already used verbatim in its own How It
   # Works section elsewhere on the page). Only the first paragraph gets
   # real copy; any extra leading <p> is decomposed below instead of being
   # filled with redundant content.
   lead_lines=[whatis_lead] if description else []
   li=0
   for el in combined:
    if el.name!='p':break
    if li<len(lead_lines):el.string=lead_lines[li];li+=1
    else:el.decompose()
   ing_names=', '.join(x['name'] for x in ingredients[:6]) if ingredients else ''
   qa_items=[
    (f'Who Is {brand} For?',
     f'Anyone looking for daily support for {_support_phrase(category)} as part of a healthy lifestyle. '
     f'As with any supplement, individual results vary.'),
    (f'What Makes {brand} Different',
     (f'{brand} combines {len(ingredients)} named ingredients — {ing_names} — to support {_support_phrase(category)}.'
      if ing_names else f'{brand} is formulated to support {_support_phrase(category)} as part of a daily routine.')),
    (f'How Do I Get {brand}?',
     f'{brand} is available through the official website. See the pricing section above for '
     f'current package options and the guarantee terms on the official product page.'),
   ]
   for i,h3 in enumerate(sub_heads):
    p=h3.find_next_sibling('p')
    if i<len(qa_items):
     h3.string=qa_items[i][0]
     if p:p.string=qa_items[i][1]
    else:
     h3.decompose()
     if p:p.decompose()
   _decompose_unused_qa_slots(sub_heads)
  else:
   # A template may carry more than 2 leading paragraphs here (e.g. a
   # mechanism paragraph, a results-timeline paragraph, a manufacturing
   # blurb) — leaving anything past the first two untouched silently kept
   # the original scraped product's specific claims on every generated
   # site. Cycle through real content for as many paragraphs as exist.
   ps=sec.find_all('p')
   fill=[whatis_lead,
         f'{brand} falls into the {category} category. As with any supplement, individual results vary and it is not intended to diagnose, treat, cure or prevent any disease.',
         data.get('how_it_works_intro','') or f'{brand} combines {len(ingredients)} named ingredients formulated to support {_support_phrase(category)}.',
         f'Produced under standard manufacturing practices. See the official {brand} product label for full ingredient and usage details.']
   for i,p in enumerate(ps):
    if i<len(fill) and fill[i]:p.string=fill[i]
    else:p.decompose()
  # Callout — clear ALL content, keep only bold label + new text
  for callout in sec.find_all(class_=re.compile('callout|flag|note',re.I)):
   b=callout.find(['b','strong'])
   label='Straight talk:'
   note=f'{brand} is a dietary supplement, not a drug. It works best alongside a balanced diet and adequate hydration.'
   # Remove any leftover <a> links (old blog/clinical trial links)
   for a in callout.find_all('a'):a.decompose()
   callout.clear()
   if b or True:
    nb=soup.new_tag('b');nb.string=label;callout.append(nb)
   callout.append(' '+note)
  # Facts/pills
  facts=sec.find(class_=re.compile('facts|pills|tags|chips',re.I))
  if facts:
   bonus_count=len(data.get('bonuses',[]))
   items=[f'{len(ingredients)} ingredients',f'{serving.get("daily_serving") or "1-2 capsules"} daily','60-day guarantee']
   if bonus_count:
    items.append(f'{bonus_count} free bonus{"es" if bonus_count!=1 else ""}')
   for i,li in enumerate(facts.find_all('li')):
    if i<len(items):li.string=items[i]
    else:li.decompose()

 # ── 4. Benefits ──
 sec=section(soup,'benefits')
 if sec:
  h=sec.find(['h2','h3'])
  if h:h.string=f'What {brand} Is Formulated To Support'
  # No "intro"-classed <p> at all (e.g. design 6's plain
  # <p class="text-gray-600">) — fall back to the heading's own next <p>
  # sibling, the same structural relationship every design's markup uses
  # regardless of what it names the class.
  intro_p=sec.find('p',class_=re.compile('intro',re.I)) or (h.find_next_sibling('p') if h else None)
  if intro_p:intro_p.string=f'{brand} is formulated to support {_support_phrase(category)}. Here is what may change with consistent use:'
  # Title/description aren't always real <h3>/<h4>/<strong>/<p> tags — some
  # templates use plain divs like <div class="benefit-title">/"benefit-desc"
  # instead, which the old check below silently skipped entirely.
  cards=[]
  for el in sec.find_all(['div','article']):
   cls=' '.join(el.get('class') or []).lower()
   if any(k in cls for k in ('card','item','tile','feature')):
    if el.find(['h4','h3','strong']) or el.find(class_=re.compile('title',re.I)):
     cards.append(el)
  cards=_dedup_leaf_elements(cards)
  if not cards:
   # A template with no "card"/"item"/"tile"/"feature" class at all (e.g.
   # design 6's plain Tailwind <div><h3>...</h3><p>...</p><p>...</p></div>,
   # no distinguishing class anywhere) left `cards` empty and this whole
   # section untouched — every generated site kept showing the ORIGINAL
   # scraped product's own benefit claims regardless of brand/category.
   # Fall back to any div whose own DIRECT child is the heading.
   cards=[el for el in sec.find_all(['div','article']) if el.find(['h4','h3','strong'],recursive=False)]
   cards=_dedup_leaf_elements(cards)
  if cards:
   for i,card in enumerate(cards):
    if i<len(benefits):
     parts=benefits[i].split(' — ',1) if ' — ' in benefits[i] else [benefits[i],'']
     h4=card.find(['h4','h3','strong']) or card.find(class_=re.compile('title',re.I))
     p=card.find('p') or card.find(class_=re.compile('desc|text',re.I))
     desc_txt=parts[1] if parts[1] else f'Supports your daily {category} routine.'
     if h4:h4.string=parts[0]
     if p:p.string=desc_txt
     # A two-paragraph-per-card layout (e.g. design 6) has a second <p>
     # sibling that find('p') never reaches — left alone, it silently keeps
     # the original scraped product's own second paragraph of benefit copy
     # sitting right under the freshly-rewritten heading/first paragraph.
     if p:
      for extra_p in card.find_all('p'):
       if extra_p is not p:extra_p.decompose()
     icon_el=card.find(class_=re.compile(r'icon',re.I))
     # A "ribbon" layout (design 7's benefits section) keeps the icon as a
     # SIBLING of the title/body wrapper (both children of one outer
     # ".mv-ribbon" div) rather than a descendant of it, so it's invisible
     # to card.find() above — the icon then silently keeps whichever emoji
     # the original scraped product happened to use for that slot.
     if not icon_el and card.parent:icon_el=card.parent.find(class_=re.compile(r'icon',re.I))
     if icon_el and not icon_el.find(['img','svg']):icon_el.string=_pick_icon(parts[0],desc_txt)
    # Decompose the closest <li> ancestor (not just the matched card div)
    # when a bullet-list template wraps each card in its own list item —
    # removing only the inner div leaves an empty, still-visible bullet.
    else:(card.find_parent('li') or card).decompose()

 # ── 5. Ingredients ──
 sec=section(soup,'ingredients')
 if sec:
  h=sec.find(['h2','h3'])
  if h:h.string=f'What Are The Ingredients In {brand}?'
  # Subtitle/intro paragraph — either in a "bpo-head" wrapper, or a direct
  # class="...-intro" paragraph right under the section heading.
  head_div=sec.find(class_=re.compile('head',re.I))
  sub_p=((head_div.find('p') if head_div else None) or sec.find('p',class_=re.compile('intro',re.I))
         or (h.find_next_sibling('p') if h else None))
  if sub_p:
   ing_names=', '.join(x.get('name','') for x in ingredients[:5] if x.get('name'))
   sub_p.string=(f'{brand} is formulated with {len(ingredients)} named ingredients'
                 +(f' — including {ing_names} — ' if ing_names else ' ')
                 +'each listed individually below with the role it plays in the formula, so you can see exactly what you are taking before you buy.')
  cards=[]
  for el in sec.find_all(['div','article']):
   cls=' '.join(el.get('class') or []).lower()
   # Some templates use a short section-specific prefix instead of a generic
   # "card"/"item"/"ingredient" class (e.g. class="ing-text" / "ing-alt-row")
   # — a plain keyword substring check misses those entirely, leaving every
   # ingredient card as the original scraped product's text.
   if (any(k in cls for k in ('card','item','ingredient')) or re.search(r'(?:^|\s)ing-',cls)) and el.find(['h4','h3','h5']):cards.append(el)
  cards=_dedup_leaf_elements(cards)
  if not cards:
   # No "card"/"item"/"ingredient"/"ing-" class anywhere (e.g. design 6's
   # plain Tailwind <div class="bg-white ..."><h3>Name</h3><p>...</p>
   # <p>...</p></div>, no distinguishing class at all) — fall back to any
   # div whose own DIRECT child is the heading, the same relaxation used
   # for Benefits above.
   cards=[el for el in sec.find_all(['div','article']) if el.find(['h4','h3','h5'],recursive=False)]
   cards=_dedup_leaf_elements(cards)
  if not cards:
   # Last-resort fallback when the template truly has no per-ingredient
   # wrapper element at all — flatten every heading/paragraph positionally.
   # Unsafe when a section intro paragraph or multi-paragraph cards are
   # present (shifts every entry after the first), so only used once the
   # card-based heuristics above have both failed to find anything. Exclude
   # sub_p explicitly — it's the section's own intro paragraph (already set
   # two lines up), not an ingredient's — without this, sec.find_all('p')
   # counts it as entry [0] and overwrites it with the first ingredient's
   # own description, clobbering the intro text that was just written.
   heads=sec.find_all(['h3','h4','h5']);pars=[p for p in sec.find_all('p') if p is not sub_p]
   for i,x in enumerate(ingredients):
    if i<len(heads):heads[i].string=x['name']
    if i<len(pars):pars[i].string=x.get('description','')
  else:
   # If AI gave more ingredients than the template has card slots for,
   # clone the last card as a template for the extra ingredients so
   # every ingredient actually gets shown (not silently dropped). Clone the
   # closest <li> ancestor when one wraps the card (e.g. <ul><li><div
   # class="ingredient-content">...) — cloning just the inner div and
   # appending it straight into that <li>'s parent skips the <li> tag
   # entirely, breaking the list markup/numbering for every cloned entry.
   if len(ingredients)>len(cards) and cards:
    template_card=cards[-1]
    template_unit=template_card.find_parent('li')
    if template_unit is None:
     # A card with no <li> ancestor might still not be a standalone,
     # independently-repeatable unit — an alternating-row layout (design 4's
     # "ing-alt-row" > .ing-text + .ing-img-col) pairs the text card with an
     # image column as ONE visual row. Cloning just the leaf .ing-text and
     # appending it back into that same parent stuffs every extra
     # ingredient's text into the last row instead of giving each one its
     # own row — clone the whole row instead when the card has such siblings.
     # But a sibling that is itself a separate card (has its own heading) —
     # e.g. design 1's 3-card "bpo-grid" — means the parent is a multi-card
     # GRID, not a one-ingredient row; cloning the whole parent there drags
     # along the other 2 (unrelated, still-original-template) sibling cards
     # every time, which then never get touched again by the populate loop
     # below (only the single matched leaf card gets added to `cards`) and
     # sit on the page as duplicated old-product leftovers. Only treat the
     # parent as a clonable "row" when its siblings are non-card companions.
     card_parent=template_card.parent
     row_siblings=[c for c in card_parent.find_all(True,recursive=False) if c is not template_card]
     sibling_cards=[c for c in row_siblings if c.find(['h4','h3','h5'])]
     template_unit=card_parent if row_siblings and not sibling_cards else template_card
    grid=template_unit.parent
    card_name=template_card.name
    card_cls=template_card.get('class') or []
    for i in range(len(cards),len(ingredients)):
     new_unit_soup=BeautifulSoup(str(template_unit),'html.parser')
     new_unit=new_unit_soup.find(template_unit.name)
     # Design 4 names this element "ing-counter" — neither "idx" nor
     # "number" matches that, so its cloned rows silently kept whatever
     # digit the template row itself had (every extra ingredient showing
     # the same stale "05" instead of counting up 06, 07, 08...).
     idx_el=new_unit.find(class_=re.compile('idx|counter',re.I))
     if idx_el:idx_el.string=str(i+1)
     num_el=new_unit.find(class_=re.compile('number',re.I))
     if num_el and num_el is not idx_el:num_el.string=str(i+1)
     grid.append(new_unit)
     if new_unit.name==card_name and (new_unit.get('class') or [])==card_cls:
      new_card=new_unit
     else:
      new_card=new_unit.find(card_name,class_=card_cls) if card_cls else new_unit.find(card_name)
     cards.append(new_card or new_unit)
   for i,card in enumerate(cards):
    if i<len(ingredients):
     h4=card.find(['h4','h3','h5'])
     # Some templates have two <p> tags per ingredient — a short subtitle
     # badge (e.g. "DIGESTION & APPETITE") followed by the real
     # description. Target the last one (or an explicit ".desc"-class
     # element) so the actual description gets replaced, not the badge.
     all_ps=card.find_all('p')
     desc_el=card.find(class_=re.compile('desc',re.I)) or (all_ps[-1] if all_ps else None)
     subtitle_el=card.find(class_=re.compile('subtitle|tag|label|role',re.I))
     name=ingredients[i]['name'];role=ingredients[i].get('role','');desc=ingredients[i].get('description','')
     if h4:h4.string=name
     # Number badge ("1","2","3"...) — only ever set for CLONED cards
     # before (zero-padded: "04","05"...), so the ORIGINAL template's own
     # first few cards kept their scraped "1","2","3" while every ingredient
     # beyond that showed a zero-padded number — "1,2,3,04,05,06...". Set it
     # here, the same plain (never zero-padded) way, for every card.
     idx_el=card.find(class_=re.compile('idx|counter',re.I))
     if idx_el:idx_el.string=str(i+1)
     if subtitle_el and subtitle_el is not desc_el:
      subtitle_el.string=role.upper() if role else category.upper()
     if desc_el:desc_el.string=desc
     # A layout with two full-length <p> tags per card and no distinguishing
     # subtitle/badge class on either one (e.g. design 6) — desc_el above
     # only ever reaches the last of the two, leaving the first exactly as
     # scraped: the ORIGINAL product's own ingredient description, still
     # sitting right under this ingredient's freshly-rewritten name.
     for extra_p in card.find_all('p'):
      if extra_p is not desc_el and extra_p is not subtitle_el:extra_p.decompose()
     # A per-ingredient external "Source: ..." citation link names the
     # OLD scraped product's own nutrient fact sheet (e.g. a Vitamin-B12 NIH
     # page under a card now describing Ginger) — no safe substitute URL
     # exists for an arbitrary new ingredient, so remove the now-mismatched
     # citation rather than leave it pointing at unrelated information.
     for a_tag in card.find_all('a'):
      if re.match(r'^\s*Source\s*:',a_tag.get_text(),re.I):a_tag.decompose()
     # Design 4's icon isn't inside this leaf "ing-text" card at all — it
     # lives in a sibling ".ing-img-col" under the shared "ing-alt-row"
     # parent, so a plain card.find() here always comes back empty. Only
     # matching "ing-visual" also missed design 7's own icon wrapper
     # (class="mv-ing-icon") entirely — that design's icon element was never
     # found, so its per-card emoji were never rewritten at all and just
     # kept whatever the ORIGINAL scraped template happened to have (mostly
     # a single repeated 🧠, since that design's own icons were themselves
     # copy-pasted for most cards) regardless of what each new ingredient
     # actually is (a 🧠 brain emoji next to "Peppermint" or "Ginger").
     icon_el=card.find(class_=re.compile(r'ing-visual|ing-icon',re.I))
     if not icon_el and card.parent:icon_el=card.parent.find(class_=re.compile(r'ing-visual|ing-icon',re.I))
     if icon_el and not icon_el.find(['img','svg']):icon_el.string=_pick_ing_icon(name,role,desc)
    # Same orphaned-wrapper risk as the benefits list above — decompose the
    # <li> ancestor, not just the matched inner content div.
    else:(card.find_parent('li') or card).decompose()
  # Callout in ingredients — replace limitation text. Previously this only
  # swapped the FIRST text node and left whatever else the scraped template
  # happened to have after it (often its own "...ingredients page</a>."
  # anchor) untouched, producing a broken run-on sentence like "...before
  # publication.ingredients page." Clear everything but the bold label and
  # write one complete sentence with a working link instead.
  for callout in sec.find_all(class_=re.compile('callout|flag|note|limitation',re.I)):
   b=callout.find(['b','strong'])
   if b:b.string='Note:'
   for child in list(callout.contents):
    if child is b:continue
    if hasattr(child,'decompose'):child.decompose()
    else:child.extract()
   callout.append(BeautifulSoup(
    f' Always check the official {html.escape(brand)} label for the current ingredient list and '
    f'serving directions. See our <a href="ingredients.html">ingredients page</a> for details.','html.parser'))
  _authority_links=_match_ingredient_authority_links(ingredients)
  links_html=ingredient_authority_links_html(_authority_links,_reuse_eyebrow_class(sec))
  if links_html:_section_wrap(sec).append(BeautifulSoup(links_html,'html.parser'))

 # ── 6. How it works ──
 sec=section(soup,'how-it-works')
 if sec:
  h=sec.find(['h2','h3'])
  if h:h.string=f'How Does {brand} Work?'
  # Top-level subtitle paragraph — either nested in a "bpo-head" wrapper, or
  # a direct class="...-intro" paragraph right under the section heading
  # (the same two patterns already handled for benefits/ingredients above —
  # missing this fallback here left e.g. class="how-it-works-intro" as the
  # original scraped product's own summary line, brand name aside).
  head_div=sec.find(class_=re.compile('head',re.I))
  sub_p=((head_div.find('p') if head_div else None) or sec.find('p',class_=re.compile('intro',re.I))
         or (h.find_next_sibling('p') if h else None))
  if sub_p:
   sub_p.string=data.get('how_it_works_intro') or (how_it_works[0].get('text','') if how_it_works else '')
  # Intro paragraph inside bpo-split (image+text block) — may contain nested <em>
  split=sec.find(class_=re.compile('split',re.I))
  if split:
   all_ps=split.find_all('p')
   # First <p> in split is typically the image caption (small, centered)
   # Second <p> is the real intro text (larger, contains the nested <em>)
   intro_p=None
   for p in all_ps:
    style=p.get('style','')
    if 'text-align' not in style and len(p.get_text())>60:
     intro_p=p;break
   if not intro_p and len(all_ps)>1:intro_p=all_ps[1]
   if intro_p:
    for em in intro_p.find_all('em'):em.decompose()
    intro_p.clear()
    intro_note=(f"{brand}'s official summary gives a simplified overview. "
                f"The steps below break down how the ingredients are intended to work together.")
    intro_p.append(intro_note)
   # Image caption under the how-it-works graphic (short, centered text)
   for p in all_ps:
    if p is not intro_p and 'text-align' in p.get('style',''):
     p.string="The manufacturer's simplified overview";break
  cards=[]
  for el in sec.find_all(['div','article']):
   cls=' '.join(el.get('class') or []).lower()
   if any(k in cls for k in ('card','item','step')) and el.find(['h4','h3','h5']):cards.append(el)
  cards=_dedup_leaf_elements(cards)
  if not cards:
   # No "card"/"item"/"step" class at all (e.g. design 6's plain Tailwind
   # <div><div class="icon-circle">...</div><h3>...</h3><p>...</p>
   # <p>...</p></div>, nothing distinguishing) — same relaxed fallback as
   # Benefits/Ingredients above: any div whose own DIRECT child is the
   # heading.
   cards=[el for el in sec.find_all(['div','article']) if el.find(['h4','h3','h5'],recursive=False)]
   cards=_dedup_leaf_elements(cards)
  for i,card in enumerate(cards):
   if i<len(how_it_works):
    h4=card.find(['h4','h3','h5']);p=card.find('p')
    if h4:h4.string=how_it_works[i].get('title','')
    if p:p.string=how_it_works[i].get('text','')
    # Same two-paragraph-per-step issue as Benefits/Ingredients — a second
    # <p> sibling left alone still shows the original scraped step's text.
    if p:
     for extra_p in card.find_all('p'):
      if extra_p is not p:extra_p.decompose()
   else:(card.find_parent('li') or card).decompose()
  # Closing summary line below the steps grid (e.g. "11 ingredients. 4
  # areas. One daily gummy.") — specific counts/product-type from the
  # original template, not this product.
  below=sec.find(class_=re.compile('below-para|steps-summary|summary-line',re.I))
  if below:
   below.string=(f'{len(ingredients)} named ingredients working together. '
                 f'Individual results vary with consistent daily use.')
  # Replace ALL callouts in how-it-works
  for callout in sec.find_all(class_=re.compile('callout|flag|clever|genuine',re.I)):
   for a in callout.find_all('a'):a.decompose()
   note=f'{brand} combines its ingredients to work together as part of a daily wellness routine.'
   callout.clear()
   nb=soup.new_tag('b');nb.string='How it works:';callout.append(nb)
   callout.append(' '+note)

 # ── 7. Reviews ──
 sec=section(soup,'reviews')
 if sec:
  h=sec.find(['h2','h3'])
  if h:h.string=f'What {brand} Customers Report'
  # Replace review card text only — keep names/photos. Match short class
  # abbreviations too (e.g. class="vc-rev") — a plain "review" substring
  # check misses those, leaving every testimonial untouched.
  # Prefer a matching <article> tag outright when one exists — it's the
  # natural semantic wrapper for a single review, and some templates nest
  # a SECOND element inside it whose class also contains "review" (e.g.
  # <article class="review-card"><div class="review-header">...<div
  # class="review-meta">...) — _dedup_leaf_elements then keeps that inner
  # meta wrapper (the innermost candidate) instead of the article, which
  # doesn't even contain the actual review-text paragraph as a descendant.
  review_articles=[el for el in sec.find_all('article') if any(k in ' '.join(el.get('class') or []).lower() for k in ('card','review','testimonial')) or re.search(r'\brev\b',' '.join(el.get('class') or []).lower())]
  if review_articles:
   review_cards=review_articles
  else:
   review_cards=[]
   for el in sec.find_all(['div','article']):
    cls=' '.join(el.get('class') or []).lower()
    if (any(k in cls for k in ('card','review','testimonial')) or re.search(r'\brev\b',cls)) and el.find('p'):
     review_cards.append(el)
   review_cards=_dedup_leaf_elements(review_cards)
  if not review_cards:
   # No "card"/"review"/"testimonial" class anywhere (e.g. design 6's plain
   # <div class="bg-cream p-8 rounded-2xl border border-beige">) — every
   # generated site kept the template's own placeholder testimonials
   # (written about a completely different product) untouched. Fall back to
   # the direct-child <div>s of the cards' shared grid/flex row — the
   # layout wrapper every one of these designs uses to lay testimonials out
   # side by side — as long as each one actually has its own <p> inside.
   grid=sec.find(class_=re.compile(r'\bgrid\b',re.I))
   if grid:
    review_cards=[c for c in grid.find_all(True,recursive=False) if c.find('p')]
   review_cards=_dedup_leaf_elements(review_cards)
  # The intro/disclaimer paragraph is the first <p> that ISN'T inside one
  # of those review cards — grabbing sec.find_all('p')[0] unconditionally
  # would instead overwrite the first review's own testimonial text.
  intro_p=next((p for p in sec.find_all('p') if not any(p in c.descendants for c in review_cards)),None)
  if intro_p:
   # reviews_note is rendered here verbatim as PUBLIC page copy, but the AI
   # that writes it is also told elsewhere that these reviews are
   # placeholders — if that leaks into this field's own wording (e.g.
   # "placeholder", "fictional", "replace before launch"), visitors would
   # see the site openly admit its own reviews aren't real. Fall back to the
   # safe generic disclaimer instead of ever publishing that admission.
   safe_default='Individual experiences vary. These reflect personal opinions, not guaranteed outcomes.'
   note=data.get('reviews_note') or safe_default
   if re.search(r'placeholder|fictional|not real|replace.{0,20}(before|prior to).{0,10}(launch|going live|publish)',note,re.I):
    note=safe_default
   intro_p.string=note
  sample_reviews=data.get('sample_reviews',[])
  reviewer_names=data.get('reviewer_names',[])
  for i,card in enumerate(review_cards):
   # Update reviewer name if AI provided appropriate ones
   if reviewer_names and i<len(reviewer_names):
    name_el=card.find(class_=re.compile('rev-name|reviewer-name',re.I))
    if not name_el:
     # No "rev-name"/"reviewer-name" class at all (e.g. design 6's plain
     # <p class="font-bold text-sm">) — left the ORIGINAL scraped
     # reviewer's own name (a different, unrelated person) sitting next to
     # this product's AI-written testimonial and the publisher's chosen name.
     name_el=card.find('p',class_=re.compile(r'font-bold',re.I))
    name_has_suffix=False
    if not name_el:
     # Some designs give the name its own combined "Name — City, State"
     # line with NO distinguishing class at all (e.g. design 2's bare
     # "<h4>Melissa H. — Seattle, WA</h4>") — neither lookup above ever
     # finds it, so the ORIGINAL scraped reviewer's name (and a photo
     # newly uploaded for a completely different, possibly different-
     # gender AI-generated name) stays on the page regardless of what
     # reviewer_names holds. Find it by its own text shape instead: a
     # short, childless line starting with a capitalized name, followed
     # by a dash and a location.
     for cand in card.find_all(['h2','h3','h4','h5','span']):
      if cand.find(True):continue
      txt=cand.get_text().strip()
      if len(txt)<90 and re.match(r"^[A-Z][A-Za-z.'-]+(?:\s[A-Z]\.)?\s*[—–-]\s*\S",txt):
       name_el=cand;name_has_suffix=True;break
    if name_el:
     if name_has_suffix:
      m=re.match(r'^[^—–-]*?(\s*[—–-].*)$',name_el.get_text())
      name_el.string=f'{reviewer_names[i]}{m.group(1)}' if m else reviewer_names[i]
     else:
      name_el.string=reviewer_names[i]
     # A small circular avatar showing the ORIGINAL reviewer's initials
     # (e.g. "S.M.") right next to the newly-set name is an obvious
     # mismatch — find it by its short, letters-and-dots-only text rather
     # than trying to match the old initials exactly first.
     avatar_el=card.find(class_=re.compile(r'rounded-full',re.I))
     if avatar_el and avatar_el is not name_el and re.fullmatch(r'[A-Za-z](?:\.[A-Za-z])?\.?',avatar_el.get_text().strip()):
      name_words=reviewer_names[i].split()
      new_initials=name_words[0][:1].upper()+('.'+name_words[-1][:1].upper() if len(name_words)>1 else '')+'.'
      avatar_el.string=new_initials
    # The visible name above gets updated, but the reviewer photo's own alt
    # text (e.g. "Jessica M. — {brand} Verified Review", scraped from the
    # original template's real reviewers) was never touched — every subpage
    # this section is copied onto shipped an alt attribute naming a person
    # who isn't the reviewer actually shown. Swap just the leading name,
    # keeping whatever separator/suffix the template used (em-dash, hyphen, …).
    photo_el=card.find('img',class_=re.compile('reviewer-photo|rev-photo|avatar',re.I))
    if not photo_el:
     # No class hook at all (design 2's bare <img alt="Melissa" .../> with
     # no class) — only safe to guess when the card has exactly one <img>,
     # so this never risks grabbing the wrong one on a card with several
     # (e.g. design 4's separate reviewer-photo + review-stars images).
     card_imgs=card.find_all('img')
     if len(card_imgs)==1:photo_el=card_imgs[0]
    if photo_el and photo_el.get('alt'):
     m=re.match(r'^[^—–\-]*?(\s*[—–\-].*)$',photo_el['alt'])
     photo_el['alt']=f'{reviewer_names[i]}{m.group(1)}' if m else reviewer_names[i]
   all_ps=card.find_all('p')
   # The reviewer's name/location can itself be a <p> nested inside a
   # header/meta wrapper that appears BEFORE the actual testimonial in
   # document order (e.g. class="reviewer-name") — a plain card.find('p')
   # grabs that instead of the review text and leaves the real testimonial,
   # with all its original-product-specific claims, completely untouched.
   # A card with a quoted-testimonial <p> styled "italic" (a common CSS
   # signal for pull-quotes, e.g. design 6's "... mb-6 italic") followed by
   # SEPARATE name and location paragraphs breaks the all_ps[-1] fallback
   # below — the true testimonial isn't the LAST <p> here, it's the FIRST,
   # so that fallback silently overwrote the reviewer's location line
   # instead and left the actual quoted text as the original scraped review.
   p=(card.find(class_=re.compile('review-text|rev-text|testimonial',re.I))
      or card.find('p',class_=re.compile(r'\bitalic\b',re.I))
      or (all_ps[-1] if all_ps else None))
   if p and sample_reviews and i<len(sample_reviews):
    p.string=sample_reviews[i]
   elif sample_reviews:
    # AI provided fewer reviews than this template has card slots for —
    # remove the extra card rather than leave the original scraped
    # product's own testimonial (with its own specific claims) in place.
    card.decompose()
   elif p:
    # No AI review data at all — best-effort generic scrub of anything
    # clearly tied to a different product category.
    for p2 in all_ps:
     txt=p2.get_text().lower()
     if any(w in txt for w in ['circulation','cardiovascular','heart health','vascular','nitric','arginine']):
      p2.string=f'I have been using {brand} as part of my daily routine and I appreciate the quality of the formula.'

 # ── 8. Pricing ──
 sec=section(soup,'pricing','order-bottle','buy-breathizen')
 if sec:
  h=sec.find(['h2','h3'])
  if h:h.string=f'Choose Your {brand} Package'
  pricing=data.get('pricing',[])
  # Map AI pricing data by bottle count for reliable lookup (AI order may vary)
  pricing_by_count={p.get('bottles'):p for p in pricing}
  # Find all pricing cards — title may be h3/h4 OR a div with 'ttl' in class
  price_cards=[]
  for el in sec.find_all(['div','article','li']):
   classes=[c.lower() for c in (el.get('class') or [])]
   is_card_class=any(c in ('plan','card','package','offer','pricing-card','price-card','pack') or
                      c.endswith('-plan') or c.endswith('-card') or c.endswith('-pack') for c in classes)
   if is_card_class:
    has_title=el.find(['h3','h4']) or el.find(class_=re.compile('ttl|title',re.I))
    has_price=el.find(class_=re.compile('price',re.I))
    if has_title and has_price:
     price_cards.append(el)
  price_cards=[c for c in price_cards if not any(c is not other and other in c.descendants for other in price_cards)]
  if not price_cards and design=='6':
   # Design 6's Tailwind pricing cards have no "price"/"plan"/"card"-style
   # class anywhere the detection above looks for — so `price_cards` came
   # back empty, this section's whole population loop never ran, and every
   # generated site kept showing Gelagen's own fixed example numbers
   # ($79/$49/$69 per bottle, "Was $358/$537/$1074") no matter what pricing
   # the AI actually generated for this product. Match this design's own
   # structure directly: a labeled "Per Bottle"/"Total" row inside each card.
   grid=sec.find(class_=re.compile(r'\bgrid\b',re.I))
   d6_cards=[]
   if grid:
    for c in grid.find_all(True,recursive=False):
     t=c.find('h3')
     if t and re.search(r'bottles?',t.get_text(),re.I):d6_cards.append(c)
   pricing_sorted=sorted(pricing,key=lambda p:p.get('bottles',0)) if pricing else []
   def _num6(v):
    try:return float(re.sub(r'[^0-9.]','',str(v) or '0') or 0)
    except Exception:return 0.0
   base_rate=_num6(pricing_sorted[0].get('price_per_bottle',0)) if pricing_sorted else 0
   for i,card in enumerate(d6_cards):
    title_el=card.find('h3')
    nums=re.findall(r'\d+',title_el.get_text()) if title_el else []
    bottles=int(nums[-1]) if nums else None
    pkg=pricing_by_count.get(bottles)
    if not pkg and i<len(pricing_sorted):pkg=pricing_sorted[i]
    if not pkg:continue
    bottles=pkg.get('bottles',bottles)
    if title_el:title_el.string=f"{bottles} Bottles"
    per_bottle=_num6(pkg.get('price_per_bottle',0))
    total=_num6(pkg.get('total',0)) or per_bottle*bottles
    # "Per Bottle" label + its price figure sit as sibling <span>s
    label=card.find(string=re.compile(r'^\s*Per Bottle\s*$'))
    if label and label.parent:
     price_span=label.parent.find_next_sibling('span')
     if price_span:price_span.string=f'${per_bottle:g}'
    save_span=card.find(class_=re.compile(r'\bbg-green-50\b',re.I)) or next(
     (s for s in card.find_all('span') if 'save' in s.get_text(' ').lower()),None)
    regular_total=base_rate*bottles
    savings=round(regular_total-total) if base_rate and regular_total>total else 0
    if save_span:
     if savings>0:save_span.string=f'You Save ${savings:g}'
     else:save_span.decompose()
    tot_label=card.find(string=re.compile(r'^\s*Total\s*$'))
    if tot_label and tot_label.parent:
     tot_wrap=tot_label.parent.find_next_sibling('div')
     if tot_wrap:
      was_span=tot_wrap.find(class_=re.compile(r'line-through',re.I))
      cur_span=tot_wrap.find_all('span')[-1] if tot_wrap.find_all('span') else None
      if was_span:
       if savings>0:was_span.string=f'${regular_total:g}'
       else:was_span.decompose()
      if cur_span and cur_span is not was_span:cur_span.string=f'${total:g}'
    ship_p=card.find_all('p')
    if ship_p:
     shipping_txt=str(pkg.get('shipping','') or '').strip()
     ship_p[-1].string=f'+ {shipping_txt}' if shipping_txt else '+ Shipping'
    img=card.find('img')
    if img:
     prod_img=_get_product_img(images,f'bottle-{bottles}',i)
     if prod_img:
      img['src']=safe_rel(prod_img)
      img['alt']=f'{brand} {bottles} bottle package'
  # Fallback bottle counts, only used when a card has no readable original
  # count of its own (see below) — NOT a reliable template-wide DOM order.
  card_bottle_counts=[2,6,3]
  # Fallback pricing if AI count doesn't match template's expected counts
  sorted_pricing=sorted(pricing,key=lambda p:p.get('bottles',0)) if pricing else []
  for i,card in enumerate(price_cards):
   title_el=card.find(['h3','h4']) or card.find(class_=re.compile('ttl|title',re.I))
   # Prefer the card's OWN original bottle count, read from the scraped
   # template's own markup, over the hardcoded fallback list above. Templates
   # don't all lay their cards out in a 2/6/3 DOM order (design 3's real order
   # is 2/3/6) — trusting a fixed guess there mismatches a card's fixed
   # tag/badge (e.g. "Lowest per bottle") with whichever bottle count ends up
   # written into it.
   orig_count=None
   if title_el:
    # Take the LAST number, not the first — some templates title a tier as a
    # range like "1-2 Bottles" for their starter card, and the upper bound is
    # the one that matches an actual pricing tier ("2 Bottles"), not the "1".
    nums=re.findall(r'\d+',title_el.get_text())
    if nums:orig_count=int(nums[-1])
   expected_count=orig_count if orig_count is not None else card_bottle_counts[min(i,2)]
   pkg=pricing_by_count.get(expected_count)
   if not pkg and i<len(sorted_pricing):
    pkg=sorted_pricing[i]  # fallback: use i-th cheapest/available if exact count missing
   if not pkg:continue
   if title_el:title_el.string=f"{expected_count} Bottles"
   # Update price/total/shipping text using the matched package data
   price_el=card.find(class_=re.compile('price',re.I))
   tot_el=card.find(class_=re.compile('tot',re.I))
   ship_el=card.find(class_=re.compile('ship',re.I))
   if price_el:
    small=price_el.find('small')
    price_el.clear()
    price_el.append(str(pkg.get('price_per_bottle','')))
    if small:price_el.append(small)
    else:
     s=soup.new_tag('small');s.string=' / bottle';price_el.append(s)
   if tot_el:tot_el.string=f"Total: {_clean_total_value(pkg.get('total',''))}"
   if ship_el:
    ship_txt=str(pkg.get('shipping',''))
    ship_el.string=ship_txt
    # The template's own cheapest-tier card carries a static "pay" class
    # (styled in a muted grey instead of the bold accent color) to visually
    # flag that tier as NOT getting free shipping — that class never
    # otherwise gets touched, so if this product's actual generated pricing
    # says that tier's shipping is free too, the card kept rendering "Free"
    # in the muted "you still pay" color, contradicting its own text.
    is_free=bool(re.search(r'\bfree\b',ship_txt,re.I))
    classes=ship_el.get('class') or []
    if is_free and 'pay' in classes:
     ship_el['class']=[c for c in classes if c!='pay']
    elif not is_free and 'pay' not in classes:
     ship_el['class']=classes+['pay']
   # Set correct bottle image
   slot=f'bottle-{expected_count}'
   img=card.find('img',class_=re.compile('pk|product|bottle',re.I)) or card.find('img')
   if img:
    prod_img=_get_product_img(images,slot,i)
    if prod_img:
     img['src']=safe_rel(prod_img)
     img['alt']=f"{brand} {expected_count} bottle package"
     img['data-populated']='1'
   # "You Save $X" / "Was $X" style badges (e.g. class="ebooks" in one
   # template, class="ge-plan-was" in design 5) — never leave the original
   # template's own fixed dollar figures in place (design 5's scraped
   # "Was $358/$537/$1,074" are the ORIGINAL Gelagen product's real
   # official-site pricing, meaningless — often wildly inconsistent with the
   # card's own Total — for whatever different product this template got
   # reused for). Derive both from the same regular per-bottle rate (the
   # highest per-bottle price among this product's own AI-provided tiers),
   # so "Was" and "You Save" always agree with each other mathematically.
   try:
    per_bottle=[float(re.sub(r'[^0-9.]','',str(p.get('price_per_bottle','')) or '0') or 0) for p in pricing if p.get('price_per_bottle')]
    highest=max(per_bottle) if per_bottle else 0
    this_total=float(re.sub(r'[^0-9.]','',str(pkg.get('total','')) or '0') or 0)
    regular_total=highest*expected_count
    savings=round(regular_total-this_total) if highest and this_total else 0
   except Exception:
    highest=0;this_total=0;regular_total=0;savings=0
   save_el=card.find(class_=re.compile(r'\bsave\b|savings|ebooks|discount-badge',re.I))
   if save_el:
    if savings>0:save_el.string=f'You Save ${savings}!'
    else:save_el.decompose()
   was_el=card.find(class_=re.compile(r'(?:^|[-_])was\b',re.I))
   if was_el:
    if savings>0:was_el.string=f'Was ${regular_total:g}'
    else:was_el.decompose()
   # A fixed "N free bonus guides" feature-list line (design 5's own scraped
   # "6 free bonus guides") is that original product's own bonus count —
   # show this product's actual bonus count instead (same figure as the
   # hero chip/bonus section elsewhere on the page), or drop the line
   # entirely when this product has no genuine bonus offers at all.
   bonus_li=next((li for li in card.find_all('li') if re.search(r'\d+\s*free\s*bonus',li.get_text(),re.I)),None)
   if bonus_li:
    n_bonus=len(data.get('bonuses',[]))
    if n_bonus:bonus_li.string=f'{n_bonus} free bonus{"es" if n_bonus!=1 else ""}'
    else:bonus_li.decompose()
   # Pricing-tier CTA button text + a trust line underneath it — the
   # original scraped wording (e.g. "Order Now", "Select This Plan") is
   # replaced with copy keyed to this exact tier, matching the native
   # pipeline's own pack2/pack3/pack6 CTAs.
   buy_a=card.find('a')
   if buy_a:
    buy_text=cta_texts(brand,category).get(f'pack{expected_count}',cta_texts(brand,category)['mid'])
    buy_a.string=buy_text
    if not card.find(class_='auto-cta-trust'):
     buy_a.insert_after(BeautifulSoup(cta_trust_line_html(),'html.parser'))

 # ── 8b. Bonus section — auto-inserted only if AI reports bonuses AND template has no existing bonus section ──
 bonuses=data.get('bonuses',[])
 existing_bonus_sec=section(soup,'bonus','bonuses')
 if not existing_bonus_sec:
  # Also check for a section whose heading mentions "bonus" (unnamed id)
  for s2 in soup.find_all('section'):
   h2=s2.find(['h2','h3'])
   if h2 and 'bonus' in h2.get_text().lower():existing_bonus_sec=s2;break
 if bonuses and not existing_bonus_sec and sec:
  bonus_soup=BeautifulSoup(_bonus_section_html(bonuses,images),'html.parser')
  sec.insert_after(bonus_soup)

 # ── 9. FAQs ──
 sec=section(soup,'faq','faqs')
 if sec:
  h=sec.find(['h2','h3'])
  if h:h.string=f'{brand} FAQ, Answered Honestly'
  faq_rows=sec.find_all(class_=re.compile('faq.row|faq-item|faq-entry|accordion-item',re.I))
  if faq_rows:
   for i,row in enumerate(faq_rows):
    if i<len(faqs):
     btn=row.find('button') or row.find(class_=re.compile('faq.btn|question|toggle|faq-q',re.I))
     # Restrict to non-button tags — Bootstrap accordions give the (closed)
     # question <button> a "collapsed" class, which a loose "collapse"
     # substring match also picks up, making this grab the button itself
     # instead of the answer wrapper and clobber the question text set above.
     # (A bare "faq-a" alternative here used to substring-match
     # class="faq-arrow", the little ▼ toggle icon span, which sits before
     # the real .faq-answer div in document order and so always won the
     # match first, leaving every answer's actual text untouched — now
     # word-bounded so it still matches an exact class="faq-a" without
     # also matching as a prefix of "faq-arrow".)
     body=row.find(['div','section','span','p'],class_=re.compile(r'faq.body|answer|collapse|\bfaq-a\b',re.I))
     if btn:btn.string=faqs[i].get('q','')
     if body:
      p=body.find('p')
      if p:p.string=faqs[i].get('a','')
      else:body.string=faqs[i].get('a','')
    else:
     row.decompose()  # Remove extra template FAQ rows not covered by AI content
  else:
   # Fallback: no row wrapper found — match buttons/bodies directly
   btns=sec.find_all('button') or sec.find_all(class_=re.compile('faq.btn|question|toggle|faq-q',re.I))
   bodies=sec.find_all(['div','section','span','p'],class_=re.compile(r'faq.body|answer|collapse|\bfaq-a\b',re.I))
   # Some templates (e.g. design 6) give the answer wrapper no distinguishing
   # class at all — just a plain "hidden" div toggled by the accordion's own
   # JS via btn.nextElementSibling, with nothing named "faq"/"answer"/
   # "collapse" for the regex above to find. That left `bodies` empty, so
   # every answer silently kept the ORIGINAL template's answer text sitting
   # under a freshly-rewritten question — looks like the Q/A pairs are
   # shuffled, but really only the questions were ever touched. Fall back to
   # each button's own next sibling element, the same relationship the
   # page's inline toggle script already assumes.
   sibling_fallback=len(bodies)<len(btns)
   if sibling_fallback:
    bodies=[btn.find_next_sibling(True) for btn in btns]
    bodies=[b for b in bodies if b is not None]
   pairs=list(zip(btns,bodies)) if sibling_fallback else None
   for i,btn in enumerate(btns):
    if i<len(faqs):btn.string=faqs[i].get('q','')
    elif not sibling_fallback:btn.decompose()
   for i,body in enumerate(bodies):
    if i<len(faqs):
     p=body.find('p')
     if p:p.string=faqs[i].get('a','')
     else:body.string=faqs[i].get('a','')
    elif not sibling_fallback:
     body.decompose()
   # In sibling-fallback mode, btn and body share one wrapper row (e.g.
   # design 6's <div class="border ...">) — decomposing each separately
   # leaves that wrapper behind as an empty visible box. Remove the shared
   # parent once instead, for any pair beyond the AI's actual FAQ count.
   if sibling_fallback:
    for i,(btn,body) in enumerate(pairs):
     if i>=len(faqs):
      shared_parent=btn.parent is body.parent
      if shared_parent:btn.parent.decompose()
      else:btn.decompose();body.decompose()

 # ── 10. Footer ──
 footer=soup.find('footer')
 if footer:
  # Footer tagline — a short brand slogan repeated under the footer logo
  # on some templates; carries the original product's own specific promise
  # (e.g. "Rediscover What It Feels Like to Breathe") if left untouched.
  tagline_el=footer.find(class_=re.compile(r'footer-tagline',re.I))
  if not tagline_el:
   # No "footer-tagline" class at all (e.g. design 6's plain <div
   # class="space-y-4"><span>{brand}</span><p>...</p><p>...</p></div>) — the
   # first <p> there is still the ORIGINAL scraped product's own one-line
   # pitch (e.g. "A daily biotin gummy ... support radiant skin, stronger
   # hair, and healthy nails"), repeated on the footer of every single page
   # regardless of what this generated site is actually about. populate()
   # runs before the brand-name swap, so the logo span here still reads the
   # old brand literally — use it to find the right column, then its first
   # sibling <p>.
   brand_col=None
   for old in ALL_OLD_BRANDS:
    hit=footer.find(string=re.compile(r'^\s*'+re.escape(old)+r'\b',re.I))
    if hit and hit.parent:brand_col=hit.parent.parent;break
   if brand_col:
    tagline_el=brand_col.find('p')
  if tagline_el:
   tagline_el.string=data.get('tagline') or f"A natural {category} formula."
  # Nav links — fix BOTH text and href
  footer_link_defs=[
   ('home','Home','index.html'),
   ('what is','What Is '+brand,'what-is-product.html'),
   ('how','How '+brand+' Works','how-it-works.html'),
   ('ingredient','Ingredients','ingredients.html'),
   ('benefit','Benefits','benefits.html'),
   ('review','Reviews','reviews.html'),
   ('blog','Blog','blog/index.html'),
   ('about','About Us','about.html'),
   ('order','Order Now','index.html#pricing'),
   ('terms','Terms of Use','terms.html'),
   ('privacy','Privacy Policy','privacy-policy.html'),
   ('disclaimer','Disclaimer','disclaimer.html'),
   ('refund','Refund Policy','refund-policy.html'),
   ('contact','Contact Us','contact.html'),
   ('editorial','editorial standards','about.html'),
  ]
  for a in footer.find_all('a',href=True):
   txt=a.get_text().strip().lower()
   href=a.get('href','').lower()
   matched=False
   for key,label,new_href in footer_link_defs:
    if key in txt or key in href:
     a.clear();a.append(label);a['href']=new_href;matched=True;break
   if not matched:
    for old in ALL_OLD_BRANDS:
     if old.lower() in txt:a.clear();a.append(brand)
  # Second pass — catch any link where text extraction failed (empty) but href still has old domain path
  for a in footer.find_all('a',href=True):
   if a.get_text().strip():continue  # already has text, skip
   href=a.get('href','').lower()
   for key,label,new_href in footer_link_defs:
    if key.replace(' ','-') in href or key.replace(' ','') in href:
     a.clear();a.append(label);a['href']=new_href;break
   else:
    if a.get_text().strip()=='':a.decompose()  # remove truly empty leftover links
  # Footer disclosure paragraphs — replace category-specific claims. Some
  # templates use <b>Label</b> as its own empty paragraph (design 2), others
  # use <strong>Label.</strong> inline with the body text in the same
  # paragraph (design 3) — check both tags.
  for p in footer.find_all('p'):
   b=p.find(['b','strong'])
   label=b.get_text().strip().lower() if b else ''
   note=None
   if 'who this is for' in label:
    note=(f'{brand} is a dietary supplement for adults aged 18 and over looking for '
          f'daily nutritional support as part of a {category} routine. It is not a '
          f'substitute for medical treatment and is not intended to diagnose, treat, '
          f'cure or prevent any disease. Consult a doctor before use if you have any '
          f'medical condition or take medication.')
   elif 'fda compliance' in label or 'fda disclaimer' in label:
    note=(f'These statements have not been evaluated by the U.S. Food & Drug Administration. '
          f'{brand} is a dietary supplement, not a drug, and is not intended to diagnose, treat, '
          f'cure or prevent any disease. Individual results vary and testimonials do not '
          f'guarantee you will achieve the same outcome.')
   elif 'manufacturing claim' in label or 'note on manufacturing' in label:
    note=(f'Dietary supplements are not approved by the FDA. {brand} is produced in an '
          f'FDA-registered facility, a real but more limited claim than "FDA approved," '
          f'described accurately here.')
   elif 'no supplement treats' in label or 'interaction warning' in label:
    # Template-specific medical claims (e.g. a named drug interaction) that
    # do not apply to this product — drop the paragraph rather than risk
    # showing an interaction warning for an ingredient this product may
    # not even contain.
    p.decompose();continue
   if note:
    for a in p.find_all('a'):a.decompose()
    for t in list(p.strings):
     if t.strip() and (not b or t!=b.string):
      t.replace_with(note);break
  # Safety net — any footer paragraph still mentioning old category terms gets scrubbed
  for p in footer.find_all('p'):
   ptxt=p.get_text()
   if re.search(r'\b(blood pressure|hypertension|nitric oxide|citrulline|arginine)\b',ptxt,re.I):
    b=p.find('b')
    label_txt=b.get_text() if b else ''
    generic=(f'{brand} is intended for general wellness support as part of a healthy lifestyle. '
             f'It is not intended to diagnose, treat, cure or prevent any disease.')
    for a in p.find_all('a'):a.decompose()
    p.clear()
    if label_txt:
     nb=soup.new_tag('b');nb.string=label_txt;p.append(nb)
    p.append(' '+generic if label_txt else generic)

 # ── 10b. Sticky/floating/inline promo CTA banners — these often live as a
 # body-level <div> outside every <section> (or as a standalone strip
 # between sections), so they're invisible to the section-based steps above
 # and to _rewrite_all_sections (which only walks <section> tags).
 pricing_all=data.get('pricing',[])
 try:
  per_bottle_all=[float(re.sub(r'[^0-9.]','',str(p.get('price_per_bottle','')) or '0') or 0) for p in pricing_all if p.get('price_per_bottle')]
  best_pb=min(per_bottle_all) if per_bottle_all else 0
  worst_pb=max(per_bottle_all) if per_bottle_all else 0
 except Exception:
  best_pb=worst_pb=0
 try:
  best_tier=max(pricing_all,key=lambda p:p.get('bottles',0)) if pricing_all else None
  best_total=float(re.sub(r'[^0-9.]','',str(best_tier.get('total','')) or '0') or 0) if best_tier else 0
  savings=round(worst_pb*best_tier.get('bottles',0)-best_total) if best_tier and worst_pb and best_total else 0
 except Exception:
  savings=0
 for banner in soup.find_all(class_=re.compile(r'sticky|bottom-cta-banner|floating-cta|bottom-banner|promo-banner|faq-banner',re.I)):
  head=banner.find(['h3','h4','h5'])
  if head:head.string=f'Save More With {brand} Bundles'
  sub_p=banner.find('p')
  if sub_p:sub_p.string=f'{category} Support'
  price_el=banner.find(class_=re.compile(r'cta-price|banner-price',re.I))
  if price_el and best_pb:price_el.string=f'${best_pb:g}/Bottle'
  elif best_pb:
   # Some designs (e.g. design 5's "ge-sticky" bar) show the price in a
   # plain <b> tag with no dedicated price class at all — the class-based
   # match above never fires for them, so the ORIGINAL scraped product's
   # real price (e.g. a literal "$49 / bottle") survived untouched on every
   # generated site regardless of this product's actual cheapest tier.
   # Match on the tag's own "$"-containing text instead of a class name, so
   # this can't accidentally rewrite an unrelated bold tag in the same banner.
   b_price=banner.find('b',string=re.compile(r'\$\s*\d'))
   if b_price:b_price.string=f'From ${best_pb:g} / bottle'
  orig_el=banner.find(class_=re.compile(r'original-price',re.I))
  if orig_el:
   if worst_pb and worst_pb>best_pb:orig_el.string=f'Was ${worst_pb:g}'
   else:orig_el.decompose()
  # "Was $X/bottle — Now $Y/bottle" style strong claim
  disc_el=banner.find(class_=re.compile(r'discounted',re.I))
  if disc_el:
   if worst_pb and best_pb:disc_el.string=f'Was ${worst_pb:g}/bottle — Now ${best_pb:g}/bottle'
   else:disc_el.decompose()
  # CTA link/button text carrying a fixed "SAVE $780 TODAY" style figure
  for a in banner.find_all('a'):
   for t in list(a.find_all(string=True)):
    if not isinstance(t,NavigableString) or t.parent.name in ('small',):continue
    if re.search(r'save\s*\$\s*[\d,]+',str(t),re.I):
     repl=f'Buy Now — Save More On {brand} Bundles' if savings<=0 else f'Buy Now — Save ${savings} Today'
     t.replace_with(repl);break

 # Some designs (e.g. design 5's "ge-final" pricing recap) show a plain
 # "was $X / now $Y" comparison as bare <div class="old">/<div class="new">
 # tags instead of the "cta-regular-price"/"cta-current-price" classes the
 # cta-final handler above looks for, so that handler's section-class match
 # (built for a different design's "cta-final" naming) never even fires here
 # — the ORIGINAL scraped product's real per-bottle price survived untouched.
 # Match narrowly on the exact "old"/"new" class plus existing "$" text so
 # this can never touch an unrelated element that merely shares that class name.
 old_price_el=soup.find(class_=re.compile(r'^old$'))
 if old_price_el and worst_pb and re.search(r'\$\s*\d',old_price_el.get_text()):
  old_price_el.string=f'Regular: ${worst_pb:g} / bottle'
 new_price_el=soup.find(class_=re.compile(r'^new$'))
 if new_price_el and best_pb and re.search(r'\$\s*\d',new_price_el.get_text()):
  new_price_el.string=f'Today from ${best_pb:g} / bottle'

 # ── 11. All remaining sections ──
 # Computed fresh from `data` (deterministic — no AI call, just string
 # building from ingredients/pricing/guarantee/FAQ already in `data`) so the
 # homepage's own "From The Blog" teaser cards link to the SAME articles,
 # under the SAME slugs, that the real generate route builds at blog/*.html —
 # never a mismatched/nonexistent slug.
 _blog_articles_for_teaser=_blog_articles(data,domain,affiliate) if domain else []
 _rewrite_all_sections(soup,data,brand,images,_desc_used,_blog_articles_for_teaser)

 # ── 11a. Design 3's bespoke investigative-article sections — runs after
 # the generic fallback above so it gets the final say on the handful of
 # sections that fallback's heading-keyword matching mishandles (it applied
 # the same 3-card "What Makes Different/Who For/How To Get" filler to
 # three unrelated sections since each happened to contain 3 <h3> tags) ──
 if str(design)=='3':
  _populate_design3_investigative(soup,data,brand)

 # ── 11a2. Design 4's title-band/symptoms/plain-text-pricing bespoke bits ──
 if str(design)=='4':
  _populate_design4_supplement(soup,data,brand,images)

 # ── 11a3. Design 5's "gummy" leftovers — the scraped Gelagen template
 # hardcodes its own product form ("Inside Every Gummy" eyebrow, "Daily
 # Beauty Gummies" hero pill, "Two gummies daily" ritual copy) in markup
 # _rewrite_all_sections' generic heading/card matching never touches ──
 if str(design)=='5':
  _populate_design5_fixes(soup,data,brand)

 # ── 11b. Global safety net — strip mentions of the ORIGINAL template's real
 # third-party retailer/payment processor (e.g. "Buygoods"/"Click Sales,
 # Inc.") and fabricated review-count/star claims that have nothing to do
 # with the new site, wherever in the page they happen to appear ──
 for p in list(soup.find_all('p')):
  ptxt=p.get_text()
  if re.search(r'buygoods|click sales,?\s*inc',ptxt,re.I):
   p.string=(f'Orders are processed through a secure third-party checkout. '
             f'See the official {brand} order page for current retailer and billing details.')
   continue
  if len(ptxt)<200 and re.search(r'★{3,}|\d[\d,]*\+\s*(happy customers|verified buyers|5[- ]star reviews)',ptxt,re.I):
   p.decompose()

 # ── 12. Final: replace ALL old brand text in ANY remaining element ──
 for t in list(soup.find_all(string=True)):
  if not isinstance(t,NavigableString):continue
  if isinstance(t,Comment):continue  # don't unwrap a comment into visible text
  if t.parent.name in ('script','style','noscript'):continue
  s2=str(t)
  for old in ALL_OLD_BRANDS:
   s2=re.sub(r'\b'+re.escape(old)+r'\b',brand,s2,flags=re.I)
  # Clean template-specific phrases
  for pat,repl in TEMPLATE_SPECIFIC_PHRASES:
   s2=re.sub(pat,repl.replace('{brand}',brand),s2,flags=re.I)
  if s2!=str(t):t.replace_with(s2)


def internal_links(soup,domain,old_slugs=None):
 exact_mapping={'index.html':'index.html','what-is.html':'what-is-product.html',
  'what-is-product.html':'what-is-product.html','how-it-works.html':'how-it-works.html',
  'ingredients.html':'ingredients.html','benefits.html':'benefits.html',
  'reviews.html':'reviews.html','faq.html':'faq.html'}
 # Keyword-based fallback for old brand-slugged filenames the template uses
 # internally (e.g. "how-bloodpril-works.html", "bloodpril-ingredients.html",
 # "what-is-bloodpril.html") — these never match the exact filenames above,
 # so without this they'd be left pointing at dead old-brand URLs (404s).
 keyword_mapping=[
  ('what-is','what-is-product.html'),
  ('how-','how-it-works.html'),
  ('ingredient','ingredients.html'),
  ('benefit','benefits.html'),
  ('review','reviews.html'),
  ('faq','faq.html'),
  ('pricing','index.html#pricing'),
  ('refund','refund-policy.html'),
  ('terms','terms.html'),
  ('privacy','privacy-policy.html'),
  ('disclaimer','disclaimer.html'),
  ('contact','contact.html'),
  ('about','about.html'),
 ]
 for a in soup.find_all('a',href=True):
  href=str(a.get('href') or '').strip()
  if not href:continue
  # strip() (not lstrip()) so a trailing-slash URL like "/what-is-vapocept/"
  # still yields "what-is-vapocept" as its last segment instead of "" —
  # an empty base silently skipped every keyword_mapping check below and
  # left the link pointing at a dead old-brand-slugged page.
  u=urlparse(href);path=u.path.strip('/');base=path.split('/')[-1].lower() if path else ''
  frag=('#'+u.fragment) if u.fragment else ''
  # Blog paths must be checked BEFORE exact_mapping, since exact_mapping's
  # 'index.html' rule would otherwise wrongly match "blog/index.html" too
  # (matching only the basename) and send it to the homepage instead.
  if '/blog/' in path.lower() or path.lower().startswith('blog/') or path.lower()=='blog':
   a['href']='blog/index.html';continue
  if base in exact_mapping:
   a['href']=exact_mapping[base]+frag;continue
  if base and base!='index.html':
   for kw,target in keyword_mapping:
    if kw in base:
     a['href']=target if '#' in target else target+frag
     break
  elif not base:
   # href has no usable path/basename at all to match against — e.g. a bare
   # "https://olddomain.com/#" placeholder link, common in cookie-consent
   # banners ("See our Privacy Policy") and other one-off inline mentions
   # that were never part of the scraped footer nav. The link's own visible
   # text is still an unambiguous signal a basename-only check can't see —
   # without this, these keep pointing at a dead anchor on the old domain.
   text=a.get_text(' ',strip=True).lower()
   if text:
    for kw,target in keyword_mapping:
     if kw in text:
      a['href']=target if '#' in target else target+frag
      break

_LEGAL_FOOTER_LINKS=[
 ('terms.html','Terms of Use'),
 ('privacy-policy.html','Privacy Policy'),
 ('disclaimer.html','Disclaimer'),
 ('refund-policy.html','Refund Policy'),
 ('about.html','About Us'),
 ('contact.html','Contact Us'),
]

def ensure_legal_footer_links(soup):
 """Every legal/info page (Terms, Privacy, Disclaimer, Refund Policy, About,
 Contact) is always generated, but each scraped template's own footer only
 links to whichever subset the ORIGINAL brand happened to include — a
 missing link means a real, working page nobody can actually reach from the
 site's own navigation. Find wherever the template already links to ANY of
 these pages, and add the missing ones there too, matching that spot's own
 existing markup (plain <a> tags with a text separator, or <li>-wrapped),
 so the addition looks native rather than bolted on."""
 legal_names={name for name,_ in _LEGAL_FOOTER_LINKS}
 existing=[]
 for a in soup.find_all('a',href=True):
  base=str(a['href']).split('/')[-1].split('#')[0].split('?')[0]
  if base in legal_names and a.parent is not None:
   existing.append((base,a))
 if not existing:return
 def group_key(a):
  # Group <li>-wrapped links by their shared <ul>/<ol> — every <a> inside
  # a <li> has a DIFFERENT immediate parent, so grouping by a.parent alone
  # would put each list item in its own group of one and never recognize
  # the list as the real, multi-link footer nav block.
  p=a.parent
  if p is not None and p.name=='li' and p.parent is not None:return id(p.parent)
  return id(p)
 groups={}
 for base,a in existing:
  groups.setdefault(group_key(a),[]).append((base,a))
 target_pid=max(groups,key=lambda k:len(groups[k]))
 group=groups[target_pid]
 # A link counts as "already present" only if it's the target nav group
 # itself, or another real multi-link nav cluster elsewhere (2+ legal links
 # sharing a parent) — a single inline body mention (e.g. "via our
 # <a href='contact.html'>contact page</a>" in an About-page paragraph) is
 # just prose, not a working footer entry, and must not block the real one
 # from being added here.
 present=set()
 for pid,grp in groups.items():
  if pid==target_pid or len(grp)>=2:
   present.update(b for b,_ in grp)
 missing=[(n,label) for n,label in _LEGAL_FOOTER_LINKS if n not in present]
 if not missing:return
 last_base,last_anchor=group[-1]
 li_wrap=last_anchor.parent is not None and last_anchor.parent.name=='li'
 sep_text=None
 if not li_wrap:
  for _,a in group:
   nxt=a.next_sibling
   if isinstance(nxt,NavigableString) and nxt.strip():
    sep_text=str(nxt);break
 anchor_template=str(last_anchor)
 insert_after_el=last_anchor.parent if li_wrap else last_anchor
 for name,label in missing:
  new_a=BeautifulSoup(anchor_template,'html.parser').find('a')
  new_a['href']=name
  new_a.string=label
  if li_wrap:
   new_li=soup.new_tag('li')
   new_li.append(new_a)
   insert_after_el.insert_after(new_li)
   insert_after_el=new_li
  else:
   insert_after_el.insert_after(new_a)
   if sep_text:new_a.insert_before(sep_text)
   insert_after_el=new_a

_CORE_PAGE_LINKS=[
 ('what-is-product.html','What Is {brand}'),
 ('how-it-works.html','How It Works'),
 ('ingredients.html','Ingredients'),
 ('benefits.html','Benefits'),
 ('reviews.html','Reviews'),
 ('faq.html','FAQs'),
 ('blog/index.html','Blog'),
]

def _core_page_key(href):
 h=str(href).split('#')[0].split('?')[0].strip()
 if h=='blog' or h.rstrip('/').endswith('/blog') or h.endswith('blog/index.html'):return 'blog/index.html'
 return h.split('/')[-1]

def ensure_core_page_links(soup,brand):
 """Every core content page (What Is, How It Works, Ingredients, Benefits,
 Reviews, FAQs, Blog) is always generated, but — same problem as
 ensure_legal_footer_links() above — a scraped template's own nav/footer
 only links to whichever subset of these the ORIGINAL brand happened to
 include. Design 4's template, for example, links Ingredients/Benefits/
 Reviews/FAQs but never What Is/How It Works/Blog, leaving those three real,
 working pages reachable only via sitemap.xml and not from the site's own
 nav or footer. Find wherever the template already links to 2+ of these
 pages, and add the missing ones there too, matching that spot's own
 existing markup — identical approach to ensure_legal_footer_links()."""
 core_names={name for name,_ in _CORE_PAGE_LINKS}
 existing=[]
 for a in soup.find_all('a',href=True):
  key=_core_page_key(a['href'])
  if key in core_names and a.parent is not None:
   existing.append((key,a))
 if not existing:return
 def group_key(a):
  p=a.parent
  if p is not None and p.name=='li' and p.parent is not None:return id(p.parent)
  return id(p)
 groups={}
 for key,a in existing:
  groups.setdefault(group_key(a),[]).append((key,a))
 target_pid=max(groups,key=lambda k:len(groups[k]))
 group=groups[target_pid]
 present=set()
 for pid,grp in groups.items():
  if pid==target_pid or len(grp)>=2:
   present.update(k for k,_ in grp)
 missing=[(n,label) for n,label in _CORE_PAGE_LINKS if n not in present]
 if not missing:return
 last_key,last_anchor=group[-1]
 li_wrap=last_anchor.parent is not None and last_anchor.parent.name=='li'
 sep_text=None
 if not li_wrap:
  for _,a in group:
   nxt=a.next_sibling
   if isinstance(nxt,NavigableString) and nxt.strip():
    sep_text=str(nxt);break
 anchor_template=str(last_anchor)
 insert_after_el=last_anchor.parent if li_wrap else last_anchor
 for name,label in missing:
  new_a=BeautifulSoup(anchor_template,'html.parser').find('a')
  new_a['href']=name
  new_a.string=label.replace('{brand}',brand)
  if li_wrap:
   new_li=soup.new_tag('li')
   new_li.append(new_a)
   insert_after_el.insert_after(new_li)
   insert_after_el=new_li
  else:
   insert_after_el.insert_after(new_a)
   if sep_text:new_a.insert_before(sep_text)
   insert_after_el=new_a

def set_ctas(soup,affiliate):
 purchase=re.compile(r'\b(order|buy|shop|claim|get|purchase|view offer|check discount|see pricing|start your|try|learn more and order|access offer|save|choose|select package|yes[,! ]+i want)\b',re.I)
 for a in soup.find_all('a',href=True):
  txt=' '.join(a.stripped_strings)
  cls=' '.join(a.get('class') or [])
  # Ghost/outline/secondary buttons are informational links, not purchase CTAs
  if re.search(r'(?i)(ghost|outline|secondary|link-btn)',cls):continue
  if txt.strip().lower().startswith(('what is','learn more about','see the full','read the full','how it works','see how')):continue
  is_button=bool(re.search(r'(?i)(button|btn|order|cta|offer|purchase|buy|shop)',cls))
  is_purchase=bool(purchase.search(txt)) and not bool(re.search(r'(?i)^(how|what|ingredients|benefits|reviews|faq|home)',txt.strip()))
  if is_button or is_purchase:
   if len(txt.strip())<2:a.decompose();continue
   if len(txt.strip())<4 or txt.strip().lower() in {'home','benefits','ingredients','reviews','faq','how it works','what is it'}:continue
   a['href']=affiliate;a['rel']=['nofollow','sponsored']

def add_jsonld(soup,data,domain,canonical,affiliate,image_paths,include_product=True):
 today=date.today().isoformat()
 site_root_url=current_domain_url(domain,'')
 org_node={'@type':'Organization','@id':site_root_url+'#organization','name':data['brand'],'url':site_root_url}
 seo_imgs=seo_images(image_paths) if image_paths else []
 if seo_imgs:
  org_node['logo']={'@type':'ImageObject','url':current_domain_url(domain,seo_imgs[0])}
 product_node=None
 # include_product=False for blog pages (article + index) — a BlogPosting
 # isn't an offer to buy the product, so Google's own structured-data
 # guidance doesn't want Product/Offer markup stamped on it; those pages
 # keep WebSite/Organization/WebPage/BreadcrumbList from this function and
 # get their own BlogPosting node from add_article_jsonld() separately.
 if include_product:
  product_node={'@type':'Product','@id':canonical+'#product','name':data['brand'],
   'description':data['description'],'image':[current_domain_url(domain,x) for x in seo_imgs[:5]],
   'brand':{'@type':'Brand','name':data['brand']},'category':data.get('category','Health & Wellness')}
  # Serving size, read from the SAME serving_info.daily_serving field every
  # other on-page serving mention (hero stat strip, Quick Facts, FAQ, blog)
  # reads, so the structured data can never quote a different number.
  _serving_daily=(data.get('serving_info') or {}).get('daily_serving')
  if _serving_daily:
   product_node['additionalProperty']=[{'@type':'PropertyValue','name':'Serving size','value':_serving_daily}]
  pricing=data.get('pricing',[])
  if pricing:
   currency=(data.get('currency') or 'USD').strip() or 'USD'
   price_valid_until=(date.today()+timedelta(days=365)).isoformat()
   offers=[]
   for p in pricing:
    total=str(p.get('total') or p.get('price_per_bottle',''))
    offer={'@type':'Offer','url':affiliate,'priceCurrency':currency,'availability':'https://schema.org/InStock',
     'priceValidUntil':price_valid_until,'seller':{'@id':site_root_url+'#organization'}}
    price_raw=re.sub(r'[^0-9.]','',total.split('/')[0].split('(')[0])
    if price_raw:offer['price']=price_raw
    if p.get('label'):offer['name']=p['label']
    offers.append(offer)
   # Always an array — one Offer per bottle-count tier — even with a single
   # tier, rather than collapsing to a lone Offer object.
   if offers:product_node['offers']=offers
 graph=[
  {'@type':'WebSite','@id':site_root_url+'#website','url':site_root_url,'name':data['brand'],
   'publisher':{'@id':site_root_url+'#organization'}},
  org_node,
  # Prefer the page's OWN <title>/meta-description over the generic
  # site-wide data['seo'] values — callers (page_variant(), legal_page(),
  # build_native_page()) already write a unique title/description per page
  # before reaching here, but this function used to ignore that and stamp
  # every page's WebPage node with the homepage's title/description instead
  # — so e.g. about.html's <title> said "About Us — Brand" while its own
  # JSON-LD WebPage.name claimed the homepage's title. Read back what's
  # actually on the page; only fall back to the generic data if it's missing.
  {'@type':'WebPage','@id':canonical+'#webpage','url':canonical,
   'name':(soup.title.get_text().strip() if soup.title and soup.title.get_text().strip() else data['seo']['title']),
   'description':((soup.find('meta',attrs={'name':'description'}) or {}).get('content','').strip() or data['seo']['description']),
   'dateModified':today,'isPartOf':{'@id':site_root_url+'#website'}},
 ]
 if product_node:graph.append(product_node)
 # Only mark up FAQPage on a page that actually renders visible FAQ content —
 # Google disallows FAQ rich-result markup for text not shown on the page.
 # Build the list from the RENDERED accordion, not data['faqs'] directly —
 # the visible accordion is capped at however many faq-row slots the
 # scraped template happened to have, so if the AI returned more Q&A pairs
 # than that, using the raw data list here claims questions in the schema
 # that never actually appear on the page (exactly what Google disallows).
 # A plain id/class substring match for "faq" can land on a decorative
 # sibling title-band div (e.g. design 4's <div id="faqs"> heading-only band
 # that sits right before the real <section class="faq-section">) instead
 # of the actual content section — that band has no Q&A rows in it at all,
 # so visible_faqs below came back empty and FAQPage was silently never
 # added even though the FAQ is genuinely visible on the page. section()
 # already prefers a real <section> tag over a same-named sibling div.
 faq_visible=section(soup,'faq','faqs')
 if faq_visible:
  visible_faqs=[]
  # Extract per-ROW, scoped to each row's own descendants — a flat,
  # section-wide "all buttons" + "all answer-divs" search (paired by
  # index) silently shifts every pairing off by one the moment the
  # section has a wrapper element whose class also substring-matches the
  # question pattern (e.g. class="faq-questions" on the <ul> matches the
  # bare "question" alternative and gets counted as button #1), which
  # then pairs every real question with the WRONG answer in the schema.
  rows=faq_visible.find_all(class_=re.compile('faq.row|faq-item|faq-entry|accordion-item',re.I))
  if rows:
   for row in rows:
    q_el=row.find('button') or row.find(class_=re.compile('faq.btn|question|toggle|faq-q',re.I))
    a_el=row.find(['div','section','span','p'],class_=re.compile(r'faq.body|answer|collapse|\bfaq-a\b',re.I))
    q=_faq_question_text(q_el) if q_el else ''
    a=''
    if a_el:
     p=a_el.find('p')
     a=p.get_text(strip=True) if p else a_el.get_text(strip=True)
    if q and a:visible_faqs.append({'q':q,'a':a})
  else:
   q_els=faq_visible.find_all('button') or faq_visible.find_all(class_=re.compile('faq.btn|question|toggle|faq-q',re.I))
   a_els=faq_visible.find_all(['div','section','span','p'],class_=re.compile(r'faq.body|answer|collapse|\bfaq-a\b',re.I))
   for q_el,a_el in zip(q_els,a_els):
    q=_faq_question_text(q_el)
    p=a_el.find('p')
    a=(p.get_text(strip=True) if p else a_el.get_text(strip=True))
    if q and a:visible_faqs.append({'q':q,'a':a})
  if visible_faqs:
   graph.append({'@type':'FAQPage','@id':canonical+'#faq','mainEntity':[
    {'@type':'Question','name':x['q'],'acceptedAnswer':{'@type':'Answer','text':x['a']}} for x in visible_faqs[:12]]})
 graph.append({'@type':'BreadcrumbList','@id':canonical+'#breadcrumb','itemListElement':[
  {'@type':'ListItem','position':1,'name':'Home','item':site_root_url},
  {'@type':'ListItem','position':2,'name':data['brand'],'item':canonical}]})
 sc=soup.new_tag('script',type='application/ld+json')
 sc.string=json.dumps({'@context':'https://schema.org','@graph':graph},ensure_ascii=False)
 soup.body.append(sc)

def _get_img(images,slot,fallback_idx=0):
 for p in images:
  if Path(p).stem.lower()==slot:return safe_rel(p)
 # Fallbacks never pick a reviewer/customer portrait, badge or bundle-pack
 # mock-up for a product-photo slot (e.g. "vapocept-customer-1" as a bottle).
 non_manual=[p for p in images if Path(p).stem.lower() not in MANUAL_SLOTS and not is_non_product_image(p)]
 if non_manual:return safe_rel(non_manual[min(fallback_idx,len(non_manual)-1)])
 pool=seo_images(images) or images
 if pool:return safe_rel(pool[min(fallback_idx,len(pool)-1)])
 return ''

def _bonus_images(images,n):
 """Match uploaded images to bonus-card slots. An exact "bonus-N" filename
 claims that specific slot; any other uploaded file that simply has "bonus"
 somewhere in its name (e.g. "bonus-heart-guide.jpg") fills the remaining
 slots in upload order — publishers often don't bother numbering them."""
 slots=[None]*n;used=set()
 for i in range(n):
  for p in images:
   if p in used:continue
   if Path(p).stem.lower() in (f'bonus-{i+1}',f'bonus{i+1}',f'bonus_{i+1}'):
    slots[i]=p;used.add(p);break
 for p in images:
  if p in used:continue
  if 'bonus' in Path(p).stem.lower():
   for i in range(n):
    if slots[i] is None:
     slots[i]=p;used.add(p);break
 return slots

def _derive_bonus_title_from_filename(path):
 """A fuzzy-matched bonus image (e.g. "bonus-heart-health-secrets.jpg") often
 has its own real title baked into the filename by the publisher — use that
 as the card's displayed title instead of the AI's independently-invented
 one, so the two can never end up describing different things. An exact
 "bonus-1"/"bonus-2"-style filename carries no extra info, so this returns
 None and the AI's own title is used as-is."""
 stem=Path(path).stem.lower()
 words=[w for w in re.split(r'[-_]+',stem) if w and w!='bonus' and not w.isdigit()]
 if not words:return None
 return ' '.join(w.capitalize() for w in words)

def _bonus_section_html(bonuses,images,design=None):
 """Shared full-width bonus-offer layout used by every design (native and
 non-native alike) that has genuine AI-reported bonus data but no bonus
 section of its own already baked into the scraped template. Colors are
 pulled from the --primary/--primary-dark/--accent CSS vars that
 apply_dynamic_accent_theme() guarantees are defined for every design
 (aliased to that design's own native palette, re-tinted toward the
 product photo when one is available) — never hardcoded, so this always
 matches the product's own bottle/theme color instead of a fixed palette."""
 if not bonuses:return ''
 n=min(len(bonuses),6)
 bonus_imgs=_bonus_images(images,n)
 count_word=f'{n} Incredible Bonus{"es" if n!=1 else ""}'
 if design=='13':
  rows13=[]
  for i,b in enumerate(bonuses[:n]):
   bonus_img=bonus_imgs[i] if i<len(bonus_imgs) else None
   derived_title=_derive_bonus_title_from_filename(bonus_img) if bonus_img else None
   title=derived_title or str(b.get('title',''))
   desc=str(b.get('description',''))
   img_tag=(f'<img src="{html.escape(safe_rel(bonus_img))}" alt="{html.escape(title)}" width="130" height="130" loading="lazy">'
             if bonus_img else '')
   rows13.append(
    f'<div class="bonus-row">{img_tag}<div>'
    f'<h4>{html.escape(title)}</h4>'
    f'<p class="bonus-price">Retail Price - <s>$97</s> Today: FREE</p>'
    f'<p>{html.escape(desc)}</p></div></div>')
  return (
   '<section class="sec paper"><div class="container">'
   '<div class="bonus-wrap">'
   f'<div class="bonus-bar">Order 3 Or 6 Bottles &amp; Get {count_word} Free!</div>'
   '<div class="bonus-rows">'+''.join(rows13)+'</div>'
   '</div></div></section>')
 rows=[]
 for i,b in enumerate(bonuses[:n]):
  bonus_img=bonus_imgs[i] if i<len(bonus_imgs) else None
  # A fuzzy-matched image (filename carrying its own real title, e.g.
  # "bonus-heart-health-secrets.jpg") always wins over the AI's title, so
  # the printed heading can never describe something different from what's
  # actually pictured.
  derived_title=_derive_bonus_title_from_filename(bonus_img) if bonus_img else None
  title=derived_title or str(b.get('title',''))
  desc=str(b.get('description',''))
  img_col=''
  if bonus_img:
   img_col=(f'<div style="flex:0 0 180px;max-width:180px;"><img src="{html.escape(safe_rel(bonus_img))}" '
            f'alt="{html.escape(title)}" style="width:180px;max-width:100%;display:block;border-radius:6px;'
            'transform:rotate(-3deg);box-shadow:0 15px 30px rgba(0,0,0,.15);"></div>')
  rows.append(
   '<div style="display:flex;gap:28px;align-items:center;flex-wrap:wrap;background:#f5f5f7;'
   'padding:28px 32px;border-bottom:1px solid #e8e8ea;">'+img_col+
   '<div style="flex:1;min-width:240px;">'
   f'<h4 style="color:var(--primary,#2D1B4E);font-weight:800;font-size:1.3rem;margin:0 0 8px;">{html.escape(title)}</h4>'
   '<p style="color:var(--accent,#5B2E9E);font-weight:700;margin:0 0 10px;font-size:15px;">Retail Price - '
   '<s>$97</s> Today: FREE</p>'
   f'<p style="color:#666;font-size:14.5px;line-height:1.65;margin:0;">{html.escape(desc)}</p>'
   '</div></div>')
 return (
  '<section id="bonuses" style="margin:40px 0;">'
  '<div style="background:var(--primary-dark,#1A2744);color:#fff;text-align:center;padding:20px 20px;'
  f'font-size:21px;font-weight:800;border-radius:10px 10px 0 0;">Order 3 or 6 Bottles &amp; '
  f'Get {count_word} Free!</div>'
  '<div style="border-radius:0 0 10px 10px;overflow:hidden;">'+''.join(rows)+'</div></section>')

def build_native_page(data,domain,affiliate,images,filename,page_kind='index',design='8',site_root=None):
 """Build native (auto-themed, own template) pages via reliable string-template
 replacement. page_kind: 'index' (full page) or a subpage kind. design: which
 native template file to use (e.g. '8', '9')."""
 tpl=(TEMPLATE_DIR/f'design-{design}.source.md').read_text(encoding='utf-8')
 brand=data['brand']
 ingredients=data.get('ingredients',[])
 benefits=data.get('benefits',[])
 how_it_works=data.get('how_it_works',[])
 faqs=data.get('faqs',[])
 pricing=data.get('pricing',[])
 sample_reviews=data.get('sample_reviews',[])
 reviewer_names=data.get('reviewer_names',[])
 bonuses=data.get('bonuses',[])
 symptoms=data.get('symptoms',[])
 serving=data.get('serving_info',{})
 category=data.get('category','wellness supplement')
 description=data.get('description','')
 _native_cta=cta_texts(brand,category)

 # ── Color theme from hero/bottle image ──
 hero_img_path=None
 for p in images:
  if Path(p).stem.lower()=='hero':hero_img_path=p;break
 if not hero_img_path and images:hero_img_path=images[0]
 # Resolve to an actual openable disk path — the `images` list holds paths
 # relative to the output site (e.g. "assets/images/hero.png"), so without
 # site_root, PIL can't find the file and color extraction silently fails.
 hero_img_disk=None
 if hero_img_path:
  candidate=Path(hero_img_path)
  if candidate.is_absolute() and candidate.exists():
   hero_img_disk=candidate
  elif site_root:
   candidate2=Path(site_root)/hero_img_path
   if candidate2.exists():hero_img_disk=candidate2
  if not hero_img_disk and candidate.exists():hero_img_disk=candidate
 rgb=extract_brand_color(hero_img_disk) if hero_img_disk else None
 palette=build_theme_palette(rgb)

 # ── Card builders (design-aware: Design 10 uses distinct structural markup) ──
 def ing_card(ing,i):
  if design=='16':
   return (f'<div class="ing-card"><div class="ing-num-circle">{i+1}</div><div class="ing-content">'
           f'<h3 class="ing-name">{html.escape(ing.get("name",""))}</h3>'
           f'<div class="ing-desc"><p>{html.escape(ing.get("description",""))}</p></div></div></div>')
  if design=='10':
   return (f'<div class="ing-row"><div class="ing-badge">{i+1}</div><div>'
           f'<h4>{html.escape(ing.get("name",""))}</h4>'
           f'<p>{html.escape(ing.get("description",""))}</p></div></div>')
  if design=='13':
   return (f'<div class="col-12 col-lg-6"><div class="ing"><div class="ing-top">'
           f'<span class="ing-ic"><i class="bi bi-capsule"></i></span><div>'
           f'<h3>{html.escape(ing.get("name",""))}</h3>'
           f'<span class="ing-role">{html.escape(ing.get("role",""))}</span></div></div>'
           f'<p>{html.escape(ing.get("description",""))}</p></div></div>')
  return (f'<div class="ing-card"><div class="ing-num">{i+1}</div><div>'
          f'<h4>{html.escape(ing.get("name",""))}</h4>'
          f'<p>{html.escape(ing.get("description",""))}</p></div></div>')
 def hiw_card(step,i):
  if design=='16':
   return (f'<div class="step16"><div class="step16-num">{i+1}</div>'
           f'<h3>{html.escape(step.get("title",""))}</h3>'
           f'<p>{html.escape(step.get("text",""))}</p></div>')
  if design=='10':
   return (f'<div class="tl-item"><div class="tl-num">{i+1}</div><div>'
           f'<h4>{html.escape(step.get("title",""))}</h4>'
           f'<p>{html.escape(step.get("text",""))}</p></div></div>')
  if design=='13':
   return (f'<li><div class="step-num"></div><div>'
           f'<h3>{html.escape(step.get("title",""))}</h3>'
           f'<p>{html.escape(step.get("text",""))}</p></div></li>')
  return (f'<div class="step-card"><div class="step-num">{i+1}</div>'
          f'<h4>{html.escape(step.get("title",""))}</h4>'
          f'<p>{html.escape(step.get("text",""))}</p></div>')
 def benefit_card(b,i=0):
  parts=b.split(' — ',1) if ' — ' in b else [b,'']
  desc=parts[1] if len(parts)>1 else "Supports your daily "+category+" routine."
  desc=desc[:1].upper()+desc[1:] if desc else desc
  if design=='16':
   icon=['🌿','💪','🛡️','⚡','🧠','❤️','✨','🌱'][i%8]
   return (f'<div class="benefit-card"><div class="benefit-icon">{icon}</div>'
           f'<h3>{html.escape(parts[0])}</h3><p>{html.escape(desc)}</p></div>')
  if design=='10':
   return (f'<div class="benefit-item"><div class="benefit-dot">✓</div><div>'
           f'<h4>{html.escape(parts[0])}</h4><p>{html.escape(desc)}</p></div></div>')
  if design=='13':
   return (f'<div class="gain"><h3>{html.escape(parts[0])}</h3><p>{html.escape(desc)}</p></div>')
  return (f'<div class="card"><h4>{html.escape(parts[0])}</h4>'
          f'<p>{html.escape(desc)}</p></div>')
 def _avatar_tag(name,size=46):
  img=None
  initial=(name.strip()[:1] or '?').upper()
  return (f'<div style="width:{size}px;height:{size}px;border-radius:50%;background:var(--primary-light);'
          f'color:var(--primary-dark);display:flex;align-items:center;justify-content:center;'
          f'font-weight:700;font-family:\'Baloo 2\',sans-serif;flex:none">{initial}</div>')

 def review_card(i):
  name=reviewer_names[i] if i<len(reviewer_names) else f'Verified Buyer {i+1}'
  text=sample_reviews[i] if i<len(sample_reviews) else 'Great product, easy to use daily.'
  img=_get_reviewer_img(images,i)
  img_tag=f'<img src="{img}" alt="{html.escape(name)}">' if img else _avatar_tag(name)
  if design=='16':
   photo=(f'<img class="testi-photo" src="{img}" alt="{html.escape(name)}" width="92" height="92" loading="lazy">'
          if img else f'<div class="testi-initial">{html.escape((name.strip()[:1] or "?").upper())}</div>')
   return (f'<div class="testimonial">{photo}<div class="stars">★★★★★</div>'
           f'<div class="verified">Verified Purchase <span>✔</span></div>'
           f'<p>&ldquo;{html.escape(text)}&rdquo;</p><div class="name">{html.escape(name)}</div></div>')
  if design=='10':
   if i==0:
    return (f'<div class="rev-spotlight"><div class="rev-stars">★★★★★</div>'
            f'<p>"{html.escape(text)}"</p>'
            f'<div class="rev-head">{img_tag}<div><div class="rev-name">{html.escape(name)}</div>'
            f'<div class="rev-sub">Verified purchase</div></div></div></div>')
   return (f'<div class="rev-mini"><div class="rev-head">{img_tag}<div>'
           f'<div class="rev-name">{html.escape(name)}</div><div class="rev-sub">Verified purchase</div></div></div>'
           f'<p>{html.escape(text)}</p></div>')
  if design=='13':
   img=_get_reviewer_img(images,i)
   img_tag13=(f'<img src="{img}" alt="{html.escape(name)}" width="56" height="56" loading="lazy">'
              if img else _avatar_tag(name,56))
   return (f'<div class="col-12 col-md-6 col-lg-4"><div class="said">{img_tag13}'
           f'<h3>{html.escape(name)}</h3>'
           f'<div class="said-stars">★★★★★ <span class="said-ok">Verified purchase</span></div>'
           f'<p>&ldquo;{html.escape(text)}&rdquo;</p></div></div>')
  return (f'<div class="rev-card"><div class="rev-head">{img_tag}<div>'
          f'<div class="rev-name">{html.escape(name)}</div><div class="rev-sub">Verified purchase</div></div></div>'
          f'<div class="rev-stars">★★★★★</div><p>{html.escape(text)}</p></div>')
 def plan_card(pkg,i,sorted_pricing):
  bottles=pkg.get('bottles',i+1)
  _cta=cta_texts(brand,category)
  buy_text=_cta.get(f'pack{bottles}',_cta['mid'])
  slot_by_count={1:'bottle-2',2:'bottle-2',3:'bottle-3',6:'bottle-6'}
  slot=slot_by_count.get(bottles,f'bottle-{bottles}')
  img=_get_img(images,slot,i)
  prices=[(p.get('bottles',0),_price_num(p.get('price_per_bottle',''))) for p in sorted_pricing]
  is_best_value=bottles==max((b for b,_ in prices),default=bottles)
  is_middle=len(sorted_pricing)==3 and bottles==sorted(b for b,_ in prices)[1]
  if design=='10':
   badge=f'<span class="price-pkg-badge">{"Best Value" if is_best_value else "Most Popular"}</span>' if (is_best_value or is_middle) else ''
   row_cls='price-row top' if is_best_value else 'price-row'
   return (f'<div class="{row_cls}">'
           f'<div class="price-pkg"><img src="{img}" alt="{html.escape(brand)} {bottles} bottle pack">'
           f'<div><div class="price-pkg-name">{bottles} Bottles</div>{badge}</div></div>'
           f'<div class="price-val">{html.escape(str(pkg.get("price_per_bottle","")))}<small>per bottle</small></div>'
           f'<div class="price-val">{html.escape(_clean_total_value(pkg.get("total","")))}<small>{html.escape(str(pkg.get("shipping","Free Shipping")))}</small></div>'
           f'<div class="price-buy"><a class="btn" href="{affiliate}">{html.escape(buy_text)}</a></div></div>')
  if design=='16':
   total_num=_price_num(pkg.get('total',''))
   regular_rate=max((p for _,p in prices),default=0)
   was_total=regular_rate*bottles
   savings=was_total-total_num
   pp=str(pkg.get('price_per_bottle',''))
   _m=re.match(r'^(\D*?)(\d[\d.,]*)',pp.strip())
   amount=(f'<span>{html.escape(_m.group(1) or "")}</span>{html.escape(_m.group(2))}' if _m else html.escape(pp))
   tag=f'{bottles} Bottles'+(' · Best Value' if is_best_value else (' · Most Popular' if is_middle else ''))
   was_html=f'<s>${was_total:.0f}</s> ' if was_total>total_num else ''
   save_html=f'<div class="price-savings">SAVE ${savings:.0f}</div>' if savings>0 else ''
   bonus_html=''
   if is_best_value and bonuses:
    nb=len(bonuses)
    bonus_html=f'<div class="price-bonus">+ {nb} FREE BONUS{"ES" if nb>1 else ""}</div>'
   cc_img=next((safe_rel(p) for p in images if Path(p).stem.lower()=='credit-cards'),None)
   pay_html=(f'<div class="price-pay"><img src="{cc_img}" alt="Accepted payment methods" width="120" height="26" loading="lazy"></div>'
             if cc_img else '')
   return (f'<div class="price-card{" best-value" if is_best_value else ""}">'
           f'<div class="price-badge">{html.escape(tag)}</div>'
           f'<img class="price-img" src="{img}" alt="{html.escape(brand)} {bottles} bottle pack" width="150" height="150" loading="lazy">'
           f'<div class="price-amount">{amount}</div>'
           f'<div class="price-per">per bottle · {bottles*30}-day supply</div>'
           f'{save_html}{bonus_html}'
           f'<a class="price-btn" href="{affiliate}">{html.escape(buy_text)}</a>'
           f'<div class="price-guarantee">60-Day Money Back Guarantee</div>{pay_html}'
           f'<div class="price-total">TOTAL: {was_html}<strong>${total_num:.0f}</strong></div>'
           f'<div class="price-ship">{html.escape(str(pkg.get("shipping","Free Shipping")))}</div></div>')
  badge='<div class="plan-badge">Best Value</div>' if is_best_value else ('<div class="plan-badge" style="background:'+palette["accent"]+'">Most Popular</div>' if is_middle else '')
  cls='plan top' if is_best_value else 'plan'
  if design=='13':
   total_num=_price_num(pkg.get('total',''))
   regular_rate=max((p for _,p in prices),default=0)
   was_total=regular_rate*bottles
   savings=was_total-total_num
   tag='Best Value' if is_best_value else ('Most Popular' if is_middle else 'Basic')
   pack_cls='pack top' if is_best_value else 'pack'
   pill_cls=' accent' if is_best_value else ''
   was_html=f'<span class="pack-was">${was_total:.0f}</span>' if was_total>total_num else ''
   pills=[]
   if savings>0:
    pills.append(f'<div class="pack-badge-pill{pill_cls}"><i class="bi bi-check-circle-fill"></i>You Save ${savings:.0f}!</div>')
   if is_best_value:
    pills.append(f'<div class="pack-badge-pill{pill_cls}"><i class="bi bi-check-circle-fill"></i>Biggest Discount</div>')
   pills.append(f'<div class="pack-badge-pill{pill_cls}"><i class="bi bi-check-circle-fill"></i>60 Days Guarantee</div>')
   if is_best_value and bonuses:
    n_bonus=len(bonuses)
    pills.append(f'<div class="pack-badge-pill{pill_cls}"><i class="bi bi-check-circle-fill"></i>{n_bonus} Free Bonus{"es" if n_bonus>1 else ""}!</div>')
   cc_img=next((safe_rel(p) for p in images if Path(p).stem.lower()=='credit-cards'),None)
   pay_html=(f'<div class="pack-pay"><img src="{cc_img}" alt="Accepted payment methods" width="120" height="26" loading="lazy"></div>'
             if cc_img else '')
   return (f'<div class="col-12 col-md-6 col-lg-4"><div class="{pack_cls}">'
           f'<div class="pack-bar">{tag}</div>'
           f'<div class="pack-body">'
           f'<div class="pack-name">{bottles} Bottles</div><div class="pack-supply">{bottles*30}-Day Supply</div>'
           f'<img src="{img}" alt="{html.escape(brand)} {bottles} bottle pack" width="150" height="150" loading="lazy">'
           f'<div class="pack-price-row"><span class="pack-price-big">{html.escape(str(pkg.get("price_per_bottle","")))}</span><span class="pack-price-sub">/ Bottle</span></div>'
           f'<div class="pack-badges">{"".join(pills)}</div>'
           f'<a class="btn btn-ember w-100 pack-buy" href="{affiliate}"><i class="bi bi-cart3 me-1"></i> {html.escape(buy_text)}</a>'
           f'{cta_trust_line_html()}'
           f'<div class="pack-total">Total: {was_html}<b>${total_num:.0f}</b></div>'
           f'<div class="pack-ship">{html.escape(str(pkg.get("shipping","Free Shipping")))}</div>'
           f'</div>'
           f'{pay_html}'
           f'</div></div>')
  return (f'<div class="{cls}">{badge}<img src="{img}" alt="{html.escape(brand)} {bottles} bottle pack">'
          f'<div class="plan-ttl">{bottles} Bottles</div><div class="plan-sub">{bottles*30}-Day Supply</div>'
          f'<div class="plan-price">{html.escape(str(pkg.get("price_per_bottle","")))}<small> / bottle</small></div>'
          f'<div class="plan-tot">Total: {html.escape(_clean_total_value(pkg.get("total","")))}</div>'
          f'<div class="plan-ship">{html.escape(str(pkg.get("shipping","Free Shipping")))}</div>'
          f'<ul><li>{bottles} bottle{"s" if bottles>1 else ""} of {html.escape(brand)}</li>'
          f'<li>60-day money-back guarantee</li><li>Secure checkout</li></ul>'
          f'<a class="btn" href="{affiliate}">{html.escape(buy_text)}</a>{cta_trust_line_html()}</div>')
 def faq_row(f):
  if design=='16':
   return (f'<div class="faq-item"><button class="faq-q" type="button" aria-expanded="false">'
           f'<span>{html.escape(f.get("q",""))}</span><span class="faq-icon">+</span></button>'
           f'<div class="faq-a"><p>{html.escape(f.get("a",""))}</p></div></div>')
  return (f'<div class="faq-row"><button class="faq-btn" type="button">{html.escape(f.get("q",""))}</button>'
          f'<div class="faq-body"><p>{html.escape(f.get("a",""))}</p></div></div>')
 def symptom_card(s,i):
  if design=='16':
   return f'<li>{html.escape(s.get("title",""))}</li>'
  if design=='13':
   ic='bi-lightning-charge' if i%2==0 else 'bi-exclamation-circle'
   ic_cls='ic dark' if i%2==0 else 'ic'
   return (f'<div class="col-12 col-md-6 col-lg-4"><div class="card-x">'
           f'<div class="{ic_cls}"><i class="bi {ic}"></i></div>'
           f'<h3>{html.escape(s.get("title",""))}</h3>'
           f'<p>{html.escape(s.get("text",""))}</p></div></div>')
  return (f'<div class="pcard"><div class="num">0{i+1}</div>'
          f'<h4>{html.escape(s.get("title",""))}</h4>'
          f'<p>{html.escape(s.get("text",""))}</p></div>')
 def pro_row(b):
  title=b.split(' — ',1)[0] if ' — ' in b else b
  if design=='13':
   return f'<li><i class="bi bi-check-lg"></i><span>{html.escape(title)}</span></li>'
  return f'<li><span>{html.escape(title)}</span></li>'

 ing_html=''.join(ing_card(x,i) for i,x in enumerate(ingredients)) or '<p>Ingredient details available on the official product page.</p>'
 # NOTE: the authority-links box is NOT appended here — __ING_CARD_TEMPLATE__
 # sits inside the ingredients grid itself (e.g. <div class="grid g3"
 # id="ing-grid">), so concatenating it onto ing_html would squeeze it in
 # as a stray grid cell instead of a section-level block below the cards.
 # It's inserted after template substitution instead, once `soup` is a
 # real parsed DOM and the grid's wrap can be found properly — see below.
 hiw_html=''.join(hiw_card(x,i) for i,x in enumerate(how_it_works[:4]))
 benefit_html=''.join(benefit_card(b,i) for i,b in enumerate(benefits[:8]))
 rev_html=''.join(review_card(i) for i in range(min(3,max(len(sample_reviews),3))))
 def _price_num(s):
  try:return float(re.sub(r'[^0-9.]','',str(s)) or 0)
  except Exception:return 0
 sorted_pricing_asc=sorted(pricing[:3],key=lambda p:p.get('bottles',0))
 plan_html=''.join(plan_card(p,i,sorted_pricing_asc) for i,p in enumerate(sorted_pricing_asc))
 faq_html=''.join(faq_row(f) for f in faqs)
 symptom_html=''.join(symptom_card(s,i) for i,s in enumerate(symptoms[:3]))
 bal_pros_html=''.join(pro_row(b) for b in benefits[:6])
 orbit_fallback=['Daily Support','Named Ingredients','Made In USA','Quality Checked']
 orbit_names=[ing.get('name','') for ing in ingredients[:4] if ing.get('name')]
 orbit_names=(orbit_names+orbit_fallback)[:4]

 # ── Bonus section (only rendered if genuine bonus data exists) ──
 bonus_section_html=_bonus_section_html(bonuses,images,design)

 n_ing=len(ingredients)
 checks=(benefits[:4]+['Every ingredient checked against published research']*4)[:4]
 chips=[f'{n_ing} ingredients','Daily use','60-day guarantee','Made in USA']
 price_low=min((p.get('price_per_bottle','') for p in pricing),default='$49',key=lambda x:x)
 prices_nums=[p.get('price_per_bottle','') for p in pricing]
 price_high=prices_nums[0] if prices_nums else '$79'
 price_low_val=sorted(prices_nums,key=lambda s:float(re.sub(r'[^0-9.]','',s) or 0))[0] if prices_nums else '$49'
 # Every native template renders __HERO_DESC__ in the <header> hero AND
 # __WHATIS_P1__ in the what-is section — both were `description`, so the home
 # page showed the same paragraph twice. Subpages replace the header with a
 # banner, so only the home page (and legal/blog pages built from it) needs a
 # different what-is lead.
 whatis_p1=description
 if page_kind=='index' and description and '__HERO_DESC__' in tpl:
  whatis_p1=(f'{brand} is a {category} formulated with {n_ing} named ingredients.' if n_ing
             else f'{brand} is formulated to support {_support_phrase(category)} as part of a daily routine.')

 replacements={
  '__TITLE__':data.get('seo',{}).get('title',f'{brand} Reviews'),
  '__META_DESC__':data.get('seo',{}).get('description',description)[:160],
  '__CANONICAL__':current_domain_url(domain,'' if filename=='index.html' else filename),
  '__COLOR_PRIMARY__':palette['primary'],'__COLOR_DARK__':palette['primary_dark'],
  '__COLOR_LIGHT__':palette['primary_light'],'__COLOR_ACCENT__':palette['accent'],
  '__COLOR_ON_PRIMARY__':palette['on_primary'],
  '__YEAR__':str(date.today().year),
  '__BRAND__':brand,'__AFFILIATE__':affiliate,
  '__PILL_TEXT__':f'{n_ing} Named Ingredients — {category}',
  '__HERO_H1__':data.get('tagline',f'{brand} — Daily {category}'),
  '__HERO_DESC__':description,
  '__REVIEW_COUNT__':'2,500+',
  '__FACT1_NUM__':str(n_ing),'__FACT1_LABEL__':'Ingredients',
  '__FACT2_NUM__':_serving_per_day_label(serving),'__FACT2_LABEL__':'Serving',
  '__FACT3_NUM__':'60-Day','__FACT3_LABEL__':'Guarantee',
  '__FACT4_NUM__':'USA','__FACT4_LABEL__':'Made In',
  '__CHECK1__':checks[0] if len(checks)>0 else '',
  '__CHECK2__':checks[1] if len(checks)>1 else '',
  '__CHECK3__':checks[2] if len(checks)>2 else '',
  '__CHECK4__':checks[3] if len(checks)>3 else '',
  '__PRICE_FROM__':price_low_val,
  '__WHATIS_P1__':whatis_p1,
  '__WHATIS_CALLOUT__':data.get('whatis_callout') or f'{brand} is a dietary supplement, not a drug. It works best alongside a balanced diet and adequate hydration.',
  '__CHIP1__':chips[0],'__CHIP2__':chips[1],'__CHIP3__':chips[2],'__CHIP4__':chips[3],
  '__ING_HEADING__':f'What Are The Ingredients In {brand}?',
  '__ING_CARD_TEMPLATE__':ing_html,
  '__HIW_INTRO__':data.get('how_it_works_intro') or f'{brand} combines its ingredients to work together as part of a daily {category} routine.',
  '__HIW_CARD_TEMPLATE__':hiw_html,
  '__BENEFIT_CARD_TEMPLATE__':benefit_html,
  '__REVIEW_CARD_TEMPLATE__':rev_html,
  '__PLAN_CARD_TEMPLATE__':plan_html,
  '__BONUS_SECTION__':bonus_section_html,
  '__PRICING_NOTE__':data.get('pricing_note') or 'Larger bundles ship free and cost less per bottle. Promotional pricing is set at checkout and may change — confirm the current offer on the official order page.',
  '__GUARANTEE_TEXT__':data.get('guarantee_text') or f'Try {brand} daily. If it is not for you, contact support within 60 days for a refund, even if you have used the entire bottle.',
  '__FAQ_ROW_TEMPLATE__':faq_html,
  '__FINAL_TEXT__':data.get('final_cta_text') or f'Join thousands who have already added {brand} to their daily routine, backed by a 60-day guarantee.',
  '__PRICE_HIGH__':price_high,'__PRICE_LOW__':price_low_val,
  '__SYMPTOM_CARD_TEMPLATE__':symptom_html,
  '__CATEGORY__':category,
  '__SERVING_DAILY__':serving.get('daily_serving','1-2 capsules'),
  '__SERVING_PER_BOTTLE__':serving.get('per_bottle','60 capsules'),
  '__ORBIT1__':orbit_names[0],'__ORBIT2__':orbit_names[1],
  '__ORBIT3__':orbit_names[2],'__ORBIT4__':orbit_names[3],
  '__BAL_PROS_TEMPLATE__':bal_pros_html,
  '__CTA_HEADER__':_native_cta['header'],'__CTA_HERO__':_native_cta['hero'],
  '__CTA_CLOSING__':_native_cta['closing'],'__CTA_AFTERFAQ__':_native_cta['afterFaq'],
  '__CTA_STICKY__':f'Get {brand} – {GUARANTEE_DAYS}-Day Guarantee →',
 }
 html_out=tpl
 for k,v in replacements.items():
  html_out=html_out.replace(k,str(v))

 # ── Images: hero, feature-shot, guarantee, badges ──
 html_out=html_out.replace('assets/images/hero.png',_get_img(images,'hero',0) or 'assets/images/hero.png')
 feat=_get_img(images,'how-it-works',0) or _get_img(images,'hero',0)
 html_out=html_out.replace('assets/images/feature-shot.png',feat or 'assets/images/hero.png')
 html_out=html_out.replace('assets/images/bottle-6.png',_get_img(images,'bottle-6',2) or 'assets/images/hero.png')
 # Badge/guarantee images — use the publisher's own upload for that exact
 # slot when one exists (this also picks up the real .webp/.jpg/.png
 # extension the file was actually saved under, since save_uploaded() may
 # have converted it to WebP). Left as the literal placeholder path when no
 # matching upload exists, same as before.
 for badge in ('badge-usa','badge-fda','badge-gmp','badge-natural','guarantee'):
  exact=next((safe_rel(p) for p in images if Path(p).stem.lower()==badge),None)
  if exact:html_out=html_out.replace(f'assets/images/{badge}.png',exact)

 # ── Optional user-supplied GA4 / Search Console / Bing verification ──
 tracking=data.get('tracking') or {}
 head_extra=''
 if tracking.get('gsc_verify'):
  head_extra+=f'<meta name="google-site-verification" content="{html.escape(tracking["gsc_verify"])}">\n'
 if tracking.get('bing_verify'):
  head_extra+=f'<meta name="msvalidate.01" content="{html.escape(tracking["bing_verify"])}">\n'
 if tracking.get('ga_id'):
  ga_id=html.escape(tracking['ga_id'])
  head_extra+=(f'<script async src="https://www.googletagmanager.com/gtag/js?id={ga_id}"></script>\n'
               f"<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}"
               f"gtag('js',new Date());gtag('config','{ga_id}');</script>\n")
 if head_extra and '</head>' in html_out:
  html_out=html_out.replace('</head>',head_extra+'</head>',1)

 # ── If this is a subpage, strip to just that section + a simple banner ──
 if page_kind!='index':
  soup=BeautifulSoup(html_out,'html.parser')
  keep_id={'what-is':'what-is','how-it-works':'how-it-works','ingredients':'ingredients',
           'benefits':'benefits','reviews':'reviews','faq':'faq'}.get(page_kind)
  main_sections=soup.find_all('section')
  for sec in main_sections:
   sid=sec.get('id','')
   if sid!=keep_id:sec.decompose()
  # Replace header/hero with simple banner
  header=soup.find('header')
  labels={'what-is':f'What Is {brand}?','how-it-works':f'How {brand} Works','ingredients':f'{brand} Ingredients',
          'benefits':f'{brand} Benefits','reviews':f'{brand} Reviews','faq':f'{brand} FAQ'}
  if header:
   banner=BeautifulSoup(f'<div style="background:{palette["primary_dark"]};padding:50px 0;text-align:center">'
                         f'<h1 style="color:#fff;margin:0">{html.escape(labels.get(page_kind,brand))}</h1></div>','html.parser')
   header.replace_with(banner)
 else:
  soup=BeautifulSoup(html_out,'html.parser')
  # Quick Facts box — the real home page only; page_kind=='index' is also
  # how legal pages/blog articles reuse this function's nav/footer chrome,
  # which filename=='index.html' tells apart from the actual homepage.
  if filename=='index.html':
   whatis_sec=soup.find('section',id='what-is')
   if whatis_sec:
    _section_wrap(whatis_sec).append(
     BeautifulSoup(quick_facts_html(data,_reuse_panel_class(whatis_sec)),'html.parser'))

 # ── Unique <title>/meta description per subpage ──
 # rebuild_metadata() always wrote the same site-wide data['seo']['title'] on
 # every page; page_variant() (scraped pipeline) already overrides it per
 # subpage kind to avoid duplicate titles across the site, but that fix was
 # never ported to the native pipeline — every native design (6/8/9/10/11)
 # was shipping the identical <title> and meta description on all 7 pages.
 page_titles={'what-is':f'What Is {brand}?','how-it-works':f'How {brand} Works',
              'ingredients':f'{brand} Ingredients','benefits':f'{brand} Benefits',
              'reviews':f'{brand} Reviews','faq':f'{brand} FAQ'}
 page_descs={'what-is':(description or f'What {brand} is and what it is formulated to support.')[:160],
             'how-it-works':(data.get('how_it_works_intro') or f'How {brand} is designed to work.')[:160],
             'ingredients':f'All {n_ing} {brand} ingredients explained individually.'[:160],
             'benefits':f'The wellness benefits {brand} is formulated to support.'[:160],
             'reviews':f'Real customer reviews and ratings for {brand}.'[:160],
             'faq':f'Answers to common questions about {brand}.'[:160]}
 meta_desc_tag=soup.find('meta',attrs={'name':'description'})
 if page_kind in page_titles:
  page_title=f'{page_titles[page_kind]} | {brand}'
  if soup.title:soup.title.string=page_title
  if meta_desc_tag:meta_desc_tag['content']=page_descs[page_kind]

 # ── Social preview (Open Graph/Twitter) + Product/FAQ structured data ──
 # The scraped-template pipeline gets these from rebuild_metadata()/add_jsonld(),
 # but native pages never went through either — every native design (6/8/9/10/11)
 # shipped with no OG/Twitter tags and no JSON-LD, hurting share-preview quality
 # and losing out on rich-result eligibility in Bing/Google search.
 canonical=current_domain_url(domain,'' if filename=='index.html' else filename)
 seo_title=(soup.title.string if soup.title and soup.title.string else None) or data.get('seo',{}).get('title') or f'{brand} Reviews'
 seo_desc=(meta_desc_tag['content'] if meta_desc_tag else None) or (data.get('seo',{}).get('description') or description)[:160]
 for p,v in [('og:title',seo_title),('og:description',seo_desc),('og:url',canonical),
             ('og:type','website'),('og:site_name',brand),('twitter:card','summary_large_image'),
             ('twitter:title',seo_title),('twitter:description',seo_desc)]:
  set_or_add_meta(soup,p,v,'property')
 og_imgs=seo_images(images) if images else []
 if og_imgs:
  og_img=og_imgs[0]
  set_or_add_meta(soup,'og:image',current_domain_url(domain,og_img),'property')
  set_or_add_meta(soup,'twitter:image',current_domain_url(domain,og_img),'property')
 # Legal pages are built by calling this function with page_kind='index' (so
 # nothing gets stripped here) and the CALLER strips all sections afterward —
 # at this point every section (FAQ included) is still in `soup`, so running
 # add_jsonld() here would embed FAQPage/Product schema for content that
 # won't actually be visible on the finished legal page. Skip it for that
 # case; a genuine index.html or subpage call always has filename=='index.html'
 # when page_kind=='index'.
 if not (page_kind=='index' and filename!='index.html'):
  add_jsonld(soup,data,domain,canonical,affiliate,images)

 ensure_legal_footer_links(soup)
 ensure_core_page_links(soup,brand)
 if filename.startswith('blog/'):rebase_internal_page_links(soup,'../')
 # Authority links — appended once the ingredients section exists as real
 # DOM (not string-concatenated into __ING_CARD_TEMPLATE__, which sits
 # inside the ingredients GRID itself and would squeeze this in as a stray
 # grid cell instead of a section-level block below the cards).
 ing_sec=soup.find('section',id='ingredients')
 if ing_sec:
  _ing_links_html=ingredient_authority_links_html(
   _match_ingredient_authority_links(ingredients),_reuse_eyebrow_class(ing_sec))
  if _ing_links_html:_section_wrap(ing_sec).append(BeautifulSoup(_ing_links_html,'html.parser'))
 apply_img_sizing(soup,site_root,brand,category)
 inject_img_css(soup)
 inject_cta_extras(soup,brand,affiliate)
 ensure_social_meta(soup,domain,images)
 # ── Minify this native design's inline CSS/JS — the counterpart to
 # _localize_one_asset()'s minification of the reference pipeline's
 # external assets/css|js files, since native designs carry their CSS/JS
 # inline instead of as separate files. Third-party/CDN scripts (src=...,
 # e.g. bootstrap.bundle.min.js) are already minified and left untouched;
 # JSON-LD <script type="application/ld+json"> blocks are structured data,
 # not JS, so they're skipped rather than run through a JS minifier. ──
 # Design 15 re-rolls its look per site: apply this site's recipe (fonts,
 # layout, section order, animations) before minification so it is minified
 # together with the rest of the page's inline CSS/JS.
 if design=='15':design15.apply(soup,data.get('_d15'),filename,page_kind)
 for style_tag in soup.find_all('style'):
  if style_tag.string:style_tag.string=minify_css(style_tag.string)
 for script_tag in soup.find_all('script'):
  if script_tag.get('src'):continue
  stype=(script_tag.get('type') or '').lower()
  if stype and stype not in ('text/javascript','application/javascript','module'):continue
  if script_tag.string:script_tag.string=minify_js(script_tag.string)
 return str(soup)

def make_page(base_soup,data,domain,affiliate,images,design,filename,site_root):
 soup=BeautifulSoup(str(base_soup),'html.parser')
 canonical=current_domain_url(domain,'' if filename=='index.html' else filename)
 populate(soup,data,design,domain,affiliate)
 # Quick Facts box — home page only (make_page() is never called for any
 # other page; page_variant() builds every subpage instead). Appended
 # INSIDE the section's own content wrapper (never as a sibling of the
 # <section>, which renders full body-width with no padding — the wrap is
 # what carries the centering/max-width/padding every other block on the
 # page already lines up with), reusing an existing callout/info-box class
 # from the same section for its visual styling when one exists.
 whatis_sec=section(soup,'what-is','about')
 if whatis_sec:
  _section_wrap(whatis_sec).append(
   BeautifulSoup(quick_facts_html(data,_reuse_panel_class(whatis_sec)),'html.parser'))
 apply_dynamic_accent_theme(soup,design,images,site_root)
 dehardcode_inline_accent_colors(soup,design)
 rebuild_metadata(soup,data,canonical,images,domain)
 strip_old_product_images(soup,TEMPLATES[design]['old_domains'],design)
 _theme_rgb,_base_css_text=localize_reference_assets(soup,site_root,design,TEMPLATES[design]['old_domains'],data.get('brand',''),images,data.get('reviewer_names',[]))
 localize_images(soup,images,design)
 scrub_image_alts(soup,data)
 strip_third_party_fa_kit(soup)
 apply_img_sizing(soup,site_root,data.get('brand',''),data.get('category',''))
 inject_img_css(soup)
 inject_cta_extras(soup,data.get('brand',''),affiliate)
 sanitize_urls(soup,TEMPLATES[design]['old_domains'],domain,affiliate)
 sanitize_text_domains(soup,TEMPLATES[design]['old_domains'],domain)
 replace_all_brand_refs(soup,data['brand'])
 internal_links(soup,domain)
 ensure_legal_footer_links(soup)
 ensure_core_page_links(soup,data['brand'])
 set_ctas(soup,affiliate)
 rebuild_metadata(soup,data,canonical,images,domain)
 ensure_social_meta(soup,domain,images)
 add_jsonld(soup,data,domain,canonical,affiliate,images)
 set_ctas(soup,affiliate)
 html_out='<!doctype html>\n'+str(soup)
 if _theme_rgb and _base_css_text:html_out=retheme_html_inline(html_out,_theme_rgb,_base_css_text)
 return html_out

def page_variant(base_soup,data,domain,affiliate,images,design,filename,kind,site_root):
 soup=BeautifulSoup(str(base_soup),'html.parser')
 main=soup.find('main') or soup.body
 # Not every template puts an id on the section this subpage needs to keep
 # (e.g. design 2's FAQ section is only class="faq-section", no id="faq")
 # — a raw sid-in-keep_ids check then matches nothing, decomposes the FAQ
 # section along with everything else, and the whole subpage ends up with
 # no FAQ content at all. Reuse the same id-or-class lookup used elsewhere
 # to find the actual target section before deciding what to remove.
 # 'how-it-works' alone misses designs (e.g. design 4) that never use that
 # exact id/class — their equivalent section is "how to order" instead,
 # marked as id="how-to-order" (on a sibling title-band div, not the
 # <section> itself) with class="order-how-section" on the real content
 # <section>. Without 'order-how' here, section() falls through to matching
 # that id on the title-band div, the how-it-works.html section-removal loop
 # below never finds a <section> "is" that div, and it decomposes the real
 # order-how-section content too — leaving the whole subpage empty.
 kind_aliases={'what-is':('what-is','about'),'how-it-works':('how-it-works','order-how','how-to-order'),
  'ingredients':('ingredients',),'benefits':('benefits',),
  'reviews':('reviews','customer-reviews'),'faq':('faq','faqs')}
 target_sec=section(soup,*kind_aliases.get(kind,(kind,)))
 if main:
  for sec in list(main.find_all('section',recursive=True)):
   sid=sec.get('id','')
   if sid in ('hero','home') or sec is target_sec:continue
   sec.decompose()
  # Some designs (e.g. design 4) precede each section with its own standalone
  # label/band div (<div class="sec-title-band">/"pricing-band"> — a heading +
  # subtitle, not part of the <section> itself). The sweep above only ever
  # touches <section> tags, so removing every *other* section left each of
  # these band divs behind with nothing under them — e.g. ingredients.html
  # showed a "Reviews"/"Guarantee"/"Benefits"/"FAQ"/... heading with a blank
  # gap where that section used to be. Drop any band whose very next sibling
  # isn't the <section> we just kept (target_sec) — this mirrors the same fix
  # already applied for legal pages in legal_page() below.
  for band in list(main.find_all('div',class_=re.compile(r'\bsec-title-band\b|\bpricing-band\b'))):
   nxt=band.find_next_sibling(True)
   if target_sec is not None and nxt is target_sec:continue
   band.decompose()
 # Replace the full hero on subpages with a compact page-title banner,
 # so it's immediately clear this is a distinct page and not the homepage.
 page_labels={'what-is':'What Is {brand}?','how-it-works':'How {brand} Works',
              'ingredients':'{brand} Ingredients','benefits':'{brand} Benefits',
              'reviews':'{brand} Reviews','faq':'{brand} FAQ'}
 header_tag=soup.find('header')
 if header_tag and kind in page_labels:
  brand_name=data.get('brand','')
  label=page_labels[kind].replace('{brand}',brand_name)
  banner_html=(f'<div class="bpo-strip" style="text-align:center;padding:26px 16px;'
               f'background:#1A2744"><h1 class="page-banner-h1" style="color:#fff;font-size:1.6rem;margin:0">'
               f'{html.escape(label)}</h1></div>')
  banner_soup=BeautifulSoup(banner_html,'html.parser')
  header_tag.replace_with(banner_soup)
  # A page should only ever carry one <h1> — the banner's own title just
  # inserted above. The template's original product-title h1 still sits
  # elsewhere in the DOM (it's a sibling, not inside <header>), so it
  # survives the replace_with untouched; text-filling it in populate() would
  # leave two <h1> tags on every subpage. Remove it outright instead — by
  # element, not by a "product-title" class guess, since not every design
  # names that h1 the same way (e.g. design 6 uses its own Tailwind classes).
  for stray_h1 in soup.find_all('h1'):
   if 'page-banner-h1' not in (stray_h1.get('class') or []):stray_h1.decompose()
 populate(soup,data,design,domain,affiliate)
 apply_dynamic_accent_theme(soup,design,images,site_root)
 dehardcode_inline_accent_colors(soup,design)
 canonical=current_domain_url(domain,filename)
 rebuild_metadata(soup,data,canonical,images,domain)
 strip_old_product_images(soup,TEMPLATES[design]['old_domains'],design)
 _theme_rgb,_base_css_text=localize_reference_assets(soup,site_root,design,TEMPLATES[design]['old_domains'],data.get('brand',''),images,data.get('reviewer_names',[]))
 localize_images(soup,images,design)
 scrub_image_alts(soup,data)
 strip_third_party_fa_kit(soup)
 apply_img_sizing(soup,site_root,data.get('brand',''),data.get('category',''))
 inject_img_css(soup)
 inject_cta_extras(soup,data.get('brand',''),affiliate)
 sanitize_urls(soup,TEMPLATES[design]['old_domains'],domain,affiliate)
 sanitize_text_domains(soup,TEMPLATES[design]['old_domains'],domain)
 replace_all_brand_refs(soup,data['brand'])
 internal_links(soup,domain)
 ensure_legal_footer_links(soup)
 ensure_core_page_links(soup,data['brand'])
 set_ctas(soup,affiliate)
 rebuild_metadata(soup,data,canonical,images,domain)
 # rebuild_metadata() always writes the site-wide data['seo']['title'] (and
 # matching og:/twitter: title), so every subpage kind it's called for here
 # (faq/reviews/benefits/ingredients/how-it-works/what-is) ended up with the
 # exact same <title> as the homepage — duplicate titles across the site,
 # which search engines treat as near-duplicate pages. Give each kind its
 # own title, reusing the page_labels text already built above for the banner.
 if kind in page_labels:
  brand_name=data.get('brand','')
  page_title=f'{page_labels[kind].replace("{brand}",brand_name)} | {brand_name}'
  if soup.title:soup.title.string=page_title
  set_or_add_meta(soup,'og:title',page_title,'property')
  set_or_add_meta(soup,'twitter:title',page_title,'property')
  # Same problem as the title above, one field over: rebuild_metadata()
  # only ever writes the site-wide data['seo']['description'], so every
  # subpage kind shared that exact same meta description/og:description
  # with the homepage AND with every other subpage — a duplicate-content
  # signal search engines penalize, and it fed straight into add_jsonld()
  # below (which reads this same meta tag) giving every subpage's WebPage
  # node an identical description too.
  n_ing=len(data.get('ingredients',[]))
  page_descs={'what-is':(data.get('description') or f'What {brand_name} is and what it is formulated to support.')[:160],
              'how-it-works':(data.get('how_it_works_intro') or f'How {brand_name} is designed to work.')[:160],
              'ingredients':f'All {n_ing} {brand_name} ingredients explained individually.'[:160],
              'benefits':f'The wellness benefits {brand_name} is formulated to support.'[:160],
              'reviews':f'Real customer reviews and ratings for {brand_name}.'[:160],
              'faq':f'Answers to common questions about {brand_name}.'[:160]}
  page_desc=page_descs[kind]
  set_or_add_meta(soup,'description',page_desc)
  set_or_add_meta(soup,'og:description',page_desc,'property')
  set_or_add_meta(soup,'twitter:description',page_desc,'property')
 ensure_social_meta(soup,domain,images)
 add_jsonld(soup,data,domain,canonical,affiliate,images)
 set_ctas(soup,affiliate)
 html_out='<!doctype html>\n'+str(soup)
 if _theme_rgb and _base_css_text:html_out=retheme_html_inline(html_out,_theme_rgb,_base_css_text)
 return html_out
LEGAL_PAGE_CONTENT={
 'terms.html':{
  'title':'Terms of Use',
  'body':lambda b,d: f"""
<p>Welcome to {b}. By accessing or using this website, you agree to be bound by these Terms of Use. If you do not agree with any part of these terms, please do not use this site.</p>
<h3>Use of Site</h3>
<p>This website provides general information about {b} and related products. Content is provided for informational purposes only and should not be considered medical or professional advice.</p>
<h3>Intellectual Property</h3>
<p>All content on this site, including text, graphics, logos and images, is the property of its respective owners and is protected by applicable copyright and trademark laws.</p>
<h3>Affiliate Relationships</h3>
<p>This website may contain affiliate links. We may earn a commission when you make a purchase through these links, at no additional cost to you. See our Affiliate Disclosure for more details.</p>
<h3>No Warranty</h3>
<p>Information on this site is provided "as is" without warranties of any kind, either express or implied. We do not guarantee the accuracy, completeness or usefulness of any content.</p>
<h3>Limitation of Liability</h3>
<p>{b} and this website's publishers shall not be liable for any damages arising from your use of, or inability to use, this website or any linked third-party sites.</p>
<h3>Changes to Terms</h3>
<p>We reserve the right to modify these Terms of Use at any time. Continued use of the site after changes constitutes acceptance of the revised terms.</p>
<h3>Contact</h3>
<p>If you have questions about these Terms of Use, please reach out via our Contact page.</p>
""",
 },
 'privacy-policy.html':{
  'title':'Privacy Policy',
  'body':lambda b,d: f"""
<p>Your privacy is important to us. This Privacy Policy explains how {b} and this website collect, use and protect information when you visit our site.</p>
<h3>Information We Collect</h3>
<p>We may collect basic, non-personally identifiable information such as browser type, pages visited and time spent on the site through standard analytics tools and cookies.</p>
<h3>How We Use Information</h3>
<p>Information collected is used solely to improve site performance, understand visitor behavior and enhance the overall user experience. We do not sell personal information to third parties.</p>
<h3>Cookies</h3>
<p>This site may use cookies to enhance your browsing experience. You can choose to disable cookies through your browser settings, though this may affect certain site features.</p>
<h3>Third-Party Links</h3>
<p>Our site may contain links to third-party websites, including the official {b} product page. We are not responsible for the privacy practices of these external sites.</p>
<h3>Data Security</h3>
<p>We take reasonable measures to protect any information collected, but no method of transmission over the internet is 100% secure.</p>
<h3>Children's Privacy</h3>
<p>This site is not directed at children under 18, and we do not knowingly collect information from minors.</p>
<h3>Changes to This Policy</h3>
<p>We may update this Privacy Policy periodically. Please review this page for the latest information.</p>
<h3>Contact</h3>
<p>For privacy-related questions, please visit our Contact page.</p>
""",
 },
 'disclaimer.html':{
  'title':'Disclaimer',
  'body':lambda b,d: f"""
<p>The information provided on this website about {b} is for general informational purposes only and is not intended as medical advice.</p>
<h3>Not Medical Advice</h3>
<p>Content on this site should not be used to diagnose, treat, cure or prevent any disease. Always consult a qualified healthcare professional before starting any new supplement, especially if you are pregnant, nursing, taking medication or have a pre-existing medical condition.</p>
<h3>FDA Disclosure</h3>
<p>Statements regarding {b} have not been evaluated by the U.S. Food and Drug Administration. This product is not intended to diagnose, treat, cure or prevent any disease.</p>
<h3>Individual Results May Vary</h3>
<p>Testimonials and reviews reflect individual experiences and are not a guarantee of results. Your experience with {b} may differ from those described on this site.</p>
<h3>Affiliate Disclosure</h3>
<p>This website may contain affiliate links to the official {b} seller. We may earn a commission on qualifying purchases at no extra cost to you.</p>
<h3>Accuracy of Information</h3>
<p>While we strive to keep information accurate and up to date, product formulations, pricing and availability may change. Always verify current details on the official {b} product page before purchasing.</p>
<h3>Contact</h3>
<p>Questions about this disclaimer can be directed to us via our Contact page.</p>
""",
 },
 'refund-policy.html':{
  'title':'Refund Policy',
  'body':lambda b,d: f"""
<p>{b} is typically backed by the seller's money-back guarantee. This page outlines general guidance — always confirm exact terms on the official {b} order page before purchasing.</p>
<h3>Money-Back Guarantee</h3>
<p>Most {b} orders are covered by a guarantee window (commonly around 60 days from the date of purchase) allowing you to request a refund if you are not satisfied with your results.</p>
<h3>How to Request a Refund</h3>
<p>To request a refund, contact the official {b} customer support team directly through the channels listed on the official order confirmation email or product website. Refund requests are typically handled by the seller, not by this website.</p>
<h3>Eligibility</h3>
<p>Refund eligibility, exact time windows and any conditions (such as returning unused product) are set by the official seller and may vary. Please review the terms provided at checkout.</p>
<h3>Processing Time</h3>
<p>Refunds, once approved, are generally processed within a standard banking timeframe, though this can vary by payment provider and seller policy.</p>
<h3>This Website's Role</h3>
<p>This is an independent informational website and is not the seller of {b}. All purchases, refunds and customer support are handled directly by the official product seller.</p>
<h3>Contact</h3>
<p>For refund questions specific to your order, please contact the official seller support listed on your receipt. For questions about this website, use our Contact page.</p>
""",
 },
 'about.html':{
  'title':'About Us',
  'body':lambda b,d: f"""
<p>Welcome to our independent {b} information website. Our goal is to provide clear, honest and well-researched content to help you make informed decisions.</p>
<h3>Our Mission</h3>
<p>We aim to present factual, easy-to-understand information about {b}, including ingredients, how it works, pricing and frequently asked questions, so visitors can evaluate the product for themselves.</p>
<h3>Editorial Standards</h3>
<p>Content on this site is researched and written with an emphasis on accuracy and transparency. We clearly disclose affiliate relationships and avoid making unverified medical claims.</p>
<h3>Independent Publisher</h3>
<p>This website is an independent publisher and is not affiliated with, endorsed by, or officially connected to the manufacturer of {b} unless explicitly stated. All trademarks belong to their respective owners.</p>
<h3>Affiliate Disclosure</h3>
<p>This site may earn a commission from qualifying purchases made through links on this page, at no additional cost to you.</p>
<h3>Get in Touch</h3>
<p>Have feedback or questions? Visit our Contact page — we'd love to hear from you.</p>
""",
 },
 'contact.html':{
  'title':'Contact Us',
  'body':lambda b,d: f"""
<p>We'd love to hear from you. Whether you have a question about {b}, feedback on our content, or a general inquiry, feel free to reach out.</p>
<h3>General Inquiries</h3>
<p>For questions about the content on this website, our editorial process, or this site in general, please use the contact details below.</p>
<h3>Product & Order Support</h3>
<p>For questions about an existing {b} order, shipping, billing or refunds, please contact the official seller's customer support team directly — they are best equipped to help with order-specific issues, as this website does not process orders or payments.</p>
<h3>Email</h3>
<p>You can reach our editorial team by email. Please allow a few business days for a response.</p>
<h3>Business Inquiries</h3>
<p>For partnership, advertising or other business inquiries, please include full details in your message so we can respond appropriately.</p>
""",
 },
}

def make_legal_page(base_soup,data,domain,affiliate,images,design,filename,site_root):
 """Build a simple legal/info page keeping the template's nav+footer but replacing body content."""
 soup=BeautifulSoup(str(base_soup),'html.parser')
 brand=data['brand']
 page_def=LEGAL_PAGE_CONTENT[filename]
 page_title=page_def['title']
 body_html=page_def['body'](brand,data)

 populate(soup,data,design,domain,affiliate)
 apply_dynamic_accent_theme(soup,design,images,site_root)
 dehardcode_inline_accent_colors(soup,design)
 canonical=current_domain_url(domain,filename)

 main=soup.find('main') or soup.body
 hero=soup.find('header')
 if main:
  for sec in list(main.find_all('section',recursive=True)):
   sec.decompose()

 wrap_cls='bpo-wrap' if soup.find(class_='bpo-wrap') else ''
 narrow_cls='bpo-narrow' if soup.find(class_='bpo-narrow') else ''
 sec_cls='bpo-sec' if soup.find(class_=re.compile('bpo-sec')) else ''

 content_html=f'''<section class="{sec_cls}"><div class="{wrap_cls}"><div class="{narrow_cls}" style="padding:40px 0;max-width:760px;margin:0 auto">
 <h1 style="margin-bottom:6px">{page_title}</h1>
 <p style="color:#8a8a8a;font-size:.85rem;margin-bottom:28px">{brand} — Last updated {date.today().strftime('%B %Y')}</p>
 {body_html}
 </div></div></section>'''

 new_section=BeautifulSoup(content_html,'html.parser')

 footer=soup.find('footer')
 if footer:
  footer.insert_before(new_section)
 elif main:
  main.append(new_section)
 else:
  soup.body.append(new_section)

 if hero:hero.decompose()

 rebuild_metadata(soup,data,canonical,images,domain)
 seo_title=f'{page_title} | {brand}'
 if soup.title:soup.title.string=seo_title
 plain_snippet=re.sub(r'<[^>]+>','',body_html)[:150].strip()
 set_or_add_meta(soup,'description',f'{page_title} for {brand}. {plain_snippet}'[:155])

 strip_old_product_images(soup,TEMPLATES[design]['old_domains'],design)
 _theme_rgb,_base_css_text=localize_reference_assets(soup,site_root,design,TEMPLATES[design]['old_domains'],data.get('brand',''),images,data.get('reviewer_names',[]))
 localize_images(soup,images,design)
 scrub_image_alts(soup,data)
 strip_third_party_fa_kit(soup)
 apply_img_sizing(soup,site_root,data.get('brand',''),data.get('category',''))
 inject_img_css(soup)
 inject_cta_extras(soup,data.get('brand',''),affiliate)
 ensure_social_meta(soup,domain,images)
 sanitize_urls(soup,TEMPLATES[design]['old_domains'],domain,affiliate)
 sanitize_text_domains(soup,TEMPLATES[design]['old_domains'],domain)
 replace_all_brand_refs(soup,brand)
 internal_links(soup,domain)
 ensure_legal_footer_links(soup)
 ensure_core_page_links(soup,brand)
 set_ctas(soup,affiliate)
 add_jsonld(soup,data,domain,canonical,affiliate,images)
 set_ctas(soup,affiliate)
 html_out='<!doctype html>\n'+str(soup)
 if _theme_rgb and _base_css_text:html_out=retheme_html_inline(html_out,_theme_rgb,_base_css_text)
 return html_out

def write_robots_sitemap(site,domain,page_defs,lastmod_overrides=None):
 # robots.txt stays a blanket "allow everything, disallow nothing" — that
 # includes AI crawlers (GPTBot, ClaudeBot, PerplexityBot, Google-Extended):
 # none of them are ever named here, so none of them are blocked.
 today=date.today().isoformat()
 lastmod_overrides=lastmod_overrides or {}
 sitemap_url=domain.rstrip('/')+'/sitemap.xml'
 (site/'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {sitemap_url}\n',encoding='utf-8')
 files=['index.html']+[x[0] for x in page_defs]
 body=['<?xml version="1.0" encoding="UTF-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
 for fn in files:
  loc=html.escape(current_domain_url(domain,'' if fn=='index.html' else fn))
  priority='1.0' if fn=='index.html' else '0.8'
  # Every page is generated in this same request, so "today" already IS the
  # real last-modified date for all of them — blog articles use their own
  # datePublished explicitly (same value today, but correct if a future
  # regenerate ever preserves an original publish date instead).
  lastmod=lastmod_overrides.get(fn,today)
  body.append(f'<url><loc>{loc}</loc><lastmod>{lastmod}</lastmod><changefreq>monthly</changefreq><priority>{priority}</priority></url>')
 body.append('</urlset>');(site/'sitemap.xml').write_text('\n'.join(body),encoding='utf-8')

def write_llms_txt(site,domain,data,blog_articles,extra_pages=None):
 """llms.txt (the emerging robots.txt-for-LLMs convention): a short plain-
 text/markdown summary plus links to every real content page, so an AI
 crawler/answer-engine can find the actual pages without guessing URLs."""
 brand=data.get('brand','');category=data.get('category','wellness supplement')
 desc=(data.get('description') or f'{brand} is a {category}.').strip()
 lines=[f'# {brand}','',f'> {brand} is a {category}. {desc}'.strip(),'','## Pages']
 core_pages=[('','Home — overview, pricing and FAQ'),
  ('what-is-product.html',f'What {brand} is'),
  ('how-it-works.html',f'How {brand} works'),
  ('ingredients.html',f'{brand} ingredients, explained individually'),
  ('benefits.html',f'{brand} benefits'),
  ('reviews.html',f'{brand} customer reviews'),
  ('faq.html',f'{brand} frequently asked questions')]
 for fn,label in core_pages:
  lines.append(f'- [{label}]({current_domain_url(domain,fn)})')
 if blog_articles:
  lines.append('')
  lines.append('## Blog')
  for a in blog_articles:
   lines.append(f'- [{a["h1"]}]({current_domain_url(domain,"blog/"+a["slug"]+".html")}): {a["meta_desc"]}')
 for fn,label in (extra_pages or []):
  lines.append(f'- [{label}]({current_domain_url(domain,fn)})')
 (site/'llms.txt').write_text('\n'.join(lines)+'\n',encoding='utf-8')

def write_indexnow(site,domain):
 """IndexNow lets a site push its URLs straight to Bing/Yandex/Seznam.cz/
 Naver instead of waiting for them to crawl sitemap.xml on their own
 schedule. Two pieces are required: a <key>.txt file at the site root
 containing just the key (how IndexNow verifies this site actually owns
 the domain), and something that POSTs the key + URL list to IndexNow's
 API. The POST itself isn't done here at generation time — the site isn't
 live yet, so Bing would just get 404s — instead a standalone script ships
 in the zip for the publisher to run once the site is actually deployed."""
 key=secrets.token_hex(16)
 (site/f'{key}.txt').write_text(key,encoding='utf-8')
 key_location=current_domain_url(domain,f'{key}.txt')
 host=re.sub(r'^https?://','',domain).rstrip('/')
 script=f'''#!/usr/bin/env python3
"""Submit every URL in sitemap.xml to IndexNow (api.indexnow.org), which
fans the submission out to Bing, Yandex, Seznam.cz and Naver so they can
crawl the site without waiting for their normal discovery schedule.

Run this ONCE the site is live at its real domain — submitting before
that just gives IndexNow a list of URLs that 404.

Usage:
    pip install requests
    python indexnow-submit.py
"""
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import requests

HOST={host!r}
KEY={key!r}
KEY_LOCATION={key_location!r}
ENDPOINT='https://api.indexnow.org/indexnow'
SITEMAP=Path(__file__).resolve().parent/'sitemap.xml'


def load_urls():
 ns={{'sm':'http://www.sitemaps.org/schemas/sitemap/0.9'}}
 root=ET.parse(SITEMAP).getroot()
 return [loc.text.strip() for loc in root.findall('sm:url/sm:loc',ns) if loc.text and loc.text.strip()]


def main():
 urls=load_urls()
 if not urls:
  print('No URLs found in sitemap.xml');sys.exit(1)
 payload={{'host':HOST,'key':KEY,'keyLocation':KEY_LOCATION,'urlList':urls}}
 resp=requests.post(ENDPOINT,json=payload,headers={{'Content-Type':'application/json; charset=utf-8'}},timeout=30)
 print(f'IndexNow: submitted {{len(urls)}} URL(s) to {{HOST}} — HTTP {{resp.status_code}}')
 if resp.text.strip():print(resp.text.strip())


if __name__=='__main__':
 main()
'''
 (site/'indexnow-submit.py').write_text(script,encoding='utf-8')

def write_htaccess(site,domain):
 """Force HTTPS and the exact canonical host (www vs non-www, whichever the
 user configured as `domain`) — without this, Bing/Google can index both
 http:// and https://, and both www./non-www variants, as separate duplicate
 pages, directly undermining the <link rel=canonical> tags every page already
 carries. Also enables gzip compression and browser caching for page speed —
 a Bing/Google ranking signal on its own. Apache-only (.htaccess); sites
 hosted on Nginx, Netlify, Vercel, Cloudflare Pages etc. need the equivalent
 rules configured on the host's own side instead — this file just won't do
 anything there, not break anything."""
 host=re.sub(r'^https?://','',domain).rstrip('/')
 host_pattern=re.escape(host)
 content=f"""# Force HTTPS and the exact canonical host — avoids Bing/Google indexing
# http/https and www/non-www as separate, duplicate versions of each page.
# Apache only. On Nginx/Netlify/Vercel/Cloudflare Pages, set the equivalent
# redirect in that host's own settings instead — this file has no effect there.
RewriteEngine On
RewriteCond %{{HTTPS}} off [OR]
RewriteCond %{{HTTP_HOST}} !^{host_pattern}$ [NC]
RewriteRule ^ https://{host}%{{REQUEST_URI}} [L,R=301]

# Custom 404 page
ErrorDocument 404 /404.html

# Compress text-based assets
<IfModule mod_deflate.c>
 AddOutputFilterByType DEFLATE text/html text/css text/plain text/xml application/xml application/xhtml+xml application/rss+xml application/javascript application/x-javascript image/svg+xml
</IfModule>

# Browser caching for static assets
<IfModule mod_expires.c>
 ExpiresActive On
 ExpiresByType image/jpg "access plus 1 year"
 ExpiresByType image/jpeg "access plus 1 year"
 ExpiresByType image/png "access plus 1 year"
 ExpiresByType image/webp "access plus 1 year"
 ExpiresByType image/gif "access plus 1 year"
 ExpiresByType image/svg+xml "access plus 1 year"
 ExpiresByType text/css "access plus 1 month"
 ExpiresByType application/javascript "access plus 1 month"
 ExpiresByType text/html "access plus 1 day"
</IfModule>

# Basic security headers
<IfModule mod_headers.c>
 Header set X-Content-Type-Options "nosniff"
 Header set X-Frame-Options "SAMEORIGIN"
 Header set Referrer-Policy "strict-origin-when-cross-origin"
</IfModule>
"""
 (site/'.htaccess').write_text(content,encoding='utf-8')

def legal_page(base_soup,data,domain,affiliate,images,design,filename,page_title,body_html,site_root):
 """Build a simple legal/info page (Terms, Privacy, Disclaimer, Refund, About, Contact)
 reusing the same nav/header-strip/footer, but with plain text content instead of the
 full product sections."""
 soup=BeautifulSoup(str(base_soup),'html.parser')
 main=soup.find('main') or soup.body
 brand=data['brand']
 if main:
  # Remove ALL sections (hero + everything else) — this is a plain content page
  for sec in list(main.find_all('section',recursive=True)):sec.decompose()
  for hdr in list(main.find_all('header',recursive=True)):hdr.decompose()
  if main.name=='header':pass
 header_tag=soup.find('header')
 # Build simple content section matching template's typography classes
 content_html=f'''<section class="bpo-sec legal-page-content" id="legal-content"><div class="bpo-wrap"><div class="bpo-narrow" style="padding:40px 0;max-width:760px;margin:0 auto;font-size:1rem;line-height:1.7;color:#333">
 <h1 class="page-banner-h1" style="font-size:2rem;margin-bottom:20px">{page_title.replace('{brand}',brand)}</h1>
 {body_html}
 </div></div></section>'''
 content_soup=BeautifulSoup(content_html,'html.parser')
 # Brand the section headings (FDA Disclosure, Cookies, etc.) consistently —
 # body_html comes from per-page lambdas that only set their own margin, so
 # without this every legal page's h3s render in the browser default color/size.
 for h3 in content_soup.find_all('h3'):
  existing=h3.get('style','').rstrip(';')
  h3['style']=(existing+';' if existing else '')+'color:#182236;font-size:1.15rem'
 # Put the content exactly where <header> used to sit (same approach as
 # page_variant()), NOT after the first <nav> found — with <header> already
 # gone, soup.find('nav') matches the mobile-sidebar's own <nav class="sidebar-nav">
 # instead, which silently inserts the whole page's content inside that
 # hidden off-canvas <aside>, where it never renders on page load.
 if header_tag:
  header_tag.replace_with(content_soup)
 elif main.name=='main':
  # <header> was already stripped by the "remove headers inside main" loop
  # above. Some designs (e.g. design 4) never wrap nav in a <header> at
  # all — <nav> sits directly under <body>, followed by a real <main>
  # landmark (optionally with a sibling <div class="mobile-menu"> in
  # between) that already had its own children (hero, sections) cleared by
  # that same sweep. Put the content there — inside main, which already
  # sits after nav/mobile-menu in the DOM — instead of leaving that <main>
  # empty and inserting content as a body-level sibling next to it, which
  # left a dangling, invisible-but-wrong empty <main> between the content
  # and the footer.
  main.append(content_soup)
 else:
  # No <header> AND no real <main> to anchor on (main fell back to
  # soup.body above) — insert right after nav (and its mobile-menu sibling,
  # if present) so nav/mobile-menu always stay on top; body_tag.insert(0,…)
  # used to drop the legal content BEFORE <nav> here, so the navbar
  # rendered under the page content instead of above it.
  body_tag=soup.find('body')
  if body_tag:
   top_nav=body_tag.find('nav',recursive=False)
   if top_nav:
    insert_after=top_nav
    nxt=top_nav.find_next_sibling(True)
    if nxt and nxt.name=='div' and 'mobile-menu' in (nxt.get('class') or []):
     insert_after=nxt
    insert_after.insert_after(content_soup)
   else:
    body_tag.insert(0,content_soup)
 # A page should only ever carry one <h1> — the legal-content title just
 # inserted above. The template's original product-title h1 is a sibling
 # elsewhere in the DOM and survives untouched; remove it by element (not by
 # a "product-title" class guess, since not every design names it that way)
 # so populate() doesn't leave two <h1> tags on every legal/info page.
 for stray_h1 in soup.find_all('h1'):
  if 'page-banner-h1' not in (stray_h1.get('class') or []):stray_h1.decompose()
 # Some designs (e.g. design 2) build their promo/order blocks — "Is My
 # Payment Safe?", the supplement-facts banner, the bundle banner, the sticky
 # order bar — as plain top-level <div>s in <body>, not <section>s, so the
 # "remove ALL sections" sweep above never touches them. Left in place, every
 # legal/info page still shows this order-page chrome right under the real
 # content, which is exactly the "order page ka niche wala section aata hai"
 # look this page is meant to avoid. Strip any top-level <div> that isn't the
 # legal content section we just inserted or the mobile-sidebar's overlay.
 body_tag=soup.find('body')
 if body_tag:
  for child in list(body_tag.find_all('div',recursive=False)):
   cls=child.get('class') or []
   # 'mobile-menu' must survive this sweep too — on designs without a
   # <header> wrapper (e.g. design 4) it's a top-level <body> child right
   # after <nav>, not nested inside it, so without this exception every
   # legal/info page silently lost its hamburger menu's dropdown content
   # (the button still rendered, but toggling it opened an empty/missing
   # panel since getElementById('mobileMenu') had nothing left to toggle).
   if child.get('id')=='sidebarOverlay' or 'sidebar-overlay' in cls or 'legal-page-content' in cls or child.get('id')=='mobileMenu' or 'mobile-menu' in cls:continue
   child.decompose()
 # Some designs (e.g. design 4) wrap their real content in an actual <main>
 # tag, with each section preceded by its own standalone label/band div
 # (<div class="sec-title-band">/"pricing-band"> — a heading + subtitle,
 # not a <section>). The sweep above only ever looked at <body>'s direct
 # children, so on these designs every one of those band divs (one per
 # removed section — symptoms, ingredients, reviews, guarantee, benefits,
 # bonuses, FAQs, how-to-order...) survived untouched, leaving every legal
 # page a wall of empty section headings with no content under any of them.
 # Everything actually inside <main> was already reduced to just those bands
 # by the "remove ALL sections" sweep at the top of this function, so any
 # <main> child left at this point besides our own inserted content is one.
 main_tag=soup.find('main')
 if main_tag:
  for child in list(main_tag.find_all(True,recursive=False)):
   cls=child.get('class') or []
   if child.get('id')=='legal-content' or 'legal-page-content' in cls:continue
   child.decompose()
 populate(soup,data,design,domain,affiliate)
 apply_dynamic_accent_theme(soup,design,images,site_root)
 dehardcode_inline_accent_colors(soup,design)
 canonical=current_domain_url(domain,filename)
 rebuild_metadata(soup,data,canonical,images,domain)
 strip_old_product_images(soup,TEMPLATES[design]['old_domains'],design)
 _theme_rgb,_base_css_text=localize_reference_assets(soup,site_root,design,TEMPLATES[design]['old_domains'],data.get('brand',''),images,data.get('reviewer_names',[]))
 localize_images(soup,images,design)
 scrub_image_alts(soup,data)
 strip_third_party_fa_kit(soup)
 apply_img_sizing(soup,site_root,data.get('brand',''),data.get('category',''))
 inject_img_css(soup)
 inject_cta_extras(soup,data.get('brand',''),affiliate)
 sanitize_urls(soup,TEMPLATES[design]['old_domains'],domain,affiliate)
 sanitize_text_domains(soup,TEMPLATES[design]['old_domains'],domain)
 replace_all_brand_refs(soup,brand)
 internal_links(soup,domain)
 ensure_legal_footer_links(soup)
 ensure_core_page_links(soup,brand)
 set_ctas(soup,affiliate)
 rebuild_metadata(soup,data,canonical,images,domain)
 # Override title/description/og/twitter for legal pages BEFORE add_jsonld()
 # runs — rebuild_metadata() above only ever writes the generic site-wide
 # data['seo'] title/description, so without this every legal page (About,
 # Contact, Disclaimer, Privacy, Refund, Terms) shipped with the exact same
 # meta description and og:title/twitter:title as the homepage, and JSON-LD's
 # WebPage node (which reads soup.title/meta description at call time) would
 # inherit that same generic, duplicated text too.
 resolved_title=page_title.replace('{brand}',brand)
 legal_seo_title=f'{resolved_title} — {brand}'
 if soup.title:soup.title.string=legal_seo_title
 # Strip tags to a SPACE (not empty string) and unescape entities — for a
 # bullet-list-of-links body (e.g. the 404 page), stripping tags to nothing
 # ran adjacent link text together with no separator and left literal
 # "&amp;larr;"-style entities in the text ("...moved.&amp;larr; Back to
 # HomeHow It Works..."), instead of a clean sentence.
 legal_plain_snippet=re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',body_html))).strip()[:150].strip()
 legal_meta_desc=f'{resolved_title} for {brand}. {legal_plain_snippet}'[:160].strip()
 set_or_add_meta(soup,'description',legal_meta_desc)
 for prop,val in (('og:title',legal_seo_title),('twitter:title',legal_seo_title),
                   ('og:description',legal_meta_desc),('twitter:description',legal_meta_desc)):
  set_or_add_meta(soup,prop,val,'property')
 ensure_social_meta(soup,domain,images)
 # Blog pages (article + index) get WebSite/Organization/WebPage/Breadcrumb
 # from here but never Product/Offer — add_article_jsonld() gives articles
 # their own BlogPosting node separately; neither a BlogPosting nor an index
 # of them is an offer to buy the product.
 add_jsonld(soup,data,domain,canonical,affiliate,images,include_product=not filename.startswith('blog/'))
 set_ctas(soup,affiliate)
 if filename.startswith('blog/'):rebase_internal_page_links(soup,'../')
 html_out='<!doctype html>\n'+str(soup)
 if _theme_rgb and _base_css_text:html_out=retheme_html_inline(html_out,_theme_rgb,_base_css_text)
 return html_out

def _article_closing_html(brand,category,affiliate):
 """Shared disclaimer + CTA block appended to every blog article — never a
 cure/treat/prevent claim, and reuses the same CTA copy as the rest of the
 site instead of inventing one-off button text per article. The affiliate
 URL is substituted directly here rather than left as a placeholder for
 set_ctas() to fill in later — set_ctas() is only ever called from the
 reference pipeline (make_page/page_variant/legal_page), never from
 build_native_page(), so a native blog article's CTA href would otherwise
 stay a literal, unsubstituted placeholder."""
 cta=cta_texts(brand,category)['closing']
 return (f'<p style="margin:28px 0 14px;font-size:.85rem;color:#6b7280">'
         f'This article is for general informational purposes only and is not medical advice. '
         f'Individual results vary, and nothing here should be taken as a guarantee of any outcome. '
         f'Consult a qualified healthcare provider before starting any new supplement.</p>'
         f'<a class="btn" href="{html.escape(affiliate)}" target="_blank" rel="nofollow sponsored noopener" '
         f'style="display:inline-block;background:var(--primary,#2563EB);color:#fff;font-weight:700;'
         f'padding:14px 24px;border-radius:10px;text-decoration:none">{html.escape(cta)}</a>')

def _blog_articles(data,domain,affiliate):
 """Real, per-product blog content — one article per topic, built from this
 product's own ingredients/pricing/guarantee/FAQ data rather than generic
 filler, so every generated site's blog text actually differs. Returns a
 list of {'slug','title','meta_desc','h1','body_html'} (body_html excludes
 the breadcrumb/related-articles/closing blocks, added by the caller once
 every article's title is known)."""
 brand=data.get('brand','')
 category=data.get('category','wellness supplement')
 cat_phrase=_support_phrase(category)
 ingredients=data.get('ingredients',[])
 benefits=data.get('benefits',[])
 pricing=sorted(data.get('pricing',[]),key=lambda p:p.get('bottles',0))
 faqs=data.get('faqs',[])
 serving=data.get('serving_info',{})
 guarantee_text=data.get('guarantee_text') or f'{brand} is backed by a {GUARANTEE_DAYS}-day money-back guarantee.'
 pricing_note=data.get('pricing_note') or 'Larger bundles typically cost less per bottle.'
 whatis=data.get('whatis_callout') or f'{brand} is a dietary supplement, not a drug.'
 n_ing=len(ingredients)
 close=_article_closing_html(brand,category,affiliate)
 articles=[]

 # 1 — What To Know Before Trying {product}
 ing_rows=''.join(f'<li><b>{html.escape(i.get("name",""))}</b> — {html.escape(i.get("description",""))}</li>'
                   for i in ingredients[:8]) or '<li>See the official product page for the full ingredient list.</li>'
 articles.append({
  'slug':'what-to-know-before-trying','h1':f'What To Know Before Trying {brand}',
  'title':f'What To Know Before Trying {brand} | {brand} Blog'[:60],
  'meta_desc':(f'A clear, honest look at {brand} — what it contains, how it is used, what it costs, '
               f'and the guarantee behind it — before you decide to order.')[:155],
  'body_html':(
   f'<p>Before ordering any {html.escape(category)}, it helps to know exactly what you are buying, how '
   f'it is meant to be used, and what happens if it does not work out. Here is a straight, honest '
   f'rundown of {html.escape(brand)} covering each of those points.</p>'
   f'<h2>What {html.escape(brand)} Actually Contains</h2>'
   f'<p>{html.escape(brand)} lists {n_ing} named ingredient{"s" if n_ing!=1 else ""} on its label. Here is '
   f'what each one is included for:</p><ul>{ing_rows}</ul>'
   f'<h2>How It Is Meant To Be Used</h2>'
   f'<p>The label calls for {html.escape(str(serving.get("daily_serving","the serving listed on the label")))} '
   f'per day, with {html.escape(str(serving.get("per_bottle","a stated capsule count")))} in each bottle. '
   f'{"Individual ingredient amounts are listed on the label." if str(serving.get("doses_published","")).lower().startswith("yes") else "Some ingredient amounts are listed as part of a combined blend rather than individually."} '
   f'Consistency day to day matters more than any single dose.</p>'
   f'<h2>How It Is Meant To Work</h2>'
   f'<p>{html.escape(data.get("how_it_works_intro") or f"{brand} combines its ingredients to work together as part of a daily routine.")}</p>'
   +(''.join(f'<p><b>{html.escape(s.get("title",""))}:</b> {html.escape(s.get("text",""))}</p>' for s in data.get('how_it_works',[])[:4]))
   +f'<h2>What It Costs</h2>'
   f'<p>{html.escape(brand)} is sold in {len(pricing)} package size{"s" if len(pricing)!=1 else ""}'
   +(': '+', '.join(f'{p.get("bottles","")} bottle{"s" if p.get("bottles",0)!=1 else ""} at {html.escape(str(p.get("price_per_bottle","")))} per bottle' for p in pricing)+'. ' if pricing else '. ')
   +f'{html.escape(pricing_note)}</p>'
   f'<h2>The Guarantee</h2>'
   f'<p>{html.escape(guarantee_text)}</p>'
   f'<h2>Before You Order — A Quick Checklist</h2>'
   f'<ul><li>Read the full ingredient list above, not just the headline benefit.</li>'
   f'<li>Check the serving size against how many servings you actually need per bottle.</li>'
   f'<li>Confirm the current guarantee window on the official order page before buying.</li>'
   f'<li>{html.escape(whatis)}</li></ul>'
  ),
 })

 # 2 — How To Read A Supplement Label (educational, still brand-specific)
 blend_line=('each ingredient amount is listed individually on the label'
             if str(serving.get('doses_published','')).lower().startswith('yes')
             else 'some ingredients are grouped into a combined blend rather than listed individually')
 articles.append({
  'slug':'how-to-read-a-supplement-label','h1':'How To Read A Supplement Label',
  'title':f'How To Read A Supplement Label | {brand} Blog'[:60],
  'meta_desc':(f'Serving size, proprietary blends and other ingredients explained — using {brand}\'s own '
               f'label as a real example of what to look for.')[:155],
  'body_html':(
   f'<p>Supplement labels pack a lot of information into a small space. Knowing how to read one properly '
   f'makes it much easier to compare products honestly — including {html.escape(brand)}.</p>'
   f'<h2>Serving Size vs. Servings Per Container</h2>'
   f'<p>The serving size tells you how much to take at once ({html.escape(str(serving.get("daily_serving","the amount listed on the label")))} '
   f'for {html.escape(brand)}); servings per container tells you how long one bottle actually lasts '
   f'({html.escape(str(serving.get("per_bottle","the count printed on the label")))} per bottle). Multiply '
   f'the two together before assuming a bottle will last a full month.</p>'
   f'<h2>Named Amounts vs. Proprietary Blends</h2>'
   f'<p>Some labels list the exact milligram amount next to every ingredient; others group several '
   f'ingredients into one "blend" with a single combined total. On {html.escape(brand)}\'s own label, '
   f'{blend_line}. Neither approach alone tells you whether a product works, but named amounts make it '
   f'easier to compare against published research.</p>'
   f'<h2>"Other Ingredients"</h2>'
   f'<p>Below the main ingredient panel, most labels list "other ingredients" — things like capsule '
   f'shells, binders or preservatives. These are not the active ingredients but are worth a glance if '
   f'you have known sensitivities.</p>'
   f'<h2>Reading {html.escape(brand)}\'s Label Specifically</h2>'
   f'<p>{html.escape(brand)} lists {n_ing} named ingredient{"s" if n_ing!=1 else ""}. '
   +(' '.join(f'{html.escape(i.get("name",""))} is included for its role in {html.escape(i.get("role","")).lower() or "the formula"}.' for i in ingredients[:4]))
   +f'</p><h2>Cost Per Serving, Not Just Cost Per Bottle</h2>'
   f'<p>A bigger bottle is not automatically a better deal. Divide the total price by the number of '
   f'servings per bottle to get a true cost-per-day figure, then compare that across package sizes '
   f'before deciding which size of {html.escape(brand)} to order.</p>'
   f'<h2>Quick Checklist</h2><ul><li>Check the serving size, not just the bottle size.</li>'
   f'<li>Look for named amounts where possible.</li><li>Scan "other ingredients" for anything you need to avoid.</li>'
   f'<li>Compare cost per serving, not just cost per bottle.</li></ul>'
  ),
 })

 # 3 — {product}: An Honest Review
 benefit_rows=''.join(f'<li>{html.escape(b)}</li>' for b in benefits[:6]) or '<li>See the official product page for the full benefits list.</li>'
 price_summary=(', '.join(f'{p.get("bottles","")}-bottle at {html.escape(str(p.get("price_per_bottle","")))}/bottle' for p in pricing)
                if pricing else 'See the official order page for current pricing.')
 articles.append({
  'slug':f'{slugify(brand)}-honest-review','h1':f'{brand}: An Honest Review',
  'title':f'{brand}: An Honest Review | {brand} Blog'[:60],
  'meta_desc':(f'An honest look at {brand} — what it claims to do, what it actually contains, what it '
               f'costs, and who it is realistically a good fit for.')[:155],
  'body_html':(
   f'<p>{html.escape(data.get("description","") or f"{brand} is a {category}.")}</p>'
   f'<h2>Who Makes {html.escape(brand)}, And What It Is Not</h2>'
   f'<p>{html.escape(whatis)} That distinction matters more than marketing copy — it shapes what a '
   f'reasonable buyer should expect from a {html.escape(category)} like this one.</p>'
   f'<h2>What {html.escape(brand)} Claims To Support</h2><ul>{benefit_rows}</ul>'
   f'<h2>Ingredients At A Glance</h2>'
   f'<p>{html.escape(brand)} is built around {n_ing} named ingredient{"s" if n_ing!=1 else ""}'
   +(': '+', '.join(html.escape(i.get('name','')) for i in ingredients[:6])+'.' if ingredients else '.')
   +f'</p><h2>Pricing Breakdown</h2><p>{html.escape(price_summary)} {html.escape(pricing_note)}</p>'
   f'<h2>What Customers Say</h2>'
   f'<p>{html.escape(data.get("reviews_note") or "Individual experiences vary, and these reflect personal opinions, not guaranteed outcomes.")}</p>'
   +(''.join(f'<p style="font-style:italic">&ldquo;{html.escape(r)}&rdquo;</p>' for r in data.get('sample_reviews',[])[:3]))
   +f'<h2>Strengths And Limitations</h2>'
   f'<p>{html.escape(whatis)} As with any {html.escape(category)}, individual results vary, and no single '
   f'product works identically for everyone.</p>'
   f'<h2>Who Should Consider It</h2>'
   f'<p>Anyone looking for daily support for {html.escape(cat_phrase)} as part of a broader routine, who '
   f'has reviewed the ingredient list above and is comfortable with the serving size and price point.</p>'
  ),
 })

 # 4 — Ingredient comparison (needs >=2 ingredients; falls back to a single-
 # ingredient spotlight, or is skipped outright, rather than ever inventing
 # ingredient names/roles that aren't in this product's real data.
 if n_ing>=2:
  ing1,ing2=ingredients[0],ingredients[1]
  n1,n2=ing1.get('name',''),ing2.get('name','')
  articles.append({
   'slug':f'{slugify(n1)}-vs-{slugify(n2)}','h1':f'{n1} vs {n2}: What Each Does In {brand}',
   'title':f'{n1} vs {n2}: What Each Does | {brand} Blog'[:60],
   'meta_desc':(f'{n1} and {n2} are both in {brand} but play different roles — here is what each one '
                f'actually does in the formula.')[:155],
   'body_html':(
    f'<p>{html.escape(brand)} combines several named ingredients rather than relying on just one. Two of '
    f'them — {html.escape(n1)} and {html.escape(n2)} — are worth looking at side by side.</p>'
    f'<table style="width:100%;border-collapse:collapse;margin:16px 0 24px;font-size:.92rem">'
    f'<tr style="background:#f8fafc"><th style="text-align:left;padding:8px 10px;border:1px solid #e5e7eb">Ingredient</th>'
    f'<th style="text-align:left;padding:8px 10px;border:1px solid #e5e7eb">Role</th>'
    f'<th style="text-align:left;padding:8px 10px;border:1px solid #e5e7eb">What It Does</th></tr>'
    f'<tr><td style="padding:8px 10px;border:1px solid #e5e7eb"><b>{html.escape(n1)}</b></td>'
    f'<td style="padding:8px 10px;border:1px solid #e5e7eb">{html.escape(ing1.get("role","") or "Supporting ingredient")}</td>'
    f'<td style="padding:8px 10px;border:1px solid #e5e7eb">{html.escape(ing1.get("description",""))}</td></tr>'
    f'<tr><td style="padding:8px 10px;border:1px solid #e5e7eb"><b>{html.escape(n2)}</b></td>'
    f'<td style="padding:8px 10px;border:1px solid #e5e7eb">{html.escape(ing2.get("role","") or "Supporting ingredient")}</td>'
    f'<td style="padding:8px 10px;border:1px solid #e5e7eb">{html.escape(ing2.get("description",""))}</td></tr>'
    f'</table>'
    f'<h2>{html.escape(n1)}</h2><p><b>Role:</b> {html.escape(ing1.get("role","") or "Supporting ingredient")}. '
    f'{html.escape(ing1.get("description",""))}</p>'
    f'<h2>{html.escape(n2)}</h2><p><b>Role:</b> {html.escape(ing2.get("role","") or "Supporting ingredient")}. '
    f'{html.escape(ing2.get("description",""))}</p>'
    f'<h2>Why {html.escape(brand)} Combines Them</h2>'
    f'<p>{html.escape(data.get("how_it_works_intro") or f"{brand} combines its ingredients to work together as part of a daily routine.")} '
    f'Neither ingredient is positioned as a replacement for the other — they are included for different reasons.</p>'
    f'<h2>The Rest Of The Formula</h2>'
    f'<p>{html.escape(brand)} includes {n_ing-2} other named ingredient{"s" if n_ing-2!=1 else ""} alongside '
    f'these two'+(': '+', '.join(html.escape(i.get('name','')) for i in ingredients[2:6])+'.' if n_ing>2 else '.')+'</p>'
    f'<h2>Making Sense Of The Label</h2>'
    f'<p>Seeing {html.escape(n1)} and {html.escape(n2)} listed together is a reminder to look at a '
    f'label\'s full ingredient list rather than judging a product by one headline ingredient alone — '
    f'{html.escape(pricing_note)}</p>'
    f'<h2>How This Fits Into A Daily Serving</h2>'
    f'<p>{html.escape(brand)}\'s label calls for {html.escape(str(serving.get("daily_serving","the listed serving")))} '
    f'per day — both {html.escape(n1)} and {html.escape(n2)} are part of that same daily serving, not '
    f'separate add-ons taken at different times.</p>'
   ),
  })
 elif n_ing==1:
  ing1=ingredients[0]
  articles.append({
   'slug':f'{slugify(ing1.get("name","key-ingredient"))}-spotlight','h1':f'Ingredient Spotlight: {ing1.get("name","")} In {brand}',
   'title':f'{ing1.get("name","")} In {brand}: Ingredient Spotlight | {brand} Blog'[:60],
   'meta_desc':f'A closer look at {ing1.get("name","")}, the named ingredient behind {brand}, and the role it plays in the formula.'[:155],
   'body_html':(
    f'<h2>What {html.escape(ing1.get("name",""))} Is Included For</h2>'
    f'<p><b>Role:</b> {html.escape(ing1.get("role","") or "Primary ingredient")}. {html.escape(ing1.get("description",""))}</p>'
    f'<h2>How It Fits Into {html.escape(brand)}</h2>'
    f'<p>{html.escape(data.get("how_it_works_intro") or f"{brand} is formulated around this ingredient as part of a daily routine.")}</p>'
   ),
  })

 # 5 — Daily Habits That Complement {product}
 articles.append({
  'slug':'daily-habits-that-complement-it','h1':f'Daily Habits That Complement {brand}',
  'title':f'Daily Habits That Complement {brand} | {brand} Blog'[:60],
  'meta_desc':(f'Simple daily habits — hydration, timing, consistency — that pair well with {brand} as '
               f'part of a {cat_phrase} routine.')[:155],
  'body_html':(
   f'<p>A supplement is only one part of a daily routine. These habits are simple, free, and pair '
   f'naturally with taking {html.escape(brand)} as directed.</p>'
   f'<h2>Hydration And Timing</h2>'
   f'<p>{html.escape(brand)}\'s label calls for {html.escape(str(serving.get("daily_serving","the listed serving")))}. '
   f'Taking it at the same time each day, with water, is an easy way to stay consistent without having '
   f'to think about it.</p>'
   f'<h2>Diet Habits That Support {html.escape(cat_phrase.title())}</h2>'
   f'<p>Whole foods, regular meals and adequate water intake all play a role in supporting '
   f'{html.escape(cat_phrase)} generally — none of that depends on any particular product.</p>'
   f'<h2>Consistency Over Weeks, Not Days</h2>'
   f'<p>{html.escape(pricing_note)} That multi-bottle pattern reflects how most {html.escape(category)} '
   f'products are meant to be used — consistently, over weeks, rather than as a one-time fix.</p>'
   f'<h2>Tracking Your Own Progress</h2>'
   f'<p>Simple notes on how you feel week to week are a more reliable guide than any single day\'s '
   f'impression, for {html.escape(brand)} or any other {html.escape(category)}.</p>'
   f'<h2>What To Watch For</h2>'
   f'<p>'+(' '.join(f'{html.escape(b)}.' for b in [b.split(" — ",1)[0] for b in benefits[:3]]) if benefits
          else f'Pay attention to how your {html.escape(cat_phrase)} routine feels week over week.')
   +'</p>'
  ),
 })

 # 6 — {product} FAQ (uses the real FAQ data directly)
 if faqs:
  faq_rows=''.join(f'<h2>{html.escape(f.get("q",""))}</h2><p>{html.escape(f.get("a",""))}</p>' for f in faqs[:8])
 else:
  faq_rows=(f'<h2>How is {html.escape(brand)} taken?</h2>'
            f'<p>Follow the serving size on the label — {html.escape(str(serving.get("daily_serving","as listed")))} per day is typical.</p>'
            f'<h2>What is the guarantee?</h2><p>{html.escape(guarantee_text)}</p>')
 articles.append({
  'slug':f'{slugify(brand)}-faq','h1':f'{brand} FAQ: Dosage, Timing, Who Should Skip It',
  'title':f'{brand} FAQ: Dosage, Timing, Who Should Skip It | {brand} Blog'[:60],
  'meta_desc':f'Common questions about {brand} — dosage, timing, the guarantee, and who should skip it — answered directly.'[:155],
  'body_html':(
   f'<p>Straight answers to the questions people ask most often before ordering {html.escape(brand)}.</p>'
   f'<h2>Dosage And Timing At A Glance</h2>'
   f'<p>The label calls for {html.escape(str(serving.get("daily_serving","the listed serving")))} per day, '
   f'with {html.escape(str(serving.get("per_bottle","a stated count")))} in each bottle — '
   f'{html.escape(str(serving.get("doses_published","the per-ingredient amounts are listed on the label")))}.</p>'
   f'{faq_rows}'
   f'<h2>Who Should Skip It</h2>'
   f'<p>Anyone who is pregnant, nursing, taking medication, or managing a medical condition should talk '
   f'to a healthcare provider before trying {html.escape(brand)} or any other {html.escape(category)}.</p>'
   f'<h2>Still Have Questions?</h2>'
   f'<p>{html.escape(guarantee_text)} The official product page has the current pricing and order details.</p>'
  ),
 })

 for a in articles:
  takeaways=re.findall(r'<h2>(.*?)</h2>',a['body_html'])[:3]
  takeaways_html=''
  if takeaways:
   items=''.join(f'<li>{t}</li>' for t in takeaways)
   takeaways_html=(f'<div class="auto-key-takeaways" style="margin:0 0 24px;padding:16px 20px;'
                    f'background:#f0f9ff;border-left:4px solid var(--primary,#2563EB);border-radius:6px">'
                    f'<b>Key Takeaways</b><ul style="margin-top:8px">{items}</ul></div>')
  a['body_html']=takeaways_html+a['body_html']+close
 return articles[:6]

def _blog_article_extras(brand,slug,title,all_articles):
 """Breadcrumb, 2-3 internal links and a related-articles block for one
 blog/<slug>.html article. Every href here is the exact final relative
 path (blog pages sit one directory below the site root) — written
 directly rather than relying on a generic '../' rebase pass, since that
 pass only ever touches the page's original template nav/footer links,
 not content inserted afterward."""
 # Every href is written "../"-prefixed from the site root (e.g.
 # "../blog/other-article.html" for a SIBLING blog page, not the shorter
 # "other-article.html") specifically so it already matches the '../'
 # rebase_internal_page_links() applies to the reference pipeline's
 # finished page (it skips anything already starting with '../', but
 # blindly prepends '../' to anything that isn't — a bare "other-article.html"
 # sibling link came out as "../other-article.html", pointing at the site
 # root instead of staying inside blog/). The native pipeline never runs
 # that rebase over this inserted content, but the same "../"-from-root
 # path still resolves correctly there too, so one path works for both.
 breadcrumb=(f'<nav aria-label="Breadcrumb" style="font-size:.85rem;color:#6b7280;margin-bottom:18px">'
             f'<a href="../index.html" style="color:#6b7280">Home</a> &gt; '
             f'<a href="../blog/index.html" style="color:#6b7280">Blog</a> &gt; <span>{html.escape(title)}</span></nav>')
 internal_links=(f'<p style="margin:18px 0 28px;font-size:.92rem">'
                  f'<a href="../ingredients.html">See all {html.escape(brand)} ingredients</a> &middot; '
                  f'<a href="../how-it-works.html">How {html.escape(brand)} works</a> &middot; '
                  f'<a href="../reviews.html">Read customer reviews</a> &middot; '
                  f'<a href="../index.html#pricing">View pricing</a></p>')
 # Pick the next 2 articles in a fixed circular order (this article's index
 # + 1, + 2, wrapping around) rather than always "the first 2 others" —
 # that always picked the same early articles as everyone's "related" link
 # and meant articles later in the list were never linked from anywhere but
 # blog/index.html itself (0 inbound links from other articles). Walking the
 # ring instead means every article is one of exactly two OTHER articles'
 # two picks, so every article gets exactly 2 inbound "related" links.
 others=[]
 n=len(all_articles)
 idx=next((i for i,a in enumerate(all_articles) if a['slug']==slug),None)
 if idx is not None and n>1:
  for off in range(1,n):
   if len(others)>=2:break
   cand=all_articles[(idx+off)%n]
   if cand['slug']!=slug:others.append(cand)
 related=''
 if others:
  items=''.join(f'<li style="margin-bottom:6px"><a href="../blog/{a["slug"]}.html">{html.escape(a["h1"])}</a></li>' for a in others)
  related=(f'<div style="margin-top:36px;padding-top:20px;border-top:1px solid #e5e7eb">'
           f'<h3 style="margin-bottom:10px">Related Articles</h3><ul>{items}</ul></div>')
 return breadcrumb,internal_links,related

def add_article_jsonld(soup,data,canonical,title,meta_desc,domain,images):
 """BlogPosting JSON-LD for one article page — headline, datePublished,
 author (Editorial Team — this content is written by the generator, not a
 named/verified individual), publisher and the hero photo as its image."""
 brand=data.get('brand','')
 hero=next((p for p in (images or []) if Path(p).stem.lower()=='hero'),None)
 node={'@context':'https://schema.org','@type':'BlogPosting','headline':title,
       'description':meta_desc,'datePublished':date.today().isoformat(),
       'dateModified':date.today().isoformat(),
       'author':{'@type':'Organization','name':'Editorial Team'},
       'publisher':{'@type':'Organization','name':brand},
       'mainEntityOfPage':{'@type':'WebPage','@id':canonical}}
 if hero:node['image']=current_domain_url(domain,safe_rel(hero))
 sc=soup.new_tag('script',type='application/ld+json')
 sc.string=json.dumps(node,ensure_ascii=False)
 soup.body.append(sc)

def _legal_pages_content(brand,domain,category):
 """Return dict of {filename: (title, body_html)} for standard legal/info pages."""
 today=date.today().strftime('%B %d, %Y')
 return {
  'terms.html': (
   'Terms of Use',
   f'''<p style="margin-bottom:14px">Last updated: {today}</p>
   <p style="margin-bottom:14px">By accessing and using this website, you accept and agree to be bound by the following terms and conditions. If you do not agree, please do not use this site.</p>
   <h3 style="margin:24px 0 10px">Use of Content</h3>
   <p style="margin-bottom:14px">All content on this website is provided for general informational purposes only about {brand}. It is not intended as medical advice and should not be treated as such.</p>
   <h3 style="margin:24px 0 10px">Affiliate Relationship</h3>
   <p style="margin-bottom:14px">This website may contain affiliate links. We may earn a commission when you purchase {brand} through links on this site, at no additional cost to you.</p>
   <h3 style="margin:24px 0 10px">No Medical Advice</h3>
   <p style="margin-bottom:14px">Nothing on this site constitutes medical advice. Always consult a qualified healthcare provider before starting any new supplement, especially if you are pregnant, nursing, taking medication, or have a medical condition.</p>
   <h3 style="margin:24px 0 10px">Limitation of Liability</h3>
   <p style="margin-bottom:14px">This website and its operators are not liable for any damages arising from the use of this site or reliance on any information presented here.</p>
   <h3 style="margin:24px 0 10px">Changes to These Terms</h3>
   <p style="margin-bottom:14px">We may update these Terms of Use at any time. Continued use of the site after changes constitutes acceptance of the revised terms.</p>
   <h3 style="margin:24px 0 10px">Contact</h3>
   <p style="margin-bottom:14px">Questions about these terms can be directed to us via our <a href="contact.html">contact page</a>.</p>'''
  ),
  'privacy-policy.html': (
   'Privacy Policy',
   f'''<p style="margin-bottom:14px">Last updated: {today}</p>
   <p style="margin-bottom:14px">This Privacy Policy explains how we collect, use and protect information when you visit this website.</p>
   <h3 style="margin:24px 0 10px">Information We Collect</h3>
   <p style="margin-bottom:14px">We may collect basic technical information such as browser type, pages visited, and time spent on the site, typically through standard analytics tools. We do not knowingly collect sensitive personal or health information through this site.</p>
   <h3 style="margin:24px 0 10px">Cookies</h3>
   <p style="margin-bottom:14px">This site may use cookies to improve browsing experience and understand site usage. You can disable cookies through your browser settings.</p>
   <h3 style="margin:24px 0 10px">Third-Party Links</h3>
   <p style="margin-bottom:14px">This site contains links to the official {brand} product page and other third-party sites. We are not responsible for the privacy practices of external websites.</p>
   <h3 style="margin:24px 0 10px">Data Security</h3>
   <p style="margin-bottom:14px">We take reasonable measures to protect any information collected, though no method of transmission over the internet is 100% secure.</p>
   <h3 style="margin:24px 0 10px">Your Choices</h3>
   <p style="margin-bottom:14px">You may contact us at any time regarding how your information is handled via our <a href="contact.html">contact page</a>.</p>
   <h3 style="margin:24px 0 10px">Changes to This Policy</h3>
   <p style="margin-bottom:14px">We may update this Privacy Policy periodically. Continued use of the site indicates acceptance of any changes.</p>'''
  ),
  'disclaimer.html': (
   'Disclaimer',
   f'''<p style="margin-bottom:14px">Last updated: {today}</p>
   <h3 style="margin:24px 0 10px">FDA Disclosure</h3>
   <p style="margin-bottom:14px">The statements on this website have not been evaluated by the U.S. Food and Drug Administration (FDA). {brand} is a dietary supplement, not a drug, and is not intended to diagnose, treat, cure or prevent any disease.</p>
   <h3 style="margin:24px 0 10px">Individual Results Vary</h3>
   <p style="margin-bottom:14px">Results from using {brand} may vary from person to person. Testimonials and reviews reflect individual experiences and do not guarantee that you will achieve similar results.</p>
   <h3 style="margin:24px 0 10px">Not Medical Advice</h3>
   <p style="margin-bottom:14px">The content on this site is for informational purposes only and is not a substitute for professional medical advice, diagnosis, or treatment. Always consult your physician or other qualified health provider before starting {brand} or any new supplement, particularly if you are pregnant, nursing, taking medication, or have an existing medical condition.</p>
   <h3 style="margin:24px 0 10px">Affiliate Disclosure</h3>
   <p style="margin-bottom:14px">This website may earn a commission from qualifying purchases made through affiliate links to the official {brand} website, at no additional cost to you.</p>
   <h3 style="margin:24px 0 10px">Accuracy of Information</h3>
   <p style="margin-bottom:14px">While we aim to keep information accurate and current, product formulations, pricing and offers may change. Always verify current details on the official {brand} product page before purchasing.</p>'''
  ),
  'refund-policy.html': (
   'Refund Policy',
   f'''<p style="margin-bottom:14px">Last updated: {today}</p>
   <p style="margin-bottom:14px">{brand} purchases are typically backed by a 60-day money-back guarantee offered directly through the official seller. This page provides a general overview — always confirm exact terms on the official order page before purchasing.</p>
   <h3 style="margin:24px 0 10px">How the Guarantee Generally Works</h3>
   <p style="margin-bottom:14px">If you are not satisfied with {brand}, most orders can typically be returned within 60 days of the purchase date for a refund, even if the bottle has been used, subject to the official seller's current terms.</p>
   <h3 style="margin:24px 0 10px">How to Request a Refund</h3>
   <p style="margin-bottom:14px">Refund requests are handled by the official {brand} seller, not by this website. Contact the official seller's customer support team directly, referencing your order number, within the applicable guarantee window.</p>
   <h3 style="margin:24px 0 10px">Shipping Costs</h3>
   <p style="margin-bottom:14px">Original shipping charges and any return shipping costs may or may not be refundable, depending on the official seller's current policy. Confirm these details before requesting a return.</p>
   <h3 style="margin:24px 0 10px">Important Note</h3>
   <p style="margin-bottom:14px">This website is an independent informational resource and does not process orders, payments, or refunds directly. All transactions and refund requests are handled through the official {brand} order page.</p>'''
  ),
  'about.html': (
   'About Us',
   f'''<p style="margin-bottom:14px">This website provides independent information about {brand}, including ingredients, how it works, pricing and frequently asked questions, to help readers make an informed decision.</p>
   <h3 style="margin:24px 0 10px">Our Approach</h3>
   <p style="margin-bottom:14px">We aim to present clear, honest information about {brand} — what it contains, what it is intended to support, and realistic expectations for use — without exaggerated claims.</p>
   <h3 style="margin:24px 0 10px">Editorial Standards</h3>
   <p style="margin-bottom:14px">Content on this site is written to reflect publicly available product information. We do not fabricate reviews, clinical claims, or certifications. Where information cannot be verified, we note that directly rather than guessing.</p>
   <h3 style="margin:24px 0 10px">How We Review</h3>
   <p style="margin-bottom:6px">Our Editorial Team checks each page against the manufacturer's own published ingredient list, pricing and guarantee terms before it is published, and updates it when that information changes.</p>
   <p style="margin-bottom:14px;color:#8a8a8a;font-size:.85rem">Last reviewed: {today}</p>
   <h3 style="margin:24px 0 10px">Affiliate Relationship</h3>
   <p style="margin-bottom:14px">This site may earn a commission from purchases made through links to the official {brand} website, at no additional cost to you. This does not affect how the product is described here.</p>
   <h3 style="margin:24px 0 10px">Questions?</h3>
   <p style="margin-bottom:14px">Feel free to reach out via our <a href="contact.html">contact page</a> with any questions about this website.</p>'''
  ),
  'contact.html': (
   'Contact Us',
   f'''<p style="margin-bottom:14px">Have a question about {brand} or this website? We would like to hear from you.</p>
   <h3 style="margin:24px 0 10px">General Inquiries</h3>
   <p style="margin-bottom:14px">For questions about the content on this website, please reach out through the contact details on the official {brand} product page.</p>
   <h3 style="margin:24px 0 10px">Order &amp; Shipping Support</h3>
   <p style="margin-bottom:14px">This website does not process orders, payments, or shipping directly. For order status, shipping questions, or refund requests, please contact the official {brand} seller's customer support team directly.</p>
   <h3 style="margin:24px 0 10px">Website Feedback</h3>
   <p style="margin-bottom:14px">If you notice an error on this website or have feedback about the content, we welcome your input to help us keep this resource accurate and useful.</p>'''
  ),
 }


 today=date.today().isoformat()
 sitemap_url=domain.rstrip('/')+'/sitemap.xml'
 (site/'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {sitemap_url}\n',encoding='utf-8')
 files=['index.html']+[x[0] for x in page_defs]
 body=['<?xml version="1.0" encoding="UTF-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
 for fn in files:
  loc=html.escape(current_domain_url(domain,'' if fn=='index.html' else fn))
  priority='1.0' if fn=='index.html' else '0.8'
  body.append(f'<url><loc>{loc}</loc><lastmod>{today}</lastmod><changefreq>monthly</changefreq><priority>{priority}</priority></url>')
 body.append('</urlset>');(site/'sitemap.xml').write_text('\n'.join(body),encoding='utf-8')

_ZIP_TEXT_EXTS={'.html','.htm','.css','.js','.json','.xml','.webmanifest','.svg','.txt'}

def unreferenced_images(site):
 """Files under assets/images that no generated HTML/CSS/JS/etc. mentions —
 leftover uploads (bonus-4, stars, vapocept-3-bottle-pack, trust-badges...)
 that never got a slot. Matched by file name, so any relative form
 ("assets/images/x.webp", "../images/x.webp", srcset) counts."""
 imgdir=site/'assets/images'
 if not imgdir.is_dir():return []
 text=[]
 for p in site.rglob('*'):
  if p.is_file() and p.suffix.lower() in _ZIP_TEXT_EXTS and imgdir not in p.parents:
   try:text.append(p.read_text(encoding='utf-8',errors='ignore'))
   except Exception:pass
 blob='\n'.join(text)
 unused=[]
 for p in imgdir.rglob('*'):
  if not p.is_file():continue
  if not re.search(r'(?<![\w.-])'+re.escape(p.name)+r'(?![\w.-])',blob):unused.append(p)
 return unused

def seo_rename_images(site,brand):
 """Rename hero/bottle-N/bonus-N files to SEO-friendly names (e.g.
 "bottle-2.webp" -> "{brand-slug}-2-bottle-pack.webp") and rewrite every
 reference to them across the site. Operates on the FINAL on-disk filename
 (whatever extension save_uploaded() actually produced — never forces a
 different format) as a last pass after every page is already written, so
 it never has to duplicate any of the slot-matching logic that identified
 these files by their original stem during generation."""
 imgdir=site/'assets/images'
 if not imgdir.is_dir():return
 slug=slugify(brand)
 rename_map={}
 for p in sorted(imgdir.iterdir()):
  if not p.is_file():continue
  stem=p.stem.lower();ext=p.suffix
  new_stem=None
  if stem=='hero':
   new_stem=f'{slug}-supplement-bottle'
  else:
   m=re.fullmatch(r'bottle-(\d+)',stem)
   if m:new_stem=f'{slug}-{m.group(1)}-bottle-pack'
   else:
    m2=re.fullmatch(r'bonus-(\d+)',stem)
    if m2:new_stem=f'{slug}-bonus-{m2.group(1)}'
  if not new_stem or new_stem==stem:continue
  new_name=new_stem+ext
  dest=imgdir/new_name
  if dest.exists() and dest!=p:continue
  p.rename(dest)
  rename_map[p.name]=new_name
 if not rename_map:return
 for f in site.rglob('*'):
  if not f.is_file() or f.suffix.lower() not in _ZIP_TEXT_EXTS:continue
  try:text=f.read_text(encoding='utf-8')
  except Exception:continue
  changed=False
  for old,new in rename_map.items():
   if old in text:text=text.replace(old,new);changed=True
  if changed:f.write_text(text,encoding='utf-8')

def output_name_slug(domain,product):
 """Zip/folder name = the site's own domain (scheme/www/trailing-slash
 stripped, lowercased), e.g. "https://www.vapacept.com/" -> "vapacept.com".
 Falls back to the old brand-based slug only when no domain is available."""
 d=(domain or '').strip()
 d=re.sub(r'^[a-zA-Z][a-zA-Z0-9+.-]*://','',d)
 d=re.sub(r'^www\.','',d,flags=re.I)
 d=d.split('/')[0].strip().lower()
 d=re.sub(r'[^a-z0-9.-]','',d).strip('.-')
 return d or slugify(product) or 'site'

def build_zip(site,domain,product):
 folder=output_name_slug(domain,product)
 out=site.parent/(folder+'.zip')
 skip=set(unreferenced_images(site))
 if skip:
  print(f'[build_zip] WARNING: skipping {len(skip)} unreferenced image(s): '
        +', '.join(sorted(p.name for p in skip)))
 if _LOW_RES_WARNINGS:
  seen=set()
  for src,sw,dw in _LOW_RES_WARNINGS:
   if src in seen:continue
   seen.add(src)
   print(f'[image-sizing] WARNING: low-res image: {src} (source width {sw}px, displayed up to {dw}px)')
 if _HIW_IMG_WARNINGS:
  print('[how-it-works] WARNING: how-it-works image missing — section sans image '
        f'(no how-it-works.* upload; {len(_HIW_IMG_WARNINGS)} occurrence(s) removed)')
 with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
  for p in site.rglob('*'):
   if p.is_file() and p not in skip:z.write(p,Path(folder)/p.relative_to(site))
 return out

def _load_cfg():
 """Saved keys from .aff_config.json — local use only. On the hosted site the
 keys come from environment variables and are never read from, written to, or
 rendered into a page."""
 if auth.HOSTED:return {}
 try:
  f=BASE/'.aff_config.json'
  if f.exists():return json.loads(f.read_text(encoding='utf-8'))
 except Exception:pass
 return {}

auth.TEMPLATES=TEMPLATES

@app.get('/app')
def index():
 _allowed=auth.allowed_designs()
 _visible={k:v for k,v in TEMPLATES.items() if not _allowed or k in _allowed}
 _allowed_n=auth.allowed_niches()
 _niches={k:v for k,v in niches.NICHES.items() if not _allowed_n or k in _allowed_n}
 return render_template('index.html',templates=_visible,cfg=_load_cfg(),
                        niche_list=_niches,default_niche=(niches.DEFAULT_NICHE if niches.DEFAULT_NICHE in _niches else next(iter(_niches))),
                        is_admin=auth.is_admin(),user=auth.current(),auth_on=auth.ENABLED)

def _resolve_keys(_cfg):
 """Shared key-resolution: form field -> env var -> saved config, same
 precedence used by both the content-only and full generate endpoints so a
 key entered once behaves identically in either request."""
 serp_key=(request.form.get('serp_api_key','').strip()
           or os.getenv('SERPAPI_KEY','')
           or _cfg.get('serpapi_key',''))
 openai_key=(request.form.get('openai_api_key','').strip()
             or os.getenv('OPENAI_API_KEY','')
             or _cfg.get('openai_key',''))
 deepseek_key=(request.form.get('deepseek_api_key','').strip()
               or os.getenv('DEEPSEEK_API_KEY','')
               or _cfg.get('deepseek_key',''))
 anthropic_key=(request.form.get('anthropic_api_key','').strip()
                or os.getenv('ANTHROPIC_API_KEY','')
                or _cfg.get('anthropic_key',''))
 return serp_key,openai_key,deepseek_key,anthropic_key

@app.post('/api/generate_content')
def generate_content():
 """Phase 1 of the two-step flow: run AI content generation only (no images
 yet) and hand the result — reviewer_names in particular — back to the
 browser. Reviewer photos can only be gender-matched to a generated name
 (e.g. "Michael") if the uploader sees that name before picking a file; the
 old single-shot flow collected the image upload in the same request that
 generated the names, so the name was never known in time to guide the
 upload, and a mismatched stock photo (wrong gender for the name) had no way
 to be caught. The browser calls this endpoint first, shows the returned
 reviewer_names next to per-reviewer upload fields, then calls /api/generate
 with that same data (as content_json) plus the now-correctly-matched files."""
 try:
  product=request.form.get('product_name','').strip()
  affiliate=clean_url(request.form.get('affiliate_link',''))
  domain=clean_url(request.form.get('domain','')).rstrip('/')
  provider=request.form.get('ai_provider','auto').strip().lower()
  if not product or not affiliate or not domain:return jsonify(error='Product Name, Affiliate Link and Domain are required.'),400
  _cfg=_load_cfg()
  _serp_key,openai_key,deepseek_key,anthropic_key=_resolve_keys(_cfg)
  product_hint=_request_hint()
  data=get_content(product,affiliate,domain,provider,openai_key,deepseek_key,anthropic_key,product_hint)
  data['brand']=data.get('brand') or product
  return jsonify(data)
 except Exception as e:
  _log_failure('generate_content',e)
  msg=str(e)
  if 'Traceback' in msg or len(msg)>800:msg='Content generation failed. Check your API keys and try again.'
  return jsonify(error=msg),500

@app.post('/api/generate')
def generate():
 work=None
 _LOW_RES_WARNINGS.clear()
 _HIW_IMG_WARNINGS.clear()
 try:
  product=request.form.get('product_name','').strip()
  affiliate=clean_url(request.form.get('affiliate_link',''))
  domain=clean_url(request.form.get('domain','')).rstrip('/')
  design=request.form.get('design','1')
  mode=request.form.get('image_source','both')
  provider=request.form.get('ai_provider','auto').strip().lower()

  # Load saved config as fallback
  _cfg=_load_cfg()

  serp_key,openai_key,deepseek_key,anthropic_key=_resolve_keys(_cfg)
  # Save keys to config for next time (local use only; never on the hosted site)
  if not auth.HOSTED:
   try:
    _save={'anthropic_key':anthropic_key,'openai_key':openai_key,
           'deepseek_key':deepseek_key,'serpapi_key':serp_key,
           'ai_provider':provider,'design':design,'image_source':mode}
    (BASE/'.aff_config.json').write_text(json.dumps(_save,indent=2),encoding='utf-8')
   except Exception:pass
  if not product or not affiliate or not domain:return jsonify(error='Product Name, Affiliate Link and Domain are required.'),400
  if design not in TEMPLATES:design='1'
  product_hint=_request_hint()
  # If the browser already ran phase 1 (/api/generate_content), reuse that
  # exact result instead of calling the AI again — a second call could
  # return different prices/ingredients/etc than what the user was just
  # shown. reviewer_names specifically gets re-verified against whatever
  # photos were actually uploaded below (gender_match_reviewer_names), so a
  # name here may still change from what phase 1 originally showed — that's
  # intentional: it's re-confirmed against the real photo instead of trusted
  # from before the photo was even picked.
  content_json=request.form.get('content_json','').strip()
  if content_json:
   try:data=json.loads(content_json)
   except Exception:data=get_content(product,affiliate,domain,provider,openai_key,deepseek_key,anthropic_key,product_hint)
  else:
   data=get_content(product,affiliate,domain,provider,openai_key,deepseek_key,anthropic_key,product_hint)
  data['brand']=data.get('brand') or product
  data=ensure_core_faqs(data)
  # Design 15 gets a fresh random look for every site; every page built below
  # reads it from `data`, so the whole site shares one consistent recipe.
  if design=='15':data['_d15']=design15.new_recipe()
  data['tracking']={
   'ga_id':request.form.get('ga_id','').strip(),
   'gsc_verify':request.form.get('gsc_verify','').strip(),
   'bing_verify':request.form.get('bing_verify','').strip(),
  }
  work=Path(tempfile.mkdtemp(prefix='aff_v9_'))
  site=work/'site';imgdir=site/'assets/images';imgdir.mkdir(parents=True)
  manual=save_uploaded(request.files.getlist('images'),imgdir) if mode in ('manual','both') else []
  serp_urls=serp_images(product,serp_key) if mode in ('serp','both') and serp_key and mode!='none' else []
  serp_dl=download_images(serp_urls,imgdir)
  images=manual+[s for s in serp_dl if s not in manual]
  data['images']=images
  data['reviewer_names']=gender_match_reviewer_names(images,site,data.get('reviewer_names',[]),product,provider,openai_key,deepseek_key,anthropic_key)
  # No publisher-uploaded how-it-works.* image — generate a numbered-steps
  # infographic from this product's own real how_it_works data instead of
  # leaving the section without an image (or, as before the wrong-brand-leak
  # fix, silently showing a different product's own mechanism graphic).
  if not any(Path(p).stem.lower() in ('how-it-works','how_it_works','howitworks','how-it-work') for p in images):
   _hiw_hero_rel=next((p for p in images if Path(p).stem.lower()=='hero'),images[0]) if images else None
   _hiw_hero_disk=None
   if _hiw_hero_rel:
    _hiw_cand=Path(_hiw_hero_rel)
    if _hiw_cand.is_absolute() and _hiw_cand.exists():_hiw_hero_disk=_hiw_cand
    elif (site/_hiw_hero_rel).exists():_hiw_hero_disk=site/_hiw_hero_rel
    elif _hiw_cand.exists():_hiw_hero_disk=_hiw_cand
   _hiw_palette=build_theme_palette(extract_brand_color(_hiw_hero_disk) if _hiw_hero_disk else None)
   _hiw_path=imgdir/'how-it-works.png'
   try:
    if generate_how_it_works_image(_hiw_path,data.get('how_it_works',[]),data['brand'],_hiw_palette['primary']):
     images.append(f'assets/images/{_hiw_path.name}')
   except Exception:pass
  blog_articles=_blog_articles(data,domain,affiliate)
  if TEMPLATES[design].get('native'):
   (site/'index.html').write_text(build_native_page(data,domain,affiliate,images,'index.html','index',design,site),encoding='utf-8')
   defs=[('what-is-product.html','what-is'),('how-it-works.html','how-it-works'),('ingredients.html','ingredients'),('benefits.html','benefits'),('reviews.html','reviews'),('faq.html','faq')]
   for fn,kind in defs:
    (site/fn).write_text(build_native_page(data,domain,affiliate,images,fn,kind,design,site),encoding='utf-8')
   # Real blog: one page per article (min 4, built from this product's own
   # ingredients/pricing/guarantee/FAQ data), plus an index that actually
   # links to each one — replaces the old 3 inert teaser cards with no
   # article pages behind them.
   (site/'blog').mkdir(exist_ok=True)
   palette_blog=build_theme_palette(extract_brand_color(
     (site/next((p for p in images if Path(p).stem.lower()=='hero'),images[0])) if images else None))
   for a in blog_articles:
    fn=f'blog/{a["slug"]}.html'
    article_html=build_native_page(data,domain,affiliate,images,fn,'index',design,site)
    asoup=BeautifulSoup(article_html,'html.parser')
    for sec in asoup.find_all('section'):sec.decompose()
    if asoup.title:asoup.title.string=a['title']
    a_meta_tag=asoup.find('meta',attrs={'name':'description'})
    if a_meta_tag:a_meta_tag['content']=a['meta_desc']
    for prop,val in (('og:title',a['title']),('twitter:title',a['title']),
                      ('og:description',a['meta_desc']),('twitter:description',a['meta_desc'])):
     tag=_find_meta(asoup,prop)
     if tag:tag['content']=val
    banner_tag=_swap_header_for_banner(asoup,f'<div style="background:{palette_blog["primary_dark"]};padding:50px 0;text-align:center">'
                           f'<h1 style="color:#fff;margin:0;font-size:1.8rem">{html.escape(a["h1"])}</h1></div>')
    breadcrumb,internal_links,related=_blog_article_extras(data['brand'],a['slug'],a['h1'],blog_articles)
    body_content=BeautifulSoup(
     f'<section><div class="wrap" style="max-width:760px;margin:0 auto;padding:40px 24px;line-height:1.75">'
     f'{breadcrumb}{internal_links}{a["body_html"]}{related}</div></section>','html.parser')
    # The article goes BELOW its title banner (it used to be inserted right
    # after <nav>, which put the body above the banner).
    anchor=banner_tag if banner_tag is not None else asoup.find('nav')
    if anchor is not None:anchor.insert_after(body_content)
    rebase_relative_assets(asoup,'../')
    article_canonical=current_domain_url(domain,fn)
    add_jsonld(asoup,data,domain,article_canonical,affiliate,images,include_product=False)
    add_article_jsonld(asoup,data,article_canonical,a['title'],a['meta_desc'],domain,images)
    (site/fn).write_text(str(asoup),encoding='utf-8')
   blog_cards=''.join(
    f'<a class="card" href="../blog/{a["slug"]}.html" style="display:block;text-decoration:none;color:inherit">'
    f'<h4>{html.escape(a["h1"])}</h4><p>{html.escape(_truncate_words(a["meta_desc"],140))}</p>'
    f'<span style="font-weight:700">Read more &rarr;</span></a>' for a in blog_articles)
   blog_html=build_native_page(data,domain,affiliate,images,'blog/index.html','index',design,site)
   bsoup=BeautifulSoup(blog_html,'html.parser')
   for sec in bsoup.find_all('section'):sec.decompose()
   blog_seo_title=f'{data["brand"]} Blog | {data["brand"]}'
   if bsoup.title:bsoup.title.string=blog_seo_title
   blog_meta_desc=f'Guides and articles about {data["brand"]} — ingredients, usage tips and honest answers.'[:160]
   blog_meta_tag=bsoup.find('meta',attrs={'name':'description'})
   if blog_meta_tag:blog_meta_tag['content']=blog_meta_desc
   for prop,val in (('og:title',blog_seo_title),('twitter:title',blog_seo_title),
                     ('og:description',blog_meta_desc),('twitter:description',blog_meta_desc)):
    tag=_find_meta(bsoup,prop)
    if tag:tag['content']=val
   banner_tag=_swap_header_for_banner(bsoup,f'<div style="background:{palette_blog["primary_dark"]};padding:50px 0;text-align:center">'
                          f'<h1 style="color:#fff;margin:0">{html.escape(data["brand"])} Blog</h1></div>')
   body_content=BeautifulSoup(f'<section><div class="wrap"><div class="grid g3" style="margin:40px 0">{blog_cards}</div></div></section>','html.parser')
   anchor=banner_tag if banner_tag is not None else bsoup.find('nav')
   if anchor is not None:anchor.insert_after(body_content)
   rebase_relative_assets(bsoup,'../')
   add_jsonld(bsoup,data,domain,current_domain_url(domain,'blog/index.html'),affiliate,images,include_product=False)
   (site/'blog/index.html').write_text(str(bsoup),encoding='utf-8')
  else:
   base=source_for(design)
   (site/'index.html').write_text(make_page(base,data,domain,affiliate,images,design,'index.html',site),encoding='utf-8')
   defs=[('what-is-product.html','what-is'),('how-it-works.html','how-it-works'),('ingredients.html','ingredients'),('benefits.html','benefits'),('reviews.html','reviews'),('faq.html','faq')]
   for fn,kind in defs:
    (site/fn).write_text(page_variant(base,data,domain,affiliate,images,design,fn,kind,site),encoding='utf-8')
   # Real blog: one page per article (min 4, built from this product's own
   # ingredients/pricing/guarantee/FAQ data), plus an index that actually
   # links to each one. internal_links() rewrites any "blog"/"guides" nav
   # item to blog/index.html on every design (not just native ones), so
   # without generating that page here, the nav link 404s on designs 1-7.
   (site/'blog').mkdir(exist_ok=True)
   for a in blog_articles:
    fn=f'blog/{a["slug"]}.html'
    breadcrumb,internal_links,related=_blog_article_extras(data['brand'],a['slug'],a['h1'],blog_articles)
    article_body=f'{breadcrumb}{internal_links}{a["body_html"]}{related}'
    article_html=legal_page(base,data,domain,affiliate,images,design,fn,a['h1'],article_body,site)
    asoup=BeautifulSoup(article_html,'html.parser')
    if asoup.title:asoup.title.string=a['title']
    a_meta_tag=asoup.find('meta',attrs={'name':'description'})
    if a_meta_tag:a_meta_tag['content']=a['meta_desc']
    for prop,val in (('og:title',a['title']),('twitter:title',a['title']),
                      ('og:description',a['meta_desc']),('twitter:description',a['meta_desc'])):
     tag=_find_meta(asoup,prop)
     if tag:tag['content']=val
    rebase_relative_assets(asoup,'../')
    article_canonical=current_domain_url(domain,fn)
    add_article_jsonld(asoup,data,article_canonical,a['title'],a['meta_desc'],domain,images)
    (site/fn).write_text(str(asoup),encoding='utf-8')
   blog_cards=''.join(
    f'<a href="../blog/{a["slug"]}.html" style="display:block;text-decoration:none;color:inherit;margin-bottom:24px">'
    f'<h3 style="margin:24px 0 6px">{html.escape(a["h1"])}</h3>'
    f'<p style="margin-bottom:6px">{html.escape(_truncate_words(a["meta_desc"],140))}</p>'
    f'<span style="font-weight:700">Read more &rarr;</span></a>' for a in blog_articles)
   blog_soup=BeautifulSoup(legal_page(base,data,domain,affiliate,images,design,'blog/index.html',f'{data["brand"]} Blog',blog_cards,site),'html.parser')
   rebase_relative_assets(blog_soup,'../')
   (site/'blog/index.html').write_text(str(blog_soup),encoding='utf-8')
  # Legal / info pages (Terms, Privacy, Disclaimer, Refund, About, Contact) so footer links work
  legal_pages=_legal_pages_content(data['brand'],domain,data.get('category',''))
  if TEMPLATES[design].get('native'):
   pass  # native design already has its own footer with correct legal links; legal pages still generated below for content
  for fn,(page_title,body_html) in legal_pages.items():
   if TEMPLATES[design].get('native'):
    # Reuse the native index page's nav/footer chrome for legal pages too
    legal_html=build_native_page(data,domain,affiliate,images,fn,'index',design,site)
    lsoup=BeautifulSoup(legal_html,'html.parser')
    for sec in lsoup.find_all('section'):sec.decompose()
    # Unique <title>/meta description per legal page — build_native_page()
    # only ever wrote the site-wide title/description into this template
    # (legal pages weren't in its page_titles map), so every legal page
    # would otherwise ship with the exact same <title> as the homepage.
    legal_seo_title=f'{page_title} | {data["brand"]}'
    if lsoup.title:lsoup.title.string=legal_seo_title
    legal_plain_snippet=re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',body_html))).strip()[:150].strip()
    legal_meta_desc=f'{page_title} for {data["brand"]}. {legal_plain_snippet}'[:160]
    legal_meta_tag=lsoup.find('meta',attrs={'name':'description'})
    if legal_meta_tag:legal_meta_tag['content']=legal_meta_desc
    for prop,val in (('og:title',legal_seo_title),('twitter:title',legal_seo_title),
                      ('og:description',legal_meta_desc),('twitter:description',legal_meta_desc)):
     tag=_find_meta(lsoup,prop)
     if tag:tag['content']=val
    # FAQ/Product schema is only safe to add here (not inside build_native_page())
    # because the section sweep just above has already removed the FAQ section —
    # adding it earlier would embed FAQPage/Product structured data referencing
    # content that never actually renders on this legal page.
    add_jsonld(lsoup,data,domain,current_domain_url(domain,fn),affiliate,images)
    header=lsoup.find('header')
    banner=None
    if header:
     hero_rel=next((p for p in images if Path(p).stem.lower()=='hero'),images[0]) if images else None
     hero_disk=None
     if hero_rel:
      cand=Path(hero_rel)
      if cand.is_absolute() and cand.exists():hero_disk=cand
      elif (site/hero_rel).exists():hero_disk=site/hero_rel
      elif cand.exists():hero_disk=cand
     palette=build_theme_palette(extract_brand_color(hero_disk) if hero_disk else None)
     banner_soup=BeautifulSoup(f'<div style="background:{palette["primary_dark"]};padding:50px 0;text-align:center">'
                                f'<h1 style="color:#fff;margin:0">{html.escape(page_title)}</h1></div>','html.parser')
     header.replace_with(banner_soup)
     # BeautifulSoup document objects (banner_soup) don't support insert_after()
     # themselves — re-find the actual <div> Tag that landed in the tree.
     nav_tag=lsoup.find('nav')
     banner=nav_tag.find_next_sibling(True) if nav_tag else None
    body_soup=BeautifulSoup(f'<div class="wrap" style="padding:50px 24px;max-width:760px;margin:0 auto">{body_html}</div>','html.parser')
    # Insert the page-title banner's replacement right after itself so the
    # title reads above the body copy — inserting after <nav> instead put
    # the banner BELOW the body text, since header.replace_with() already
    # placed the banner in that exact spot (immediately after <nav>).
    if banner is not None:
     banner.insert_after(body_soup)
    else:
     nav=lsoup.find('nav')
     if nav:nav.insert_after(body_soup)
    (site/fn).write_text(str(lsoup),encoding='utf-8')
   else:
    (site/fn).write_text(legal_page(base,data,domain,affiliate,images,design,fn,page_title,body_html,site),encoding='utf-8')
  # 404 page — same nav/footer chrome as every other page, noindex'd so it
  # is never itself indexed, with links back to the real content.
  notfound_body=('<p>The page you were looking for doesn\'t exist or may have moved.</p>'
    '<ul style="list-style:none;padding:0;margin-top:16px">'
    '<li style="margin-bottom:8px"><a href="index.html">&larr; Back to Home</a></li>'
    '<li style="margin-bottom:8px"><a href="how-it-works.html">How It Works</a></li>'
    '<li style="margin-bottom:8px"><a href="ingredients.html">Ingredients</a></li>'
    '<li style="margin-bottom:8px"><a href="reviews.html">Reviews</a></li>'
    '<li style="margin-bottom:8px"><a href="blog/index.html">Blog</a></li></ul>')
  if TEMPLATES[design].get('native'):
   nf_html=build_native_page(data,domain,affiliate,images,'404.html','index',design,site)
   nfsoup=BeautifulSoup(nf_html,'html.parser')
   for sec in nfsoup.find_all('section'):sec.decompose()
   if nfsoup.title:nfsoup.title.string=f'Page Not Found | {data["brand"]}'
   nf_meta_tag=nfsoup.find('meta',attrs={'name':'description'})
   if nf_meta_tag:nf_meta_tag['content']=f'This page could not be found on {data["brand"]}.'
   header=nfsoup.find('header')
   nf_banner_tag=None
   if header:
    nf_hero_rel=next((p for p in images if Path(p).stem.lower()=='hero'),images[0]) if images else None
    nf_hero_disk=None
    if nf_hero_rel:
     nf_cand=Path(nf_hero_rel)
     if nf_cand.is_absolute() and nf_cand.exists():nf_hero_disk=nf_cand
     elif (site/nf_hero_rel).exists():nf_hero_disk=site/nf_hero_rel
     elif nf_cand.exists():nf_hero_disk=nf_cand
    nf_palette=build_theme_palette(extract_brand_color(nf_hero_disk) if nf_hero_disk else None)
    nf_banner_tag=BeautifulSoup(f'<div style="background:{nf_palette["primary_dark"]};padding:60px 0;text-align:center">'
                             f'<h1 style="color:#fff;margin:0">404 — Page Not Found</h1></div>','html.parser').find()
    header.replace_with(nf_banner_tag)
   nf_body=BeautifulSoup(f'<div class="wrap" style="padding:50px 24px;max-width:600px;margin:0 auto;text-align:center">{notfound_body}</div>','html.parser')
   nf_anchor=nf_banner_tag if nf_banner_tag is not None else nfsoup.find('nav')
   if nf_anchor is not None:nf_anchor.insert_after(nf_body)
   nf_robots=nfsoup.new_tag('meta');nf_robots['name']='robots';nf_robots['content']='noindex,follow'
   if nfsoup.head:nfsoup.head.append(nf_robots)
   (site/'404.html').write_text(str(nfsoup),encoding='utf-8')
  else:
   nf_html=legal_page(base,data,domain,affiliate,images,design,'404.html','Page Not Found',notfound_body,site)
   nfsoup=BeautifulSoup(nf_html,'html.parser')
   # legal_page()'s own auto-generated meta description strips HTML tags from
   # body_html but not entities/link text — for this page's link list that
   # produced a garbled "...moved.&amp;larr; Back to HomeHow It Works..."
   # description. Override with a clean, purpose-written one instead.
   nf_desc=f'This page could not be found on {data["brand"]}.'
   nf_meta_tag=nfsoup.find('meta',attrs={'name':'description'})
   if nf_meta_tag:nf_meta_tag['content']=nf_desc
   for prop in ('og:description','twitter:description'):
    tag=_find_meta(nfsoup,prop)
    if tag:tag['content']=nf_desc
   nf_robots=nfsoup.new_tag('meta');nf_robots['name']='robots';nf_robots['content']='noindex,follow'
   if nfsoup.head:nfsoup.head.append(nf_robots)
   (site/'404.html').write_text(str(nfsoup),encoding='utf-8')

  _blog_lastmod={f'blog/{a["slug"]}.html':date.today().isoformat() for a in blog_articles}
  write_robots_sitemap(site,domain,defs+[('blog/index.html','blog')]
                        +[(f'blog/{a["slug"]}.html','') for a in blog_articles]
                        +[(fn,'') for fn in legal_pages.keys()],
                        lastmod_overrides=_blog_lastmod)
  write_htaccess(site,domain)
  write_indexnow(site,domain)
  write_llms_txt(site,domain,data,blog_articles,
                  extra_pages=[(fn,title) for fn,(title,_) in legal_pages.items()])
  (site/'README.txt').write_text(f'Website package\nProduct: {product}\nDomain: {domain}\nGenerated: {date.today().isoformat()}\n\nVerify claims, pricing, guarantees, testimonials, certifications and image usage rights before publishing.\n\nHosting note: .htaccess in this zip enforces HTTPS + your exact www/non-www domain and enables compression/caching. It only works on Apache hosting — if you\'re on Nginx, Netlify, Vercel or Cloudflare Pages, set the equivalent redirect/caching rules on that host instead; this file will simply be ignored there.\n\nIndexNow: once the site is live at its real domain, run `python indexnow-submit.py` (requires `pip install requests`) to notify Bing/Yandex/Seznam.cz/Naver about every page in sitemap.xml right away instead of waiting for them to crawl it on their own schedule.\n',encoding='utf-8')
  # A publisher can upload bonus-1.png/bonus-2.png etc. as manual images
  # before knowing whether the AI will actually report any genuine bonus
  # offers for this product — when data['bonuses'] comes back empty, no
  # bonus section is ever built (by design — no fake bonuses) and those
  # uploads never get referenced anywhere in the generated pages. Strip
  # them here so the shipped zip doesn't carry unused dead-weight images.
  if not data.get('bonuses'):
   for p in list((site/'assets/images').glob('bonus*')):
    if re.fullmatch(r'bonus-?\d+',p.stem.lower()):
     p.unlink()
  _fav_hero_rel=next((p for p in images if Path(p).stem.lower()=='hero'),images[0]) if images else None
  _fav_hero_disk=None
  if _fav_hero_rel:
   _cand=Path(_fav_hero_rel)
   if _cand.is_absolute() and _cand.exists():_fav_hero_disk=_cand
   elif (site/_fav_hero_rel).exists():_fav_hero_disk=site/_fav_hero_rel
   elif _cand.exists():_fav_hero_disk=_cand
  _fav_palette=build_theme_palette(extract_brand_color(_fav_hero_disk) if _fav_hero_disk else None)
  generate_favicon_files(site,images,data['brand'],_fav_palette['primary'])
  apply_favicon_links(site,_fav_palette['primary'])
  seo_rename_images(site,data['brand'])
  out=build_zip(site,domain,product)
  return send_file(out,as_attachment=True,download_name=out.name,mimetype='application/zip')
 except Exception as e:
  _log_failure('generate',e)
  msg=str(e)
  if 'Traceback' in msg or len(msg)>800:msg='Generation failed. Check your API keys and try again.'
  return jsonify(error=msg),500
 finally:
  if work and work.exists():
   try:shutil.rmtree(work,ignore_errors=True)
   except Exception:pass

if __name__=='__main__':app.run(host=os.getenv('HOST','127.0.0.1'),port=int(os.getenv('PORT','5000')),debug=False)
