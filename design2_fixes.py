"""
design2_fixes.py - drop-in helpers for the local affiliate generator (app.py).

Fixes found in the Design 2 output (synogut-affiliate-site01.zip):
  1. og:image / twitter:image / Product+Organization JSON-LD images pointed at
     badge-fda.png, badge-*.png, bonus-*.png (images[0] of an alphabetical list).
  2. Weak / stale image alt text ("Synogut", "Quality", "Payment", old-product words).
  3. Reference-design CSS keeps the template's own colour (Design 2 = JellyTide purple)
     so the site never matches the bottle.
  4. FontAwesome "kit" script that belongs to the ORIGINAL template owner's account.
  5. Bundled badge-fda.png literally says "FDA APPROVED" (supplements are not FDA approved).

Everything here is pure functions: import and call them, no globals to configure.
"""
import re
import colorsys
from pathlib import Path


# --------------------------------------------------------------------------- 1
_NON_PRODUCT_KW = ('badge', 'card', 'credit', 'guarantee', 'seal', 'bonus', 'reviewer', 'stars',
                   'checkout', 'supplement-facts', 'favicon', 'how-it-works', 'feature',
                   'payment', 'logo',
                   # reviewer / testimonial portraits under custom names ("vapocept-customer-1")
                   'customer', 'testimonial', 'review', 'avatar', 'member',
                   # bundle mock-ups, trust strips, badge art, feature/screen shots
                   'pack', 'trust', 'gmp', 'natural', 'shot')

_REVIEWER_KW = re.compile(r'customer|testimonial|review|avatar|member')
_BOTTLE_N = re.compile(r'(?:bottles?[-_]?(\d+)|(\d+)[-_]?bottles?)')


def is_non_product_image(path):
    """True for anything that must never stand in for a product photo."""
    s = Path(path).stem.lower()
    return any(k in s for k in _NON_PRODUCT_KW)


def reviewer_photo_slot(path):
    """Custom-named reviewer photos ("vapocept-customer-1", "testimonial_2",
    "jane-review-3") -> 1-based slot number; 0 when it's a reviewer photo with
    no number; None when it isn't a reviewer photo at all. Star-rating graphics
    ("5-star-review") are not portraits."""
    s = Path(path).stem.lower()
    if 'star' in s or 'badge' in s or not _REVIEWER_KW.search(s):
        return None
    m = re.search(r'(?:customer|testimonial|reviewer|review|avatar|member)s?[-_]?(\d+)$', s)
    return int(m.group(1)) if m else 0


def seo_images(images):
    """Product photos only, for og:image / twitter:image / Product JSON-LD:
    hero first, then bottle-N ascending. Never badges / seals / payment cards /
    bonus covers / bundle-pack mock-ups / reviewer or customer portraits.
    Falls back to other neutral images (e.g. SERP downloads) only when no
    hero/bottle photo exists at all; returns [] rather than ever handing back
    a non-product image."""
    def stem(p):
        return Path(p).stem.lower()

    good = [p for p in images if not is_non_product_image(p)]
    hero = [p for p in good if stem(p) == 'hero']

    def bottle_n(p):
        m = _BOTTLE_N.search(stem(p))
        return int(m.group(1) or m.group(2)) if m else None

    bottles = sorted([p for p in good if stem(p) != 'hero' and bottle_n(p) is not None],
                     key=lambda p: (bottle_n(p), stem(p)))
    if hero or bottles:
        return hero + bottles
    return sorted(good, key=stem)


# --------------------------------------------------------------------------- 2
# Words that belong to the ORIGINAL templates' products. They are "stale" for a new
# product unless the new product's own copy also uses them.
STALE_ALT_WORDS = ('cognitive', 'memory restoration', 'memory function', 'nootropic', 'brain health',
                   'mental vitality', 'gummy', 'gummies', 'metabolism', 'appetite', 'portion support',
                   'blood pressure', 'circulation', 'arginine', 'citrulline',
                   'vapocept', 'jellytide', 'bloodpril')


def scrub_image_alts(soup, data):
    """Call right after localize_images(...) in make_page / page_variant / legal_page."""
    brand = data.get('brand', '')
    cat = data.get('category', 'dietary') or 'dietary'
    # Strip a trailing generic product-type word ("...wellness supplement")
    # before it gets appended to "supplement bottle"/"supplement facts label"
    # below, so hero alt text doesn't double up ("...supplement supplement").
    for _suffix in (' supplement', ' formula', ' product'):
        if cat.lower().endswith(_suffix):
            cat = cat[:-len(_suffix)]
            break
    own = ' '.join(str(data.get(k, '')) for k in ('category', 'description', 'tagline')).lower()
    stale = [w for w in STALE_ALT_WORDS if w not in own]
    generic = {'', brand.lower(), 'quality', 'gmp', 'payment', 'natural', 'usa', 'image', 'product image'}

    for img in soup.find_all('img'):
        alt = (img.get('alt') or '').strip()
        low = alt.lower()
        stem = Path(str(img.get('src', ''))).stem.lower()
        # `title` on scraped templates is often its own separate leftover
        # blurb about the ORIGINAL product ("Rediscover What It Feels Like to
        # Breathe" on a respiratory-spray template, still showing up verbatim
        # — brand name aside — on every other product this template gets
        # reused for). alt gets rewritten below case by case; title never
        # does, so it's synced to whatever alt we land on, but only when a
        # title attribute already exists — this fixes stale copy, it doesn't
        # invent a tooltip where the template had none.
        had_title = img.has_attr('title')

        m = re.fullmatch(r'bottle[-_]?(\d+)', stem)
        if m:
            n = int(m.group(1))
            img['alt'] = f'{brand} {n} bottle package' if n > 1 else f'{brand} bottle'
            if had_title:
                img['title'] = img['alt']
            continue

        desc = None
        if stem == 'hero':
            desc = f'{brand} {cat} supplement bottle'
        elif stem.startswith('supplement-facts'):
            desc = f'{brand} supplement facts label'
        elif 'credit' in stem or stem.startswith('cards'):
            desc = 'Accepted payment methods: Visa, Mastercard, American Express, Discover'
        elif stem.startswith('badge-gmp'):
            desc = 'GMP certified manufacturing facility'
        elif stem.startswith('badge-usa'):
            desc = 'Made in the USA'
        elif stem.startswith('badge-natural'):
            desc = 'Natural ingredients badge'
        elif stem.startswith('badge-fda'):
            desc = 'FDA registered facility badge'
        elif stem == 'guarantee' or 'money-back' in stem:
            desc = '60-day money-back guarantee seal'
        elif stem == 'checkout':
            desc = 'Secure checkout preview'
        elif stem in ('how-it-works', 'feature-shot'):
            desc = f'How {brand} works'

        if desc and (low in generic or any(w in low for w in stale)):
            img['alt'] = desc
            if had_title:
                img['title'] = desc
        elif any(w in low for w in stale):
            img['alt'] = f'{brand} product image'
            if had_title:
                img['title'] = img['alt']


# --------------------------------------------------------------------------- 3
_HEX = re.compile(r'#([0-9a-fA-F]{6})\b')
_RGBA = re.compile(r'rgba?\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*,\s*(\d{1,3})\s*(?:,\s*([0-9.]+)\s*)?\)')


def retheme_reference_css(text, target_rgb, span=0.11, min_sat=0.10):
    """Hue-rotate the template's brand colour family to the bottle's hue.

    * base hue is auto-detected from the template's own `--accent: #xxxxxx`
    * only colours within +/-span (~40 deg) of that hue are touched, so greys, whites,
      success-green, gold stars etc. stay exactly as they are
    * lightness & saturation are kept, so shadows / tints / gradients stay consistent
    * works on CSS files AND on inline style="" strings / <style> blocks (any text)
    * returns the text unchanged when the bottle colour is too bland to be a theme colour
    Use:  css = retheme_reference_css(css, extract_brand_color(hero_path))
    """
    if not target_rgb:
        return text
    m = re.search(r'--accent:\s*#([0-9a-fA-F]{6})', text)
    if not m:
        return text
    base_h = colorsys.rgb_to_hls(*[int(m.group(1)[i:i + 2], 16) / 255 for i in (0, 2, 4)])[0]
    t_h, _t_l, t_s = colorsys.rgb_to_hls(*[c / 255 for c in target_rgb])
    if t_s < 0.20:
        return text

    def shift(r, g, b):
        h, l, s = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)
        if s < min_sat or l < 0.03 or l > 0.985:
            return None
        d = (h - base_h + 0.5) % 1 - 0.5
        if abs(d) > span:
            return None
        nr, ng, nb = colorsys.hls_to_rgb((t_h + d) % 1, l, s)
        return round(nr * 255), round(ng * 255), round(nb * 255)

    def hex_sub(mo):
        h = mo.group(1)
        out = shift(int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))
        return mo.group(0) if out is None else '#%02X%02X%02X' % out

    def rgba_sub(mo):
        out = shift(int(mo.group(1)), int(mo.group(2)), int(mo.group(3)))
        if out is None:
            return mo.group(0)
        a = mo.group(4)
        return f'rgba({out[0]},{out[1]},{out[2]},{a})' if a is not None else f'rgb({out[0]},{out[1]},{out[2]})'

    return _RGBA.sub(rgba_sub, _HEX.sub(hex_sub, text))


def retheme_html_inline(html_text, target_rgb, base_css_text):
    """Same hue rotation for inline style="" values that carry var(--x,#fallback) hexes.
    base_css_text = the ORIGINAL (un-themed) css, only used to detect the template base hue."""
    if not target_rgb:
        return html_text
    probe = re.search(r'--accent:\s*#[0-9a-fA-F]{6}', base_css_text)
    if not probe:
        return html_text
    def fix_style(mo):
        return mo.group(1) + retheme_reference_css(probe.group(0) + ';' + mo.group(2), target_rgb).split(';', 1)[1] + mo.group(3)
    html_text = re.sub(r'(style=")([^"]*)(")', fix_style, html_text)
    # mobile browser toolbar colour: <meta name="theme-color" content="#xxxxxx">
    def fix_meta(mo):
        tag = mo.group(0)
        if 'theme-color' not in tag:
            return tag
        def fix_content(c):
            return c.group(1) + retheme_reference_css(probe.group(0) + ';' + c.group(2), target_rgb).split(';', 1)[1] + c.group(3)
        return re.sub(r'(content=")([^"]*)(")', fix_content, tag)
    return re.sub(r'<meta[^>]*>', fix_meta, html_text)


# --------------------------------------------------------------------------- 4
def strip_third_party_fa_kit(soup):
    """kit.fontawesome.com/<id>.js is the ORIGINAL template owner's Font Awesome account.
    The cdnjs font-awesome stylesheet the templates also load is enough - remove the kit."""
    for s in soup.find_all('script', src=True):
        if 'kit.fontawesome.com' in s['src']:
            s.decompose()


# --------------------------------------------------------------------------- 5
def make_fda_registered_badge(path, size=420):
    """Replace the bundled 'FDA APPROVED' seal. Supplements are NOT FDA approved and the site's
    own FAQ says so. Only use this badge if the supplier confirms an FDA-registered facility;
    otherwise delete the badge element instead."""
    from PIL import Image, ImageDraw, ImageFont
    S = size
    im = Image.new('RGBA', (S, S), (255, 255, 255, 0))
    d = ImageDraw.Draw(im)
    navy = (16, 68, 96, 255)
    d.ellipse((6, 6, S - 6, S - 6), outline=navy, width=14)
    d.ellipse((34, 34, S - 34, S - 34), outline=navy, width=4)
    def font(px):
        for f in ('DejaVuSans-Bold.ttf', 'arialbd.ttf', 'Arial Bold.ttf'):
            try:
                return ImageFont.truetype(f, px)
            except Exception:
                pass
        return ImageFont.load_default()
    def center(text, y, px):
        f = font(px)
        w = d.textlength(text, font=f)
        d.text(((S - w) / 2, y), text, font=f, fill=navy)
    center('FDA', int(S * 0.24), int(S * 0.24))
    center('REGISTERED', int(S * 0.52), int(S * 0.095))
    center('FACILITY', int(S * 0.64), int(S * 0.095))
    im.save(path)
