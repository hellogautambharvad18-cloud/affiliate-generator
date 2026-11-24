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
.wrap{max-width:1160px;margin:0 auto;padding:0 24px}
/* Strip + nav */
.plx-strip{background:var(--surface-alt);color:var(--ink-soft);font-size:13px;padding:9px 0;display:flex;gap:26px;justify-content:center;flex-wrap:wrap;text-align:center;letter-spacing:.03em;border-bottom:1px solid var(--line)}
.plx-strip b{color:var(--gold)}
nav.navbar{position:sticky;top:0;z-index:200;background:rgba(18,15,12,.92);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
nav.navbar .wrap{display:flex;align-items:center;gap:24px;padding:16px 24px}
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
/* Hero */
header.hero{padding:52px 0 14px;background:radial-gradient(1000px 440px at 88% -12%,var(--surface-alt) 0%,transparent 60%),var(--bg)}
.hero .wrap{display:grid;grid-template-columns:1.1fr .9fr;gap:50px;align-items:start}
.plx-pill{display:inline-block;background:transparent;color:var(--gold);font-weight:600;font-size:.76rem;letter-spacing:.14em;text-transform:uppercase;padding:7px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.hero h1{font-size:2.5rem;margin:18px 0 4px;letter-spacing:-.01em}
.hero h1 em{font-style:normal;color:var(--gold)}
.plx-answer{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:20px 22px;margin:18px 0}
.plx-answer .tag{display:inline-block;color:var(--gold);font-size:11px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;margin-bottom:9px}
.plx-answer p{margin:0;color:var(--ink-soft);font-size:.98rem}
.plx-facts{display:flex;flex-wrap:wrap;gap:9px;margin:16px 0}
.plx-facts li{list-style:none;background:var(--surface);border:1px solid var(--line);border-radius:999px;padding:7px 16px;font-size:13px;font-weight:500;color:var(--ink);letter-spacing:.02em}
.hero-checks{display:grid;gap:10px;margin:18px 0 24px;font-weight:500;font-size:.95rem}
.hero-checks div{display:flex;gap:10px;align-items:flex-start;color:var(--ink-soft)}
.hero-checks div:before{content:"✓";flex:none;width:19px;height:19px;border:1px solid var(--gold);color:var(--gold);font-size:.62rem;font-weight:800;display:flex;align-items:center;justify-content:center;margin-top:1px}
.hero-cta-row{display:flex;gap:14px;align-items:center;flex-wrap:wrap;margin-bottom:8px}
.hero-media{display:flex;justify-content:center}
.plx-hero-card{background:var(--surface);border:1px solid var(--line);padding:30px;width:100%;max-width:380px;box-shadow:var(--shadow);text-align:center}
.plx-hero-card img{max-width:250px;margin:0 auto 14px}
.plx-hero-card .plx-facts{justify-content:center}
/* Section head */
.sec{padding:74px 0}
.sec.alt{background:var(--surface-alt)}
.head{max-width:700px;margin:0 auto 40px;text-align:center}
.eyebrow{display:inline-block;color:var(--gold);font-weight:600;font-size:.74rem;letter-spacing:.16em;text-transform:uppercase;margin-bottom:12px}
.head h2{font-size:2rem;margin:0 0 12px}
.head p{color:var(--ink-soft);font-size:1.02rem;margin:0}
.grid{display:grid;gap:20px}
.g2{grid-template-columns:repeat(2,minmax(0,1fr))}
.g3{grid-template-columns:repeat(3,minmax(0,1fr))}
.reveal{opacity:0;transform:translateY(14px);transition:opacity .5s ease,transform .5s ease}
.reveal.in{opacity:1;transform:none}
@media(prefers-reduced-motion:reduce){.reveal{opacity:1;transform:none;transition:none}}
/* Shared card markup (from build_native_page's default card builders) */
.card,.pcard,.ing-card,.rev-card,.step-card{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:28px}
.card h4,.ing-card h4,.step-card h4{margin:0 0 8px;font-size:1.05rem;font-family:'Cinzel',serif;font-weight:600}
.card p,.ing-card p,.step-card p,.rev-card p{color:var(--ink-soft);margin:0;font-size:.93rem}
.ing-card{display:flex;gap:16px;border-top:2px solid var(--gold)}
.ing-num,.step-num{flex:none;width:36px;height:36px;border:1px solid var(--gold);display:flex;align-items:center;justify-content:center;font-family:'Cinzel',serif;font-weight:700;font-size:.9rem;color:var(--gold);background:transparent}
.step-card{border-top:2px solid var(--gold)}
.step-card .step-num{margin-bottom:14px}
.pcard{text-align:left}
.pcard .num{font-family:'Cinzel',serif;font-size:1.3rem;color:var(--gold);font-weight:700;display:block;margin-bottom:6px}
.rev-card .rev-head{display:flex;gap:12px;align-items:center;margin-bottom:9px}
.rev-card .rev-head img,.rev-card .rev-head>div{width:44px;height:44px;border-radius:50%;object-fit:cover}
.rev-name{font-weight:600}
.rev-sub{font-size:.78rem;color:var(--ink-soft)}
.rev-stars{color:var(--gold);font-size:1rem;letter-spacing:.1em;margin-bottom:8px}
/* Trust strip */
section.trust{padding:22px 0;background:var(--surface);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
section.trust .wrap{display:flex;gap:30px;justify-content:center;flex-wrap:wrap;align-items:center}
section.trust .t-item{display:flex;align-items:center;gap:9px;font-weight:500;font-size:.85rem;color:var(--ink-soft);letter-spacing:.02em}
section.trust img{width:32px;height:32px;object-fit:contain;filter:brightness(1.25) sepia(.3)}
/* Callout reused by Quick Facts auto-box */
.plx-callout{background:var(--surface);border-left:2px solid var(--gold);border-radius:0;padding:20px 22px;font-weight:400;color:var(--ink)}
.plx-chips{display:flex;gap:10px;flex-wrap:wrap;margin:20px 0}
.plx-chips span{background:transparent;border:1px solid var(--line);border-radius:999px;padding:7px 16px;font-weight:500;font-size:.78rem;color:var(--ink-soft);letter-spacing:.02em}
/* Benefits feature block */
.feature{display:grid;grid-template-columns:.85fr 1.15fr;gap:44px;align-items:center;margin-bottom:44px}
.feature img{border-radius:var(--radius);box-shadow:var(--shadow)}
.feature h3{font-size:1.4rem;margin:0 0 12px}
.feature p{color:var(--ink-soft)}
/* Formula Profile — original distinctive component: 3-ring radial donut chart */
.plx-profile{background:var(--surface);border:1px solid var(--line);padding:40px 28px;display:grid;grid-template-columns:auto 1fr;gap:40px;align-items:center}
.plx-donut{position:relative;width:180px;height:180px;margin:0 auto}
.plx-donut svg{width:100%;height:100%;transform:rotate(-90deg)}
.plx-donut circle{fill:none;stroke-width:9}
.plx-donut .trk{stroke:var(--surface-alt)}
.plx-legend{display:flex;flex-direction:column;gap:14px}
.plx-legend-row{display:flex;align-items:center;gap:12px}
.plx-legend-row i{width:11px;height:11px;flex:none;border-radius:50%}
.plx-legend-row b{font-weight:600;font-size:.95rem;color:var(--ink);display:block}
.plx-legend-row span{font-size:.8rem;color:var(--ink-soft)}
.plx-profile-cap{grid-column:1/-1;text-align:center;font-size:.8rem;color:var(--ink-soft);opacity:.85;font-style:italic;margin-top:4px}
/* Pricing */
.plans{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:22px;align-items:stretch}
.plan{position:relative;background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:32px 24px;text-align:center;display:flex;flex-direction:column}
.plan.top{border:1px solid var(--gold);box-shadow:var(--shadow);transform:translateY(-8px)}
.plan-badge{position:absolute;top:-13px;left:50%;transform:translateX(-50%);background:var(--gold);color:#120F0C;border-radius:999px;padding:6px 16px;font-weight:700;font-size:.72rem;letter-spacing:.04em;text-transform:uppercase;white-space:nowrap}
.plan img{max-width:160px;margin:4px auto 14px}
.plan-ttl{font-size:1.15rem}
.plan-sub{font-weight:500;color:var(--ink-soft);font-size:.82rem}
.plan-price{font-size:2rem;margin:14px 0 4px;font-family:'Cinzel',serif;font-weight:700;color:var(--gold)}
.plan-price small{font-size:.78rem;color:var(--ink-soft);font-weight:500}
.plan-tot,.plan-ship{font-weight:500;color:var(--ink-soft);font-size:.84rem}
.plan-ship{color:var(--gold)}
.plan ul{list-style:none;padding:0;margin:16px 0;text-align:left}
.plan ul li{padding:6px 0 6px 22px;position:relative;font-weight:400;font-size:.88rem;color:var(--ink-soft)}
.plan ul li:before{content:"✓";position:absolute;left:0;color:var(--gold);font-weight:800}
.plan .btn{margin-top:auto;width:100%}
/* Guarantee */
.plx-guarantee{background:var(--surface);border:1px solid var(--line);padding:42px;text-align:center}
.plx-guarantee img{max-width:130px;margin:0 auto;filter:brightness(1.2) sepia(.2)}
/* FAQ accordion */
.faq-row{border:1px solid var(--line);margin-bottom:10px;background:var(--surface);overflow:hidden}
.faq-btn{width:100%;text-align:left;background:transparent;border:0;padding:18px 22px;font-family:'Jost',sans-serif;font-size:1rem;font-weight:600;cursor:pointer;display:flex;justify-content:space-between;gap:16px;align-items:center;color:var(--ink)}
.faq-btn:after{content:"+";font-size:1.25rem;font-weight:400;color:var(--gold);transition:transform .2s ease}
.faq-row.open .faq-btn:after{transform:rotate(45deg)}
.faq-body{display:none;padding:0 22px 18px;color:var(--ink-soft)}
.faq-row.open .faq-body{display:block}
/* Compare */
.compare{width:100%;border-collapse:collapse;background:var(--surface);border:1px solid var(--line)}
.compare th,.compare td{padding:14px 16px;text-align:left;border-bottom:1px solid var(--line);font-weight:400;font-size:.9rem;color:var(--ink)}
.compare th{background:var(--surface-alt);font-family:'Cinzel',serif;font-size:.84rem;font-weight:600}
.compare td:first-child{font-weight:600}
.compare .yes{color:var(--gold);font-weight:700}
.compare .no{color:#8A7768;font-weight:700}
/* References */
.refs{columns:2;column-gap:40px}
.refs li{font-size:.86rem;color:var(--ink-soft);margin-bottom:10px;break-inside:avoid}
.refs-note{font-size:.84rem;color:var(--ink-soft);text-align:center;max-width:720px;margin:0 auto 26px}
.refs-wrap.collapsed .refs li:nth-child(n+7){display:none}
.refs-more{display:block;text-align:center;margin-top:18px;background:transparent;border:1px solid var(--line);border-radius:999px;padding:9px 20px;font-weight:600;font-size:.86rem;cursor:pointer;color:var(--ink)}
/* Final CTA — contrasting ivory panel against the dark body */
section.final{text-align:center;background:linear-gradient(160deg,#F3ECE0,#E7DAC0);border-radius:0;margin:0 24px;padding:4px}
section.final .wrap{padding:58px 24px}
section.final .head h2{color:#120F0C}
section.final .head p{color:#5A4D37;max-width:620px;margin:0 auto}
section.final .plan{background:rgba(18,15,12,.04);border-color:rgba(18,15,12,.14)}
section.final .plan-ttl{color:#120F0C}
section.final .plan-price{color:#8A6A1F}
section.final .plan-sub,section.final .plan-tot{color:#5A4D37}
footer{background:var(--surface-alt);border-top:1px solid var(--line);padding:42px 0;text-align:center;color:var(--ink-soft)}
footer a{color:var(--ink-soft);font-weight:500;text-decoration:none;margin:0 8px;font-size:.86rem}
footer a:hover{color:var(--gold)}
footer .fnote{font-size:.76rem;margin-top:10px;opacity:.75}
.auto-sticky-cta{background:var(--surface)!important;border-top:1px solid var(--line)!important}
.auto-sticky-cta-btn{background:var(--gold)!important;color:#120F0C!important;border-radius:4px!important}
@media(max-width:900px){.hero .wrap{grid-template-columns:1fr}.hero-media{order:-1}.hero h1{font-size:2.1rem}.g3,.g2,.plans,.feature,.plx-profile{grid-template-columns:1fr}.plan.top{transform:none}.feature img{max-width:340px;margin:0 auto}.refs{columns:1}}
@media(max-width:760px){.nav-links{position:fixed;top:64px;left:0;right:0;background:var(--bg);flex-direction:column;align-items:flex-start;padding:18px 24px;gap:16px;display:none;border-bottom:1px solid var(--line)}.nav-links.open{display:flex}.nav-toggle{display:block}}
</style>
</head>
<body>
<div class="plx-strip"><span><b>__FACT3_NUM__ __FACT3_LABEL__</b></span><span>Made In USA</span><span>GMP-Certified Facility</span></div>
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
<div>
<span class="plx-pill">__PILL_TEXT__</span>
<h1>__HERO_H1__</h1>
<div class="plx-answer reveal"><span class="tag">In Short</span><p>__HERO_DESC__</p></div>
<ul class="plx-facts reveal">
<li>__FACT1_NUM__ __FACT1_LABEL__</li>
<li>__FACT2_NUM__ Per Day</li>
<li>__FACT3_NUM__ __FACT3_LABEL__</li>
</ul>
<div class="hero-checks"><div>__CHECK1__</div><div>__CHECK2__</div><div>__CHECK3__</div></div>
<div class="hero-cta-row">
<a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_HERO__</a>
<a class="btn btn-big btn-ghost" href="#how-it-works">See How It Works</a>
</div>
</div>
<div class="hero-media">
<div class="plx-hero-card reveal">
<img id="hero-img" src="assets/images/hero.png" alt="__BRAND__ __CATEGORY__ supplement bottle" width="250" height="250" fetchpriority="high">
<ul class="plx-facts"><li>★ 4.8 / 5</li><li>__REVIEW_COUNT__ reviews</li></ul>
</div>
</div>
</div></header>
<section class="trust"><div class="wrap">
<div class="t-item"><img src="assets/images/badge-usa.png" alt="Made in USA" width="32" height="32" loading="lazy"> <span>Made in USA<small style="display:block;font-weight:400;opacity:.8">Manufactured under strict quality control standards.</small></span></div>
<div class="t-item"><img src="assets/images/badge-gmp.png" alt="GMP certified" width="32" height="32" loading="lazy"> <span>GMP Certified<small style="display:block;font-weight:400;opacity:.8">Made under Good Manufacturing Practice procedures.</small></span></div>
<div class="t-item"><img src="assets/images/badge-fda.png" alt="FDA-registered facility" width="32" height="32" loading="lazy"> <span>FDA-Registered Facility<small style="display:block;font-weight:400;opacity:.8">Produced in an FDA-registered facility.</small></span></div>
<div class="t-item"><img src="assets/images/badge-natural.png" alt="Natural ingredients" width="32" height="32" loading="lazy"> <span>100% Natural<small style="display:block;font-weight:400;opacity:.8">No artificial fillers or synthetic additives.</small></span></div>
</div></section>
<section class="sec alt" id="pricing"><div class="wrap">
<div class="head reveal"><span class="eyebrow">Choose your package</span><h2>Pick The __BRAND__ Package That Fits You</h2><p>__PRICING_NOTE__</p></div>
<div class="plans">__PLAN_CARD_TEMPLATE__</div>
<p class="reveal" style="text-align:center;font-weight:500;margin-top:22px;color:var(--ink-soft)">Lowest price: __PRICE_LOW__ per bottle · Highest listed: __PRICE_HIGH__ per bottle</p>
</div></section>
<section class="sec" id="what-is"><div class="wrap">
<div class="head reveal"><span class="eyebrow">What is __BRAND__?</span><h2>A Straightforward Answer</h2></div>
<p class="reveal" style="font-size:1.05rem;max-width:760px;margin:0 auto 18px;text-align:center;color:var(--ink-soft)">__WHATIS_P1__</p>
<div class="plx-callout reveal" style="max-width:760px;margin:0 auto">__WHATIS_CALLOUT__</div>
<div class="plx-chips reveal" style="justify-content:center"><span>__CHIP1__</span><span>__CHIP2__</span><span>__CHIP3__</span><span>__CHIP4__</span></div>
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
<ul class="reveal" style="max-width:720px;margin:30px auto 0;font-weight:500;line-height:2;list-style:none;padding:0">__BAL_PROS_TEMPLATE__</ul>
</div></section>
<section class="sec" id="how-it-works"><div class="wrap">
<div class="head reveal"><span class="eyebrow">How it works</span><h2>From Bottle To Daily Habit</h2><p>__HIW_INTRO__</p></div>
<div class="grid g2">__HIW_CARD_TEMPLATE__</div>
<div class="reveal" style="text-align:center;margin-top:32px"><a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_AFTER_HIW__</a></div>
</div></section>
<section class="sec alt"><div class="wrap">
<div class="head reveal"><span class="eyebrow">At a glance</span><h2>The __BRAND__ Formula Profile</h2><p>A quick visual summary of what's behind the label.</p></div>
<div class="plx-profile reveal">
<div class="plx-donut"><svg viewBox="0 0 160 160">
<circle class="trk" cx="80" cy="80" r="70"></circle>
<circle cx="80" cy="80" r="70" stroke="var(--gold)" stroke-dasharray="440" stroke-dashoffset="40" stroke-linecap="round"></circle>
<circle class="trk" cx="80" cy="80" r="52" stroke-width="9"></circle>
<circle cx="80" cy="80" r="52" stroke="var(--primary)" stroke-width="9" stroke-dasharray="327" stroke-dashoffset="55" stroke-linecap="round"></circle>
<circle class="trk" cx="80" cy="80" r="34" stroke-width="9"></circle>
<circle cx="80" cy="80" r="34" stroke="var(--ink-soft)" stroke-width="9" stroke-dasharray="214" stroke-dashoffset="20" stroke-linecap="round"></circle>
</svg></div>
<div class="plx-legend">
<div class="plx-legend-row"><i style="background:var(--gold)"></i><div><b>Ingredient Transparency</b><span>Every ingredient named on the label, no proprietary blend.</span></div></div>
<div class="plx-legend-row"><i style="background:var(--primary)"></i><div><b>Manufacturing Standard</b><span>Made in a GMP-certified, FDA-registered facility.</span></div></div>
<div class="plx-legend-row"><i style="background:var(--ink-soft)"></i><div><b>Guarantee Coverage</b><span>Backed by a __FACT3_NUM__ money-back __FACT3_LABEL__.</span></div></div>
</div>
<p class="plx-profile-cap">Illustrative summary — see the Ingredients section below and the official order page for full details.</p>
</div>
</div></section>
<section class="sec" id="ingredients"><div class="wrap">
<div class="head reveal"><span class="eyebrow">Inside every serving</span><h2>__ING_HEADING__</h2><p>Every ingredient, explained plainly. Serving: __SERVING_DAILY__ · Per bottle: __SERVING_PER_BOTTLE__.</p></div>
<div class="grid g3">__ING_CARD_TEMPLATE__</div>
<div class="reveal" style="text-align:center;margin-top:30px"><a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_AFTER_INGREDIENTS__</a></div>
</div></section>
<section class="sec alt" id="pricing-again"><div class="wrap">
<div class="head reveal"><span class="eyebrow">Still deciding?</span><h2>Get __BRAND__ Today</h2><p>Current package pricing, while supplies last.</p></div>
<div class="plans">__PLAN_CARD_TEMPLATE__</div>
<div class="reveal" style="text-align:center;margin-top:22px;font-weight:500;color:var(--ink-soft)"><a href="#reviews">Read Reviews</a> &nbsp;|&nbsp; <a href="#faq">View FAQs</a></div>
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
<section class="sec alt"><div class="wrap"><div class="plx-guarantee reveal">
<img src="assets/images/guarantee.png" alt="60-day money-back guarantee" loading="lazy">
<h2 style="font-size:1.65rem;margin:14px 0">__FACT3_NUM__ Money-Back __FACT3_LABEL__</h2>
<p style="color:var(--ink-soft);max-width:640px;margin:0 auto 20px">__GUARANTEE_TEXT__</p>
<div style="display:flex;gap:26px;justify-content:center;flex-wrap:wrap;margin-top:8px">
<figure style="margin:0;text-align:center;max-width:110px"><img src="assets/images/badge-usa.png" alt="Made in USA" width="32" height="32" loading="lazy"><figcaption style="font-size:.7rem;color:var(--ink-soft);margin-top:4px">Strict quality control standards</figcaption></figure>
<figure style="margin:0;text-align:center;max-width:110px"><img src="assets/images/badge-gmp.png" alt="GMP certified" width="32" height="32" loading="lazy"><figcaption style="font-size:.7rem;color:var(--ink-soft);margin-top:4px">Good Manufacturing Practice</figcaption></figure>
<figure style="margin:0;text-align:center;max-width:110px"><img src="assets/images/badge-fda.png" alt="FDA-registered facility" width="32" height="32" loading="lazy"><figcaption style="font-size:.7rem;color:var(--ink-soft);margin-top:4px">Produced in a registered facility</figcaption></figure>
<figure style="margin:0;text-align:center;max-width:110px"><img src="assets/images/badge-natural.png" alt="Natural ingredients" width="32" height="32" loading="lazy"><figcaption style="font-size:.7rem;color:var(--ink-soft);margin-top:4px">No artificial fillers or additives</figcaption></figure>
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
