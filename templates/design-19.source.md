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
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Source+Sans+3:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
:root{--primary:__COLOR_PRIMARY__;--primary-dark:__COLOR_DARK__;--primary-light:__COLOR_LIGHT__;--accent:__COLOR_ACCENT__;--on-primary:__COLOR_ON_PRIMARY__;--cta:#b8690a;--cta-dark:#8f5207;--cta-soft:#fdf3df;--ink:#2a1e0f;--muted:#6b5a45;--border:#ead9b4;--cream:#fdf9f0;--paper:#fffdf7;--gold:#cf8a1d;--gold-soft:#f6e0b4;--sage:#6b7a2e;--green:#3f7a3a}
*{box-sizing:border-box}
html{scroll-behavior:smooth;font-size:20px}
body{margin:0;font-family:'Source Sans 3','Inter',system-ui,-apple-system,Segoe UI,Roboto,sans-serif;color:var(--ink);background:var(--cream);line-height:1.65}
h1,h2,h3,h4,.logo,.plan-price,.plan-ttl{font-family:'DM Serif Display',Georgia,serif;line-height:1.15;letter-spacing:0;font-weight:400}
a{color:var(--cta)}
img{max-width:100%;height:auto}
.wrap{max-width:1120px;margin:0 auto;padding:0 24px}
.container{max-width:1120px;margin:0 auto;padding:0 24px}
/* Top announcement bar */
.topbar{background:linear-gradient(90deg,#8f5207,#b8690a,#cf8a1d);color:#fff;text-align:center;padding:10px 16px;font-weight:700;font-size:.92rem;letter-spacing:.02em}
.topbar strong{color:#ffe9b8}
.topbar #d19-count{color:#ffe9b8;font-variant-numeric:tabular-nums;font-weight:800}
/* Honeycomb divider */
.honeycomb{height:26px;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='52' height='26' viewBox='0 0 52 26'%3E%3Cpath d='M13 1 L25 8 L25 18 L13 25 L1 18 L1 8 Z' fill='none' stroke='%23eab55a' stroke-width='1.4'/%3E%3Cpath d='M39 1 L51 8 L51 18 L39 25 L27 18 L27 8 Z' fill='%23f6e0b4' stroke='%23eab55a' stroke-width='1.4'/%3E%3C/svg%3E");background-repeat:repeat-x;background-position:center;opacity:.9}
/* Nav */
nav.site{position:sticky;top:0;z-index:100;background:rgba(255,253,247,.97);border-bottom:1px solid var(--border);box-shadow:0 2px 14px rgba(120,72,0,.06)}
nav.site .wrap{display:flex;align-items:center;gap:20px;padding-top:12px;padding-bottom:12px}
.logo{font-size:1.5rem;text-decoration:none;color:var(--ink)}
.logo span{color:var(--cta)}
.nav-links{display:flex;gap:18px;margin-left:auto;flex-wrap:wrap}
.nav-links a,.nav-link-c{color:var(--ink);text-decoration:none;font-weight:600;font-size:.93rem}
.nav-links a:hover{color:var(--cta);text-decoration:underline}
.btn,.btn-cta,.btn-big{display:inline-block;background:var(--cta);color:#fff!important;font-weight:800;text-decoration:none;padding:15px 28px;border-radius:999px;border:0;box-shadow:0 6px 18px rgba(184,105,10,.35);font-size:1.02rem;line-height:1.25;text-align:center;transition:transform .15s ease,box-shadow .15s ease,background .15s ease}
.btn:hover,.btn-cta:hover,.btn-big:hover{background:var(--cta-dark);transform:translateY(-2px);box-shadow:0 10px 24px rgba(184,105,10,.4)}
.btn-ghost{display:inline-block;background:transparent;color:var(--cta)!important;font-weight:800;text-decoration:none;padding:15px 28px;border-radius:999px;border:2px solid var(--cta);font-size:1.02rem;line-height:1.25;text-align:center;transition:background .15s ease}
.btn-ghost:hover{background:var(--cta-soft)}
.nav-cta{padding:10px 20px!important;font-size:.93rem}
/* Hero */
header.hero{background:var(--paper);padding:56px 0 60px;border-bottom:1px solid var(--border)}
.hero .wrap{display:grid;grid-template-columns:1.05fr .95fr;gap:48px;align-items:start}
.pill{display:inline-block;background:var(--cta-soft);border:1px solid var(--gold);border-radius:999px;padding:6px 16px;font-weight:700;font-size:.83rem;color:var(--cta-dark);letter-spacing:.02em}
.hero h1{font-size:2.9rem;margin:18px 0 14px}
.hero h1 em{font-style:italic;color:var(--cta)}
.hero-sub{font-size:1.16rem;color:var(--muted);margin:0 0 22px}
.hero-checks{display:grid;gap:9px;margin:0 0 24px;font-weight:600}
.hero-checks div:before{content:"✓ ";color:var(--sage);font-weight:800}
.hero-cta-row{display:flex;gap:16px;align-items:center;flex-wrap:wrap}
.hero-price{font-weight:800;font-size:1.2rem}
.hero-price small{display:block;font-size:.85rem;color:var(--muted);font-weight:600}
.hero-note{font-size:.88rem;color:var(--muted);margin-top:12px}
.hero-media{position:relative}
.hero-media img{width:100%;border-radius:24px;box-shadow:0 18px 40px rgba(120,72,0,.16);background:#fff}
.hero-badge{position:absolute;top:-14px;right:14px;background:var(--gold);color:#fff;border-radius:999px;padding:9px 16px;font-weight:800;box-shadow:0 6px 16px rgba(184,105,10,.35);transform:rotate(2deg);font-size:.9rem}
/* Quick facts table */
.quick-facts{margin-top:26px;border:1px solid var(--border);border-radius:16px;overflow:hidden;background:#fff}
.quick-facts .qf-title{background:var(--cta-soft);padding:10px 18px;font-weight:800;color:var(--cta-dark);font-size:.85rem;letter-spacing:.08em;text-transform:uppercase}
.quick-facts dl{margin:0;display:grid;grid-template-columns:1fr 1fr}
.quick-facts dl div{padding:11px 18px;border-top:1px solid var(--border)}
.quick-facts dt{font-size:.78rem;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:.05em}
.quick-facts dd{margin:2px 0 0;font-weight:700}
/* Trust badges */
.badges{display:flex;gap:12px;flex-wrap:wrap;margin-top:18px;align-items:center}
.badges img{width:90px;height:90px;object-fit:contain;background:#fff;border:1px solid var(--border);border-radius:14px;padding:4px;box-shadow:0 4px 12px rgba(120,72,0,.08)}
.hero-facts{display:flex;gap:14px;flex-wrap:wrap;margin-top:20px}
.hero-facts div{background:#fff;border:1px solid var(--border);border-radius:14px;padding:10px 16px;text-align:center;min-width:104px;box-shadow:0 4px 12px rgba(120,72,0,.06)}
.hero-facts b{display:block;font-family:'DM Serif Display',serif;font-size:1.3rem;color:var(--cta-dark)}
.hero-facts span{font-size:.78rem;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:.05em}
/* Sections */
.sec{padding:64px 0}
.sec.soft{background:var(--paper);border-top:1px solid var(--border);border-bottom:1px solid var(--border)}
.sec.amber{background:linear-gradient(180deg,#fdf3df,#fbefd2)}
.sec.amber h2{color:var(--ink)}
.head{max-width:760px;margin:0 auto 36px;text-align:center}
.head h2{font-size:2.3rem;margin:0 0 12px}
.head h2:after{content:"";display:block;width:64px;height:4px;background:var(--gold);margin:16px auto 0;border-radius:2px}
.head p{color:var(--muted);font-size:1.08rem;margin:0}
.eyebrow{display:inline-block;background:var(--cta-soft);border:1px solid var(--gold);color:var(--cta-dark);padding:4px 14px;border-radius:999px;font-weight:800;font-size:.78rem;letter-spacing:.08em;text-transform:uppercase;margin-bottom:12px}
.grid{display:grid;gap:20px}
.g1{grid-template-columns:1fr}
.g2{grid-template-columns:repeat(2,minmax(0,1fr))}
.g3{grid-template-columns:repeat(3,minmax(0,1fr))}
.g4{grid-template-columns:repeat(4,minmax(0,1fr))}
/* Cards - shared markup from build_native_page */
.card,.pcard,.ing-card,.rev-card,.trust-card,.science-col,.step-card{background:#fff;border:1px solid var(--border);border-radius:20px;padding:24px;box-shadow:0 8px 24px rgba(120,72,0,.07)}
.card h4,.pcard h4,.ing-card h4,.step-card h4{margin:0 0 8px;font-size:1.25rem}
.card p,.pcard p,.ing-card p,.step-card p,.rev-card p{color:var(--muted);margin:0}
.pcard .num{font-family:'DM Serif Display',serif;font-size:2rem;color:var(--cta-dark)}
.ing-card{display:flex;gap:16px}
.ing-num,.ing-num-circle{flex:none;width:52px;height:56px;clip-path:polygon(50% 0,100% 25%,100% 75%,50% 100%,0 75%,0 25%);background:linear-gradient(180deg,#cf8a1d,#b8690a);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:1.05rem}
.step-card .step-num{width:48px;height:48px;clip-path:polygon(50% 0,100% 25%,100% 75%,50% 100%,0 75%,0 25%);background:var(--cta);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:1.2rem;margin-bottom:14px}
.rev-card .rev-head{display:flex;gap:12px;align-items:center;margin-bottom:10px}
.rev-card .rev-head img{width:46px;height:46px;border-radius:50%;object-fit:cover;border:2px solid var(--gold-soft)}
.rev-name{font-weight:800}
.rev-sub{font-size:.82rem;color:var(--muted)}
.rev-stars{color:#f59e0b;font-size:1.1rem;letter-spacing:.1em;margin-bottom:8px}
/* Trust strip */
section.trust{padding:22px 0;background:var(--paper);border-bottom:1px solid var(--border)}
section.trust .wrap{display:flex;gap:28px;justify-content:center;flex-wrap:wrap;font-weight:700;text-align:center;color:var(--muted)}
section.trust span:before{content:"★ ";color:var(--gold)}
/* What-is / chips */
.chips{display:flex;gap:10px;flex-wrap:wrap;margin:20px 0}
.chips span{background:var(--cta-soft);border:1px solid var(--gold);border-radius:999px;padding:6px 14px;font-weight:700;font-size:.86rem;color:var(--cta-dark)}
.callout,.note{background:var(--cta-soft);border:1px solid var(--gold);border-left:6px solid var(--gold);border-radius:14px;padding:18px 20px;font-weight:600}
/* Pricing */
.plans{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:22px;align-items:stretch}
.plan{position:relative;background:#fff;border:1px solid var(--border);border-radius:22px;padding:28px 22px;text-align:center;box-shadow:0 10px 28px rgba(120,72,0,.08);display:flex;flex-direction:column}
.plan.top{border:2px solid var(--cta);transform:scale(1.03);box-shadow:0 16px 36px rgba(184,105,10,.22)}
.plan-badge{position:absolute;top:-14px;left:50%;transform:translateX(-50%);background:var(--cta);color:#fff;border-radius:999px;padding:6px 14px;font-weight:800;font-size:.82rem;white-space:nowrap;box-shadow:0 6px 14px rgba(184,105,10,.3)}
.plan img{max-width:220px;margin:10px auto;display:block}
.plan-ttl{font-size:1.5rem}
.plan-sub{font-weight:600;color:var(--muted)}
.plan-price{font-size:2.5rem;margin:12px 0 4px;color:var(--cta-dark)}
.plan-price small{font-size:1rem}
.plan-tot,.plan-ship{font-weight:700}
.plan ul{list-style:none;padding:0;margin:16px 0;text-align:left}
.plan ul li{padding:6px 0 6px 28px;position:relative;font-weight:600}
.plan ul li:before{content:"✓";position:absolute;left:0;color:var(--sage);font-weight:800}
.plan .btn{margin-top:auto}
/* Guarantee */
.guarantee{background:#fff;border:1px solid var(--border);border-radius:22px;padding:32px;box-shadow:0 10px 28px rgba(120,72,0,.08);text-align:center}
.guarantee img{max-width:180px}
/* FAQ */
.faq-row{border:1px solid var(--border);border-radius:16px;margin-bottom:12px;background:#fff;overflow:hidden;box-shadow:0 4px 14px rgba(120,72,0,.05)}
.faq-btn{width:100%;text-align:left;background:#fff;border:0;padding:18px 20px;font-family:'DM Serif Display',serif;font-size:1.15rem;cursor:pointer;display:flex;justify-content:space-between;gap:16px;align-items:center;color:var(--ink)}
.faq-btn:after{content:"+";font-size:1.6rem;font-weight:700;color:var(--cta)}
.faq-row.open .faq-btn:after{content:"–"}
.faq-body{display:none;padding:0 20px 18px;color:var(--muted)}
.faq-row.open .faq-body{display:block}
/* Final CTA */
section.final{background:linear-gradient(180deg,#fdf3df,#f6e0b4);text-align:center}
section.final h2{font-size:2.4rem}
section.final p{color:var(--muted);max-width:680px;margin:0 auto 24px}
footer{background:var(--paper);border-top:1px solid var(--border);padding:36px 0;text-align:center;color:var(--muted)}
footer a{color:var(--ink);font-weight:700;text-decoration:none;margin:0 8px}
footer a:hover{color:var(--cta);text-decoration:underline}
/* Sticky CTA injected by app.py */
.auto-sticky-cta-btn{background:var(--cta)!important;border-radius:999px!important;box-shadow:0 8px 20px rgba(184,105,10,.4)!important}
/* Comparison table */
.compare{width:100%;border-collapse:collapse;background:#fff;border:1px solid var(--border);border-radius:16px;overflow:hidden;box-shadow:0 8px 24px rgba(120,72,0,.07)}
.compare th,.compare td{padding:14px 16px;text-align:left;border-bottom:1px solid var(--border);font-weight:600}
.compare th{background:var(--cta);color:#fff;font-family:'DM Serif Display',serif;font-size:1rem}
.compare td:first-child{font-weight:800}
.compare .yes{color:var(--sage);font-weight:800}
.compare .no{color:#b3261e;font-weight:800}
@media(max-width:900px){.hero .wrap{grid-template-columns:1fr}.hero h1{font-size:2.2rem}.g3,.g4,.plans{grid-template-columns:1fr}.g2{grid-template-columns:1fr}.plan.top{transform:none}.nav-links{display:none}.quick-facts dl{grid-template-columns:1fr}}
</style>
</head>
<body>
<div class="topbar">🍯 <strong>Limited-time offer</strong> — Today only: from <strong>__PRICE_FROM__</strong> per bottle &nbsp;·&nbsp; Offer ends in <span id="d19-count">23:59:59</span></div>
<nav class="site"><div class="wrap">
<a class="logo" href="index.html">__BRAND__<span>.</span></a>
<div class="nav-links">
<a href="what-is-product.html">What Is __BRAND__</a>
<a href="how-it-works.html">How It Works</a>
<a href="ingredients.html">Ingredients</a>
<a href="benefits.html">Benefits</a>
<a href="reviews.html">Reviews</a>
<a href="faq.html">FAQs</a>
<a href="blog/index.html">Blog</a>
</div>
<a class="btn nav-cta" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_HEADER__</a>
</div></nav>
<header class="hero"><div class="wrap">
<div>
<span class="pill">__PILL_TEXT__</span>
<h1>__HERO_H1__</h1>
<p class="hero-sub">__HERO_DESC__</p>
<div class="hero-checks"><div>__CHECK1__</div><div>__CHECK2__</div><div>__CHECK3__</div><div>__CHECK4__</div></div>
<div class="hero-cta-row">
<a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_HERO__</a>
<div class="hero-price">From __PRICE_FROM__<small>per bottle · 60-day guarantee</small></div>
</div>
<p class="hero-note">★★★★★ __REVIEW_COUNT__ reviews · Secure checkout · 60-Day Money-Back Guarantee</p>
<div class="badges"><figure style="margin:0;text-align:center;max-width:100px"><img src="assets/images/badge-usa.png" alt="Made in USA" width="90" height="90" loading="lazy"><figcaption style="font-size:.7rem;color:var(--muted);margin-top:4px">Strict quality control standards</figcaption></figure><figure style="margin:0;text-align:center;max-width:100px"><img src="assets/images/badge-fda.png" alt="FDA-registered facility" width="90" height="90" loading="lazy"><figcaption style="font-size:.7rem;color:var(--muted);margin-top:4px">Produced in a registered facility</figcaption></figure><figure style="margin:0;text-align:center;max-width:100px"><img src="assets/images/badge-gmp.png" alt="GMP certified" width="90" height="90" loading="lazy"><figcaption style="font-size:.7rem;color:var(--muted);margin-top:4px">Good Manufacturing Practice</figcaption></figure><figure style="margin:0;text-align:center;max-width:100px"><img src="assets/images/badge-natural.png" alt="Natural ingredients" width="90" height="90" loading="lazy"><figcaption style="font-size:.7rem;color:var(--muted);margin-top:4px">No artificial fillers or additives</figcaption></figure></div>
<div class="quick-facts">
<div class="qf-title">Quick Facts</div>
<dl>
<div><dt>Ingredients</dt><dd>__FACT1_NUM__ named actives</dd></div>
<div><dt>Daily serving</dt><dd>__FACT2_NUM__</dd></div>
<div><dt>Guarantee</dt><dd>__FACT3_NUM__ money-back</dd></div>
<div><dt>Made in</dt><dd>__FACT4_NUM__</dd></div>
<div><dt>Serving size</dt><dd>__SERVING_DAILY__</dd></div>
<div><dt>Per bottle</dt><dd>__SERVING_PER_BOTTLE__</dd></div>
</dl>
</div>
<div class="hero-facts">
<div><b>__FACT1_NUM__</b><span>__FACT1_LABEL__</span></div>
<div><b>__FACT2_NUM__</b><span>__FACT2_LABEL__</span></div>
<div><b>__FACT3_NUM__</b><span>__FACT3_LABEL__</span></div>
<div><b>__FACT4_NUM__</b><span>__FACT4_LABEL__</span></div>
</div>
</div>
<div class="hero-media">
<div class="hero-badge">Save big today</div>
<img id="hero-img" src="assets/images/hero.png" alt="__BRAND__ __CATEGORY__ supplement bottle" width="640" height="640" fetchpriority="high">
</div>
</div></header>
<div class="honeycomb" aria-hidden="true"></div>
<section class="trust"><div class="wrap"><span>__REVIEW_COUNT__ Verified Reviews</span><span>60-Day Guarantee</span><span>Made In USA</span><span>Secure Checkout</span></div></section>
<section class="sec" id="symptoms"><div class="wrap">
<div class="head"><span class="eyebrow">Does this sound familiar?</span><h2>A Gentle Nudge, If Any of This Sounds Like You</h2><p>If any of these feel like your everyday, __BRAND__ was made with you in mind.</p></div>
<div class="grid g3">__SYMPTOM_CARD_TEMPLATE__</div>
</div></section>
<section class="sec soft" id="what-is"><div class="wrap">
<div class="head"><span class="eyebrow">What is __BRAND__?</span><h2>The Honest Answer, in Plain Words</h2></div>
<p style="font-size:1.15rem;max-width:820px;margin:0 auto 16px;text-align:center">__WHATIS_P1__</p>
<div class="callout" style="max-width:820px;margin:0 auto">__WHATIS_CALLOUT__</div>
<div class="chips" style="justify-content:center"><span>__CHIP1__</span><span>__CHIP2__</span><span>__CHIP3__</span><span>__CHIP4__</span></div>
<div style="text-align:center;margin-top:28px"><a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_AFTER_WHATIS__</a></div>
</div></section>
<section class="sec" id="how-it-works"><div class="wrap">
<div class="head"><span class="eyebrow">Simple by design</span><h2>How __BRAND__ Works, Step by Step</h2><p>__HIW_INTRO__</p></div>
<div style="text-align:center;margin-bottom:28px"><img src="assets/images/feature-shot.png" alt="How __BRAND__ works" style="max-width:680px;border-radius:20px;box-shadow:0 14px 34px rgba(120,72,0,.14)"></div>
<div class="grid g2">__HIW_CARD_TEMPLATE__</div>
<div style="text-align:center;margin-top:28px"><a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_AFTER_HIW__</a></div>
</div></section>
<section class="sec soft" id="benefits"><div class="wrap">
<div class="head"><span class="eyebrow">Why people choose it</span><h2>Small Daily Wins That Add Up</h2><p>Real, everyday support — no hype, no promises it cannot keep.</p></div>
<div class="grid g3">__BENEFIT_CARD_TEMPLATE__</div>
<ul style="max-width:720px;margin:28px auto 0;font-weight:700;line-height:2">__BAL_PROS_TEMPLATE__</ul>
<div style="text-align:center;margin-top:28px"><a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_AFTER_BENEFITS__</a></div>
</div></section>
<section class="sec soft" id="compare"><div class="wrap">
<div class="head"><span class="eyebrow">An honest comparison</span><h2>__BRAND__ vs The Alternatives</h2><p>Decide with the facts in front of you — no hype.</p></div>
<table class="compare">
<tr><th></th><th>__BRAND__</th><th>Typical Pills</th><th>Doing Nothing</th></tr>
<tr><td>Named ingredients listed</td><td class="yes">✓ Yes</td><td class="no">✗ Often hidden in blends</td><td class="no">✗ —</td></tr>
<tr><td>One simple daily serving</td><td class="yes">✓ Yes</td><td class="no">✗ Several pills a day</td><td class="no">✗ —</td></tr>
<tr><td>60-day money-back guarantee</td><td class="yes">✓ Yes</td><td class="no">✗ Rarely</td><td class="no">✗ —</td></tr>
<tr><td>Made in USA, GMP facility</td><td class="yes">✓ Yes</td><td class="no">✗ Varies</td><td class="no">✗ —</td></tr>
</table>
<div style="text-align:center;margin-top:28px"><a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">Try __BRAND__ Risk-Free →</a></div>
</div></section>
<section class="sec" id="ingredients"><div class="wrap">
<div class="head"><span class="eyebrow">Inside every serving</span><h2>__ING_HEADING__</h2><p>Every ingredient, explained plainly. Serving: __SERVING_DAILY__ · Per bottle: __SERVING_PER_BOTTLE__.</p></div>
<div class="grid g3" id="ing-grid">__ING_CARD_TEMPLATE__</div>
<div style="text-align:center;margin-top:28px"><a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_AFTER_INGREDIENTS__</a></div>
</div></section>
<section class="sec soft" id="pricing"><div class="wrap">
<div class="head"><span class="eyebrow">Choose your package</span><h2>Pick the Best Value for You</h2><p>__PRICING_NOTE__</p></div>
<div class="plans">__PLAN_CARD_TEMPLATE__</div>
<p style="text-align:center;font-weight:700;margin-top:22px">Lowest price: __PRICE_LOW__ per bottle · Highest listed: __PRICE_HIGH__ per bottle</p>
</div></section>
__BONUS_SECTION__
<section class="sec" id="reviews"><div class="wrap">
<div class="head"><span class="eyebrow">Verified reviews</span><h2>What Customers Say</h2><p>★★★★★ __REVIEW_COUNT__ reviews and counting.</p></div>
<div class="grid g3">__REVIEW_CARD_TEMPLATE__</div>
<div style="text-align:center;margin-top:28px"><a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_AFTERREVIEWS__</a></div>
</div></section>
<section class="sec soft"><div class="wrap"><div class="guarantee">
<img src="assets/images/guarantee.png" alt="60-day money-back guarantee" loading="lazy">
<h2 style="font-size:2rem;margin:12px 0">60-Day Money-Back Guarantee</h2>
<p style="color:var(--muted);max-width:680px;margin:0 auto">__GUARANTEE_TEXT__</p>
</div></div></section>
<section class="sec" id="faq"><div class="wrap">
<div class="head"><span class="eyebrow">Got questions?</span><h2>Frequently Asked Questions</h2></div>
__FAQ_ROW_TEMPLATE__
<div style="text-align:center;margin-top:28px"><a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_AFTERFAQ__</a></div>
</div></section>
<section class="sec final"><div class="wrap">
<h2>Ready to Start Today?</h2>
<p>__FINAL_TEXT__</p>
<a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_CLOSING__</a>
</div></section>
<footer><div class="wrap">
<p><a href="index.html">Home</a> · <a href="what-is-product.html">What Is __BRAND__</a> · <a href="how-it-works.html">How It Works</a> · <a href="ingredients.html">Ingredients</a> · <a href="benefits.html">Benefits</a> · <a href="reviews.html">Reviews</a> · <a href="faq.html">FAQs</a> · <a href="blog/index.html">Blog</a></p>
<p><a href="terms.html">Terms of Use</a> · <a href="privacy-policy.html">Privacy Policy</a> · <a href="disclaimer.html">Disclaimer</a> · <a href="refund-policy.html">Refund Policy</a> · <a href="about.html">About Us</a> · <a href="contact.html">Contact Us</a></p>
<p>© __YEAR__ __BRAND__ · __CATEGORY__ · This site is an independent review site. Always check the official product page for the latest pricing and terms.</p>
</div></footer>
<script>
(function(){
var rows=document.querySelectorAll('.faq-row');
rows.forEach(function(r){var b=r.querySelector('.faq-btn');if(b){b.addEventListener('click',function(){r.classList.toggle('open');});}});
var el=document.getElementById('d19-count');
function tick(){if(!el)return;var n=new Date();var end=new Date(n);end.setHours(23,59,59,999);var s=Math.max(0,Math.floor((end-n)/1000));var h=Math.floor(s/3600),m=Math.floor(s%3600/60),sec=s%60;el.textContent=(h<10?'0'+h:h)+':'+(m<10?'0'+m:m)+':'+(sec<10?'0'+sec:sec);}
tick();setInterval(tick,1000);
})();
</script>
</body>
</html>
