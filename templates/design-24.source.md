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
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,500;0,600;0,700;1,500&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
:root{--primary:__COLOR_PRIMARY__;--primary-dark:__COLOR_DARK__;--primary-light:__COLOR_LIGHT__;--accent:__COLOR_ACCENT__;--on-primary:__COLOR_ON_PRIMARY__;--bg:#fbf9f5;--surface:#fff;--surface-alt:#f5f1e8;--ink:#20232b;--muted:#6c7280;--line:#e9e3d6;--radius:22px;--shadow:0 20px 44px -24px rgba(32,35,43,.22)}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;font-family:'Plus Jakarta Sans',system-ui,-apple-system,Segoe UI,Roboto,sans-serif;color:var(--ink);background:var(--bg);line-height:1.65;overflow-x:hidden;font-size:17px}
h1,h2,h3,h4{font-family:'Lora',Georgia,serif;font-weight:600;line-height:1.22;margin:0;color:var(--ink)}
a{color:var(--primary)}
img{max-width:100%;height:auto;display:block}
.wrap{max-width:1160px;margin:0 auto;padding:0 24px}
.lx-tag{color:var(--primary)}
/* Nav */
nav.navbar{position:sticky;top:0;z-index:200;background:rgba(251,249,245,.92);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
nav.navbar .wrap{display:flex;align-items:center;gap:24px;padding:16px 24px}
.logo{font-family:'Lora',serif;font-weight:700;font-size:1.32rem;text-decoration:none;color:var(--ink);display:flex;align-items:center;gap:9px}
.logo .dot{width:9px;height:9px;border-radius:50%;background:var(--primary);display:inline-block}
.nav-links{display:flex;gap:22px;margin-left:auto;flex-wrap:wrap;align-items:center}
.nav-links a{color:var(--muted);text-decoration:none;font-weight:600;font-size:.92rem}
.nav-links a:hover{color:var(--ink)}
.nav-toggle{display:none;background:none;border:1px solid var(--line);border-radius:8px;font-size:22px;cursor:pointer;color:var(--ink);padding:4px 10px;min-height:40px;margin-left:auto}
.btn,.btn-big{display:inline-flex;align-items:center;justify-content:center;gap:6px;background:var(--primary);color:var(--on-primary)!important;font-weight:700;text-decoration:none;padding:14px 26px;border-radius:999px;border:0;box-shadow:var(--shadow);font-size:1rem;line-height:1.2;text-align:center;transition:transform .15s ease;white-space:nowrap}
.btn:hover,.btn-big:hover{transform:translateY(-2px)}
.btn-ghost{background:transparent!important;color:var(--ink)!important;border:1.5px solid var(--line)!important;box-shadow:none!important}
.btn-big{padding:17px 32px;font-size:1.05rem}
.nav-cta{padding:10px 18px!important;font-size:.88rem;box-shadow:none}
/* Hero */
header.hero{padding:60px 0 54px}
.hero .wrap{display:grid;grid-template-columns:1.05fr .95fr;gap:52px;align-items:center}
.pill{display:inline-flex;align-items:center;gap:8px;background:var(--surface-alt);border:1px solid var(--line);border-radius:999px;padding:7px 16px;font-weight:700;font-size:.78rem;color:var(--primary-dark);letter-spacing:.02em}
.hero h1{font-size:2.7rem;margin:18px 0 16px;letter-spacing:-.01em}
.hero-sub{font-size:1.1rem;color:var(--muted);margin:0 0 24px;max-width:48ch}
.hero-checks{display:grid;gap:11px;margin:0 0 28px;font-weight:600;font-size:.96rem}
.hero-checks div{display:flex;gap:10px;align-items:flex-start}
.hero-checks div:before{content:"✓";flex:none;width:22px;height:22px;border-radius:50%;background:var(--primary-light);color:var(--primary-dark);font-size:.72rem;font-weight:800;display:flex;align-items:center;justify-content:center;margin-top:1px}
.hero-cta-row{display:flex;gap:14px;align-items:center;flex-wrap:wrap;margin-bottom:18px}
.hero-stats{display:flex;gap:28px;flex-wrap:wrap;margin-top:8px;padding-top:18px;border-top:1px solid var(--line)}
.hero-stats div{display:flex;flex-direction:column}
.hero-stats b{font-family:'Lora',serif;font-size:1.4rem;color:var(--ink)}
.hero-stats span{font-size:.74rem;color:var(--muted);text-transform:uppercase;letter-spacing:.06em}
.hero-media{position:relative;display:flex;justify-content:center}
.hero-media .frame{position:relative;background:var(--surface-alt);border-radius:28px;padding:30px;width:100%;max-width:400px;display:flex;justify-content:center}
.hero-media img{max-width:280px;border-radius:14px}
.hero-float{position:absolute;background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:10px 14px;font-size:.82rem;font-weight:700;color:var(--ink);box-shadow:var(--shadow);display:flex;align-items:center;gap:7px}
.hero-float.top{top:8px;right:-14px}
.hero-float.bottom{bottom:16px;left:-20px}
/* Sections */
.sec{padding:72px 0}
.sec.alt{background:var(--surface-alt)}
.head{max-width:700px;margin:0 auto 40px;text-align:center}
.eyebrow{display:inline-flex;align-items:center;gap:7px;color:var(--primary-dark);font-weight:700;font-size:.76rem;letter-spacing:.09em;text-transform:uppercase;margin-bottom:12px}
.head h2{font-size:2.05rem;margin:0 0 12px}
.head p{color:var(--muted);font-size:1.03rem;margin:0}
.grid{display:grid;gap:22px}
.g2{grid-template-columns:repeat(2,minmax(0,1fr))}
.g3{grid-template-columns:repeat(3,minmax(0,1fr))}
.reveal{opacity:0;transform:translateY(14px);transition:opacity .5s ease,transform .5s ease}
.reveal.in{opacity:1;transform:none}
@media(prefers-reduced-motion:reduce){.reveal{opacity:1;transform:none;transition:none}}
/* Shared card markup (from build_native_page's default card builders) */
.card,.pcard,.ing-card,.rev-card,.step-card{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:28px;box-shadow:var(--shadow)}
.card h4,.ing-card h4,.step-card h4{margin:0 0 8px;font-size:1.1rem}
.card p,.ing-card p,.step-card p,.rev-card p{color:var(--muted);margin:0;font-size:.95rem}
.ing-card{display:flex;gap:16px}
.ing-num,.step-num{flex:none;width:44px;height:44px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-family:'Lora',serif;font-weight:700;font-size:1rem;color:var(--on-primary);background:var(--primary)}
.step-card .step-num{margin-bottom:16px}
.pcard{text-align:left}
.pcard .num{font-family:'Lora',serif;font-size:1.5rem;color:var(--primary);font-weight:700;display:block;margin-bottom:6px}
.rev-card .rev-head{display:flex;gap:12px;align-items:center;margin-bottom:10px}
.rev-card .rev-head img,.rev-card .rev-head>div{width:46px;height:46px;border-radius:50%;object-fit:cover}
.rev-name{font-weight:700}
.rev-sub{font-size:.78rem;color:var(--muted)}
.rev-stars{color:var(--primary);font-size:1rem;letter-spacing:.1em;margin-bottom:8px}
/* Trust strip */
section.trust{padding:22px 0;background:var(--surface);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
section.trust .wrap{display:flex;gap:32px;justify-content:center;flex-wrap:wrap;align-items:center}
section.trust .t-item{display:flex;align-items:center;gap:9px;font-weight:700;font-size:.88rem;color:var(--muted)}
section.trust img{width:36px;height:36px;object-fit:contain}
/* Info strip (3 icon callouts) */
.info-strip{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:22px}
.info-strip .ic-item{text-align:center;padding:10px}
.info-strip .ic-badge{width:52px;height:52px;border-radius:50%;background:var(--primary-light);color:var(--primary-dark);display:flex;align-items:center;justify-content:center;margin:0 auto 14px;font-size:1.4rem}
.info-strip h4{font-size:1.02rem;margin:0 0 6px}
.info-strip p{color:var(--muted);font-size:.9rem;margin:0}
/* Chips / callout */
.chips{display:flex;gap:10px;flex-wrap:wrap;margin:22px 0}
.chips span{background:var(--surface-alt);border:1px solid var(--line);border-radius:999px;padding:7px 15px;font-weight:700;font-size:.82rem;color:var(--ink)}
.callout{background:var(--surface-alt);border-left:3px solid var(--primary);border-radius:14px;padding:20px 22px;font-weight:500;color:var(--ink)}
/* Benefits feature block */
.feature{display:grid;grid-template-columns:.85fr 1.15fr;gap:46px;align-items:center;margin-bottom:46px}
.feature img{border-radius:var(--radius);box-shadow:var(--shadow)}
.feature h3{font-size:1.5rem;margin:0 0 12px}
.feature p{color:var(--muted)}
/* Shipping banner */
.ship-banner{display:flex;align-items:center;gap:20px;background:var(--primary-dark);color:#fff;border-radius:var(--radius);padding:26px 30px}
.ship-banner .ic{flex:none;width:52px;height:52px;border-radius:50%;background:rgba(255,255,255,.18);display:flex;align-items:center;justify-content:center;font-size:1.5rem}
.ship-banner h3{color:#fff;font-size:1.2rem;margin:0 0 4px}
.ship-banner p{margin:0;opacity:.88;font-size:.94rem}
/* Pricing */
.plans{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px;align-items:stretch}
.plan{position:relative;background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:30px 24px;text-align:center;display:flex;flex-direction:column;box-shadow:var(--shadow)}
.plan.top{border:2px solid var(--primary);transform:scale(1.03)}
.plan-badge{position:absolute;top:-14px;left:50%;transform:translateX(-50%);background:var(--primary);color:var(--on-primary);border-radius:999px;padding:6px 16px;font-weight:800;font-size:.76rem;white-space:nowrap}
.plan img{max-width:160px;margin:4px auto 14px}
.plan-ttl{font-size:1.3rem}
.plan-sub{font-weight:600;color:var(--muted);font-size:.85rem}
.plan-price{font-size:2.2rem;margin:14px 0 4px;font-family:'Lora',serif;font-weight:700}
.plan-price small{font-size:.92rem;color:var(--muted);font-weight:600}
.plan-tot,.plan-ship{font-weight:600;color:var(--muted);font-size:.86rem}
.plan ul{list-style:none;padding:0;margin:16px 0;text-align:left}
.plan ul li{padding:6px 0 6px 24px;position:relative;font-weight:500;font-size:.9rem}
.plan ul li:before{content:"✓";position:absolute;left:0;color:var(--primary);font-weight:800}
.plan .btn{margin-top:auto;width:100%}
.quick-links{text-align:center;margin-top:26px;font-weight:600;font-size:.92rem;color:var(--muted)}
.quick-links a{color:var(--primary-dark)}
/* Guarantee */
.guarantee{background:var(--surface-alt);border-radius:var(--radius);padding:44px;text-align:center}
.guarantee img{max-width:150px;margin:0 auto}
/* FAQ */
.faq-row{border:1px solid var(--line);border-radius:16px;margin-bottom:12px;background:var(--surface);overflow:hidden}
.faq-btn{width:100%;text-align:left;background:transparent;border:0;padding:18px 20px;font-family:'Lora',serif;font-size:1.02rem;font-weight:600;cursor:pointer;display:flex;justify-content:space-between;gap:16px;align-items:center;color:var(--ink)}
.faq-btn:after{content:"+";font-size:1.4rem;font-weight:700;color:var(--primary)}
.faq-row.open .faq-btn:after{content:"–"}
.faq-body{display:none;padding:0 20px 18px;color:var(--muted)}
.faq-row.open .faq-body{display:block}
/* Compare */
.compare{width:100%;border-collapse:collapse;background:var(--surface);border:1px solid var(--line);border-radius:16px;overflow:hidden}
.compare th,.compare td{padding:14px 16px;text-align:left;border-bottom:1px solid var(--line);font-weight:500;font-size:.92rem}
.compare th{background:var(--surface-alt);font-family:'Lora',serif;font-size:.92rem}
.compare td:first-child{font-weight:700}
.compare .yes{color:var(--primary-dark);font-weight:700}
.compare .no{color:#b4523f;font-weight:700}
/* References */
.refs{columns:2;column-gap:40px}
.refs li{font-size:.88rem;color:var(--muted);margin-bottom:10px;break-inside:avoid}
.refs-note{font-size:.84rem;color:var(--muted);text-align:center;max-width:720px;margin:0 auto 26px}
.refs-wrap.collapsed .refs li:nth-child(n+7){display:none}
.refs-more{display:block;text-align:center;margin-top:18px;background:transparent;border:1px solid var(--line);border-radius:999px;padding:9px 20px;font-weight:700;font-size:.88rem;cursor:pointer;color:var(--ink)}
/* Final CTA */
section.final{text-align:center}
section.final .head p{max-width:620px;margin:0 auto}
footer{background:var(--surface-alt);border-top:1px solid var(--line);padding:40px 0;text-align:center;color:var(--muted)}
footer a{color:var(--ink);font-weight:600;text-decoration:none;margin:0 8px;font-size:.9rem}
footer a:hover{color:var(--primary)}
footer .fnote{font-size:.78rem;margin-top:10px;opacity:.8}
.auto-sticky-cta{background:var(--surface)!important;border-top:1px solid var(--line)!important}
.auto-sticky-cta-btn{background:var(--primary)!important;color:var(--on-primary)!important;border-radius:999px!important}
@media(max-width:900px){.hero .wrap{grid-template-columns:1fr}.hero-media{order:-1}.hero h1{font-size:2.1rem}.g3,.g2,.plans,.info-strip{grid-template-columns:1fr}.plan.top{transform:none}.feature{grid-template-columns:1fr}.feature img{max-width:340px;margin:0 auto}.refs{columns:1}}
@media(max-width:760px){.nav-links{position:fixed;top:64px;left:0;right:0;background:var(--bg);flex-direction:column;align-items:flex-start;padding:18px 24px;gap:16px;display:none;border-bottom:1px solid var(--line)}.nav-links.open{display:flex}.nav-toggle{display:block}}
</style>
</head>
<body>
<nav class="navbar"><div class="wrap">
<a class="logo" href="index.html"><span class="dot"></span>__BRAND__</a>
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
<div>
<span class="pill">__PILL_TEXT__</span>
<h1>__HERO_H1__</h1>
<p class="hero-sub">__HERO_DESC__</p>
<div class="hero-checks"><div>__CHECK1__</div><div>__CHECK2__</div><div>__CHECK3__</div></div>
<div class="hero-cta-row">
<a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_HERO__</a>
<a class="btn btn-big btn-ghost" href="#how-it-works">See How It Works</a>
</div>
<div class="hero-stats">
<div><b>__FACT1_NUM__</b><span>__FACT1_LABEL__</span></div>
<div><b>__FACT2_NUM__</b><span>__FACT2_LABEL__</span></div>
<div><b>__FACT3_NUM__</b><span>__FACT3_LABEL__</span></div>
<div><b>__FACT4_NUM__</b><span>__FACT4_LABEL__</span></div>
</div>
</div>
<div class="hero-media">
<div class="frame reveal">
<img id="hero-img" src="assets/images/hero.png" alt="__BRAND__ __CATEGORY__ supplement bottle" width="280" height="280" fetchpriority="high">
</div>
<div class="hero-float top">★ 4.8 / 5 rating</div>
<div class="hero-float bottom">✓ __REVIEW_COUNT__ reviews</div>
</div>
</div></header>
<section class="trust"><div class="wrap">
<div class="t-item"><img src="assets/images/badge-usa.png" alt="Made in USA" width="36" height="36" loading="lazy"> <span>Made in USA<small style="display:block;font-weight:500;opacity:.8">Manufactured under strict quality control standards.</small></span></div>
<div class="t-item"><img src="assets/images/badge-gmp.png" alt="GMP certified" width="36" height="36" loading="lazy"> <span>GMP Certified<small style="display:block;font-weight:500;opacity:.8">Made under Good Manufacturing Practice procedures.</small></span></div>
<div class="t-item"><img src="assets/images/badge-fda.png" alt="FDA-registered facility" width="36" height="36" loading="lazy"> <span>FDA-Registered Facility<small style="display:block;font-weight:500;opacity:.8">Produced in an FDA-registered facility.</small></span></div>
<div class="t-item"><img src="assets/images/badge-natural.png" alt="Natural ingredients" width="36" height="36" loading="lazy"> <span>100% Natural<small style="display:block;font-weight:500;opacity:.8">No artificial fillers or synthetic additives.</small></span></div>
</div></section>
<section class="sec"><div class="wrap">
<div class="info-strip">
<div class="ic-item reveal"><div class="ic-badge">①</div><h4>One Simple Daily Step</h4><p>A single serving, easy to fold into any routine.</p></div>
<div class="ic-item reveal"><div class="ic-badge">②</div><h4>__FACT1_NUM__ __FACT1_LABEL__</h4><p>Every one listed individually — nothing hidden behind a blend.</p></div>
<div class="ic-item reveal"><div class="ic-badge">③</div><h4>__FACT3_NUM__ __FACT3_LABEL__</h4><p>Try it without pressure, with a full refund window.</p></div>
</div>
</div></section>
<section class="sec alt" id="pricing"><div class="wrap">
<div class="head reveal"><span class="eyebrow">Choose your package</span><h2>Pick The __BRAND__ Package That Fits You</h2><p>__PRICING_NOTE__</p></div>
<div class="plans">__PLAN_CARD_TEMPLATE__</div>
<p class="reveal" style="text-align:center;font-weight:600;margin-top:22px;color:var(--muted)">Lowest price: __PRICE_LOW__ per bottle · Highest listed: __PRICE_HIGH__ per bottle</p>
</div></section>
<section class="sec" id="what-is"><div class="wrap">
<div class="head reveal"><span class="eyebrow">What is __BRAND__?</span><h2>A Straightforward Answer</h2></div>
<p class="reveal" style="font-size:1.08rem;max-width:760px;margin:0 auto 18px;text-align:center;color:var(--muted)">__WHATIS_P1__</p>
<div class="callout reveal" style="max-width:760px;margin:0 auto">__WHATIS_CALLOUT__</div>
<div class="chips reveal" style="justify-content:center"><span>__CHIP1__</span><span>__CHIP2__</span><span>__CHIP3__</span><span>__CHIP4__</span></div>
<div class="reveal" style="text-align:center;margin-top:28px"><a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_AFTER_WHATIS__</a></div>
</div></section>
<section class="sec alt" id="benefits"><div class="wrap">
<div class="feature reveal">
<img src="assets/images/feature-shot.png" alt="Daily __BRAND__ routine" width="420" height="340" loading="lazy">
<div>
<h3>Daily Support, Built Into Your Routine</h3>
<p>__HIW_INTRO__</p>
<a class="btn" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_AFTER_BENEFITS__</a>
</div>
</div>
<div class="head reveal"><span class="eyebrow">Why people choose it</span><h2>What You Can Expect To Notice</h2><p>Real, everyday support — no overpromising.</p></div>
<div class="grid g3">__BENEFIT_CARD_TEMPLATE__</div>
<ul class="reveal" style="max-width:720px;margin:30px auto 0;font-weight:600;line-height:2;list-style:none;padding:0">__BAL_PROS_TEMPLATE__</ul>
</div></section>
<section class="sec" id="how-it-works"><div class="wrap">
<div class="head reveal"><span class="eyebrow">How it works</span><h2>From Bottle To Daily Habit</h2><p>__HIW_INTRO__</p></div>
<div class="grid g2">__HIW_CARD_TEMPLATE__</div>
<div class="reveal" style="text-align:center;margin-top:32px"><a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_AFTER_HIW__</a></div>
</div></section>
<section class="sec alt"><div class="wrap">
<div class="ship-banner reveal">
<span class="ic">🚚</span>
<div><h3>Free U.S. Shipping On Multi-Bottle Orders</h3><p>Every larger __BRAND__ bundle ships free, so stocking up costs less per bottle.</p></div>
</div>
</div></section>
<section class="sec" id="ingredients"><div class="wrap">
<div class="head reveal"><span class="eyebrow">Inside every serving</span><h2>__ING_HEADING__</h2><p>Every ingredient, explained plainly. Serving: __SERVING_DAILY__ · Per bottle: __SERVING_PER_BOTTLE__.</p></div>
<div class="grid g3" id="ing-grid">__ING_CARD_TEMPLATE__</div>
<div class="reveal" style="text-align:center;margin-top:30px"><a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_AFTER_INGREDIENTS__</a></div>
</div></section>
<section class="sec alt" id="pricing-again"><div class="wrap">
<div class="head reveal"><span class="eyebrow">Still deciding?</span><h2>Get __BRAND__ Today</h2><p>Current package pricing, while supplies last.</p></div>
<div class="plans">__PLAN_CARD_TEMPLATE__</div>
<div class="quick-links reveal"><a href="#reviews">Read Reviews</a> &nbsp;|&nbsp; <a href="#faq">View FAQs</a></div>
</div></section>
__BONUS_SECTION__
<section class="sec" id="reviews"><div class="wrap">
<div class="head reveal"><span class="eyebrow">Verified reviews</span><h2>What Customers Say</h2><p>★★★★★ __REVIEW_COUNT__ reviews and counting.</p></div>
<div class="grid g3">__REVIEW_CARD_TEMPLATE__</div>
<div class="reveal" style="text-align:center;margin-top:30px"><a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_AFTERREVIEWS__</a></div>
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
<div class="reveal" style="text-align:center;margin-top:30px"><a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_AFTERFAQ__</a></div>
</div></section>
<section class="sec alt"><div class="wrap"><div class="guarantee reveal">
<img src="assets/images/guarantee.png" alt="60-day money-back guarantee" loading="lazy">
<h2 style="font-size:1.8rem;margin:14px 0">__FACT3_NUM__ Money-Back __FACT3_LABEL__</h2>
<p style="color:var(--muted);max-width:640px;margin:0 auto 20px">__GUARANTEE_TEXT__</p>
<div style="display:flex;gap:26px;justify-content:center;flex-wrap:wrap">
<figure style="margin:0;text-align:center;max-width:110px"><img src="assets/images/badge-usa.png" alt="Made in USA" width="34" height="34" loading="lazy"><figcaption style="font-size:.72rem;color:var(--muted);margin-top:4px">Strict quality control standards</figcaption></figure>
<figure style="margin:0;text-align:center;max-width:110px"><img src="assets/images/badge-gmp.png" alt="GMP certified" width="34" height="34" loading="lazy"><figcaption style="font-size:.72rem;color:var(--muted);margin-top:4px">Good Manufacturing Practice</figcaption></figure>
<figure style="margin:0;text-align:center;max-width:110px"><img src="assets/images/badge-fda.png" alt="FDA-registered facility" width="34" height="34" loading="lazy"><figcaption style="font-size:.72rem;color:var(--muted);margin-top:4px">Produced in a registered facility</figcaption></figure>
<figure style="margin:0;text-align:center;max-width:110px"><img src="assets/images/badge-natural.png" alt="Natural ingredients" width="34" height="34" loading="lazy"><figcaption style="font-size:.72rem;color:var(--muted);margin-top:4px">No artificial fillers or additives</figcaption></figure>
</div>
</div></div></section>
<section class="sec final"><div class="wrap">
<div class="head reveal"><h2>Ready To Start Today?</h2><p>__FINAL_TEXT__</p></div>
<div class="plans">__PLAN_CARD_TEMPLATE__</div>
<div class="reveal" style="margin-top:28px"><a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_CLOSING__</a></div>
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
