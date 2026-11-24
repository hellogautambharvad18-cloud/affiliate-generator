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
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
:root{--primary:__COLOR_PRIMARY__;--primary-dark:__COLOR_DARK__;--primary-light:__COLOR_LIGHT__;--accent:__COLOR_ACCENT__;--on-primary:__COLOR_ON_PRIMARY__;--glow:#22d3ee;--bg:#0a0c12;--bg-alt:#10131c;--surface:rgba(255,255,255,.045);--surface-hi:rgba(255,255,255,.07);--line:rgba(255,255,255,.1);--text:#e7eaf3;--muted:#92a0b8;--cta-shadow:0 10px 30px -8px rgba(34,211,238,.45)}
*{box-sizing:border-box}
html{scroll-behavior:smooth;font-size:18px}
body{margin:0;font-family:'Inter',system-ui,-apple-system,Segoe UI,Roboto,sans-serif;color:var(--text);background:var(--bg);line-height:1.65;overflow-x:hidden}
h1,h2,h3,h4{font-family:'Space Grotesk',system-ui,sans-serif;line-height:1.18;letter-spacing:-.01em;font-weight:700;color:#fff;margin:0}
a{color:var(--glow)}
img{max-width:100%;height:auto}
.wrap{max-width:1140px;margin:0 auto;padding:0 24px}
.gtext{background:linear-gradient(120deg,var(--glow),var(--primary) 70%);-webkit-background-clip:text;background-clip:text;color:transparent}
.topbar{background:linear-gradient(90deg,#0b0f1a,#131a2b);color:#cfe7ef;text-align:center;padding:10px 16px;font-weight:600;font-size:.88rem;letter-spacing:.02em;border-bottom:1px solid var(--line)}
.topbar strong{color:var(--glow)}
.topbar #d23-count{color:#fff;font-variant-numeric:tabular-nums;font-weight:800;background:rgba(34,211,238,.12);padding:2px 8px;border-radius:6px}
nav.navbar{position:sticky;top:0;z-index:200;background:rgba(10,12,18,.72);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);border-bottom:1px solid var(--line)}
nav.navbar .wrap{display:flex;align-items:center;gap:22px;padding-top:14px;padding-bottom:14px}
.logo{font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:1.3rem;text-decoration:none;color:#fff;display:flex;align-items:center;gap:8px}
.logo .dot{width:9px;height:9px;border-radius:50%;background:var(--glow);box-shadow:0 0 12px 2px var(--glow);display:inline-block}
.nav-links{display:flex;gap:22px;margin-left:auto;flex-wrap:wrap}
.nav-links a{color:var(--muted);text-decoration:none;font-weight:600;font-size:.92rem;transition:color .15s}
.nav-links a:hover{color:#fff}
.nav-toggle{display:none;background:none;border:1px solid var(--line);border-radius:8px;font-size:22px;cursor:pointer;color:#fff;padding:4px 10px;min-height:40px;margin-left:auto}
.btn,.btn-big{display:inline-flex;align-items:center;justify-content:center;gap:6px;background:linear-gradient(120deg,var(--glow),var(--primary));color:#06121a!important;font-weight:800;text-decoration:none;padding:14px 26px;border-radius:12px;border:0;box-shadow:var(--cta-shadow);font-size:1rem;line-height:1.2;text-align:center;transition:transform .15s ease,box-shadow .15s ease;white-space:nowrap}
.btn:hover,.btn-big:hover{transform:translateY(-2px);box-shadow:0 14px 34px -6px rgba(34,211,238,.55)}
.btn-big{padding:17px 32px;font-size:1.05rem}
.nav-cta{padding:10px 18px!important;font-size:.9rem;box-shadow:0 6px 16px -4px rgba(34,211,238,.4)}
/* Hero */
header.hero{position:relative;padding:70px 0 56px;overflow:hidden}
.hero-glow{position:absolute;top:-180px;right:-120px;width:560px;height:560px;border-radius:50%;background:radial-gradient(circle,rgba(34,211,238,.28),rgba(34,211,238,0) 70%);filter:blur(10px);pointer-events:none;animation:pulseGlow 6s ease-in-out infinite}
.hero-glow.alt{top:auto;bottom:-220px;left:-160px;right:auto;background:radial-gradient(circle,rgba(99,102,241,.22),rgba(99,102,241,0) 70%);animation-delay:1.4s}
@keyframes pulseGlow{0%,100%{opacity:.55;transform:scale(1)}50%{opacity:.9;transform:scale(1.08)}}
@media(prefers-reduced-motion:reduce){.hero-glow{animation:none}}
.hero .wrap{display:grid;grid-template-columns:1.05fr .95fr;gap:52px;align-items:start;position:relative}
.hero-media{padding-top:6px}
.pill{display:inline-flex;align-items:center;gap:8px;background:var(--surface);border:1px solid var(--line);border-radius:999px;padding:7px 16px;font-weight:700;font-size:.8rem;color:var(--glow);letter-spacing:.03em}
.hero h1{font-size:2.9rem;margin:18px 0 16px}
.hero-sub{font-size:1.12rem;color:var(--muted);margin:0 0 24px;max-width:46ch}
.hero-checks{display:grid;gap:10px;margin:0 0 26px;font-weight:600;font-size:.96rem}
.hero-checks div{display:flex;gap:10px;align-items:flex-start}
.hero-checks div:before{content:"";flex:none;width:18px;height:18px;margin-top:3px;border-radius:50%;background:linear-gradient(120deg,var(--glow),var(--primary));box-shadow:0 0 0 3px rgba(34,211,238,.15)}
.hero-cta-row{display:flex;gap:18px;align-items:center;flex-wrap:wrap;margin-bottom:16px}
.hero-price{font-weight:800;font-size:1.15rem;color:#fff}
.hero-price small{display:block;font-size:.8rem;color:var(--muted);font-weight:600}
.hero-stats{display:flex;gap:26px;flex-wrap:wrap;margin-top:6px}
.hero-stats div{display:flex;flex-direction:column}
.hero-stats b{font-family:'Space Grotesk',sans-serif;font-size:1.3rem;color:#fff}
.hero-stats span{font-size:.75rem;color:var(--muted);text-transform:uppercase;letter-spacing:.06em}
.hero-media{position:relative;display:flex;justify-content:center}
.hero-media .frame{position:relative;background:var(--surface);border:1px solid var(--line);border-radius:28px;padding:28px;backdrop-filter:blur(10px)}
.hero-media img{display:block;border-radius:18px;max-width:320px}
.hero-float{position:absolute;background:var(--bg-alt);border:1px solid var(--line);border-radius:14px;padding:10px 14px;font-size:.82rem;font-weight:700;color:#fff;box-shadow:0 10px 24px rgba(0,0,0,.35);display:flex;align-items:center;gap:8px}
.hero-float.top{top:-6px;right:-18px}
.hero-float.bottom{bottom:10px;left:-26px}
.hero-float .ic{color:var(--glow);font-size:1rem}
.pulse-divider{height:46px;width:100%;overflow:hidden;line-height:0}
.pulse-divider svg{width:100%;height:100%;display:block}
/* Sections */
.sec{padding:76px 0}
.sec.alt{background:var(--bg-alt)}
.head{max-width:700px;margin:0 auto 42px;text-align:center}
.eyebrow{display:inline-flex;align-items:center;gap:7px;background:var(--surface);border:1px solid var(--line);color:var(--glow);padding:5px 14px;border-radius:999px;font-weight:700;font-size:.74rem;letter-spacing:.09em;text-transform:uppercase;margin-bottom:14px}
.eyebrow:before{content:"";width:6px;height:6px;border-radius:50%;background:var(--glow);box-shadow:0 0 8px 1px var(--glow)}
.head h2{font-size:2.15rem;margin:0 0 12px}
.head p{color:var(--muted);font-size:1.05rem;margin:0}
.grid{display:grid;gap:22px}
.g1{grid-template-columns:1fr}
.g2{grid-template-columns:repeat(2,minmax(0,1fr))}
.g3{grid-template-columns:repeat(3,minmax(0,1fr))}
.g4{grid-template-columns:repeat(4,minmax(0,1fr))}
.reveal{opacity:0;transform:translateY(16px);transition:opacity .55s ease,transform .55s ease}
.reveal.in{opacity:1;transform:none}
@media(prefers-reduced-motion:reduce){.reveal{opacity:1;transform:none;transition:none}}
/* Cards - shared markup from build_native_page */
.card,.pcard,.ing-card,.rev-card,.trust-card,.science-col,.step-card{background:var(--surface);border:1px solid var(--line);border-radius:18px;padding:26px;position:relative}
.card:before,.pcard:before,.ing-card:before,.step-card:before{content:"";position:absolute;inset:0 0 auto 0;height:2px;border-radius:18px 18px 0 0;background:linear-gradient(90deg,var(--glow),var(--primary));opacity:.7}
.card h4,.pcard h4,.ing-card h4,.step-card h4{margin:0 0 8px;font-size:1.12rem;color:#fff}
.card p,.pcard p,.ing-card p,.step-card p,.rev-card p{color:var(--muted);margin:0;font-size:.95rem}
.pcard .num{font-family:'Space Grotesk',sans-serif;font-size:1.6rem;color:var(--glow);font-weight:700;display:block;margin-bottom:6px}
.ing-card{display:flex;gap:16px}
.ing-num,.ing-num-circle,.step-num{flex:none;width:50px;height:50px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:1.05rem;color:#fff;border:2px solid transparent;background:linear-gradient(#0d1019,#0d1019) padding-box,conic-gradient(from 200deg,var(--glow),var(--primary),var(--glow)) border-box}
.step-card .step-num{margin-bottom:16px}
.rev-card .rev-head{display:flex;gap:12px;align-items:center;margin-bottom:10px}
.rev-card .rev-head img{width:44px;height:44px;border-radius:50%;object-fit:cover;border:2px solid var(--line)}
.rev-name{font-weight:700;color:#fff}
.rev-sub{font-size:.78rem;color:var(--muted)}
.rev-stars{color:var(--glow);font-size:1rem;letter-spacing:.1em;margin-bottom:8px}
/* Trust strip */
section.trust{padding:20px 0;background:var(--bg-alt);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
section.trust .wrap{display:flex;gap:30px;justify-content:center;flex-wrap:wrap;align-items:center}
section.trust .t-item{display:flex;align-items:center;gap:8px;font-weight:700;font-size:.9rem;color:var(--muted)}
section.trust img{width:38px;height:38px;object-fit:contain;filter:grayscale(.2) brightness(1.3)}
/* Chips / callout */
.chips{display:flex;gap:10px;flex-wrap:wrap;margin:22px 0}
.chips span{background:var(--surface);border:1px solid var(--line);border-radius:999px;padding:7px 15px;font-weight:700;font-size:.84rem;color:#dfe6f2}
.callout{background:linear-gradient(120deg,rgba(34,211,238,.08),rgba(99,102,241,.08));border:1px solid var(--line);border-left:3px solid var(--glow);border-radius:14px;padding:20px 22px;font-weight:500;color:#dfe6f2}
/* Pricing */
.plans{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px;align-items:stretch}
.plan{position:relative;background:var(--surface);border:1px solid var(--line);border-radius:22px;padding:30px 24px;text-align:center;display:flex;flex-direction:column}
.plan.top{border:1px solid rgba(34,211,238,.5);box-shadow:0 0 0 1px rgba(34,211,238,.25),0 20px 44px -12px rgba(34,211,238,.3);transform:scale(1.04);background:var(--surface-hi)}
.plan-badge{position:absolute;top:-14px;left:50%;transform:translateX(-50%);background:linear-gradient(120deg,var(--glow),var(--primary));color:#06121a;border-radius:999px;padding:6px 16px;font-weight:800;font-size:.78rem;white-space:nowrap}
.plan img{max-width:170px;margin:6px auto 14px;display:block}
.plan-ttl{font-size:1.35rem;color:#fff}
.plan-sub{font-weight:600;color:var(--muted);font-size:.86rem}
.plan-price{font-size:2.3rem;margin:14px 0 4px;color:#fff;font-family:'Space Grotesk',sans-serif;font-weight:700}
.plan-price small{font-size:.95rem;color:var(--muted);font-weight:600}
.plan-tot,.plan-ship{font-weight:600;color:var(--muted);font-size:.88rem}
.plan ul{list-style:none;padding:0;margin:18px 0;text-align:left}
.plan ul li{padding:7px 0 7px 26px;position:relative;font-weight:500;font-size:.92rem;color:#dfe6f2}
.plan ul li:before{content:"✓";position:absolute;left:0;color:var(--glow);font-weight:800}
.plan .btn{margin-top:auto;width:100%}
/* Guarantee */
.guarantee{background:var(--surface);border:1px solid var(--line);border-radius:24px;padding:40px;text-align:center}
.guarantee img{max-width:160px}
/* FAQ */
.faq-row{border:1px solid var(--line);border-radius:14px;margin-bottom:12px;background:var(--surface);overflow:hidden}
.faq-btn{width:100%;text-align:left;background:transparent;border:0;padding:18px 20px;font-family:'Space Grotesk',sans-serif;font-size:1.02rem;font-weight:600;cursor:pointer;display:flex;justify-content:space-between;gap:16px;align-items:center;color:#fff}
.faq-btn:after{content:"+";font-size:1.5rem;font-weight:700;color:var(--glow)}
.faq-row.open .faq-btn:after{content:"–"}
.faq-body{display:none;padding:0 20px 18px;color:var(--muted)}
.faq-row.open .faq-body{display:block}
/* Compare */
.compare{width:100%;border-collapse:collapse;background:var(--surface);border:1px solid var(--line);border-radius:16px;overflow:hidden}
.compare th,.compare td{padding:14px 16px;text-align:left;border-bottom:1px solid var(--line);font-weight:500;font-size:.92rem;color:#dfe6f2}
.compare th{background:rgba(34,211,238,.1);color:#fff;font-family:'Space Grotesk',sans-serif;font-size:.92rem}
.compare td:first-child{font-weight:700;color:#fff}
.compare .yes{color:var(--glow);font-weight:700}
.compare .no{color:#f87171;font-weight:700}
/* Final CTA */
section.final{background:linear-gradient(160deg,var(--bg-alt),#0a0c12);text-align:center;border-top:1px solid var(--line)}
section.final h2{font-size:2.3rem}
section.final p{color:var(--muted);max-width:620px;margin:14px auto 26px}
footer{background:var(--bg-alt);border-top:1px solid var(--line);padding:40px 0;text-align:center;color:var(--muted)}
footer a{color:#dfe6f2;font-weight:600;text-decoration:none;margin:0 8px;font-size:.92rem}
footer a:hover{color:var(--glow)}
footer .fnote{font-size:.78rem;margin-top:10px;opacity:.75}
/* The shared bonus-section injector (_bonus_section_html in app.py) hardcodes
   a light #f5f5f7 row background + #666 body text, which is correct for every
   other (light-background) design but reads as a jarring white blob against
   this design's dark page — override those two hardcoded values only; the
   header bar and h4/price lines already read var(--primary-dark)/var(--primary)/
   var(--accent) with light-theme fallbacks, so they adopt this design's own
   palette automatically and need no override. */
#bonuses{color:var(--text)}
#bonuses>div:last-child{background:var(--bg-alt)}
#bonuses>div:last-child>div{background:var(--surface)!important;border-bottom:1px solid var(--line)!important}
#bonuses p[style*="color:#666"]{color:var(--muted)!important}
.auto-sticky-cta{background:var(--bg-alt)!important;border-top:1px solid var(--line)!important}
.auto-sticky-cta-btn{background:linear-gradient(120deg,var(--glow),var(--primary))!important;color:#06121a!important;border-radius:12px!important;box-shadow:0 8px 24px -6px rgba(34,211,238,.5)!important}
@media(max-width:900px){.hero .wrap{grid-template-columns:1fr}.hero-media{order:-1}.hero h1{font-size:2.2rem}.g3,.g4,.plans{grid-template-columns:1fr}.g2{grid-template-columns:1fr}.plan.top{transform:none}}
@media(max-width:760px){.nav-links{position:fixed;top:62px;left:0;right:0;background:rgba(10,12,18,.98);backdrop-filter:blur(14px);flex-direction:column;align-items:flex-start;padding:18px 24px;gap:16px;display:none;border-bottom:1px solid var(--line)}.nav-links.open{display:flex}.nav-toggle{display:block}}
</style>
</head>
<body>
<div class="topbar">⚡ <strong>Launch offer live</strong> — from <strong>__PRICE_FROM__</strong> per bottle &nbsp;·&nbsp; Ends in <span id="d23-count">23:59:59</span></div>
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
<header class="hero"><div class="hero-glow" aria-hidden="true"></div><div class="hero-glow alt" aria-hidden="true"></div><div class="wrap">
<div>
<span class="pill">__PILL_TEXT__</span>
<h1>__HERO_H1__</h1>
<p class="hero-sub">__HERO_DESC__</p>
<div class="hero-checks"><div>__CHECK1__</div><div>__CHECK2__</div><div>__CHECK3__</div><div>__CHECK4__</div></div>
<div class="hero-cta-row">
<a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_HERO__</a>
<div class="hero-price">From __PRICE_FROM__<small>per bottle · 60-day guarantee</small></div>
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
<img id="hero-img" src="assets/images/hero.png" alt="__BRAND__ __CATEGORY__ supplement bottle" width="320" height="320" fetchpriority="high">
</div>
<div class="hero-float top"><span class="ic">★</span> 4.8 / 5 rating</div>
<div class="hero-float bottom"><span class="ic">✓</span> __REVIEW_COUNT__ reviews</div>
</div>
</div></header>
<div class="pulse-divider" aria-hidden="true"><svg viewBox="0 0 1200 40" preserveAspectRatio="none"><path d="M0 20 H380 L410 6 L440 34 L470 20 H700 L730 2 L760 38 L790 20 H1200" fill="none" stroke="#22d3ee" stroke-width="2" opacity=".45"/></svg></div>
<section class="trust"><div class="wrap">
<div class="t-item"><img src="assets/images/badge-usa.png" alt="Made in USA" width="38" height="38" loading="lazy"> <span>Made in USA<small style="display:block;font-weight:500;opacity:.8">Manufactured under strict quality control standards.</small></span></div>
<div class="t-item"><img src="assets/images/badge-gmp.png" alt="GMP certified" width="38" height="38" loading="lazy"> <span>GMP Certified<small style="display:block;font-weight:500;opacity:.8">Made under Good Manufacturing Practice procedures.</small></span></div>
<div class="t-item"><img src="assets/images/badge-fda.png" alt="FDA-registered facility" width="38" height="38" loading="lazy"> <span>FDA-Registered Facility<small style="display:block;font-weight:500;opacity:.8">Produced in an FDA-registered facility.</small></span></div>
<div class="t-item"><img src="assets/images/badge-natural.png" alt="Natural ingredients" width="38" height="38" loading="lazy"> <span>100% Natural<small style="display:block;font-weight:500;opacity:.8">No artificial fillers or synthetic additives.</small></span></div>
</div></section>
<section class="sec" id="symptoms"><div class="wrap">
<div class="head reveal"><span class="eyebrow">Sound familiar?</span><h2>Here's What Usually Gets In The Way</h2><p>If any of this feels familiar, __BRAND__ was built with exactly this in mind.</p></div>
<div class="grid g3">__SYMPTOM_CARD_TEMPLATE__</div>
</div></section>
<section class="sec alt" id="what-is"><div class="wrap">
<div class="head reveal"><span class="eyebrow">What is __BRAND__?</span><h2>A Straightforward Answer, No Hype</h2></div>
<p class="reveal" style="font-size:1.1rem;max-width:760px;margin:0 auto 18px;text-align:center;color:var(--muted)">__WHATIS_P1__</p>
<div class="callout reveal" style="max-width:760px;margin:0 auto">__WHATIS_CALLOUT__</div>
<div class="chips reveal" style="justify-content:center"><span>__CHIP1__</span><span>__CHIP2__</span><span>__CHIP3__</span><span>__CHIP4__</span></div>
<div class="reveal" style="text-align:center;margin-top:30px"><a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_AFTER_WHATIS__</a></div>
</div></section>
<section class="sec" id="how-it-works"><div class="wrap">
<div class="head reveal"><span class="eyebrow">How it works</span><h2>From Bottle To Daily Routine</h2><p>__HIW_INTRO__</p></div>
<div style="text-align:center;margin-bottom:32px" class="reveal"><img src="assets/images/feature-shot.png" alt="How __BRAND__ works" style="max-width:620px;border-radius:20px;border:1px solid var(--line)"></div>
<div class="grid g2">__HIW_CARD_TEMPLATE__</div>
<div class="reveal" style="text-align:center;margin-top:32px"><a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_AFTER_HIW__</a></div>
</div></section>
<section class="sec alt" id="benefits"><div class="wrap">
<div class="head reveal"><span class="eyebrow">Why people choose it</span><h2>What You Can Expect To Notice</h2><p>Real, everyday support — no overpromising.</p></div>
<div class="grid g3">__BENEFIT_CARD_TEMPLATE__</div>
<ul style="max-width:720px;margin:30px auto 0;font-weight:600;line-height:2;color:#dfe6f2">__BAL_PROS_TEMPLATE__</ul>
<div class="reveal" style="text-align:center;margin-top:30px"><a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_AFTER_BENEFITS__</a></div>
</div></section>
<section class="sec" id="compare"><div class="wrap">
<div class="head reveal"><span class="eyebrow">An honest comparison</span><h2>__BRAND__ vs The Alternatives</h2><p>Decide with the facts in front of you.</p></div>
<table class="compare reveal">
<tr><th></th><th>__BRAND__</th><th>Typical Pills</th><th>Doing Nothing</th></tr>
<tr><td>Named ingredients listed</td><td class="yes">✓ Yes</td><td class="no">✗ Often hidden</td><td class="no">✗ —</td></tr>
<tr><td>One simple daily serving</td><td class="yes">✓ Yes</td><td class="no">✗ Several pills</td><td class="no">✗ —</td></tr>
<tr><td>60-day money-back guarantee</td><td class="yes">✓ Yes</td><td class="no">✗ Rarely</td><td class="no">✗ —</td></tr>
<tr><td>Made in USA, GMP facility</td><td class="yes">✓ Yes</td><td class="no">✗ Varies</td><td class="no">✗ —</td></tr>
</table>
<div class="reveal" style="text-align:center;margin-top:30px"><a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">Try __BRAND__ Risk-Free →</a></div>
</div></section>
<section class="sec alt" id="ingredients"><div class="wrap">
<div class="head reveal"><span class="eyebrow">Inside every serving</span><h2>__ING_HEADING__</h2><p>Every ingredient, explained plainly. Serving: __SERVING_DAILY__ · Per bottle: __SERVING_PER_BOTTLE__.</p></div>
<div class="grid g3" id="ing-grid">__ING_CARD_TEMPLATE__</div>
<div class="reveal" style="text-align:center;margin-top:30px"><a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_AFTER_INGREDIENTS__</a></div>
</div></section>
<section class="sec" id="pricing"><div class="wrap">
<div class="head reveal"><span class="eyebrow">Choose your package</span><h2>Pick The Best Value For You</h2><p>__PRICING_NOTE__</p></div>
<div class="plans">__PLAN_CARD_TEMPLATE__</div>
<p class="reveal" style="text-align:center;font-weight:600;margin-top:24px;color:var(--muted)">Lowest price: __PRICE_LOW__ per bottle · Highest listed: __PRICE_HIGH__ per bottle</p>
</div></section>
__BONUS_SECTION__
<section class="sec alt" id="reviews"><div class="wrap">
<div class="head reveal"><span class="eyebrow">Verified reviews</span><h2>What Customers Say</h2><p>★★★★★ __REVIEW_COUNT__ reviews and counting.</p></div>
<div class="grid g3">__REVIEW_CARD_TEMPLATE__</div>
<div class="reveal" style="text-align:center;margin-top:30px"><a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_AFTERREVIEWS__</a></div>
</div></section>
<section class="sec"><div class="wrap"><div class="guarantee reveal">
<img src="assets/images/guarantee.png" alt="60-day money-back guarantee" loading="lazy">
<h2 style="font-size:1.9rem;margin:14px 0">60-Day Money-Back Guarantee</h2>
<p style="color:var(--muted);max-width:640px;margin:0 auto">__GUARANTEE_TEXT__</p>
</div></div></section>
<section class="sec alt" id="faq"><div class="wrap">
<div class="head reveal"><span class="eyebrow">Got questions?</span><h2>Frequently Asked Questions</h2></div>
__FAQ_ROW_TEMPLATE__
<div class="reveal" style="text-align:center;margin-top:30px"><a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_AFTERFAQ__</a></div>
</div></section>
<section class="sec final"><div class="wrap">
<h2 class="reveal">Ready To Start Today?</h2>
<p class="reveal">__FINAL_TEXT__</p>
<a class="btn btn-big reveal" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_CLOSING__</a>
</div></section>
<footer><div class="wrap">
<p><a href="index.html">Home</a> · <a href="what-is-product.html">What Is __BRAND__</a> · <a href="how-it-works.html">How It Works</a> · <a href="ingredients.html">Ingredients</a> · <a href="benefits.html">Benefits</a> · <a href="reviews.html">Reviews</a> · <a href="faq.html">FAQs</a> · <a href="blog/index.html">Blog</a></p>
<p><a href="terms.html">Terms of Use</a> · <a href="privacy-policy.html">Privacy Policy</a> · <a href="disclaimer.html">Disclaimer</a> · <a href="refund-policy.html">Refund Policy</a> · <a href="about.html">About Us</a> · <a href="contact.html">Contact Us</a></p>
<p class="fnote">© __YEAR__ __BRAND__ · __CATEGORY__ · This site is an independent review site. Always check the official product page for the latest pricing and terms.</p>
</div></footer>
<script>
(function(){
var rows=document.querySelectorAll('.faq-row');
rows.forEach(function(r){var b=r.querySelector('.faq-btn');if(b){b.addEventListener('click',function(){r.classList.toggle('open');});}});
var el=document.getElementById('d23-count');
function tick(){if(!el)return;var n=new Date();var end=new Date(n);end.setHours(23,59,59,999);var s=Math.max(0,Math.floor((end-n)/1000));var h=Math.floor(s/3600),m=Math.floor(s%3600/60),sec=s%60;el.textContent=(h<10?'0'+h:h)+':'+(m<10?'0'+m:m)+':'+(sec<10?'0'+sec:sec);}
tick();setInterval(tick,1000);
var toggle=document.querySelector('.nav-toggle'),links=document.querySelector('.nav-links');
if(toggle&&links){toggle.addEventListener('click',function(){links.classList.toggle('open');});}
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
