<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<meta name="description" content="__META_DESC__">
<link rel="canonical" href="__CANONICAL__">
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&family=Nunito+Sans:wght@400;600;700;800&display=swap" rel="stylesheet">
<style>
:root{--primary:__COLOR_PRIMARY__;--primary-dark:__COLOR_DARK__;--primary-light:__COLOR_LIGHT__;--accent:__COLOR_ACCENT__;--on-primary:__COLOR_ON_PRIMARY__;--ink:#3B2A20;--ink-soft:#8A7158;--bg:#FBF3EA;--surface:#fff;--surface-alt:#F3E4D3;--line:rgba(59,42,32,.14);--good:#5B7F3A;--radius:16px;--shadow:0 18px 40px -20px rgba(59,42,32,.28)}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;font-family:'Nunito Sans',system-ui,-apple-system,Segoe UI,Roboto,sans-serif;color:var(--ink);background:var(--bg);line-height:1.65;overflow-x:hidden;font-size:17px}
h1,h2,h3,h4{font-family:'Cormorant Garamond',Georgia,serif;font-weight:700;line-height:1.2;margin:0;color:var(--ink)}
a{color:var(--primary-dark)}
img{max-width:100%;height:auto;display:block}
.wrap{max-width:1080px;margin:0 auto;padding:0 24px}
/* Strip + nav */
.trc-strip{background:var(--ink);color:#F6E6D6;font-size:13.5px;padding:9px 0;display:flex;gap:26px;justify-content:center;flex-wrap:wrap;text-align:center}
.trc-strip b{color:var(--primary-light)}
nav.navbar{position:sticky;top:0;z-index:200;background:rgba(251,243,234,.93);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
nav.navbar .wrap{display:flex;align-items:center;gap:24px;padding:15px 24px;max-width:1160px}
.logo{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:1.5rem;text-decoration:none;color:var(--ink)}
.logo em{font-style:normal;color:var(--primary-dark)}
.nav-links{display:flex;gap:22px;margin-left:auto;flex-wrap:wrap;align-items:center}
.nav-links a{color:var(--ink-soft);text-decoration:none;font-weight:700;font-size:.9rem}
.nav-links a:hover{color:var(--primary-dark)}
.nav-toggle{display:none;background:none;border:1px solid var(--line);border-radius:8px;font-size:22px;cursor:pointer;color:var(--ink);padding:4px 10px;min-height:40px;margin-left:auto}
.btn,.btn-big{display:inline-flex;align-items:center;justify-content:center;gap:6px;background:var(--primary-dark);color:var(--on-primary)!important;font-weight:800;text-decoration:none;padding:14px 26px;border-radius:10px;border:0;box-shadow:var(--shadow);font-size:1rem;line-height:1.2;text-align:center;transition:transform .15s ease;white-space:nowrap}
.btn:hover,.btn-big:hover{transform:translateY(-2px)}
.btn-ghost{background:transparent!important;color:var(--ink)!important;border:2px solid var(--ink)!important;box-shadow:none!important}
.btn-big{padding:16px 30px;font-size:1.03rem}
.nav-cta{padding:9px 18px!important;font-size:.86rem;box-shadow:none}
/* Hero — single centered column, editorial masthead feel */
header.hero{padding:56px 0 20px;background:radial-gradient(1000px 440px at 50% -20%,var(--surface-alt) 0%,transparent 60%),var(--bg);text-align:center}
.hero .wrap{max-width:760px}
.trc-pill{display:inline-block;background:var(--surface-alt);color:var(--primary-dark);font-weight:800;font-size:.78rem;letter-spacing:.03em;text-transform:uppercase;padding:7px 15px;border-radius:999px}
.hero h1{font-size:2.9rem;margin:18px 0 16px;letter-spacing:-.01em}
.hero h1 em{font-style:normal;color:var(--primary-dark)}
.hero-media{display:flex;justify-content:center;margin:14px 0 22px}
.trc-hero-card{background:var(--surface);border:1px solid var(--line);border-radius:20px;padding:18px 26px;display:flex;align-items:center;gap:18px;box-shadow:var(--shadow)}
.trc-hero-card img{max-width:96px}
.trc-hero-card p{margin:0;font-weight:700;font-size:.92rem;text-align:left}
.hero-lede{font-size:1.1rem;color:var(--ink-soft);max-width:620px;margin:0 auto 22px;font-style:italic}
.hero-cta-row{display:flex;gap:14px;align-items:center;justify-content:center;flex-wrap:wrap;margin-bottom:8px}
/* Section head */
.sec{padding:64px 0}
.sec.alt{background:var(--surface-alt)}
.head{max-width:680px;margin:0 auto 32px;text-align:center}
.eyebrow{display:inline-flex;align-items:center;gap:7px;color:var(--primary-dark);font-weight:800;font-size:.75rem;letter-spacing:.09em;text-transform:uppercase;margin-bottom:11px;font-family:'Nunito Sans',sans-serif}
.head h2{font-size:2.1rem;margin:0 0 12px}
.head p{color:var(--ink-soft);font-size:1.02rem;margin:0}
.grid{display:grid;gap:18px}
.g2{grid-template-columns:repeat(2,minmax(0,1fr))}
.g3{grid-template-columns:repeat(3,minmax(0,1fr))}
.reveal{opacity:0;transform:translateY(14px);transition:opacity .5s ease,transform .5s ease}
.reveal.in{opacity:1;transform:none}
@media(prefers-reduced-motion:reduce){.reveal{opacity:1;transform:none;transition:none}}
/* Shared card markup (from build_native_page's default card builders) */
.card,.pcard,.ing-card,.rev-card,.step-card{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:24px;box-shadow:var(--shadow)}
.card h4,.ing-card h4,.step-card h4{margin:0 0 8px;font-size:1.1rem;font-family:'Cormorant Garamond',serif}
.card p,.ing-card p,.step-card p,.rev-card p{color:var(--ink-soft);margin:0;font-size:.93rem}
.ing-card{display:flex;gap:16px;border-left:4px solid var(--good)}
.ing-num,.step-num{flex:none;width:36px;height:36px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-family:'Cormorant Garamond',serif;font-weight:700;font-size:1rem;color:var(--on-primary);background:var(--primary-dark)}
.step-card{border-left:4px solid var(--good)}
.step-card .step-num{margin-bottom:14px}
.pcard{text-align:left}
.pcard .num{font-family:'Cormorant Garamond',serif;font-size:1.5rem;color:var(--primary-dark);font-weight:700;display:block;margin-bottom:6px}
.rev-card .rev-head{display:flex;gap:12px;align-items:center;margin-bottom:9px}
.rev-card .rev-head img,.rev-card .rev-head>div{width:44px;height:44px;border-radius:50%;object-fit:cover}
.rev-name{font-weight:800;font-family:'Nunito Sans',sans-serif}
.rev-sub{font-size:.78rem;color:var(--ink-soft)}
.rev-stars{color:var(--primary-dark);font-size:1rem;letter-spacing:.1em;margin-bottom:8px}
/* Trust strip */
section.trust{padding:18px 0;background:var(--surface);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
section.trust .wrap{display:flex;gap:30px;justify-content:center;flex-wrap:wrap;align-items:center;max-width:1160px}
section.trust .t-item{display:flex;align-items:center;gap:9px;font-weight:700;font-size:.87rem;color:var(--ink-soft)}
section.trust img{width:32px;height:32px;object-fit:contain}
/* Callout reused by Quick Facts auto-box */
.trc-callout{background:var(--surface-alt);border-left:4px solid var(--primary-dark);border-radius:14px;padding:20px 22px;font-weight:600;color:var(--ink)}
.trc-chips{display:flex;gap:10px;flex-wrap:wrap;margin:20px 0}
.trc-chips span{background:var(--surface-alt);border:1px solid var(--line);border-radius:999px;padding:7px 15px;font-weight:700;font-size:.8rem;color:var(--ink)}
/* Pull-quote — original editorial divider used between major sections */
.trc-quote{max-width:720px;margin:0 auto;text-align:center;padding:10px 0}
.trc-quote blockquote{margin:0;font-family:'Cormorant Garamond',serif;font-style:italic;font-size:1.7rem;line-height:1.4;color:var(--ink)}
.trc-quote blockquote:before{content:"“";color:var(--primary-dark)}
.trc-quote blockquote:after{content:"”";color:var(--primary-dark)}
.trc-quote cite{display:block;margin-top:14px;font-style:normal;font-weight:800;font-size:.82rem;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-soft)}
/* Benefits as a staggered editorial strip (zigzag offset), not a uniform grid —
   this design's structural identity alongside the Sourcing Trail. */
.trc-stagger{display:grid;gap:16px;max-width:860px;margin:0 auto}
.trc-stagger>*{border-left:4px solid var(--good);border-right:none}
.trc-stagger>*:nth-child(odd){margin-right:9%}
.trc-stagger>*:nth-child(even){margin-left:9%;border-left:none;border-right:4px solid var(--primary-dark);text-align:right}
/* Sourcing Trail — original distinctive component: dotted path with leaf-shaped origin nodes */
.trc-trail{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:36px 30px}
.trc-trail-path{position:relative;display:flex;justify-content:space-between;gap:12px;padding-top:10px}
.trc-trail-path:before{content:"";position:absolute;top:19px;left:24px;right:24px;height:2px;background:repeating-linear-gradient(90deg,var(--good) 0 8px,transparent 8px 16px)}
.trc-leaf{flex:1;text-align:center;position:relative}
.trc-leaf .dot{width:38px;height:38px;margin:0 auto 12px;border-radius:70% 0 70% 0;background:var(--good);border:3px solid var(--surface);box-shadow:0 0 0 2px var(--good);position:relative;z-index:1}
.trc-leaf b{display:block;font-family:'Cormorant Garamond',serif;font-size:1.1rem;font-weight:700;color:var(--ink)}
.trc-leaf span{display:block;font-size:.78rem;color:var(--ink-soft);margin-top:3px}
.trc-trail-cap{text-align:center;font-size:.8rem;color:var(--ink-soft);opacity:.85;font-style:italic;margin-top:22px}
/* Ingredients — single-column stacked editorial list with alternating tint,
   instead of a card grid */
.trc-ing-list{display:flex;flex-direction:column;max-width:780px;margin:0 auto;border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;background:var(--surface)}
.trc-ing-list .ing-card{border-radius:0;border-left:0;box-shadow:none;border-bottom:1px solid var(--line)}
.trc-ing-list .ing-card:last-child{border-bottom:0}
.trc-ing-list .ing-card:nth-child(even){background:var(--surface-alt)}
/* Pricing */
.plans{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px;align-items:stretch}
.plan{position:relative;background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:28px 22px;text-align:center;display:flex;flex-direction:column}
.plan.top{border:2px solid var(--primary-dark);box-shadow:var(--shadow);transform:translateY(-6px)}
.plan-badge{position:absolute;top:-14px;left:50%;transform:translateX(-50%);background:var(--primary-dark);color:var(--on-primary);border-radius:999px;padding:6px 16px;font-weight:800;font-size:.75rem;white-space:nowrap;font-family:'Nunito Sans',sans-serif}
.plan img{max-width:150px;margin:4px auto 12px}
.plan-ttl{font-size:1.3rem}
.plan-sub{font-weight:700;color:var(--ink-soft);font-size:.83rem}
.plan-price{font-size:2.1rem;margin:12px 0 4px;font-family:'Cormorant Garamond',serif;font-weight:700}
.plan-price small{font-size:.88rem;color:var(--ink-soft);font-weight:600}
.plan-tot,.plan-ship{font-weight:700;color:var(--ink-soft);font-size:.83rem}
.plan-ship{color:var(--good)}
.plan ul{list-style:none;padding:0;margin:14px 0;text-align:left}
.plan ul li{padding:5px 0 5px 24px;position:relative;font-weight:600;font-size:.87rem;color:var(--ink-soft)}
.plan ul li:before{content:"✓";position:absolute;left:0;color:var(--good);font-weight:800}
.plan .btn{margin-top:auto;width:100%}
/* Guarantee */
.trc-guarantee{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:36px;text-align:center}
.trc-guarantee img{max-width:130px;margin:0 auto}
/* FAQ accordion */
.faq-row{border:1px solid var(--line);border-radius:14px;margin-bottom:12px;background:var(--surface);overflow:hidden}
.faq-btn{width:100%;text-align:left;background:transparent;border:0;padding:16px 18px;font-family:'Cormorant Garamond',serif;font-size:1.1rem;font-weight:700;cursor:pointer;display:flex;justify-content:space-between;gap:16px;align-items:center;color:var(--ink)}
.faq-btn:after{content:"+";font-size:1.3rem;font-weight:700;color:var(--primary-dark);transition:transform .2s ease}
.faq-row.open .faq-btn:after{transform:rotate(45deg)}
.faq-body{display:none;padding:0 18px 16px;color:var(--ink-soft)}
.faq-row.open .faq-body{display:block}
/* Compare */
.compare{width:100%;border-collapse:collapse;background:var(--surface);border:1px solid var(--line);border-radius:16px;overflow:hidden}
.compare th,.compare td{padding:12px 14px;text-align:left;border-bottom:1px solid var(--line);font-weight:600;font-size:.9rem}
.compare th{background:var(--surface-alt);font-family:'Cormorant Garamond',serif;font-size:1rem}
.compare td:first-child{font-weight:800}
.compare .yes{color:var(--good);font-weight:800}
.compare .no{color:#B0523F;font-weight:800}
/* References */
.refs{columns:2;column-gap:40px}
.refs li{font-size:.86rem;color:var(--ink-soft);margin-bottom:10px;break-inside:avoid}
.refs-note{font-size:.84rem;color:var(--ink-soft);text-align:center;max-width:720px;margin:0 auto 24px}
.refs-wrap.collapsed .refs li:nth-child(n+7){display:none}
.refs-more{display:block;text-align:center;margin-top:18px;background:transparent;border:1px solid var(--line);border-radius:999px;padding:9px 20px;font-weight:700;font-size:.88rem;cursor:pointer;color:var(--ink)}
/* Final CTA — contrasting deep cocoa panel */
section.final{text-align:center;background:linear-gradient(160deg,#3B2A20,#5B4531);border-radius:28px;margin:0 24px;padding:4px}
section.final .wrap{padding:52px 24px;max-width:1160px}
section.final .head h2{color:#fff}
section.final .head p{color:#E3CBAE;max-width:620px;margin:0 auto}
section.final .plan{background:rgba(255,255,255,.06);border-color:rgba(255,255,255,.18)}
section.final .plan-ttl,section.final .plan-price{color:#fff}
section.final .plan-sub,section.final .plan-tot{color:#E3CBAE}
footer{background:var(--surface-alt);border-top:1px solid var(--line);padding:40px 0;text-align:center;color:var(--ink-soft)}
footer .wrap{max-width:1160px}
footer a{color:var(--ink);font-weight:700;text-decoration:none;margin:0 8px;font-size:.9rem}
footer a:hover{color:var(--primary-dark)}
footer .fnote{font-size:.78rem;margin-top:10px;opacity:.8}
.auto-sticky-cta{background:var(--surface)!important;border-top:1px solid var(--line)!important}
.auto-sticky-cta-btn{background:var(--primary-dark)!important;color:var(--on-primary)!important;border-radius:999px!important}
@media(max-width:900px){.hero h1{font-size:2.3rem}.g3,.g2,.feature{grid-template-columns:1fr}.refs{columns:1}.trc-trail-path{flex-direction:column;gap:22px}.trc-trail-path:before{display:none}.trc-stagger>*:nth-child(odd){margin-right:0}.trc-stagger>*:nth-child(even){margin-left:0;text-align:left;border-right:none;border-left:4px solid var(--primary-dark)}}
@media(max-width:760px){.nav-links{position:fixed;top:60px;left:0;right:0;background:var(--bg);flex-direction:column;align-items:flex-start;padding:18px 24px;gap:16px;display:none;border-bottom:1px solid var(--line)}.nav-links.open{display:flex}.nav-toggle{display:block}}
</style>
</head>
<body>
<div class="trc-strip"><span><b>__FACT3_NUM__ __FACT3_LABEL__</b></span><span>Made In USA</span><span>GMP-Certified Facility</span></div>
<nav class="navbar"><div class="wrap">
<a class="logo" href="index.html">__BRAND__</a>
<button class="nav-toggle" aria-label="Toggle menu" type="button">&#9776;</button>
<div class="nav-links">
<a href="what-is-product.html">What Is __BRAND__</a>
<a href="how-it-works.html">How It Works</a>
<a href="ingredients.html">Ingredients</a>
<a href="benefits.html">Benefits</a>
<a href="reviews.html">Reviews</a>
<a href="faq.html">FAQs</a>
<a href="blog/index.html">Blog</a>
<a class="btn nav-cta" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_HEADER__</a>
</div>
</div></nav>
<header class="hero"><div class="wrap">
<span class="trc-pill">__PILL_TEXT__</span>
<h1>__HERO_H1__</h1>
<p class="hero-lede reveal">__HERO_DESC__</p>
<div class="hero-media">
<div class="trc-hero-card reveal">
<img id="hero-img" src="assets/images/hero.png" alt="__BRAND__ __CATEGORY__ supplement bottle" width="96" height="96" fetchpriority="high">
<p>★ 4.8 / 5<br>__REVIEW_COUNT__ reviews</p>
</div>
</div>
<div class="hero-cta-row">
<a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_HERO__</a>
<a class="btn btn-big btn-ghost" href="#how-it-works">See How It Works</a>
</div>
</div></header>
<section class="trust"><div class="wrap">
<div class="t-item"><img src="assets/images/badge-usa.png" alt="Made in USA" width="32" height="32" loading="lazy"> <span>Made in USA<small style="display:block;font-weight:500;opacity:.8">Manufactured under strict quality control standards.</small></span></div>
<div class="t-item"><img src="assets/images/badge-gmp.png" alt="GMP certified" width="32" height="32" loading="lazy"> <span>GMP Certified<small style="display:block;font-weight:500;opacity:.8">Made under Good Manufacturing Practice procedures.</small></span></div>
<div class="t-item"><img src="assets/images/badge-fda.png" alt="FDA-registered facility" width="32" height="32" loading="lazy"> <span>FDA-Registered Facility<small style="display:block;font-weight:500;opacity:.8">Produced in an FDA-registered facility.</small></span></div>
<div class="t-item"><img src="assets/images/badge-natural.png" alt="Natural ingredients" width="32" height="32" loading="lazy"> <span>100% Natural<small style="display:block;font-weight:500;opacity:.8">No artificial fillers or synthetic additives.</small></span></div>
</div></section>
<section class="sec" id="what-is"><div class="wrap">
<div class="head reveal"><span class="eyebrow">What is __BRAND__?</span><h2>A Clear, Straight Answer</h2></div>
<p class="reveal" style="font-size:1.05rem;max-width:720px;margin:0 auto 18px;text-align:center;color:var(--ink-soft)">__WHATIS_P1__</p>
<div class="trc-callout reveal" style="max-width:720px;margin:0 auto">__WHATIS_CALLOUT__</div>
<div class="trc-chips reveal" style="justify-content:center"><span>__CHIP1__</span><span>__CHIP2__</span><span>__CHIP3__</span><span>__CHIP4__</span></div>
<div class="reveal" style="text-align:center;margin-top:26px"><a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_AFTER_WHATIS__</a></div>
</div></section>
<section class="sec alt"><div class="wrap">
<div class="head reveal"><span class="eyebrow">Named on the label</span><h2>The __BRAND__ Sourcing Trail</h2><p>A quick walk through what's named on the label — tap any name for the full page.</p></div>
<div class="trc-trail reveal">
<div class="trc-trail-path">
<div class="trc-leaf"><div class="dot"></div><b>__ORBIT1__</b><span>Named on the label</span></div>
<div class="trc-leaf"><div class="dot"></div><b>__ORBIT2__</b><span>Named on the label</span></div>
<div class="trc-leaf"><div class="dot"></div><b>__ORBIT3__</b><span>Named on the label</span></div>
<div class="trc-leaf"><div class="dot"></div><b>__ORBIT4__</b><span>Named on the label</span></div>
</div>
<p class="trc-trail-cap">A quick map of what's on the label — see the Ingredients section below for the full description of each.</p>
</div>
</div></section>
<div class="sec"><div class="trc-quote reveal wrap">
<blockquote>A daily __CATEGORY__ routine should be simple enough to keep, and clear enough to trust.</blockquote>
<cite>The __BRAND__ Editorial Note</cite>
</div></div>
<section class="sec alt" id="benefits"><div class="wrap">
<div class="head reveal"><span class="eyebrow">Why people choose it</span><h2>What You Can Expect To Notice</h2><p>Real, everyday support — no overpromising.</p></div>
<div class="trc-stagger">__BENEFIT_CARD_TEMPLATE__</div>
<ul class="reveal" style="max-width:720px;margin:28px auto 0;font-weight:600;line-height:2;list-style:none;padding:0">__BAL_PROS_TEMPLATE__</ul>
</div></section>
<section class="sec" id="how-it-works"><div class="wrap">
<div class="head reveal"><span class="eyebrow">How it works</span><h2>From Bottle To Daily Habit</h2><p>__HIW_INTRO__</p></div>
<div class="grid g2">__HIW_CARD_TEMPLATE__</div>
<div class="reveal" style="text-align:center;margin-top:28px"><a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_AFTER_HIW__</a></div>
</div></section>
<section class="sec alt" id="ingredients"><div class="wrap">
<div class="head reveal"><span class="eyebrow">Inside every serving</span><h2>__ING_HEADING__</h2><p>Every ingredient, explained plainly. Serving: __SERVING_DAILY__ · Per bottle: __SERVING_PER_BOTTLE__.</p></div>
<div class="trc-ing-list reveal">__ING_CARD_TEMPLATE__</div>
<div class="reveal" style="text-align:center;margin-top:26px"><a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_AFTER_INGREDIENTS__</a></div>
</div></section>
<section class="sec" id="pricing"><div class="wrap">
<div class="head reveal"><span class="eyebrow">Choose your package</span><h2>Pick The __BRAND__ Package That Fits You</h2><p>__PRICING_NOTE__</p></div>
<div class="plans">__PLAN_CARD_TEMPLATE__</div>
<p class="reveal" style="text-align:center;font-weight:700;margin-top:20px;color:var(--ink-soft)">Lowest price: __PRICE_LOW__ per bottle · Highest listed: __PRICE_HIGH__ per bottle</p>
</div></section>
__BONUS_SECTION__
<div class="sec alt"><div class="trc-quote reveal wrap">
<blockquote>__FACT1_NUM__ named __FACT1_LABEL__, __FACT3_NUM__ to decide if it's right for you — nothing hidden behind a proprietary blend.</blockquote>
<cite>What __BRAND__ Is — And Isn't</cite>
</div></div>
<section class="sec" id="reviews"><div class="wrap">
<div class="head reveal"><span class="eyebrow">Verified reviews</span><h2>What Customers Say</h2><p>★★★★★ __REVIEW_COUNT__ reviews and counting.</p></div>
<div class="grid g3">__REVIEW_CARD_TEMPLATE__</div>
<div class="reveal" style="text-align:center;margin-top:26px"><a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_AFTERREVIEWS__</a></div>
</div></section>
<section class="sec alt" id="compare"><div class="wrap">
<div class="head reveal"><span class="eyebrow">An honest look</span><h2>__BRAND__ vs The Alternatives</h2><p>Decide with the facts in front of you.</p></div>
<table class="compare reveal">
<tr><th></th><th>__BRAND__</th><th>Typical Products</th><th>Doing Nothing</th></tr>
<tr><td>Ingredients listed individually</td><td class="yes">✓ Yes</td><td class="no">✗ Often a blend</td><td class="no">✗ —</td></tr>
<tr><td>One simple daily serving</td><td class="yes">✓ Yes</td><td class="no">✗ Varies</td><td class="no">✗ —</td></tr>
<tr><td>__FACT3_NUM__ money-back __FACT3_LABEL__</td><td class="yes">✓ Yes</td><td class="no">✗ Rarely</td><td class="no">✗ —</td></tr>
<tr><td>Made in USA, GMP facility</td><td class="yes">✓ Yes</td><td class="no">✗ Varies</td><td class="no">✗ —</td></tr>
</table>
</div></section>
<section class="sec" id="faq"><div class="wrap">
<div class="head reveal"><span class="eyebrow">Got questions?</span><h2>Frequently Asked Questions</h2></div>
__FAQ_ROW_TEMPLATE__
<div class="reveal" style="text-align:center;margin-top:26px"><a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_AFTERFAQ__</a></div>
</div></section>
<section class="sec alt"><div class="wrap"><div class="trc-guarantee reveal">
<img src="assets/images/guarantee.png" alt="60-day money-back guarantee" loading="lazy">
<h2 style="font-size:1.6rem;margin:14px 0">__FACT3_NUM__ Money-Back __FACT3_LABEL__</h2>
<p style="color:var(--ink-soft);max-width:640px;margin:0 auto 20px">__GUARANTEE_TEXT__</p>
<div style="display:flex;gap:22px;justify-content:center;flex-wrap:wrap;margin-top:8px">
<figure style="margin:0;text-align:center;max-width:110px"><img src="assets/images/badge-usa.png" alt="Made in USA" width="32" height="32" loading="lazy"><figcaption style="font-size:.72rem;color:var(--ink-soft);margin-top:4px">Strict quality control standards</figcaption></figure>
<figure style="margin:0;text-align:center;max-width:110px"><img src="assets/images/badge-gmp.png" alt="GMP certified" width="32" height="32" loading="lazy"><figcaption style="font-size:.72rem;color:var(--ink-soft);margin-top:4px">Good Manufacturing Practice</figcaption></figure>
<figure style="margin:0;text-align:center;max-width:110px"><img src="assets/images/badge-fda.png" alt="FDA-registered facility" width="32" height="32" loading="lazy"><figcaption style="font-size:.72rem;color:var(--ink-soft);margin-top:4px">Produced in a registered facility</figcaption></figure>
<figure style="margin:0;text-align:center;max-width:110px"><img src="assets/images/badge-natural.png" alt="Natural ingredients" width="32" height="32" loading="lazy"><figcaption style="font-size:.72rem;color:var(--ink-soft);margin-top:4px">No artificial fillers or additives</figcaption></figure>
</div>
</div></div></section>
<section class="sec final"><div class="wrap">
<div class="head reveal"><h2>Ready To Start Today?</h2><p>__FINAL_TEXT__</p></div>
<div class="plans">__PLAN_CARD_TEMPLATE__</div>
<div class="reveal" style="margin-top:24px"><a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_CLOSING__</a></div>
</div></section>
<section class="sec alt"><div class="wrap">
<div class="head reveal"><span class="eyebrow">Background reading</span><h2>Research Behind These Ingredients</h2></div>
<p class="refs-note reveal">The references below offer general background on individual nutrients and ingredient categories used in daily wellness products. They are included for context and are not clinical trials of the finished __BRAND__ formula.</p>
<div class="refs-wrap collapsed reveal">
<ul class="refs">
<li>Dietary Supplements and Daily Nutrition — Nutrition Science Overview</li>
<li>Understanding Ingredient Labels — Consumer Science Review</li>
<li>Antioxidants and Everyday Cellular Health — Nutrition Research</li>
<li>Daily Routines and Long-Term Wellness — Behavioral Science Review</li>
<li>Manufacturing Standards in Dietary Supplements — Industry Overview</li>
<li>Botanical Extracts in Modern Wellness Formulas — Research Overview</li>
<li>Micronutrients and Everyday Vitality — Nutritional Review</li>
<li>Serving Consistency and Habit Formation — Behavioral Research</li>
<li>Quality Testing in Supplement Manufacturing — Industry Review</li>
<li>Plant-Based Compounds in Daily Wellness — Nutrition Research</li>
<li>Healthy Aging and Everyday Nutrition — Wellness Research</li>
<li>Reading Clinical Research as a Consumer — Science Literacy Overview</li>
</ul>
</div>
<button class="refs-more" type="button">Show More</button>
</div></section>
<footer><div class="wrap">
<p><a href="index.html">Home</a> · <a href="what-is-product.html">What Is __BRAND__</a> · <a href="how-it-works.html">How It Works</a> · <a href="ingredients.html">Ingredients</a> · <a href="benefits.html">Benefits</a> · <a href="reviews.html">Reviews</a> · <a href="faq.html">FAQs</a> · <a href="blog/index.html">Blog</a></p>
<p><a href="terms.html">Terms of Use</a> · <a href="privacy-policy.html">Privacy Policy</a> · <a href="disclaimer.html">Disclaimer</a> · <a href="refund-policy.html">Refund Policy</a> · <a href="about.html">About Us</a> · <a href="contact.html">Contact Us</a></p>
<p class="fnote">© __YEAR__ __BRAND__ · __CATEGORY__ · This site is an independent review site. Always check the official product page for the latest pricing and terms.</p>
</div></footer>
<script>
(function(){
var rows=document.querySelectorAll('.faq-row');
rows.forEach(function(r,i){if(i===0)r.classList.add('open');var b=r.querySelector('.faq-btn');if(b){b.addEventListener('click',function(){r.classList.toggle('open');});}});
var toggle=document.querySelector('.nav-toggle'),links=document.querySelector('.nav-links');
if(toggle&&links){toggle.addEventListener('click',function(){links.classList.toggle('open');});}
var moreBtn=document.querySelector('.refs-more'),refsWrap=document.querySelector('.refs-wrap');
if(moreBtn&&refsWrap){moreBtn.addEventListener('click',function(){refsWrap.classList.remove('collapsed');moreBtn.style.display='none';});}
if('IntersectionObserver' in window){
 var io=new IntersectionObserver(function(entries){entries.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{threshold:.15});
 document.querySelectorAll('.reveal').forEach(function(el){io.observe(el);});
}else{
 document.querySelectorAll('.reveal').forEach(function(el){el.classList.add('in');});
}
})();
</script>
</body>
</html>
