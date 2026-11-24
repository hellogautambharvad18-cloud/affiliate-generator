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
.wrap{max-width:1160px;margin:0 auto;padding:0 24px}
/* Strip + nav */
.trc-strip{background:var(--ink);color:#F6E6D6;font-size:13.5px;padding:9px 0;display:flex;gap:26px;justify-content:center;flex-wrap:wrap;text-align:center}
.trc-strip b{color:var(--primary-light)}
nav.navbar{position:sticky;top:0;z-index:200;background:rgba(251,243,234,.93);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
nav.navbar .wrap{display:flex;align-items:center;gap:24px;padding:15px 24px}
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
/* Hero */
header.hero{padding:48px 0 14px;background:radial-gradient(1000px 440px at 88% -12%,var(--surface-alt) 0%,transparent 60%),var(--bg)}
.hero .wrap{display:grid;grid-template-columns:1.1fr .9fr;gap:50px;align-items:start}
.trc-pill{display:inline-block;background:var(--surface-alt);color:var(--primary-dark);font-weight:800;font-size:.78rem;letter-spacing:.03em;text-transform:uppercase;padding:7px 15px;border-radius:999px}
.hero h1{font-size:2.8rem;margin:16px 0 4px;letter-spacing:-.01em}
.hero h1 em{font-style:normal;color:var(--primary-dark)}
.trc-answer{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:20px 22px;margin:18px 0}
.trc-answer .tag{display:inline-block;background:var(--primary-dark);color:var(--on-primary);font-size:11.5px;font-weight:800;letter-spacing:.05em;text-transform:uppercase;padding:4px 10px;border-radius:8px;margin-bottom:9px;font-family:'Nunito Sans',sans-serif}
.trc-answer p{margin:0;color:var(--ink-soft);font-size:1rem}
.trc-facts{display:flex;flex-wrap:wrap;gap:9px;margin:16px 0}
.trc-facts li{list-style:none;background:var(--surface);border:1px solid var(--line);border-radius:999px;padding:7px 15px;font-size:13.5px;font-weight:700;color:var(--ink)}
.hero-checks{display:grid;gap:10px;margin:18px 0 24px;font-weight:700;font-size:.95rem}
.hero-checks div{display:flex;gap:10px;align-items:flex-start;color:var(--ink-soft)}
.hero-checks div:before{content:"✓";flex:none;width:21px;height:21px;border-radius:50%;background:var(--good);color:#fff;font-size:.68rem;font-weight:800;display:flex;align-items:center;justify-content:center;margin-top:1px}
.hero-cta-row{display:flex;gap:14px;align-items:center;flex-wrap:wrap;margin-bottom:8px}
.hero-media{display:flex;justify-content:center}
.trc-hero-card{background:var(--surface-alt);border:1px solid var(--line);border-radius:28px;padding:28px;width:100%;max-width:380px;box-shadow:var(--shadow);text-align:center}
.trc-hero-card img{max-width:260px;margin:0 auto 14px}
.trc-hero-card .trc-facts{justify-content:center}
/* Section head */
.sec{padding:70px 0}
.sec.alt{background:var(--surface-alt)}
.head{max-width:700px;margin:0 auto 38px;text-align:center}
.eyebrow{display:inline-flex;align-items:center;gap:7px;color:var(--primary-dark);font-weight:800;font-size:.75rem;letter-spacing:.09em;text-transform:uppercase;margin-bottom:11px;font-family:'Nunito Sans',sans-serif}
.head h2{font-size:2.2rem;margin:0 0 12px}
.head p{color:var(--ink-soft);font-size:1.02rem;margin:0}
.grid{display:grid;gap:20px}
.g2{grid-template-columns:repeat(2,minmax(0,1fr))}
.g3{grid-template-columns:repeat(3,minmax(0,1fr))}
.reveal{opacity:0;transform:translateY(14px);transition:opacity .5s ease,transform .5s ease}
.reveal.in{opacity:1;transform:none}
@media(prefers-reduced-motion:reduce){.reveal{opacity:1;transform:none;transition:none}}
/* Shared card markup (from build_native_page's default card builders) */
.card,.pcard,.ing-card,.rev-card,.step-card{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:26px;box-shadow:var(--shadow)}
.card h4,.ing-card h4,.step-card h4{margin:0 0 8px;font-size:1.15rem;font-family:'Cormorant Garamond',serif}
.card p,.ing-card p,.step-card p,.rev-card p{color:var(--ink-soft);margin:0;font-size:.94rem}
.ing-card{display:flex;gap:16px;border-left:4px solid var(--good)}
.ing-num,.step-num{flex:none;width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-family:'Cormorant Garamond',serif;font-weight:700;font-size:1.05rem;color:var(--on-primary);background:var(--primary-dark)}
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
section.trust{padding:20px 0;background:var(--surface);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
section.trust .wrap{display:flex;gap:30px;justify-content:center;flex-wrap:wrap;align-items:center}
section.trust .t-item{display:flex;align-items:center;gap:9px;font-weight:700;font-size:.87rem;color:var(--ink-soft)}
section.trust img{width:34px;height:34px;object-fit:contain}
/* Callout reused by Quick Facts auto-box */
.trc-callout{background:var(--surface-alt);border-left:4px solid var(--primary-dark);border-radius:14px;padding:20px 22px;font-weight:600;color:var(--ink)}
.trc-chips{display:flex;gap:10px;flex-wrap:wrap;margin:20px 0}
.trc-chips span{background:var(--surface-alt);border:1px solid var(--line);border-radius:999px;padding:7px 15px;font-weight:700;font-size:.8rem;color:var(--ink)}
/* Benefits feature block */
.feature{display:grid;grid-template-columns:.85fr 1.15fr;gap:44px;align-items:center;margin-bottom:44px}
.feature img{border-radius:var(--radius);box-shadow:var(--shadow)}
.feature h3{font-size:1.6rem;margin:0 0 12px}
.feature p{color:var(--ink-soft)}
/* Sourcing Trail — original distinctive component: dotted path with leaf-shaped origin nodes */
.trc-trail{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:40px 32px}
.trc-trail-path{position:relative;display:flex;justify-content:space-between;gap:12px;padding-top:10px}
.trc-trail-path:before{content:"";position:absolute;top:19px;left:24px;right:24px;height:2px;background:repeating-linear-gradient(90deg,var(--good) 0 8px,transparent 8px 16px)}
.trc-leaf{flex:1;text-align:center;position:relative}
.trc-leaf .dot{width:38px;height:38px;margin:0 auto 12px;border-radius:70% 0 70% 0;background:var(--good);border:3px solid var(--surface);box-shadow:0 0 0 2px var(--good);position:relative;z-index:1}
.trc-leaf b{display:block;font-family:'Cormorant Garamond',serif;font-size:1.1rem;font-weight:700;color:var(--ink)}
.trc-leaf span{display:block;font-size:.78rem;color:var(--ink-soft);margin-top:3px}
.trc-trail-cap{text-align:center;font-size:.8rem;color:var(--ink-soft);opacity:.85;font-style:italic;margin-top:24px}
/* Pricing */
.plans{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:22px;align-items:stretch}
.plan{position:relative;background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:30px 24px;text-align:center;display:flex;flex-direction:column}
.plan.top{border:2px solid var(--primary-dark);box-shadow:var(--shadow);transform:translateY(-8px)}
.plan-badge{position:absolute;top:-14px;left:50%;transform:translateX(-50%);background:var(--primary-dark);color:var(--on-primary);border-radius:999px;padding:6px 16px;font-weight:800;font-size:.75rem;white-space:nowrap;font-family:'Nunito Sans',sans-serif}
.plan img{max-width:160px;margin:4px auto 14px}
.plan-ttl{font-size:1.4rem}
.plan-sub{font-weight:700;color:var(--ink-soft);font-size:.84rem}
.plan-price{font-size:2.2rem;margin:14px 0 4px;font-family:'Cormorant Garamond',serif;font-weight:700}
.plan-price small{font-size:.9rem;color:var(--ink-soft);font-weight:600}
.plan-tot,.plan-ship{font-weight:700;color:var(--ink-soft);font-size:.85rem}
.plan-ship{color:var(--good)}
.plan ul{list-style:none;padding:0;margin:16px 0;text-align:left}
.plan ul li{padding:6px 0 6px 24px;position:relative;font-weight:600;font-size:.89rem;color:var(--ink-soft)}
.plan ul li:before{content:"✓";position:absolute;left:0;color:var(--good);font-weight:800}
.plan .btn{margin-top:auto;width:100%}
/* Guarantee */
.trc-guarantee{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:40px;text-align:center}
.trc-guarantee img{max-width:140px;margin:0 auto}
/* FAQ accordion */
.faq-row{border:1px solid var(--line);border-radius:14px;margin-bottom:12px;background:var(--surface);overflow:hidden}
.faq-btn{width:100%;text-align:left;background:transparent;border:0;padding:18px 20px;font-family:'Cormorant Garamond',serif;font-size:1.15rem;font-weight:700;cursor:pointer;display:flex;justify-content:space-between;gap:16px;align-items:center;color:var(--ink)}
.faq-btn:after{content:"+";font-size:1.3rem;font-weight:700;color:var(--primary-dark);transition:transform .2s ease}
.faq-row.open .faq-btn:after{transform:rotate(45deg)}
.faq-body{display:none;padding:0 20px 18px;color:var(--ink-soft)}
.faq-row.open .faq-body{display:block}
/* Compare */
.compare{width:100%;border-collapse:collapse;background:var(--surface);border:1px solid var(--line);border-radius:16px;overflow:hidden}
.compare th,.compare td{padding:14px 16px;text-align:left;border-bottom:1px solid var(--line);font-weight:600;font-size:.92rem}
.compare th{background:var(--surface-alt);font-family:'Cormorant Garamond',serif;font-size:1.05rem}
.compare td:first-child{font-weight:800}
.compare .yes{color:var(--good);font-weight:800}
.compare .no{color:#B0523F;font-weight:800}
/* References */
.refs{columns:2;column-gap:40px}
.refs li{font-size:.87rem;color:var(--ink-soft);margin-bottom:10px;break-inside:avoid}
.refs-note{font-size:.84rem;color:var(--ink-soft);text-align:center;max-width:720px;margin:0 auto 26px}
.refs-wrap.collapsed .refs li:nth-child(n+7){display:none}
.refs-more{display:block;text-align:center;margin-top:18px;background:transparent;border:1px solid var(--line);border-radius:999px;padding:9px 20px;font-weight:700;font-size:.88rem;cursor:pointer;color:var(--ink)}
/* Final CTA — contrasting deep cocoa panel */
section.final{text-align:center;background:linear-gradient(160deg,#3B2A20,#5B4531);border-radius:28px;margin:0 24px;padding:4px}
section.final .wrap{padding:56px 24px}
section.final .head h2{color:#fff}
section.final .head p{color:#E3CBAE;max-width:620px;margin:0 auto}
section.final .plan{background:rgba(255,255,255,.06);border-color:rgba(255,255,255,.18)}
section.final .plan-ttl,section.final .plan-price{color:#fff}
section.final .plan-sub,section.final .plan-tot{color:#E3CBAE}
footer{background:var(--surface-alt);border-top:1px solid var(--line);padding:40px 0;text-align:center;color:var(--ink-soft)}
footer a{color:var(--ink);font-weight:700;text-decoration:none;margin:0 8px;font-size:.9rem}
footer a:hover{color:var(--primary-dark)}
footer .fnote{font-size:.78rem;margin-top:10px;opacity:.8}
.auto-sticky-cta{background:var(--surface)!important;border-top:1px solid var(--line)!important}
.auto-sticky-cta-btn{background:var(--primary-dark)!important;color:var(--on-primary)!important;border-radius:999px!important}
@media(max-width:900px){.hero .wrap{grid-template-columns:1fr}.hero-media{order:-1}.hero h1{font-size:2.2rem}.g3,.g2,.plans,.feature{grid-template-columns:1fr}.plan.top{transform:none}.feature img{max-width:340px;margin:0 auto}.refs{columns:1}.trc-trail-path{flex-direction:column;gap:22px}.trc-trail-path:before{display:none}}
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
<div>
<span class="trc-pill">__PILL_TEXT__</span>
<h1>__HERO_H1__</h1>
<div class="trc-answer reveal"><span class="tag">In Short</span><p>__HERO_DESC__</p></div>
<ul class="trc-facts reveal">
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
<div class="trc-hero-card reveal">
<img id="hero-img" src="assets/images/hero.png" alt="__BRAND__ __CATEGORY__ supplement bottle" width="260" height="260" fetchpriority="high">
<ul class="trc-facts"><li>★ 4.8 / 5</li><li>__REVIEW_COUNT__ reviews</li></ul>
</div>
</div>
</div></header>
<section class="trust"><div class="wrap">
<div class="t-item"><img src="assets/images/badge-usa.png" alt="Made in USA" width="34" height="34" loading="lazy"> <span>Made in USA<small style="display:block;font-weight:500;opacity:.8">Manufactured under strict quality control standards.</small></span></div>
<div class="t-item"><img src="assets/images/badge-gmp.png" alt="GMP certified" width="34" height="34" loading="lazy"> <span>GMP Certified<small style="display:block;font-weight:500;opacity:.8">Made under Good Manufacturing Practice procedures.</small></span></div>
<div class="t-item"><img src="assets/images/badge-fda.png" alt="FDA-registered facility" width="34" height="34" loading="lazy"> <span>FDA-Registered Facility<small style="display:block;font-weight:500;opacity:.8">Produced in an FDA-registered facility.</small></span></div>
<div class="t-item"><img src="assets/images/badge-natural.png" alt="Natural ingredients" width="34" height="34" loading="lazy"> <span>100% Natural<small style="display:block;font-weight:500;opacity:.8">No artificial fillers or synthetic additives.</small></span></div>
</div></section>
<section class="sec alt" id="pricing"><div class="wrap">
<div class="head reveal"><span class="eyebrow">Choose your package</span><h2>Pick The __BRAND__ Package That Fits You</h2><p>__PRICING_NOTE__</p></div>
<div class="plans">__PLAN_CARD_TEMPLATE__</div>
<p class="reveal" style="text-align:center;font-weight:700;margin-top:22px;color:var(--ink-soft)">Lowest price: __PRICE_LOW__ per bottle · Highest listed: __PRICE_HIGH__ per bottle</p>
</div></section>
<section class="sec" id="what-is"><div class="wrap">
<div class="head reveal"><span class="eyebrow">What is __BRAND__?</span><h2>A Straightforward Answer</h2></div>
<p class="reveal" style="font-size:1.1rem;max-width:760px;margin:0 auto 18px;text-align:center;color:var(--ink-soft)">__WHATIS_P1__</p>
<div class="trc-callout reveal" style="max-width:760px;margin:0 auto">__WHATIS_CALLOUT__</div>
<div class="trc-chips reveal" style="justify-content:center"><span>__CHIP1__</span><span>__CHIP2__</span><span>__CHIP3__</span><span>__CHIP4__</span></div>
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
<ul class="reveal" style="max-width:720px;margin:30px auto 0;font-weight:700;line-height:2;list-style:none;padding:0">__BAL_PROS_TEMPLATE__</ul>
</div></section>
<section class="sec" id="how-it-works"><div class="wrap">
<div class="head reveal"><span class="eyebrow">How it works</span><h2>From Bottle To Daily Habit</h2><p>__HIW_INTRO__</p></div>
<div class="grid g2">__HIW_CARD_TEMPLATE__</div>
<div class="reveal" style="text-align:center;margin-top:32px"><a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_AFTER_HIW__</a></div>
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
<section class="sec" id="ingredients"><div class="wrap">
<div class="head reveal"><span class="eyebrow">Inside every serving</span><h2>__ING_HEADING__</h2><p>Every ingredient, explained plainly. Serving: __SERVING_DAILY__ · Per bottle: __SERVING_PER_BOTTLE__.</p></div>
<div class="grid g3">__ING_CARD_TEMPLATE__</div>
<div class="reveal" style="text-align:center;margin-top:30px"><a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_AFTER_INGREDIENTS__</a></div>
</div></section>
<section class="sec alt" id="pricing-again"><div class="wrap">
<div class="head reveal"><span class="eyebrow">Still deciding?</span><h2>Get __BRAND__ Today</h2><p>Current package pricing, while supplies last.</p></div>
<div class="plans">__PLAN_CARD_TEMPLATE__</div>
<div class="reveal" style="text-align:center;margin-top:22px;font-weight:700;color:var(--ink-soft)"><a href="#reviews">Read Reviews</a> &nbsp;|&nbsp; <a href="#faq">View FAQs</a></div>
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
<section class="sec alt"><div class="wrap"><div class="trc-guarantee reveal">
<img src="assets/images/guarantee.png" alt="60-day money-back guarantee" loading="lazy">
<h2 style="font-size:1.9rem;margin:14px 0">__FACT3_NUM__ Money-Back __FACT3_LABEL__</h2>
<p style="color:var(--ink-soft);max-width:640px;margin:0 auto 20px">__GUARANTEE_TEXT__</p>
<div style="display:flex;gap:26px;justify-content:center;flex-wrap:wrap;margin-top:8px">
<figure style="margin:0;text-align:center;max-width:110px"><img src="assets/images/badge-usa.png" alt="Made in USA" width="34" height="34" loading="lazy"><figcaption style="font-size:.72rem;color:var(--ink-soft);margin-top:4px">Strict quality control standards</figcaption></figure>
<figure style="margin:0;text-align:center;max-width:110px"><img src="assets/images/badge-gmp.png" alt="GMP certified" width="34" height="34" loading="lazy"><figcaption style="font-size:.72rem;color:var(--ink-soft);margin-top:4px">Good Manufacturing Practice</figcaption></figure>
<figure style="margin:0;text-align:center;max-width:110px"><img src="assets/images/badge-fda.png" alt="FDA-registered facility" width="34" height="34" loading="lazy"><figcaption style="font-size:.72rem;color:var(--ink-soft);margin-top:4px">Produced in a registered facility</figcaption></figure>
<figure style="margin:0;text-align:center;max-width:110px"><img src="assets/images/badge-natural.png" alt="Natural ingredients" width="34" height="34" loading="lazy"><figcaption style="font-size:.72rem;color:var(--ink-soft);margin-top:4px">No artificial fillers or additives</figcaption></figure>
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
