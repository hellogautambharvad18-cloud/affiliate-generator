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
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700&family=Jost:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{--primary:__COLOR_PRIMARY__;--primary-dark:__COLOR_DARK__;--primary-light:__COLOR_LIGHT__;--accent:__COLOR_ACCENT__;--on-primary:__COLOR_ON_PRIMARY__;--gold:#C9A24A;--ink:#F3ECE0;--ink-soft:#C9B98E;--bg:#120F0C;--surface:#1B1713;--surface-alt:#211C16;--line:rgba(243,236,224,.12);--good:#C9A24A;--radius:6px;--shadow:0 20px 50px -20px rgba(201,162,74,.22)}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;font-family:'Jost',system-ui,-apple-system,Segoe UI,Roboto,sans-serif;color:var(--ink);background:var(--bg);line-height:1.68;overflow-x:hidden;font-size:17px}
h1,h2,h3,h4{font-family:'Cinzel',Georgia,serif;font-weight:700;line-height:1.3;margin:0;color:var(--ink);letter-spacing:.01em}
a{color:var(--gold)}
img{max-width:100%;height:auto;display:block}
.wrap{max-width:680px;margin:0 auto;padding:0 24px}
.wrap-wide{max-width:1160px;margin:0 auto;padding:0 24px}
/* Strip + nav */
.plx-strip{background:var(--surface-alt);color:var(--ink-soft);font-size:13px;padding:9px 0;display:flex;gap:26px;justify-content:center;flex-wrap:wrap;text-align:center;letter-spacing:.03em;border-bottom:1px solid var(--line)}
.plx-strip b{color:var(--gold)}
nav.navbar{position:sticky;top:0;z-index:200;background:rgba(18,15,12,.92);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
nav.navbar .wrap-wide{display:flex;align-items:center;gap:24px;padding:16px 24px}
.logo{font-family:'Cinzel',serif;font-weight:700;font-size:1.25rem;text-decoration:none;color:var(--ink);letter-spacing:.03em}
.logo em{font-style:normal;color:var(--gold)}
.nav-links{display:flex;gap:22px;margin-left:auto;flex-wrap:wrap;align-items:center}
.nav-links a{color:var(--ink-soft);text-decoration:none;font-weight:500;font-size:.88rem;letter-spacing:.02em}
.nav-links a:hover{color:var(--gold)}
.nav-toggle{display:none;background:none;border:1px solid var(--line);border-radius:4px;font-size:22px;cursor:pointer;color:var(--ink);padding:4px 10px;min-height:40px;margin-left:auto}
.btn,.btn-big{display:inline-flex;align-items:center;justify-content:center;gap:6px;background:var(--gold);color:#120F0C!important;font-weight:700;text-decoration:none;padding:14px 28px;border-radius:var(--radius);border:0;box-shadow:var(--shadow);font-size:.92rem;letter-spacing:.04em;text-transform:uppercase;line-height:1.2;text-align:center;transition:transform .15s ease;white-space:nowrap}
.btn:hover,.btn-big:hover{transform:translateY(-2px)}
.btn-ghost{background:transparent!important;color:var(--ink)!important;border:1px solid var(--gold)!important;box-shadow:none!important}
.btn-big{padding:16px 32px;font-size:.95rem}
.nav-cta{padding:9px 18px!important;font-size:.78rem;box-shadow:none}
/* Hero — minimal/sparse: short, tight, centered, heavy whitespace */
header.hero{padding:88px 0 56px;text-align:center}
.plx-pill{display:inline-block;background:transparent;color:var(--gold);font-weight:600;font-size:.76rem;letter-spacing:.14em;text-transform:uppercase;padding:7px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.hero h1{font-size:2.4rem;margin:22px 0 14px;letter-spacing:-.01em}
.hero h1 em{font-style:normal;color:var(--gold)}
.hero-lede{color:var(--ink-soft);font-size:1.04rem;max-width:520px;margin:0 auto 26px}
.hero-media{display:flex;justify-content:center;margin-bottom:22px}
.plx-hero-mini{display:flex;align-items:center;gap:14px}
.plx-hero-mini img{max-width:84px}
.plx-chart{width:150px;background:var(--surface);border:1px solid var(--line);border-radius:4px;padding:10px 12px;text-align:left}
.plx-chart span{display:block;font-size:.68rem;color:var(--ink-soft);letter-spacing:.06em;text-transform:uppercase;margin-bottom:4px}
.plx-chart svg{width:100%;height:30px;display:block}
.hero-cta-row{display:flex;gap:14px;align-items:center;justify-content:center;flex-wrap:wrap}
/* Section head — generous vertical rhythm */
.sec{padding:92px 0}
.sec.alt{background:var(--surface-alt)}
.head{max-width:620px;margin:0 auto 36px;text-align:center}
.eyebrow{display:inline-block;color:var(--gold);font-weight:600;font-size:.74rem;letter-spacing:.16em;text-transform:uppercase;margin-bottom:12px}
.head h2{font-size:1.85rem;margin:0 0 12px}
.head p{color:var(--ink-soft);font-size:1.01rem;margin:0}
.grid{display:grid;gap:16px}
.g1{grid-template-columns:1fr;max-width:620px;margin:0 auto}
.reveal{opacity:0;transform:translateY(14px);transition:opacity .5s ease,transform .5s ease}
.reveal.in{opacity:1;transform:none}
@media(prefers-reduced-motion:reduce){.reveal{opacity:1;transform:none;transition:none}}
/* Shared card markup (from build_native_page's default card builders) */
.card,.pcard,.ing-card,.rev-card,.step-card{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:24px}
.card h4,.ing-card h4,.step-card h4{margin:0 0 8px;font-size:1.02rem;font-family:'Cinzel',serif;font-weight:600}
.card p,.ing-card p,.step-card p,.rev-card p{color:var(--ink-soft);margin:0;font-size:.92rem}
.ing-card{display:flex;gap:16px;border-top:2px solid var(--gold)}
.ing-num,.step-num{flex:none;width:34px;height:34px;border:1px solid var(--gold);display:flex;align-items:center;justify-content:center;font-family:'Cinzel',serif;font-weight:700;font-size:.86rem;color:var(--gold);background:transparent}
.step-card{border-top:2px solid var(--gold)}
.step-card .step-num{margin-bottom:12px}
.pcard{text-align:left}
.pcard .num{font-family:'Cinzel',serif;font-size:1.3rem;color:var(--gold);font-weight:700;display:block;margin-bottom:6px}
.rev-card .rev-head{display:flex;gap:12px;align-items:center;margin-bottom:9px}
.rev-card .rev-head img,.rev-card .rev-head>div{width:40px;height:40px;border-radius:50%;object-fit:cover}
.rev-name{font-weight:600}
.rev-sub{font-size:.76rem;color:var(--ink-soft)}
.rev-stars{color:var(--gold);font-size:.95rem;letter-spacing:.1em;margin-bottom:8px}
/* Trust strip — compact single line */
section.trust{padding:16px 0;background:var(--surface);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
section.trust .wrap-wide{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;align-items:center;text-align:center;font-size:.82rem;color:var(--ink-soft);letter-spacing:.02em}
section.trust .t-sep{opacity:.5}
/* Callout reused by Quick Facts auto-box */
.plx-callout{background:var(--surface);border-left:2px solid var(--gold);border-radius:0;padding:20px 22px;font-weight:400;color:var(--ink)}
.plx-chips{display:flex;gap:10px;flex-wrap:wrap;margin:20px 0;justify-content:center}
.plx-chips span{background:transparent;border:1px solid var(--line);border-radius:999px;padding:7px 16px;font-weight:500;font-size:.76rem;color:var(--ink-soft);letter-spacing:.02em}
/* Formula Profile — original distinctive component: 3-ring radial donut chart */
.plx-profile{display:flex;flex-direction:column;align-items:center;gap:26px}
.plx-donut{position:relative;width:160px;height:160px}
.plx-donut svg{width:100%;height:100%;transform:rotate(-90deg)}
.plx-donut circle{fill:none;stroke-width:8}
.plx-donut .trk{stroke:var(--surface-alt)}
.plx-legend{display:flex;flex-direction:column;gap:12px;max-width:500px}
.plx-legend-row{display:flex;align-items:center;gap:12px}
.plx-legend-row i{width:10px;height:10px;flex:none;border-radius:50%}
.plx-legend-row b{font-weight:600;font-size:.92rem;color:var(--ink);display:block}
.plx-legend-row span{font-size:.78rem;color:var(--ink-soft)}
.plx-profile-cap{text-align:center;font-size:.78rem;color:var(--ink-soft);opacity:.85;font-style:italic}
/* Pricing — one full presentation only; the repeat lower on the page is a
   slim text order-bar instead, per this design's minimal/sparse ethos */
.plans{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px;align-items:stretch;max-width:1160px;margin:0 auto}
.plan{position:relative;background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:28px 22px;text-align:center;display:flex;flex-direction:column}
.plan.top{border:1px solid var(--gold);box-shadow:var(--shadow);transform:translateY(-6px)}
.plan-badge{position:absolute;top:-13px;left:50%;transform:translateX(-50%);background:var(--gold);color:#120F0C;border-radius:999px;padding:6px 16px;font-weight:700;font-size:.72rem;letter-spacing:.04em;text-transform:uppercase;white-space:nowrap}
.plan img{max-width:140px;margin:4px auto 12px}
.plan-ttl{font-size:1.08rem}
.plan-sub{font-weight:500;color:var(--ink-soft);font-size:.8rem}
.plan-price{font-size:1.85rem;margin:12px 0 4px;font-family:'Cinzel',serif;font-weight:700;color:var(--gold)}
.plan-price small{font-size:.76rem;color:var(--ink-soft);font-weight:500}
.plan-tot,.plan-ship{font-weight:500;color:var(--ink-soft);font-size:.82rem}
.plan-ship{color:var(--gold)}
.plan ul{list-style:none;padding:0;margin:14px 0;text-align:left}
.plan ul li{padding:5px 0 5px 22px;position:relative;font-weight:400;font-size:.86rem;color:var(--ink-soft)}
.plan ul li:before{content:"✓";position:absolute;left:0;color:var(--gold);font-weight:800}
.plan .btn{margin-top:auto;width:100%}
.plx-orderbar{display:flex;align-items:center;justify-content:center;gap:18px;flex-wrap:wrap;background:var(--surface);border:1px solid var(--line);padding:16px 22px;max-width:1160px;margin:0 auto}
.plx-orderbar span{font-size:.92rem;color:var(--ink-soft)}
.plx-orderbar b{color:var(--gold)}
/* Guarantee */
.plx-guarantee{background:var(--surface);border:1px solid var(--line);padding:40px;text-align:center}
.plx-guarantee img{max-width:120px;margin:0 auto;filter:brightness(1.2) sepia(.2)}
/* FAQ accordion */
.faq-row{border:1px solid var(--line);margin-bottom:10px;background:var(--surface);overflow:hidden}
.faq-btn{width:100%;text-align:left;background:transparent;border:0;padding:16px 20px;font-family:'Jost',sans-serif;font-size:.96rem;font-weight:600;cursor:pointer;display:flex;justify-content:space-between;gap:16px;align-items:center;color:var(--ink)}
.faq-btn:after{content:"+";font-size:1.2rem;font-weight:400;color:var(--gold);transition:transform .2s ease}
.faq-row.open .faq-btn:after{transform:rotate(45deg)}
.faq-body{display:none;padding:0 20px 16px;color:var(--ink-soft)}
.faq-row.open .faq-body{display:block}
/* Compare */
.compare{width:100%;border-collapse:collapse;background:var(--surface);border:1px solid var(--line)}
.compare th,.compare td{padding:12px 14px;text-align:left;border-bottom:1px solid var(--line);font-weight:400;font-size:.88rem;color:var(--ink)}
.compare th{background:var(--surface-alt);font-family:'Cinzel',serif;font-size:.8rem;font-weight:600}
.compare td:first-child{font-weight:600}
.compare .yes{color:var(--gold);font-weight:700}
.compare .no{color:#8A7768;font-weight:700}
/* References */
.refs{columns:1}
.refs li{font-size:.85rem;color:var(--ink-soft);margin-bottom:10px;break-inside:avoid}
.refs-note{font-size:.83rem;color:var(--ink-soft);text-align:center;margin:0 auto 24px}
.refs-wrap.collapsed .refs li:nth-child(n+6){display:none}
.refs-more{display:block;text-align:center;margin-top:16px;background:transparent;border:1px solid var(--line);border-radius:999px;padding:9px 20px;font-weight:600;font-size:.84rem;cursor:pointer;color:var(--ink)}
/* Final CTA — contrasting ivory panel against the dark body */
section.final{text-align:center;background:linear-gradient(160deg,#F3ECE0,#E7DAC0);border-radius:0;margin:0 24px;padding:4px}
section.final .wrap-wide{padding:56px 24px}
section.final .head h2{color:#120F0C}
section.final .head p{color:#5A4D37;max-width:620px;margin:0 auto}
section.final .plan{background:rgba(18,15,12,.04);border-color:rgba(18,15,12,.14)}
section.final .plan-ttl{color:#120F0C}
section.final .plan-price{color:#8A6A1F}
section.final .plan-sub,section.final .plan-tot{color:#5A4D37}
footer{background:var(--surface-alt);border-top:1px solid var(--line);padding:40px 0;text-align:center;color:var(--ink-soft)}
footer .wrap-wide{max-width:1160px;margin:0 auto;padding:0 24px}
footer a{color:var(--ink-soft);font-weight:500;text-decoration:none;margin:0 8px;font-size:.84rem}
footer a:hover{color:var(--gold)}
footer .fnote{font-size:.74rem;margin-top:10px;opacity:.75}
.auto-sticky-cta{background:var(--surface)!important;border-top:1px solid var(--line)!important}
.auto-sticky-cta-btn{background:var(--gold)!important;color:#120F0C!important;border-radius:4px!important}
@media(max-width:900px){.plans{grid-template-columns:1fr}.plan.top{transform:none}}
@media(max-width:760px){.nav-links{position:fixed;top:64px;left:0;right:0;background:var(--bg);flex-direction:column;align-items:flex-start;padding:18px 24px;gap:16px;display:none;border-bottom:1px solid var(--line)}.nav-links.open{display:flex}.nav-toggle{display:block}}
</style>
</head>
<body>
<div class="plx-strip"><span><b>__FACT3_NUM__ __FACT3_LABEL__</b></span><span>Made In USA</span><span>GMP-Certified Facility</span></div>
<nav class="navbar"><div class="wrap-wide">
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
<span class="plx-pill">__PILL_TEXT__</span>
<h1>__HERO_H1__</h1>
<p class="hero-lede reveal">__WHATIS_CALLOUT__</p>
<div class="hero-media reveal">
<div class="plx-hero-mini">
<img id="hero-img" src="assets/images/hero.png" alt="__BRAND__ __CATEGORY__ supplement bottle" width="84" height="84" fetchpriority="high">
<div class="plx-chart">
<span>Consistency Trend</span>
<svg viewBox="0 0 150 30" preserveAspectRatio="none" aria-hidden="true"><polyline points="0,26 30,20 60,22 90,10 120,12 150,3" fill="none" stroke="var(--gold)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></polyline></svg>
</div>
</div>
</div>
<div class="hero-cta-row">
<a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_HERO__</a>
<a class="btn btn-big btn-ghost" href="#how-it-works">See How It Works</a>
</div>
</div></header>
<section class="trust"><div class="wrap-wide">
<span>Made in USA</span><span class="t-sep">·</span><span>GMP Certified</span><span class="t-sep">·</span><span>FDA-Registered Facility</span><span class="t-sep">·</span><span>100% Natural</span>
</div></section>
<section class="sec" id="what-is"><div class="wrap">
<div class="head reveal"><span class="eyebrow">What is __BRAND__?</span><h2>A Straightforward Answer</h2></div>
<p class="reveal" style="font-size:1.02rem;margin:0 0 18px;text-align:center;color:var(--ink-soft)">__WHATIS_P1__</p>
<div class="plx-callout reveal">__HERO_DESC__</div>
<div class="plx-chips reveal"><span>__CHIP1__</span><span>__CHIP2__</span><span>__CHIP3__</span><span>__CHIP4__</span></div>
<div class="reveal" style="text-align:center;margin-top:26px"><a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_AFTER_WHATIS__</a></div>
</div></section>
<section class="sec alt"><div class="wrap">
<div class="head reveal"><span class="eyebrow">At a glance</span><h2>The __BRAND__ Formula Profile</h2><p>A quick visual summary of what's behind the label.</p></div>
<div class="plx-profile reveal">
<div class="plx-donut"><svg viewBox="0 0 160 160">
<circle class="trk" cx="80" cy="80" r="70"></circle>
<circle cx="80" cy="80" r="70" stroke="var(--gold)" stroke-dasharray="440" stroke-dashoffset="40" stroke-linecap="round"></circle>
<circle class="trk" cx="80" cy="80" r="52" stroke-width="8"></circle>
<circle cx="80" cy="80" r="52" stroke="var(--ink-soft)" stroke-width="8" stroke-dasharray="327" stroke-dashoffset="55" stroke-linecap="round"></circle>
</svg></div>
<div class="plx-legend">
<div class="plx-legend-row"><i style="background:var(--gold)"></i><div><b>Ingredient Transparency</b><span>Every ingredient named on the label, no proprietary blend.</span></div></div>
<div class="plx-legend-row"><i style="background:var(--ink-soft)"></i><div><b>Guarantee Coverage</b><span>Backed by a __FACT3_NUM__ money-back __FACT3_LABEL__.</span></div></div>
</div>
<p class="plx-profile-cap">Illustrative summary — see the Ingredients section below and the official order page for full details.</p>
</div>
</div></section>
<section class="sec" id="pricing"><div class="wrap-wide">
<div class="head reveal"><span class="eyebrow">Choose your package</span><h2>Pick The __BRAND__ Package That Fits You</h2><p>__PRICING_NOTE__</p></div>
<div class="plans">__PLAN_CARD_TEMPLATE__</div>
<p class="reveal" style="text-align:center;font-weight:500;margin-top:20px;color:var(--ink-soft)">Lowest price: __PRICE_LOW__ per bottle · Highest listed: __PRICE_HIGH__ per bottle</p>
</div></section>
<section class="sec alt" id="benefits"><div class="wrap">
<div class="head reveal"><span class="eyebrow">Why people choose it</span><h2>What You Can Expect To Notice</h2><p>Real, everyday support — no overpromising.</p></div>
<div class="grid g1">__BENEFIT_CARD_TEMPLATE__</div>
<a class="btn" style="display:block;max-width:300px;margin:26px auto 0" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_AFTER_BENEFITS__</a>
</div></section>
<section class="sec" id="how-it-works"><div class="wrap">
<div class="head reveal"><span class="eyebrow">How it works</span><h2>From Bottle To Daily Habit</h2><p>__HIW_INTRO__</p></div>
<div class="grid g1">__HIW_CARD_TEMPLATE__</div>
<div class="reveal" style="text-align:center;margin-top:28px"><a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_AFTER_HIW__</a></div>
</div></section>
<section class="sec alt" id="ingredients"><div class="wrap">
<div class="head reveal"><span class="eyebrow">Inside every serving</span><h2>__ING_HEADING__</h2><p>Every ingredient, explained plainly. Serving: __SERVING_DAILY__ · Per bottle: __SERVING_PER_BOTTLE__.</p></div>
<div class="grid g1">__ING_CARD_TEMPLATE__</div>
<div class="reveal" style="text-align:center;margin-top:26px"><a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_AFTER_INGREDIENTS__</a></div>
</div></section>
<div class="sec" style="padding:40px 0"><div class="plx-orderbar reveal wrap-wide">
<span>Ready when you are — from <b>__PRICE_LOW__</b> per bottle.</span>
<a class="btn" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">View Packages</a>
</div></div>
__BONUS_SECTION__
<section class="sec alt" id="reviews"><div class="wrap">
<div class="head reveal"><span class="eyebrow">Verified reviews</span><h2>What Customers Say</h2><p>★★★★★ __REVIEW_COUNT__ reviews and counting.</p></div>
<div class="grid g1">__REVIEW_CARD_TEMPLATE__</div>
<div class="reveal" style="text-align:center;margin-top:26px"><a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_AFTERREVIEWS__</a></div>
</div></section>
<section class="sec" id="compare"><div class="wrap">
<div class="head reveal"><span class="eyebrow">An honest look</span><h2>__BRAND__ vs The Alternatives</h2><p>Decide with the facts in front of you.</p></div>
<table class="compare reveal">
<tr><th></th><th>__BRAND__</th><th>Typical</th><th>Nothing</th></tr>
<tr><td>Ingredients listed individually</td><td class="yes">✓</td><td class="no">✗</td><td class="no">✗</td></tr>
<tr><td>One simple daily serving</td><td class="yes">✓</td><td class="no">✗</td><td class="no">✗</td></tr>
<tr><td>__FACT3_NUM__ money-back __FACT3_LABEL__</td><td class="yes">✓</td><td class="no">✗</td><td class="no">✗</td></tr>
<tr><td>Made in USA, GMP facility</td><td class="yes">✓</td><td class="no">✗</td><td class="no">✗</td></tr>
</table>
</div></section>
<section class="sec alt" id="faq"><div class="wrap">
<div class="head reveal"><span class="eyebrow">Got questions?</span><h2>Frequently Asked Questions</h2></div>
__FAQ_ROW_TEMPLATE__
<div class="reveal" style="text-align:center;margin-top:26px"><a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_AFTERFAQ__</a></div>
</div></section>
<section class="sec"><div class="wrap"><div class="plx-guarantee reveal">
<img src="assets/images/guarantee.png" alt="60-day money-back guarantee" loading="lazy">
<h2 style="font-size:1.5rem;margin:14px 0">__FACT3_NUM__ Money-Back __FACT3_LABEL__</h2>
<p style="color:var(--ink-soft);margin:0 auto 20px">__GUARANTEE_TEXT__</p>
<div style="display:flex;gap:20px;justify-content:center;flex-wrap:wrap;margin-top:8px">
<figure style="margin:0;text-align:center;max-width:100px"><img src="assets/images/badge-usa.png" alt="Made in USA" width="30" height="30" loading="lazy"><figcaption style="font-size:.68rem;color:var(--ink-soft);margin-top:4px">Strict quality control</figcaption></figure>
<figure style="margin:0;text-align:center;max-width:100px"><img src="assets/images/badge-gmp.png" alt="GMP certified" width="30" height="30" loading="lazy"><figcaption style="font-size:.68rem;color:var(--ink-soft);margin-top:4px">GMP practice</figcaption></figure>
<figure style="margin:0;text-align:center;max-width:100px"><img src="assets/images/badge-fda.png" alt="FDA-registered facility" width="30" height="30" loading="lazy"><figcaption style="font-size:.68rem;color:var(--ink-soft);margin-top:4px">FDA-registered</figcaption></figure>
<figure style="margin:0;text-align:center;max-width:100px"><img src="assets/images/badge-natural.png" alt="Natural ingredients" width="30" height="30" loading="lazy"><figcaption style="font-size:.68rem;color:var(--ink-soft);margin-top:4px">No fillers</figcaption></figure>
</div>
</div></div></section>
<section class="sec final"><div class="wrap-wide">
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
<footer><div class="wrap-wide">
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
