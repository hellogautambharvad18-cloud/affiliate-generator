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
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@500;600;700;800&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{--primary:__COLOR_PRIMARY__;--primary-dark:__COLOR_DARK__;--primary-light:__COLOR_LIGHT__;--accent:__COLOR_ACCENT__;--on-primary:__COLOR_ON_PRIMARY__;--ink:#0F2A2E;--ink-soft:#4E6B6E;--bg:#F3FAFA;--surface:#fff;--surface-alt:#E3F3F2;--line:rgba(15,42,46,.12);--good:#1E8F6B;--radius:18px;--shadow:0 18px 40px -20px rgba(15,42,46,.25)}
*{box-sizing:border-box}
html{scroll-behavior:smooth;font-size:112.5%}
body{margin:0;font-family:'IBM Plex Sans',system-ui,-apple-system,Segoe UI,Roboto,sans-serif;color:var(--ink);background:var(--bg);line-height:1.65;overflow-x:hidden;font-size:18px}
h1,h2,h3,h4{font-family:'Outfit',system-ui,-apple-system,Segoe UI,Roboto,sans-serif;font-weight:700;line-height:1.22;margin:0;color:var(--ink)}
a{color:var(--primary-dark)}
img{max-width:100%;height:auto;display:block}
.wrap{max-width:1160px;margin:0 auto;padding:0 24px}
/* Strip + nav */
.glm-strip{background:var(--ink);color:#DFF5F1;font-size:13.5px;padding:9px 0;display:flex;gap:26px;justify-content:center;flex-wrap:wrap;text-align:center}
.glm-strip b{color:var(--primary-light)}
nav.navbar{position:sticky;top:0;z-index:200;background:rgba(243,250,250,.93);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
nav.navbar .wrap{display:flex;align-items:center;gap:24px;padding:15px 24px}
.logo{font-family:'Outfit',sans-serif;font-weight:800;font-size:1.3rem;text-decoration:none;color:var(--ink)}
.logo em{font-style:normal;color:var(--primary-dark)}
.nav-links{display:flex;gap:22px;margin-left:auto;flex-wrap:wrap;align-items:center}
.nav-links a{color:var(--ink-soft);text-decoration:none;font-weight:600;font-size:.92rem}
.nav-links a:hover{color:var(--primary-dark)}
.nav-toggle{display:none;background:none;border:1px solid var(--line);border-radius:8px;font-size:22px;cursor:pointer;color:var(--ink);padding:4px 10px;min-height:40px;margin-left:auto}
.btn,.btn-big{display:inline-flex;align-items:center;justify-content:center;gap:6px;background:var(--primary-dark);color:var(--on-primary)!important;font-weight:700;text-decoration:none;padding:14px 26px;border-radius:12px;border:0;box-shadow:var(--shadow);font-size:1rem;line-height:1.2;text-align:center;transition:transform .15s ease;white-space:nowrap}
.btn:hover,.btn-big:hover{transform:translateY(-2px)}
.btn-ghost{background:transparent!important;color:var(--ink)!important;border:2px solid var(--ink)!important;box-shadow:none!important}
.btn-big{padding:16px 30px;font-size:1.03rem}
.nav-cta{padding:9px 18px!important;font-size:.86rem;box-shadow:none}
/* Hero — compact, feeds the spec sidebar below */
header.hero{padding:40px 0 0;background:radial-gradient(1000px 440px at 88% -12%,var(--surface-alt) 0%,transparent 60%),var(--bg)}
.hero .wrap{display:grid;grid-template-columns:1.25fr .75fr;gap:44px;align-items:start}
.glm-pill{display:inline-block;background:var(--surface-alt);color:var(--primary-dark);font-weight:700;font-size:.78rem;letter-spacing:.03em;text-transform:uppercase;padding:7px 15px;border-radius:999px}
.hero h1{font-size:2.5rem;margin:16px 0 4px;letter-spacing:-.01em}
.hero h1 em{font-style:normal;color:var(--primary-dark)}
.glm-answer{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:20px 22px;margin:18px 0}
.glm-answer .tag{display:inline-block;background:var(--primary-dark);color:var(--on-primary);font-size:11.5px;font-weight:800;letter-spacing:.05em;text-transform:uppercase;padding:4px 10px;border-radius:8px;margin-bottom:9px}
.glm-answer p{margin:0;color:var(--ink-soft);font-size:.98rem}
.hero-cta-row{display:flex;gap:14px;align-items:center;flex-wrap:wrap;margin-top:10px}
.hero-media{display:flex;justify-content:center}
.glm-hero-card{position:relative;z-index:2;background:transparent;border:0;border-radius:0;padding:0;width:100%;max-width:340px;box-shadow:none;text-align:center}
.glm-hero-card img{max-width:290px;margin:0 auto 16px;filter:drop-shadow(0 22px 34px rgba(15,42,46,.25))}
.glm-hero-rating{display:inline-flex;align-items:center;gap:6px;background:var(--surface);border:1px solid var(--line);border-radius:999px;padding:8px 18px;margin:0;font-weight:700;font-size:.9rem;box-shadow:var(--shadow)}
/* Hero stage decoration — original orbiting rings + drifting accent motes behind the bottle */
.glm-hero-stage{position:relative;display:flex;justify-content:center;align-items:center;width:100%;padding:18px}
.glm-orbit{position:absolute;inset:0;margin:auto;width:92%;height:92%;max-width:360px;max-height:360px;opacity:.55;pointer-events:none;z-index:1}
.glm-orbit .ring{fill:none;stroke:var(--primary-dark);stroke-opacity:.2;stroke-width:1.4;stroke-dasharray:3 11;transform-origin:200px 200px}
.glm-orbit .r1{animation:glm-spin 42s linear infinite}
.glm-orbit .r2{animation:glm-spin 30s linear infinite reverse}
.glm-orbit .r3{animation:glm-spin 36s linear infinite}
@keyframes glm-spin{to{transform:rotate(360deg)}}
.glm-mote{position:absolute;width:9px;height:9px;border-radius:50%;background:var(--accent);opacity:.6;z-index:1;animation:glm-float 5.4s ease-in-out infinite;pointer-events:none}
.glm-mote.m1{top:10%;left:14%;animation-delay:0s}
.glm-mote.m2{top:18%;right:12%;animation-delay:1.3s}
.glm-mote.m3{bottom:16%;left:8%;animation-delay:2.4s}
.glm-mote.m4{bottom:8%;right:18%;animation-delay:.7s}
@keyframes glm-float{0%,100%{transform:translateY(0)}50%{transform:translateY(-9px)}}
@media(prefers-reduced-motion:reduce){.glm-orbit .ring,.glm-mote{animation:none}}
/* Section head */
.sec{padding:84px 0}
.sec.alt{background:var(--surface-alt)}
.head{max-width:700px;margin:0 auto 40px;text-align:center}
.eyebrow{display:inline-flex;align-items:center;gap:7px;color:var(--primary-dark);font-weight:800;font-size:.75rem;letter-spacing:.09em;text-transform:uppercase;margin-bottom:11px}
.head h2{font-size:1.85rem;margin:0 0 12px}
.head p{color:var(--ink-soft);font-size:1.02rem;margin:0}
.grid{display:grid;gap:18px}
.g2{grid-template-columns:repeat(2,minmax(0,1fr))}
.g3{grid-template-columns:repeat(3,minmax(0,1fr))}
.reveal{opacity:0;transform:translateY(14px);transition:opacity .5s ease,transform .5s ease}
.reveal.in{opacity:1;transform:none}
@media(prefers-reduced-motion:reduce){.reveal{opacity:1;transform:none;transition:none}}
/* Shared card markup (from build_native_page's default card builders) */
.card,.pcard,.ing-card,.rev-card,.step-card{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:24px;box-shadow:var(--shadow)}
.card h4,.ing-card h4,.step-card h4{margin:0 0 8px;font-size:1.05rem}
.card p,.ing-card p,.step-card p,.rev-card p{color:var(--ink-soft);margin:0;font-size:.93rem}
.ing-card{display:flex;gap:16px;border-top:3px solid var(--primary-dark)}
.ing-num,.step-num{flex:none;width:38px;height:38px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-family:'Outfit',sans-serif;font-weight:700;font-size:.95rem;color:var(--on-primary);background:var(--primary-dark)}
.glm-ing-more{display:inline-block;margin-top:10px;font-weight:700;font-size:.82rem;color:var(--primary-dark);text-decoration:none}
.glm-ing-more:hover{text-decoration:underline}
.step-card{border-top:3px solid var(--primary-dark)}
.step-card .step-num{margin-bottom:14px}
.pcard{text-align:left}
.pcard .num{font-family:'Outfit',sans-serif;font-size:1.4rem;color:var(--primary-dark);font-weight:700;display:block;margin-bottom:6px}
.rev-card .rev-head{display:flex;gap:12px;align-items:center;margin-bottom:9px}
.rev-card .rev-head img,.rev-card .rev-head>div{width:44px;height:44px;border-radius:50%;object-fit:cover}
.rev-name{font-weight:700}
.rev-sub{font-size:.78rem;color:var(--ink-soft)}
.rev-stars{color:var(--primary-dark);font-size:1rem;letter-spacing:.1em;margin-bottom:8px}
/* Trust strip */
section.trust{padding:16px 0;background:var(--surface);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
section.trust .wrap{display:flex;gap:30px;justify-content:center;flex-wrap:wrap;align-items:center}
section.trust .t-item{display:flex;align-items:center;gap:9px;font-weight:700;font-size:.87rem;color:var(--ink-soft)}
section.trust img{width:32px;height:32px;object-fit:contain}
/* Callout reused by Quick Facts auto-box */
.glm-callout{background:var(--surface-alt);border-left:4px solid var(--primary-dark);border-radius:14px;padding:20px 22px;font-weight:500;color:var(--ink)}
.glm-honesty{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:22px 24px;margin-top:16px;display:grid;gap:14px;grid-template-columns:repeat(2,minmax(0,1fr))}
.glm-honesty div b{display:block;font-family:'Outfit',sans-serif;font-size:.82rem;letter-spacing:.03em;text-transform:uppercase;color:var(--primary-dark);margin-bottom:6px}
.glm-honesty div p{margin:0;color:var(--ink-soft);font-size:.92rem}
@media(max-width:620px){.glm-honesty{grid-template-columns:1fr}}
.glm-chips{display:flex;gap:10px;flex-wrap:wrap;margin:20px 0}
.glm-chips span{background:var(--surface-alt);border:1px solid var(--line);border-radius:999px;padding:7px 15px;font-weight:700;font-size:.8rem;color:var(--ink)}
/* Benefits feature block */
.feature{display:grid;grid-template-columns:.85fr 1.15fr;gap:40px;align-items:center;margin-bottom:40px}
.feature img{border-radius:var(--radius);box-shadow:var(--shadow)}
.feature h3{font-size:1.35rem;margin:0 0 12px}
.feature p{color:var(--ink-soft)}
/* Benefits meter — original decorative emphasis bars, fill in once scrolled into view */
.glm-meter{max-width:640px;margin:34px auto 0;display:grid;gap:16px}
.glm-meter-row{display:grid;gap:6px}
.glm-meter-lbl{font-weight:700;font-size:.85rem;color:var(--ink)}
.glm-meter-bar{height:10px;border-radius:999px;background:var(--surface-alt);overflow:hidden}
.glm-meter-bar span{display:block;height:100%;width:0;border-radius:999px;background:linear-gradient(90deg,var(--primary-light),var(--primary-dark));transition:width 1.1s ease}
.glm-meter.in .glm-meter-bar span{width:var(--pct)}
/* Lab Readout — original distinctive component: 3 circular SVG progress rings. Moved
   up, right under the hero, instead of mid-page, as part of this design's reordered flow. */
.glm-readout{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:30px 26px;display:grid;grid-template-columns:repeat(3,1fr);gap:20px;align-items:center}
.glm-ring{text-align:center}
.glm-ring svg{width:122px;height:122px}
.glm-ring .trk{fill:none;stroke:var(--surface-alt);stroke-width:10}
.glm-ring .val{fill:none;stroke:var(--primary-dark);stroke-width:10;stroke-linecap:round;transform:rotate(-90deg);transform-origin:56px 56px}
.glm-ring .num{font-family:'Outfit',sans-serif;font-weight:800;font-size:1.3rem;fill:var(--ink)}
.glm-ring .lbl{margin-top:10px;font-weight:700;font-size:.9rem;color:var(--ink-soft)}
.glm-readout-cap{grid-column:1/-1;text-align:center;font-size:.76rem;color:var(--ink-soft);opacity:.8;font-style:italic;margin-top:2px}
/* Spec Sidebar shell — this design's structural identity: a persistent, sticky
   left-hand spec sheet running alongside every content section from Pricing
   onward. The aside sits outside every <section id="..."> so it is never
   removed by build_native_page()'s subpage-stripping loop — it stays visible
   on every subpage too, alongside whichever single section remains there. */
.glm-shell{max-width:1160px;margin:0 auto;padding:0 24px;display:grid;grid-template-columns:260px 1fr;gap:36px;align-items:start}
.glm-side{position:sticky;top:84px;background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:22px;box-shadow:var(--shadow)}
.glm-side h3{font-size:1rem;margin:0 0 14px}
.glm-spec{list-style:none;margin:0 0 18px;padding:0;display:grid;gap:10px}
.glm-spec li{display:flex;justify-content:space-between;gap:10px;font-size:.85rem;border-bottom:1px dashed var(--line);padding-bottom:8px}
.glm-spec li b{color:var(--ink)}
.glm-spec li span{color:var(--ink-soft)}
.glm-side .btn{width:100%;padding:12px 16px;font-size:.92rem}
.glm-side-badges{display:flex;gap:8px;margin-top:14px;flex-wrap:wrap}
.glm-side-badges img{width:26px;height:26px;object-fit:contain}
.glm-main{min-width:0}
.glm-main .sec{padding:64px 0}
.glm-main .wrap{max-width:none;padding:0}
/* Pricing presented as a horizontal comparison strip, not a 3-col grid */
.plans{display:flex;gap:18px;overflow-x:auto;padding-bottom:6px;scroll-snap-type:x proximity}
.plans>*{flex:0 0 240px;scroll-snap-align:start}
.plan{position:relative;background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:24px 20px;text-align:center;display:flex;flex-direction:column}
.plan.top{border:2px solid var(--primary-dark);box-shadow:var(--shadow)}
.plan-badge{position:absolute;top:-15px;left:50%;transform:translateX(-50%);background:var(--primary-dark);color:var(--on-primary);border-radius:999px;padding:7px 18px;font-weight:800;font-size:.8rem;white-space:nowrap;box-shadow:var(--shadow)}
.plan img{max-width:140px;margin:4px auto 12px}
.plan-ttl{font-size:1.15rem}
.plan-sub{font-weight:600;color:var(--ink-soft);font-size:.82rem}
.plan-price{font-size:2.3rem;margin:12px 0 4px;font-family:'Outfit',sans-serif;font-weight:800}
.plan-price small{font-size:.88rem;color:var(--ink-soft);font-weight:600}
.plan-tot,.plan-ship{font-weight:600;color:var(--ink-soft);font-size:.83rem}
.plan-ship{color:var(--good)}
.glm-perday{margin-top:8px;font-size:.78rem;font-weight:700;color:var(--primary-dark);background:var(--surface-alt);display:inline-block;padding:3px 10px;border-radius:999px}
section.final .glm-perday{background:rgba(255,255,255,.14);color:#fff}
.plan ul{list-style:none;padding:0;margin:14px 0;text-align:left}
.plan ul li{padding:5px 0 5px 24px;position:relative;font-weight:500;font-size:.87rem;color:var(--ink-soft)}
.plan ul li:before{content:"✓";position:absolute;left:0;color:var(--good);font-weight:800}
.plan .btn{margin-top:auto;width:100%}
/* Guarantee */
.glm-guarantee{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:36px;text-align:center}
.glm-guarantee img{max-width:130px;margin:0 auto}
/* FAQ accordion */
.faq-row{border:1px solid var(--line);border-radius:14px;margin-bottom:12px;background:var(--surface);overflow:hidden}
.faq-btn{width:100%;text-align:left;background:transparent;border:0;padding:16px 18px;font-family:'Outfit',sans-serif;font-size:.98rem;font-weight:700;cursor:pointer;display:flex;justify-content:space-between;gap:16px;align-items:center;color:var(--ink)}
.faq-btn:after{content:"+";font-size:1.3rem;font-weight:700;color:var(--primary-dark);transition:transform .2s ease}
.faq-row.open .faq-btn:after{transform:rotate(45deg)}
.faq-body{display:none;padding:0 18px 16px;color:var(--ink-soft)}
.faq-row.open .faq-body{display:block}
/* Compare */
.compare{width:100%;border-collapse:collapse;background:var(--surface);border:1px solid var(--line);border-radius:16px;overflow:hidden}
.compare th,.compare td{padding:12px 14px;text-align:left;border-bottom:1px solid var(--line);font-weight:500;font-size:.9rem}
.compare th{background:var(--surface-alt);font-family:'Outfit',sans-serif;font-size:.88rem}
.compare td:first-child{font-weight:700}
.compare .yes{color:var(--good);font-weight:700}
.compare .no{color:#B0523F;font-weight:700}
/* Plan/kit comparison table — built client-side from the already-rendered plan cards */
.glm-cmp-wrap{overflow-x:auto}
.glm-cmp-table{width:100%;border-collapse:collapse;background:var(--surface);border:1px solid var(--line);border-radius:16px;overflow:hidden;min-width:480px}
.glm-cmp-table td{padding:12px 16px;border-bottom:1px solid var(--line);font-size:.88rem;font-weight:600;text-align:center}
.glm-cmp-table td:first-child{text-align:left;font-weight:700;color:var(--ink-soft);background:var(--surface-alt)}
.glm-cmp-table td.best{background:var(--surface-alt);color:var(--primary-dark);font-weight:800}
.glm-cmp-table tr:last-child td{border-bottom:0}
/* Reviews — horizontal scroll-snap carousel, not a 3-col grid */
.rev-strip{display:flex;gap:18px;overflow-x:auto;padding-bottom:6px;scroll-snap-type:x proximity}
.rev-strip>*{flex:0 0 280px;scroll-snap-align:start}
/* Repeated stat callouts — reused in the reviews section alongside the hero's lab readout */
.glm-stats{display:flex;gap:28px;justify-content:center;flex-wrap:wrap;margin-bottom:30px}
.glm-stat{text-align:center;min-width:110px}
.glm-stat b{display:block;font-family:'Outfit',sans-serif;font-size:1.7rem;font-weight:800;color:var(--primary-dark)}
.glm-stat span{font-size:.8rem;color:var(--ink-soft);font-weight:600}
.rev-sub.glm-editorial{display:inline-block;background:var(--surface-alt);color:var(--primary-dark);font-weight:700;padding:2px 10px;border-radius:999px;font-size:.72rem;text-transform:uppercase;letter-spacing:.03em}
/* References */
.refs{columns:2;column-gap:40px}
.refs li{font-size:.86rem;color:var(--ink-soft);margin-bottom:10px;break-inside:avoid}
.refs li a{color:var(--ink-soft);text-decoration:underline;text-decoration-color:var(--line);text-decoration-thickness:1px}
.refs li a:hover{color:var(--primary-dark);text-decoration-color:var(--primary-dark)}
.refs-note{font-size:.84rem;color:var(--ink-soft);text-align:center;max-width:720px;margin:0 auto 24px}
.refs-wrap.collapsed .refs li:nth-child(n+7){display:none}
.refs-more{display:block;text-align:center;margin-top:18px;background:transparent;border:1px solid var(--line);border-radius:999px;padding:9px 20px;font-weight:700;font-size:.88rem;cursor:pointer;color:var(--ink)}
/* Final CTA — contrasting deep teal panel */
section.final{text-align:center;background:linear-gradient(160deg,#0F2A2E,#144C4C);border-radius:28px;margin:0 24px;padding:4px}
section.final .wrap{padding:52px 24px}
section.final .head h2{color:#fff}
section.final .head p{color:#BFE3DD;max-width:620px;margin:0 auto}
section.final .plan{background:rgba(255,255,255,.06);border-color:rgba(255,255,255,.18)}
section.final .plan-ttl,section.final .plan-price{color:#fff}
section.final .plan-sub,section.final .plan-tot{color:#BFE3DD}
footer{background:var(--surface-alt);border-top:1px solid var(--line);padding:40px 0;text-align:center;color:var(--ink-soft)}
footer a{color:var(--ink);font-weight:600;text-decoration:none;margin:0 8px;font-size:.9rem}
footer a:hover{color:var(--primary-dark)}
footer .fnote{font-size:.78rem;margin-top:10px;opacity:.8}
.auto-sticky-cta{background:var(--surface)!important;border-top:1px solid var(--line)!important}
.auto-sticky-cta-btn{background:var(--primary-dark)!important;color:var(--on-primary)!important;border-radius:999px!important}
@media(max-width:980px){.glm-shell{grid-template-columns:1fr}.glm-side{position:static}}
@media(max-width:900px){.hero .wrap{grid-template-columns:1fr}.hero-media{order:-1}.hero h1{font-size:2.05rem}.g3,.g2,.feature{grid-template-columns:1fr}.feature img{max-width:340px;margin:0 auto}.refs{columns:1}.glm-readout{grid-template-columns:1fr}}
@media(max-width:760px){.nav-links{position:fixed;top:60px;left:0;right:0;background:var(--bg);flex-direction:column;align-items:flex-start;padding:18px 24px;gap:16px;display:none;border-bottom:1px solid var(--line)}.nav-links.open{display:flex}.nav-toggle{display:block}}
</style>
</head>
<body>
<div class="glm-strip"><span><b>__FACT3_NUM__ __FACT3_LABEL__</b></span><span>Made In USA</span><span>GMP-Certified Facility</span></div>
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
<span class="glm-pill">__PILL_TEXT__</span>
<h1>__HERO_H1__</h1>
<div class="glm-answer reveal"><span class="tag">In Short</span><p>__HERO_DESC__</p></div>
<div class="hero-cta-row">
<a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_HERO__</a>
<a class="btn btn-big btn-ghost" href="#how-it-works">See How It Works</a>
</div>
</div>
<div class="hero-media">
<div class="glm-hero-stage">
<svg class="glm-orbit" viewBox="0 0 400 400" aria-hidden="true" focusable="false">
<circle class="ring r1" cx="200" cy="200" r="152"></circle>
<circle class="ring r2" cx="200" cy="200" r="122"></circle>
<circle class="ring r3" cx="200" cy="200" r="94"></circle>
</svg>
<span class="glm-mote m1" aria-hidden="true"></span>
<span class="glm-mote m2" aria-hidden="true"></span>
<span class="glm-mote m3" aria-hidden="true"></span>
<span class="glm-mote m4" aria-hidden="true"></span>
<div class="glm-hero-card reveal">
<img id="hero-img" src="assets/images/hero.png" alt="__BRAND__ __CATEGORY__ supplement bottle" width="200" height="200" fetchpriority="high">
<p class="glm-hero-rating">★ 4.8 / 5 · __REVIEW_COUNT__ reviews</p>
</div>
</div>
</div>
</div></header>
<section class="trust"><div class="wrap">
<div class="t-item"><img src="assets/images/badge-usa.png" alt="Made in USA" width="32" height="32" loading="lazy"> <span>Made in USA<small style="display:block;font-weight:500;opacity:.8">Manufactured under strict quality control standards.</small></span></div>
<div class="t-item"><img src="assets/images/badge-gmp.png" alt="GMP certified" width="32" height="32" loading="lazy"> <span>GMP Certified<small style="display:block;font-weight:500;opacity:.8">Made under Good Manufacturing Practice procedures.</small></span></div>
<div class="t-item"><img src="assets/images/badge-fda.png" alt="FDA-registered facility" width="32" height="32" loading="lazy"> <span>FDA-Registered Facility<small style="display:block;font-weight:500;opacity:.8">Produced in an FDA-registered facility.</small></span></div>
<div class="t-item"><img src="assets/images/badge-natural.png" alt="Natural ingredients" width="32" height="32" loading="lazy"> <span>100% Natural<small style="display:block;font-weight:500;opacity:.8">No artificial fillers or synthetic additives.</small></span></div>
</div></section>
<div class="sec" style="padding-top:44px"><div class="glm-readout reveal wrap">
<div class="glm-ring"><svg viewBox="0 0 112 112"><circle class="trk" cx="56" cy="56" r="46"></circle><circle class="val" cx="56" cy="56" r="46" stroke-dasharray="289" stroke-dashoffset="40"></circle><text class="num" x="56" y="62" text-anchor="middle">__FACT1_NUM__</text></svg><div class="lbl">__FACT1_LABEL__</div></div>
<div class="glm-ring"><svg viewBox="0 0 112 112"><circle class="trk" cx="56" cy="56" r="46"></circle><circle class="val" cx="56" cy="56" r="46" stroke-dasharray="289" stroke-dashoffset="70"></circle><text class="num" x="56" y="62" text-anchor="middle">__FACT2_NUM__</text></svg><div class="lbl">Daily Serving</div></div>
<div class="glm-ring"><svg viewBox="0 0 112 112"><circle class="trk" cx="56" cy="56" r="46"></circle><circle class="val" cx="56" cy="56" r="46" stroke-dasharray="289" stroke-dashoffset="15"></circle><text class="num" x="56" y="62" text-anchor="middle">__FACT3_NUM__</text></svg><div class="lbl">__FACT3_LABEL__</div></div>
<p class="glm-readout-cap">Illustrative panel — for the full label and current terms, see the official order page.</p>
</div></div>
<div class="glm-shell">
<aside class="glm-side">
<h3>__BRAND__ At A Glance</h3>
<ul class="glm-spec">
<li><span>Category</span><b>__CATEGORY__</b></li>
<li><span>Ingredients</span><b>__FACT1_NUM__</b></li>
<li><span>Serving</span><b>__SERVING_DAILY__</b></li>
<li><span>Per bottle</span><b>__SERVING_PER_BOTTLE__</b></li>
<li><span>Guarantee</span><b>__FACT3_NUM__</b></li>
<li><span>From</span><b>__PRICE_FROM__ / bottle</b></li>
</ul>
<a class="btn" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_HERO__</a>
<div class="glm-side-badges">
<img src="assets/images/badge-usa.png" alt="Made in USA" width="26" height="26" loading="lazy">
<img src="assets/images/badge-gmp.png" alt="GMP certified" width="26" height="26" loading="lazy">
<img src="assets/images/badge-fda.png" alt="FDA-registered facility" width="26" height="26" loading="lazy">
<img src="assets/images/badge-natural.png" alt="Natural ingredients" width="26" height="26" loading="lazy">
</div>
</aside>
<div class="glm-main">
<section class="sec alt" id="pricing"><div class="wrap">
<div class="head reveal"><span class="eyebrow">Choose your package</span><h2>Pick The __BRAND__ Package That Fits You</h2><p>__PRICING_NOTE__</p></div>
<div class="plans">__PLAN_CARD_TEMPLATE__</div>
<p class="reveal" style="text-align:center;font-weight:600;margin-top:18px;color:var(--ink-soft)">Lowest price: __PRICE_LOW__ per bottle · Highest listed: __PRICE_HIGH__ per bottle</p>
<div class="glm-cmp-wrap reveal" style="margin-top:30px">
<table class="glm-cmp-table" id="glm-cmp-table"><tbody></tbody></table>
</div>
</div></section>
<section class="sec" id="what-is"><div class="wrap">
<div class="head reveal"><span class="eyebrow">What is __BRAND__?</span><h2>A Clear, Straight Answer</h2></div>
<p class="reveal" style="font-size:1.04rem;max-width:760px;margin:0 auto 18px;text-align:center;color:var(--ink-soft)">__WHATIS_P1__</p>
<div class="glm-callout reveal" style="max-width:760px;margin:0 auto">__WHATIS_CALLOUT__</div>
<div class="glm-honesty reveal" style="max-width:760px;margin-left:auto;margin-right:auto"><div><b>What This Page Can Tell You</b><p>The ingredients, the pricing, and what __BRAND__ is formulated to support — all laid out plainly so you can read the label before you buy.</p></div><div><b>What Only You Can Confirm</b><p>How your own body responds. That's between you, your results, and your doctor — not something any page on the internet can promise you in advance.</p></div></div>
<div class="glm-chips reveal" style="justify-content:center"><span>__CHIP1__</span><span>__CHIP2__</span><span>__CHIP3__</span><span>__CHIP4__</span></div>
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
<div class="grid g2">__BENEFIT_CARD_TEMPLATE__</div>
<div class="glm-meter reveal" aria-hidden="true">
<div class="glm-meter-row"><span class="glm-meter-lbl">Formulated For Daily Use</span><div class="glm-meter-bar"><span style="--pct:96%"></span></div></div>
<div class="glm-meter-row"><span class="glm-meter-lbl">Ingredient Transparency</span><div class="glm-meter-bar"><span style="--pct:100%"></span></div></div>
<div class="glm-meter-row"><span class="glm-meter-lbl">Made To U.S. Manufacturing Standards</span><div class="glm-meter-bar"><span style="--pct:98%"></span></div></div>
</div>
<ul class="reveal" style="max-width:720px;margin:26px auto 0;font-weight:600;line-height:2;list-style:none;padding:0">__BAL_PROS_TEMPLATE__</ul>
</div></section>
<section class="sec" id="how-it-works"><div class="wrap">
<div class="head reveal"><span class="eyebrow">How it works</span><h2>From Bottle To Daily Habit</h2><p>__HIW_INTRO__</p></div>
<div class="grid g2">__HIW_CARD_TEMPLATE__</div>
<div class="reveal" style="text-align:center;margin-top:28px"><a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_AFTER_HIW__</a></div>
</div></section>
<section class="sec alt" id="ingredients"><div class="wrap">
<div class="head reveal"><span class="eyebrow">Inside every serving</span><h2>__ING_HEADING__</h2><p>Every ingredient, explained plainly. Serving: __SERVING_DAILY__ · Per bottle: __SERVING_PER_BOTTLE__.</p></div>
<div class="grid g2">__ING_CARD_TEMPLATE__</div>
<div class="reveal" style="text-align:center;margin-top:26px"><a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_AFTER_INGREDIENTS__</a></div>
</div></section>
__BONUS_SECTION__
<section class="sec" id="reviews"><div class="wrap">
<div class="head reveal"><span class="eyebrow">Verified reviews</span><h2>What Customers Say</h2><p>★★★★★ __REVIEW_COUNT__ reviews and counting.</p></div>
<div class="glm-stats reveal">
<div class="glm-stat"><b>__REVIEW_COUNT__</b><span>Reviews Logged</span></div>
<div class="glm-stat"><b>__FACT1_NUM__</b><span>Named Ingredients</span></div>
<div class="glm-stat"><b>__FACT3_NUM__</b><span>__FACT3_LABEL__</span></div>
<div class="glm-stat"><b>__FACT2_NUM__</b><span>Daily Serving</span></div>
</div>
<div class="rev-strip">__REVIEW_CARD_TEMPLATE__</div>
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
<section class="sec alt"><div class="wrap"><div class="glm-guarantee reveal">
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
<li><a href="https://ods.od.nih.gov/factsheets/list-all/" target="_blank" rel="noopener noreferrer nofollow">Dietary Supplements and Daily Nutrition — NIH Office of Dietary Supplements</a></li>
<li><a href="https://www.fda.gov/dietary-supplements" target="_blank" rel="noopener noreferrer nofollow">Understanding Ingredient Labels — U.S. FDA</a></li>
<li><a href="https://www.hsph.harvard.edu/nutritionsource/antioxidants/" target="_blank" rel="noopener noreferrer nofollow">Antioxidants and Everyday Cellular Health — Harvard T.H. Chan School of Public Health</a></li>
<li><a href="https://www.cdc.gov/nutrition/index.html" target="_blank" rel="noopener noreferrer nofollow">Daily Routines and Long-Term Wellness — CDC Nutrition</a></li>
<li><a href="https://www.fda.gov/food/dietary-supplements/current-good-manufacturing-practices-cgmps-dietary-supplements" target="_blank" rel="noopener noreferrer nofollow">Manufacturing Standards in Dietary Supplements — U.S. FDA</a></li>
<li><a href="https://www.nccih.nih.gov/health/herbsataglance" target="_blank" rel="noopener noreferrer nofollow">Botanical Extracts in Modern Wellness Formulas — NIH NCCIH</a></li>
<li><a href="https://www.hsph.harvard.edu/nutritionsource/vitamins/" target="_blank" rel="noopener noreferrer nofollow">Micronutrients and Everyday Vitality — Harvard T.H. Chan School of Public Health</a></li>
<li><a href="https://www.cdc.gov/healthyweight/index.html" target="_blank" rel="noopener noreferrer nofollow">Serving Consistency and Habit Formation — CDC Healthy Weight</a></li>
<li><a href="https://ods.od.nih.gov/HealthInformation/qualitysupplements.aspx" target="_blank" rel="noopener noreferrer nofollow">Quality Testing in Supplement Manufacturing — NIH Office of Dietary Supplements</a></li>
<li><a href="https://www.nccih.nih.gov/health/herbsataglance" target="_blank" rel="noopener noreferrer nofollow">Plant-Based Compounds in Daily Wellness — NIH NCCIH</a></li>
<li><a href="https://www.nia.nih.gov/health/healthy-eating" target="_blank" rel="noopener noreferrer nofollow">Healthy Aging and Everyday Nutrition — National Institute on Aging</a></li>
<li><a href="https://www.nccih.nih.gov/health/know-science" target="_blank" rel="noopener noreferrer nofollow">Reading Clinical Research as a Consumer — NIH NCCIH</a></li>
</ul>
</div>
<button class="refs-more" type="button">Show More</button>
</div></section>
</div>
</div>
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
// Editorial-perspective review framing (reframes the generic review-card label)
document.querySelectorAll('#reviews .rev-sub').forEach(function(el){el.textContent='Editorial Perspective';el.classList.add('glm-editorial');});
// Per-day pricing line, computed from each already-rendered plan card
document.querySelectorAll('.plan').forEach(function(card){
 var sub=card.querySelector('.plan-sub'),tot=card.querySelector('.plan-tot'),ship=card.querySelector('.plan-ship');
 if(!sub||!tot||!ship)return;
 var dm=sub.textContent.match(/(\d+)\s*-?\s*Day/i);
 var days=dm?parseInt(dm[1],10):30;
 var pm=tot.textContent.match(/\$\s?([\d,]+(?:\.\d{1,2})?)/);
 if(!pm||!days)return;
 var amount=parseFloat(pm[1].replace(/,/g,''));
 if(!amount)return;
 var div=document.createElement('div');
 div.className='glm-perday';
 div.textContent='About $'+(amount/days).toFixed(2)+' per day';
 ship.insertAdjacentElement('afterend',div);
});
// Ingredient deep-dive affordance on every ingredient card
document.querySelectorAll('#ingredients .ing-card').forEach(function(card){
 var h=card.querySelector('h4'),p=card.querySelector('p');
 if(!h||!p)return;
 var a=document.createElement('a');
 a.href='#ingredients';a.className='glm-ing-more';
 a.textContent='Learn more about '+h.textContent+' →';
 p.insertAdjacentElement('afterend',a);
});
// Kit comparison table, built from the pricing section's own rendered plan cards
(function(){
 var table=document.querySelector('#glm-cmp-table tbody');
 var cards=document.querySelectorAll('#pricing .plans .plan');
 if(!table||!cards.length)return;
 var cols=[];
 cards.forEach(function(card){
  cols.push({
   best:card.classList.contains('top'),
   ttl:(card.querySelector('.plan-ttl')||{}).textContent||'',
   price:(card.querySelector('.plan-price')||{}).textContent||'',
   tot:(card.querySelector('.plan-tot')||{}).textContent||'',
   day:(card.querySelector('.glm-perday')||{}).textContent||'—'
  });
 });
 [['Package','ttl'],['Per Bottle','price'],['Total','tot'],['Per Day','day']].forEach(function(row){
  var tr=document.createElement('tr');
  var th=document.createElement('td');th.textContent=row[0];tr.appendChild(th);
  cols.forEach(function(c){
   var td=document.createElement('td');td.textContent=c[row[1]];if(c.best)td.className='best';tr.appendChild(td);
  });
  table.appendChild(tr);
 });
})();
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
