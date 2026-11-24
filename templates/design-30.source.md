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
<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&family=Nunito:wght@400;600;700;800&display=swap" rel="stylesheet">
<style>
:root{--primary:__COLOR_PRIMARY__;--primary-dark:__COLOR_DARK__;--primary-light:__COLOR_LIGHT__;--accent:__COLOR_ACCENT__;--on-primary:__COLOR_ON_PRIMARY__;--ink:#3A2A33;--ink-soft:#8A6E79;--bg:#FFF6F8;--surface:#fff;--surface-alt:#FDE9EE;--line:rgba(58,42,51,.12);--good:#3F9142;--radius:24px;--shadow:0 18px 40px -20px rgba(58,42,51,.22)}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;font-family:'Nunito',system-ui,-apple-system,Segoe UI,Roboto,sans-serif;color:var(--ink);background:var(--bg);line-height:1.65;overflow-x:hidden;font-size:17px}
h1,h2,h3,h4{font-family:'Fredoka',system-ui,-apple-system,Segoe UI,Roboto,sans-serif;font-weight:600;line-height:1.25;margin:0;color:var(--ink)}
a{color:var(--primary-dark)}
img{max-width:100%;height:auto;display:block}
.wrap{max-width:1160px;margin:0 auto;padding:0 24px}
/* Strip + nav */
.ptl-strip{background:var(--ink);color:#FBE4E9;font-size:13.5px;padding:9px 0;display:flex;gap:26px;justify-content:center;flex-wrap:wrap;text-align:center}
.ptl-strip b{color:var(--primary-light)}
nav.navbar{position:sticky;top:0;z-index:200;background:rgba(255,246,248,.93);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
nav.navbar .wrap{display:flex;align-items:center;gap:24px;padding:15px 24px}
.logo{font-family:'Fredoka',sans-serif;font-weight:700;font-size:1.35rem;text-decoration:none;color:var(--ink)}
.logo em{font-style:normal;color:var(--primary-dark)}
.nav-links{display:flex;gap:22px;margin-left:auto;flex-wrap:wrap;align-items:center}
.nav-links a{color:var(--ink-soft);text-decoration:none;font-weight:700;font-size:.92rem}
.nav-links a:hover{color:var(--primary-dark)}
.nav-toggle{display:none;background:none;border:1px solid var(--line);border-radius:12px;font-size:22px;cursor:pointer;color:var(--ink);padding:4px 10px;min-height:40px;margin-left:auto}
.btn,.btn-big{display:inline-flex;align-items:center;justify-content:center;gap:6px;background:var(--primary-dark);color:var(--on-primary)!important;font-weight:700;text-decoration:none;padding:14px 26px;border-radius:999px;border:0;box-shadow:var(--shadow);font-size:1rem;line-height:1.2;text-align:center;transition:transform .15s ease;white-space:nowrap}
.btn:hover,.btn-big:hover{transform:translateY(-2px)}
.btn-ghost{background:transparent!important;color:var(--ink)!important;border:2px solid var(--ink)!important;box-shadow:none!important}
.btn-big{padding:16px 30px;font-size:1.03rem}
.nav-cta{padding:9px 18px!important;font-size:.86rem;box-shadow:none}
/* Hero — classic/info-dense: headline + lead copy + an explicit Quick Facts
   table right in the hero, this design's structural identity alongside its
   photo-illustrated ingredient grid and dedicated safety section below. */
header.hero{padding:44px 0 14px;background:radial-gradient(1000px 440px at 88% -12%,var(--surface-alt) 0%,transparent 60%),var(--bg)}
.hero .wrap{display:grid;grid-template-columns:1.05fr .95fr;gap:46px;align-items:start}
.ptl-pill{display:inline-block;background:var(--surface-alt);color:var(--primary-dark);font-weight:700;font-size:.78rem;letter-spacing:.03em;text-transform:uppercase;padding:7px 15px;border-radius:999px}
.hero h1{font-size:2.35rem;margin:16px 0 4px;letter-spacing:-.01em}
.hero h1 em{font-style:normal;color:var(--primary-dark)}
.ptl-answer{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:18px 20px;margin:16px 0}
.ptl-answer .tag{display:inline-block;background:var(--primary-dark);color:var(--on-primary);font-size:11.5px;font-weight:800;letter-spacing:.05em;text-transform:uppercase;padding:4px 12px;border-radius:999px;margin-bottom:9px}
.ptl-answer p{margin:0;color:var(--ink-soft);font-size:.96rem}
.hero-cta-row{display:flex;gap:14px;align-items:center;flex-wrap:wrap;margin-top:8px}
.hero-media{display:flex;flex-direction:column;gap:14px;align-items:center}
.ptl-hero-card{background:var(--surface-alt);border:1px solid var(--line);border-radius:28px;padding:22px;width:100%;max-width:300px;box-shadow:var(--shadow);text-align:center}
.ptl-hero-card img{max-width:180px;margin:0 auto 10px}
/* Quick Facts table — explicit, original, lives in the hero (distinct from
   the auto-generated Quick Facts box the builder appends after What Is) */
.ptl-glance{background:var(--surface);border:1px solid var(--line);border-radius:18px;padding:16px 18px;width:100%;max-width:300px;box-shadow:var(--shadow)}
.ptl-glance b{display:block;font-size:.78rem;letter-spacing:.04em;text-transform:uppercase;color:var(--primary-dark);margin-bottom:8px}
.ptl-glance table{width:100%;border-collapse:collapse}
.ptl-glance td{padding:5px 0;font-size:.86rem;border-bottom:1px dashed var(--line)}
.ptl-glance tr:last-child td{border-bottom:0}
.ptl-glance td:first-child{color:var(--ink-soft)}
.ptl-glance td:last-child{text-align:right;font-weight:700}
/* Section head */
.sec{padding:66px 0}
.sec.alt{background:var(--surface-alt)}
.head{max-width:700px;margin:0 auto 34px;text-align:center}
.eyebrow{display:inline-flex;align-items:center;gap:7px;color:var(--primary-dark);font-weight:800;font-size:.75rem;letter-spacing:.09em;text-transform:uppercase;margin-bottom:11px}
.head h2{font-size:1.9rem;margin:0 0 12px}
.head p{color:var(--ink-soft);font-size:1.02rem;margin:0}
.grid{display:grid;gap:18px}
.g2{grid-template-columns:repeat(2,minmax(0,1fr))}
.g3{grid-template-columns:repeat(3,minmax(0,1fr))}
.g4{grid-template-columns:repeat(4,minmax(0,1fr))}
.reveal{opacity:0;transform:translateY(14px);transition:opacity .5s ease,transform .5s ease}
.reveal.in{opacity:1;transform:none}
@media(prefers-reduced-motion:reduce){.reveal{opacity:1;transform:none;transition:none}}
/* Shared card markup (from build_native_page's default card builders) */
.card,.pcard,.ing-card,.rev-card,.step-card{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:22px;box-shadow:var(--shadow)}
.card h4,.ing-card h4,.step-card h4{margin:0 0 8px;font-size:1.02rem}
.card p,.ing-card p,.step-card p,.rev-card p{color:var(--ink-soft);margin:0;font-size:.92rem}
.ing-card{display:flex;gap:14px}
.ing-num,.step-num{flex:none;width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-family:'Fredoka',sans-serif;font-weight:700;font-size:.95rem;color:var(--on-primary);background:var(--primary-dark)}
.step-card .step-num{margin-bottom:12px}
.pcard{text-align:left}
.pcard .num{font-family:'Fredoka',sans-serif;font-size:1.35rem;color:var(--primary-dark);font-weight:700;display:block;margin-bottom:6px}
.rev-card .rev-head{display:flex;gap:12px;align-items:center;margin-bottom:9px}
.rev-card .rev-head img,.rev-card .rev-head>div{width:42px;height:42px;border-radius:50%;object-fit:cover}
.rev-name{font-weight:800}
.rev-sub{font-size:.76rem;color:var(--ink-soft)}
.rev-stars{color:var(--primary-dark);font-size:.95rem;letter-spacing:.1em;margin-bottom:7px}
/* Ingredient grid rows get the photo-illustrated tile treatment below */
#ingredients .ing-num{width:48px;height:48px;border-radius:14px;font-size:1.2rem}
#ingredients .ing-card{align-items:flex-start;flex-direction:column}
/* Trust strip */
section.trust{padding:16px 0;background:var(--surface);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
section.trust .wrap{display:flex;gap:28px;justify-content:center;flex-wrap:wrap;align-items:center}
section.trust .t-item{display:flex;align-items:center;gap:9px;font-weight:700;font-size:.86rem;color:var(--ink-soft)}
section.trust img{width:30px;height:30px;object-fit:contain}
/* Callout reused by Quick Facts auto-box */
.ptl-callout{background:var(--surface-alt);border-radius:var(--radius);padding:18px 20px;font-weight:600;color:var(--ink)}
.ptl-chips{display:flex;gap:10px;flex-wrap:wrap;margin:18px 0}
.ptl-chips span{background:var(--surface-alt);border:1px solid var(--line);border-radius:999px;padding:7px 15px;font-weight:700;font-size:.8rem;color:var(--ink)}
/* Benefits feature block */
.feature{display:grid;grid-template-columns:.85fr 1.15fr;gap:38px;align-items:center;margin-bottom:36px}
.feature img{border-radius:var(--radius);box-shadow:var(--shadow)}
.feature h3{font-size:1.3rem;margin:0 0 12px}
.feature p{color:var(--ink-soft)}
/* Your Match Card — original distinctive component: badge + fit checklist */
.ptl-match{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:30px 28px;display:grid;grid-template-columns:auto 1fr;gap:28px;align-items:center}
.ptl-badge{width:96px;height:96px;border-radius:50%;background:var(--good);display:flex;flex-direction:column;align-items:center;justify-content:center;color:#fff;flex:none;box-shadow:0 14px 28px -12px rgba(63,145,66,.5)}
.ptl-badge .tick{font-size:1.9rem;line-height:1}
.ptl-badge span{font-size:.64rem;font-weight:800;letter-spacing:.04em;text-transform:uppercase;margin-top:2px}
.ptl-match-list{display:flex;flex-direction:column;gap:10px}
.ptl-match-list div{display:flex;gap:10px;align-items:flex-start;font-weight:700;font-size:.92rem;color:var(--ink)}
.ptl-match-list div:before{content:"✓";flex:none;width:20px;height:20px;border-radius:50%;background:var(--surface-alt);color:var(--primary-dark);font-size:.68rem;font-weight:800;display:flex;align-items:center;justify-content:center;margin-top:1px}
/* Safety & interactions — dedicated grid, original to this design's
   info-dense, classic long-form composition */
.ptl-safety{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}
.ptl-safety-card{background:var(--surface);border:1px solid var(--line);border-radius:18px;padding:20px 22px}
.ptl-safety-card h4{font-size:1rem;margin:0 0 8px;display:flex;align-items:center;gap:8px}
.ptl-safety-card h4:before{content:"";width:9px;height:9px;border-radius:50%;background:var(--primary-dark);flex:none}
.ptl-safety-card p{margin:0;color:var(--ink-soft);font-size:.9rem}
/* Pricing */
.plans{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px;align-items:stretch}
.plan{position:relative;background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:28px 22px;text-align:center;display:flex;flex-direction:column}
.plan.top{border:2px solid var(--primary-dark);box-shadow:var(--shadow);transform:translateY(-6px)}
.plan-badge{position:absolute;top:-14px;left:50%;transform:translateX(-50%);background:var(--primary-dark);color:var(--on-primary);border-radius:999px;padding:6px 16px;font-weight:800;font-size:.75rem;white-space:nowrap}
.plan img{max-width:150px;margin:4px auto 12px}
.plan-ttl{font-size:1.18rem}
.plan-sub{font-weight:700;color:var(--ink-soft);font-size:.82rem}
.plan-price{font-size:2rem;margin:12px 0 4px;font-family:'Fredoka',sans-serif;font-weight:700}
.plan-price small{font-size:.86rem;color:var(--ink-soft);font-weight:600}
.plan-tot,.plan-ship{font-weight:700;color:var(--ink-soft);font-size:.83rem}
.plan-ship{color:var(--good)}
.plan ul{list-style:none;padding:0;margin:14px 0;text-align:left}
.plan ul li{padding:5px 0 5px 24px;position:relative;font-weight:600;font-size:.87rem;color:var(--ink-soft)}
.plan ul li:before{content:"✓";position:absolute;left:0;color:var(--good);font-weight:800}
.plan .btn{margin-top:auto;width:100%}
/* Guarantee */
.ptl-guarantee{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:36px;text-align:center}
.ptl-guarantee img{max-width:130px;margin:0 auto}
/* FAQ accordion */
.faq-row{border:1px solid var(--line);border-radius:18px;margin-bottom:12px;background:var(--surface);overflow:hidden}
.faq-btn{width:100%;text-align:left;background:transparent;border:0;padding:16px 18px;font-family:'Fredoka',sans-serif;font-size:.96rem;font-weight:600;cursor:pointer;display:flex;justify-content:space-between;gap:16px;align-items:center;color:var(--ink)}
.faq-btn:after{content:"+";font-size:1.3rem;font-weight:700;color:var(--primary-dark);transition:transform .2s ease}
.faq-row.open .faq-btn:after{transform:rotate(45deg)}
.faq-body{display:none;padding:0 18px 16px;color:var(--ink-soft)}
.faq-row.open .faq-body{display:block}
/* Compare */
.compare{width:100%;border-collapse:collapse;background:var(--surface);border:1px solid var(--line);border-radius:18px;overflow:hidden}
.compare th,.compare td{padding:12px 14px;text-align:left;border-bottom:1px solid var(--line);font-weight:600;font-size:.9rem}
.compare th{background:var(--surface-alt);font-family:'Fredoka',sans-serif;font-size:.88rem}
.compare td:first-child{font-weight:700}
.compare .yes{color:var(--good);font-weight:800}
.compare .no{color:#C9697A;font-weight:800}
/* References */
.refs{columns:2;column-gap:40px}
.refs li{font-size:.86rem;color:var(--ink-soft);margin-bottom:10px;break-inside:avoid}
.refs-note{font-size:.84rem;color:var(--ink-soft);text-align:center;max-width:720px;margin:0 auto 24px}
.refs-wrap.collapsed .refs li:nth-child(n+7){display:none}
.refs-more{display:block;text-align:center;margin-top:18px;background:transparent;border:1px solid var(--line);border-radius:999px;padding:9px 20px;font-weight:700;font-size:.88rem;cursor:pointer;color:var(--ink)}
/* Final CTA — contrasting deep berry panel */
section.final{text-align:center;background:linear-gradient(160deg,#3A2A33,#5C3A48);border-radius:32px;margin:0 24px;padding:4px}
section.final .wrap{padding:52px 24px}
section.final .head h2{color:#fff}
section.final .head p{color:#F0D4DC;max-width:620px;margin:0 auto}
section.final .plan{background:rgba(255,255,255,.07);border-color:rgba(255,255,255,.2)}
section.final .plan-ttl,section.final .plan-price{color:#fff}
section.final .plan-sub,section.final .plan-tot{color:#F0D4DC}
footer{background:var(--surface-alt);border-top:1px solid var(--line);padding:40px 0;text-align:center;color:var(--ink-soft)}
footer a{color:var(--ink);font-weight:700;text-decoration:none;margin:0 8px;font-size:.9rem}
footer a:hover{color:var(--primary-dark)}
footer .fnote{font-size:.78rem;margin-top:10px;opacity:.8}
.auto-sticky-cta{background:var(--surface)!important;border-top:1px solid var(--line)!important}
.auto-sticky-cta-btn{background:var(--primary-dark)!important;color:var(--on-primary)!important;border-radius:999px!important}
@media(max-width:900px){.hero .wrap{grid-template-columns:1fr}.hero-media{order:-1}.hero h1{font-size:2rem}.g4,.g3,.g2,.plans,.feature,.ptl-match,.ptl-safety{grid-template-columns:1fr}.plan.top{transform:none}.feature img{max-width:340px;margin:0 auto}.refs{columns:1}.ptl-match{text-align:center}.ptl-badge{margin:0 auto}}
@media(max-width:760px){.nav-links{position:fixed;top:60px;left:0;right:0;background:var(--bg);flex-direction:column;align-items:flex-start;padding:18px 24px;gap:16px;display:none;border-bottom:1px solid var(--line)}.nav-links.open{display:flex}.nav-toggle{display:block}}
</style>
</head>
<body>
<div class="ptl-strip"><span><b>__FACT3_NUM__ __FACT3_LABEL__</b></span><span>Made In USA</span><span>GMP-Certified Facility</span></div>
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
<span class="ptl-pill">__PILL_TEXT__</span>
<h1>__HERO_H1__</h1>
<div class="ptl-answer reveal"><span class="tag">In Short</span><p>__HERO_DESC__</p></div>
<div class="hero-cta-row">
<a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_HERO__</a>
<a class="btn btn-big btn-ghost" href="#how-it-works">See How It Works</a>
</div>
</div>
<div class="hero-media">
<div class="ptl-hero-card reveal">
<img id="hero-img" src="assets/images/hero.png" alt="__BRAND__ __CATEGORY__ supplement bottle" width="180" height="180" fetchpriority="high">
<p style="margin:0;font-weight:700;font-size:.88rem">★ 4.8 / 5 · __REVIEW_COUNT__ reviews</p>
</div>
<div class="ptl-glance reveal">
<b>Quick Facts</b>
<table>
<tr><td>Category</td><td>__CATEGORY__</td></tr>
<tr><td>Ingredients</td><td>__FACT1_NUM__</td></tr>
<tr><td>Daily serving</td><td>__SERVING_DAILY__</td></tr>
<tr><td>Per bottle</td><td>__SERVING_PER_BOTTLE__</td></tr>
<tr><td>Guarantee</td><td>__FACT3_NUM__</td></tr>
<tr><td>From</td><td>__PRICE_FROM__</td></tr>
</table>
</div>
</div>
</div></header>
<section class="trust"><div class="wrap">
<div class="t-item"><img src="assets/images/badge-usa.png" alt="Made in USA" width="30" height="30" loading="lazy"> <span>Made in USA<small style="display:block;font-weight:500;opacity:.8">Manufactured under strict quality control standards.</small></span></div>
<div class="t-item"><img src="assets/images/badge-gmp.png" alt="GMP certified" width="30" height="30" loading="lazy"> <span>GMP Certified<small style="display:block;font-weight:500;opacity:.8">Made under Good Manufacturing Practice procedures.</small></span></div>
<div class="t-item"><img src="assets/images/badge-fda.png" alt="FDA-registered facility" width="30" height="30" loading="lazy"> <span>FDA-Registered Facility<small style="display:block;font-weight:500;opacity:.8">Produced in an FDA-registered facility.</small></span></div>
<div class="t-item"><img src="assets/images/badge-natural.png" alt="Natural ingredients" width="30" height="30" loading="lazy"> <span>100% Natural<small style="display:block;font-weight:500;opacity:.8">No artificial fillers or synthetic additives.</small></span></div>
</div></section>
<section class="sec" id="what-is"><div class="wrap">
<div class="head reveal"><span class="eyebrow">What is __BRAND__?</span><h2>A Straightforward Answer</h2></div>
<p class="reveal" style="font-size:1.04rem;max-width:760px;margin:0 auto 18px;text-align:center;color:var(--ink-soft)">__WHATIS_P1__</p>
<div class="ptl-callout reveal" style="max-width:760px;margin:0 auto">__WHATIS_CALLOUT__</div>
<div class="ptl-chips reveal" style="justify-content:center"><span>__CHIP1__</span><span>__CHIP2__</span><span>__CHIP3__</span><span>__CHIP4__</span></div>
<div class="reveal" style="text-align:center;margin-top:26px"><a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_AFTER_WHATIS__</a></div>
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
<ul class="reveal" style="max-width:720px;margin:28px auto 0;font-weight:700;line-height:2;list-style:none;padding:0">__BAL_PROS_TEMPLATE__</ul>
</div></section>
<section class="sec" id="reviews"><div class="wrap">
<div class="head reveal"><span class="eyebrow">Verified reviews</span><h2>What Customers Say</h2><p>★★★★★ __REVIEW_COUNT__ reviews and counting.</p></div>
<div class="grid g3">__REVIEW_CARD_TEMPLATE__</div>
<div class="reveal" style="text-align:center;margin-top:26px"><a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_AFTERREVIEWS__</a></div>
</div></section>
<section class="sec alt" id="how-it-works"><div class="wrap">
<div class="head reveal"><span class="eyebrow">How it works</span><h2>From Bottle To Daily Habit</h2><p>__HIW_INTRO__</p></div>
<div class="grid g2">__HIW_CARD_TEMPLATE__</div>
<div class="reveal" style="text-align:center;margin-top:28px"><a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_AFTER_HIW__</a></div>
</div></section>
<section class="sec"><div class="wrap">
<div class="head reveal"><span class="eyebrow">Is it for you?</span><h2>Your __BRAND__ Match Card</h2><p>A quick, honest read on who this is built for.</p></div>
<div class="ptl-match reveal">
<div class="ptl-badge"><span class="tick">✓</span><span>Good Fit</span></div>
<div class="ptl-match-list">
<div>You want a simple daily routine, not a complicated regimen</div>
<div>You prefer ingredients listed individually, not a hidden blend</div>
<div>You're comfortable trying a new daily wellness habit for a few weeks</div>
<div>You'd rather have a guarantee than a no-returns policy</div>
</div>
</div>
</div></section>
<section class="sec alt" id="ingredients"><div class="wrap">
<div class="head reveal"><span class="eyebrow">Inside every serving</span><h2>__ING_HEADING__</h2><p>Every ingredient, explained plainly. Serving: __SERVING_DAILY__ · Per bottle: __SERVING_PER_BOTTLE__.</p></div>
<div class="grid g4">__ING_CARD_TEMPLATE__</div>
<div class="reveal" style="text-align:center;margin-top:26px"><a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_AFTER_INGREDIENTS__</a></div>
</div></section>
<section class="sec"><div class="wrap">
<div class="head reveal"><span class="eyebrow">Before you start</span><h2>Safety &amp; Interactions</h2><p>A plain-language rundown — not a substitute for medical advice.</p></div>
<div class="ptl-safety reveal">
<div class="ptl-safety-card"><h4>Who should avoid __BRAND__</h4><p>Pregnant or nursing individuals, anyone under 18, and anyone with a known allergy to a listed ingredient should not use __BRAND__ without medical guidance.</p></div>
<div class="ptl-safety-card"><h4>Medication interactions</h4><p>If you take prescription medication, check the full ingredient list against it and ask a pharmacist or doctor before adding __BRAND__ to your routine.</p></div>
<div class="ptl-safety-card"><h4>Allergy notes</h4><p>Check the label against any known sensitivities. Discontinue use and consult a doctor if you notice an unexpected reaction.</p></div>
<div class="ptl-safety-card"><h4>Existing conditions</h4><p>If you manage a medical condition, talk to your healthcare provider first — this page is general information, not personalized medical advice.</p></div>
</div>
</div></section>
<section class="sec alt" id="pricing"><div class="wrap">
<div class="head reveal"><span class="eyebrow">Choose your package</span><h2>Pick The __BRAND__ Package That Fits You</h2><p>__PRICING_NOTE__</p></div>
<div class="plans">__PLAN_CARD_TEMPLATE__</div>
<p class="reveal" style="text-align:center;font-weight:700;margin-top:20px;color:var(--ink-soft)">Lowest price: __PRICE_LOW__ per bottle · Highest listed: __PRICE_HIGH__ per bottle</p>
</div></section>
__BONUS_SECTION__
<section class="sec" id="pricing-again"><div class="wrap">
<div class="head reveal"><span class="eyebrow">Still deciding?</span><h2>Get __BRAND__ Today</h2><p>Current package pricing, while supplies last.</p></div>
<div class="plans">__PLAN_CARD_TEMPLATE__</div>
<div class="reveal" style="text-align:center;margin-top:20px;font-weight:700;color:var(--ink-soft)"><a href="#faq">View FAQs</a></div>
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
<section class="sec alt"><div class="wrap"><div class="ptl-guarantee reveal">
<img src="assets/images/guarantee.png" alt="60-day money-back guarantee" loading="lazy">
<h2 style="font-size:1.6rem;margin:14px 0">__FACT3_NUM__ Money-Back __FACT3_LABEL__</h2>
<p style="color:var(--ink-soft);max-width:640px;margin:0 auto 20px">__GUARANTEE_TEXT__</p>
<div style="display:flex;gap:22px;justify-content:center;flex-wrap:wrap;margin-top:8px">
<figure style="margin:0;text-align:center;max-width:110px"><img src="assets/images/badge-usa.png" alt="Made in USA" width="30" height="30" loading="lazy"><figcaption style="font-size:.72rem;color:var(--ink-soft);margin-top:4px">Strict quality control standards</figcaption></figure>
<figure style="margin:0;text-align:center;max-width:110px"><img src="assets/images/badge-gmp.png" alt="GMP certified" width="30" height="30" loading="lazy"><figcaption style="font-size:.72rem;color:var(--ink-soft);margin-top:4px">Good Manufacturing Practice</figcaption></figure>
<figure style="margin:0;text-align:center;max-width:110px"><img src="assets/images/badge-fda.png" alt="FDA-registered facility" width="30" height="30" loading="lazy"><figcaption style="font-size:.72rem;color:var(--ink-soft);margin-top:4px">Produced in a registered facility</figcaption></figure>
<figure style="margin:0;text-align:center;max-width:110px"><img src="assets/images/badge-natural.png" alt="Natural ingredients" width="30" height="30" loading="lazy"><figcaption style="font-size:.72rem;color:var(--ink-soft);margin-top:4px">No artificial fillers or additives</figcaption></figure>
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
