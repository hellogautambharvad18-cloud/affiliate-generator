<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>__TITLE__</title>
<meta name="description" content="__META_DESC__">
<link rel="canonical" href="__CANONICAL__">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;0,9..144,700;0,9..144,900;1,9..144,500&family=Work+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
:root{
 --primary:__COLOR_PRIMARY__;
 --primary-dark:__COLOR_DARK__;
 --primary-light:__COLOR_LIGHT__;
 --accent:__COLOR_ACCENT__;
 --on-primary:__COLOR_ON_PRIMARY__;
 --ink:#171f1a;
 --paper:#f7f1e2;
 --paper2:#efe4c8;
 --card:#fffdf7;
 --text:#1d241d;
 --muted:#686d5f;
 --border:#e3d9ba;
 --radius:20px;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:'Work Sans',system-ui,sans-serif;color:var(--text);background:var(--paper);line-height:1.65;-webkit-font-smoothing:antialiased}
h1,h2,h3,h4{font-family:'Fraunces',Georgia,serif;line-height:1.12;letter-spacing:-.01em;color:var(--ink)}
.wrap{max-width:1180px;margin:0 auto;padding:0 24px}
a{color:inherit;text-decoration:none}
img{max-width:100%;display:block}
ul{list-style:none}
section{padding:96px 0}
@media(max-width:640px){section{padding:64px 0}}

.ticker-wrap{background:var(--ink);overflow:hidden;padding:11px 0;border-bottom:1px solid rgba(255,255,255,.08)}
.ticker{display:flex;gap:48px;white-space:nowrap;animation:scroll 26s linear infinite;width:max-content}
.ticker span{color:var(--paper2);font-size:.78rem;font-weight:600;letter-spacing:.03em;display:flex;align-items:center;gap:8px}
.ticker span b{color:var(--primary);font-weight:700}
@keyframes scroll{from{transform:translateX(0)}to{transform:translateX(-50%)}}

nav{position:sticky;top:0;z-index:80;background:rgba(247,241,226,.92);backdrop-filter:blur(10px);border-bottom:1px solid var(--border)}
nav .wrap{display:flex;align-items:center;justify-content:space-between;gap:24px;padding:16px 24px}
.logo{display:flex;align-items:center;gap:9px;font-family:'Fraunces',serif;font-weight:700;font-size:1.35rem;color:var(--ink)}
.logo svg{width:24px;height:24px;flex:none}
.navlinks{display:flex;align-items:center;gap:26px;flex-wrap:wrap}
.navlinks a{font-size:.87rem;font-weight:600;color:var(--ink);opacity:.8}
.navlinks a:hover{opacity:1;color:var(--primary-dark)}
.nav-cta{background:var(--ink)!important;color:var(--paper)!important;padding:11px 22px;border-radius:999px;opacity:1!important;font-weight:700!important}
.nav-cta:hover{background:var(--primary-dark)!important}
@media(max-width:960px){.navlinks{display:none}}

.btn{display:inline-flex;align-items:center;gap:10px;background:var(--primary);color:var(--on-primary);padding:17px 32px;border-radius:999px;font-weight:700;font-size:1rem;cursor:pointer;border:none;box-shadow:0 10px 24px -8px rgba(0,0,0,.35);transition:.15s ease}
.btn:hover{background:var(--primary-dark);transform:translateY(-2px)}
.btn-ghost{display:inline-flex;align-items:center;gap:8px;background:transparent;color:var(--paper);padding:16px 28px;border-radius:999px;font-weight:600;font-size:.96rem;border:1.5px solid rgba(247,241,226,.35)}
.btn-ghost:hover{border-color:var(--paper)}
.btn-dark{display:inline-flex;align-items:center;gap:10px;background:var(--ink);color:var(--paper);padding:17px 32px;border-radius:999px;font-weight:700;font-size:1rem}
.btn-dark:hover{background:var(--primary-dark)}
.btn-sub{display:block;font-size:.72rem;font-weight:500;opacity:.85;margin-top:2px}
.btn-wide{width:100%;justify-content:center}

.hero{background:radial-gradient(1200px 600px at 15% -10%,#233c30 0%,var(--ink) 55%);position:relative;overflow:hidden;padding:88px 0 110px}
.hero-grid{display:grid;grid-template-columns:1.05fr .95fr;gap:64px;align-items:center;position:relative;z-index:2}
.eyebrow{display:inline-flex;align-items:center;gap:8px;font-size:.76rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--primary);margin-bottom:18px}
.eyebrow:before{content:'';width:22px;height:1.5px;background:var(--primary)}
.hero h1{font-size:2.9rem;color:var(--paper);font-weight:600;margin-bottom:20px}
.hero .lede{font-size:1.08rem;color:rgba(247,241,226,.72);max-width:520px;margin-bottom:28px;font-weight:400}
.rating-row{display:flex;align-items:center;gap:12px;margin-bottom:30px}
.stars{color:var(--primary);letter-spacing:2px;font-size:1.05rem}
.rating-row span{font-size:.86rem;color:rgba(247,241,226,.65);font-weight:600}
.hero-actions{display:flex;gap:14px;flex-wrap:wrap;margin-bottom:30px}
.hero-checks{display:grid;grid-template-columns:1fr 1fr;gap:10px 22px;max-width:520px;list-style:none}
.hero-checks li{position:relative;padding-left:26px;font-size:.86rem;color:rgba(247,241,226,.78);font-weight:500}
.hero-checks li:before{content:'✓';position:absolute;left:0;top:0;color:var(--primary);font-weight:800}

.orbit{position:relative;width:100%;max-width:400px;aspect-ratio:1/1;margin:0 auto}
.orbit-ring{position:absolute;inset:0;border:1.5px dashed rgba(247,241,226,.16);border-radius:50%}
.orbit-ring.r2{inset:36px;border-color:rgba(247,241,226,.1)}
.hero-frame{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:220px;background:linear-gradient(155deg,var(--primary) 0%,var(--primary-dark) 100%);border-radius:32px;padding:26px;box-shadow:0 30px 60px -20px rgba(0,0,0,.6),inset 0 2px 0 rgba(255,255,255,.15)}
.hero-frame img{border-radius:16px;filter:drop-shadow(0 16px 26px rgba(0,0,0,.4))}
.chip{position:absolute;background:rgba(247,241,226,.08);border:1px solid rgba(247,241,226,.18);color:var(--paper);font-size:.72rem;font-weight:600;padding:8px 14px;border-radius:999px;backdrop-filter:blur(4px);white-space:nowrap;max-width:150px;overflow:hidden;text-overflow:ellipsis}
.chip.c1{top:2%;left:50%}
.chip.c2{top:22%;left:-6%}
.chip.c3{top:70%;left:-4%}
.chip.c4{top:80%;left:56%}
@media(max-width:1050px){.hero-grid{grid-template-columns:1fr}.orbit{max-width:320px;margin-top:20px}.hero h1{font-size:2.3rem}.hero-checks{grid-template-columns:1fr}}
@media(max-width:640px){.chip{display:none}}

.head{text-align:center;max-width:640px;margin:0 auto 52px}
.head .eyebrow{justify-content:center}
.head .eyebrow:before{display:none}
.head h2{font-size:2.1rem;font-weight:600;margin-bottom:14px}
.head p{color:var(--muted);font-size:1.02rem}

.trust{background:var(--card);border-top:1px solid var(--border);border-bottom:1px solid var(--border);padding:48px 0}
.trust .wrap{display:grid;grid-template-columns:repeat(4,1fr);gap:20px}
.tcard{display:flex;flex-direction:column;align-items:center;text-align:center;gap:10px;padding:10px}
.tcard .ic{width:52px;height:52px;border-radius:50%;background:var(--paper2);display:flex;align-items:center;justify-content:center;color:var(--primary-dark)}
.tcard b{font-size:.86rem;font-weight:700}
.tcard span{font-size:.78rem;color:var(--muted)}
@media(max-width:760px){.trust .wrap{grid-template-columns:1fr 1fr}}

.grid{display:grid;gap:24px}
.g3{grid-template-columns:repeat(3,1fr)}
.g4{grid-template-columns:repeat(4,1fr)}
@media(max-width:900px){.g3,.g4{grid-template-columns:1fr 1fr}}
@media(max-width:560px){.g3,.g4{grid-template-columns:1fr}}

.pcard{background:var(--card);border:1px solid var(--border);border-radius:var(--radius);padding:30px 26px}
.pcard .num{font-family:'Fraunces',serif;font-size:1.5rem;color:var(--primary);font-weight:600;margin-bottom:14px}
.pcard h4{font-size:1.06rem;margin-bottom:10px;font-weight:600}
.pcard p{color:var(--muted);font-size:.93rem}

.card{background:var(--card);border:1px solid var(--border);border-radius:16px;padding:26px;text-align:center}
.card h4{font-size:.96rem;margin-bottom:8px;font-weight:700}
.card p{font-size:.84rem;color:var(--muted)}

.ing-card{display:flex;gap:16px;background:var(--card);border:1px solid var(--border);border-radius:var(--radius);padding:24px}
.ing-num{width:38px;height:38px;border-radius:12px;background:var(--primary);color:var(--on-primary);display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.9rem;flex:none}
.ing-card h4{font-size:1rem;font-weight:700;margin-bottom:6px}
.ing-card p{font-size:.87rem;color:var(--muted)}

.split{display:grid;grid-template-columns:.85fr 1.15fr;gap:64px;align-items:center}
@media(max-width:900px){.split{grid-template-columns:1fr}}
.statcard{background:var(--ink);border-radius:28px;padding:44px 36px;color:var(--paper)}
.statcard .big{font-family:'Fraunces',serif;font-size:3.4rem;font-weight:600;color:var(--primary);line-height:1}
.statcard .lbl{font-size:.86rem;color:rgba(247,241,226,.65);margin:6px 0 26px;font-weight:600}
.statcard hr{border:none;border-top:1px solid rgba(247,241,226,.15);margin:22px 0}
.statrow{display:flex;justify-content:space-between;font-size:.88rem;color:rgba(247,241,226,.85);margin-bottom:10px;font-weight:500}
.statrow b{color:var(--paper)}
.callout{background:var(--paper2);border-left:4px solid var(--primary);border-radius:0 12px 12px 0;padding:18px 22px;margin:22px 0;font-size:.95rem;font-weight:500;color:var(--text)}
.chiprow{display:flex;flex-wrap:wrap;gap:10px;margin-top:20px}
.chiprow span{background:var(--card);border:1px solid var(--border);border-radius:999px;padding:8px 16px;font-size:.8rem;font-weight:600;color:var(--primary-dark)}

.dark{background:var(--ink);color:var(--paper)}
.dark .head h2,.dark h3,.dark h4{color:var(--paper)}
.dark .head p{color:rgba(247,241,226,.6)}
.step-card{background:rgba(247,241,226,.05);border:1px solid rgba(247,241,226,.14);border-radius:var(--radius);padding:26px}
.step-num{width:38px;height:38px;border-radius:12px;background:var(--primary);color:var(--on-primary);display:flex;align-items:center;justify-content:center;font-weight:700;font-family:'Fraunces',serif;margin-bottom:16px}
.step-card h4{color:var(--paper);font-size:1.02rem;margin-bottom:8px;font-weight:600}
.step-card p{color:rgba(247,241,226,.6);font-size:.88rem}

.tblwrap{overflow-x:auto;border-radius:var(--radius);border:1px solid var(--border)}
table.cmp{width:100%;border-collapse:collapse;min-width:640px;background:var(--card)}
table.cmp th{text-align:left;padding:18px 22px;font-size:.82rem;text-transform:uppercase;letter-spacing:.04em;font-weight:700;background:var(--ink);color:var(--paper)}
table.cmp th:first-child{color:rgba(247,241,226,.55);font-weight:600}
table.cmp th.hl{background:var(--primary-dark)}
table.cmp td{padding:18px 22px;font-size:.92rem;border-top:1px solid var(--border);vertical-align:top}
table.cmp td:first-child{color:var(--muted);font-weight:600;white-space:nowrap}
table.cmp td.bad{color:#8a5a3f}
table.cmp td.bad:before{content:'✕ ';color:#b4401f;font-weight:800}
table.cmp td.good{color:var(--primary-dark);font-weight:600;background:var(--primary-light)}
table.cmp td.good:before{content:'✓ ';color:var(--primary);font-weight:800}

.rev-card{background:var(--card);border:1px solid var(--border);border-radius:var(--radius);padding:28px}
.rev-stars{color:var(--primary);font-size:.95rem;margin-bottom:12px}
.rev-card p{font-size:.93rem;color:var(--text);margin-bottom:18px}
.rev-head{display:flex;align-items:center;gap:12px}
.rev-head img{width:42px;height:42px;border-radius:50%;object-fit:cover}
.rev-name{font-weight:700;font-size:.88rem}
.rev-sub{font-size:.76rem;color:var(--muted)}
.rev-board{display:flex;justify-content:center;gap:64px;margin-top:52px;flex-wrap:wrap;text-align:center}
.rev-board b{display:block;font-family:'Fraunces',serif;font-size:2.1rem;font-weight:600;color:var(--primary)}
.rev-board span{font-size:.78rem;color:var(--muted);font-weight:700;text-transform:uppercase;letter-spacing:.03em}

.plans{display:grid;grid-template-columns:repeat(3,1fr);gap:26px;align-items:stretch}
@media(max-width:900px){.plans{grid-template-columns:1fr}}
.plan{background:var(--card);border:1.5px solid var(--border);border-radius:24px;padding:32px 26px;text-align:center;display:flex;flex-direction:column;position:relative}
.plan.top{border-color:var(--primary);box-shadow:0 18px 40px -16px rgba(0,0,0,.28);transform:translateY(-8px)}
@media(max-width:900px){.plan.top{transform:none}}
.plan img{max-width:110px;margin:0 auto 14px}
.plan-badge{position:absolute;top:-14px;left:50%;transform:translateX(-50%);background:var(--primary);color:var(--on-primary);font-size:.72rem;font-weight:800;padding:7px 18px;border-radius:999px;white-space:nowrap}
.plan-ttl{font-family:'Fraunces',serif;font-weight:600;font-size:1.2rem;margin-bottom:4px}
.plan-sub{font-size:.8rem;color:var(--muted);margin-bottom:20px;font-weight:500}
.plan-price{font-family:'Fraunces',serif;font-size:2.4rem;font-weight:600;color:var(--ink)}
.plan-price small{font-size:.85rem;font-weight:500;color:var(--muted);font-family:'Work Sans',sans-serif}
.plan-tot{font-size:.84rem;color:var(--muted);margin:6px 0 4px}
.plan-ship{font-size:.8rem;color:var(--primary-dark);font-weight:700;margin-bottom:22px}
.plan ul{text-align:left;margin-bottom:24px;flex:1}
.plan ul li{font-size:.85rem;padding:7px 0 7px 26px;position:relative;font-weight:500;color:var(--text)}
.plan ul li:before{content:'✓';position:absolute;left:0;color:var(--primary-dark);font-weight:800}
.plan .btn{width:100%;justify-content:center;padding:16px}
.plan-note{text-align:center;margin-top:34px;font-size:.85rem;color:var(--muted)}

.guar{background:linear-gradient(120deg,var(--primary-dark),var(--ink));border-radius:32px;padding:56px 48px;display:flex;align-items:center;gap:48px;color:var(--paper)}
.guar .seal{width:120px;height:120px;border-radius:50%;border:2px dashed rgba(247,241,226,.4);display:flex;align-items:center;justify-content:center;flex:none;font-family:'Fraunces',serif;font-size:1.5rem;font-weight:700;color:var(--primary);text-align:center;line-height:1.1}
.guar h3{color:var(--paper);font-size:1.7rem;margin-bottom:12px;font-weight:600}
.guar p{color:rgba(247,241,226,.72);font-size:.96rem}
@media(max-width:760px){.guar{flex-direction:column;text-align:center;padding:40px 26px}}

.faq{max-width:800px;margin:0 auto}
.faq-row{border:1px solid var(--border);border-radius:16px;margin-bottom:14px;background:var(--card);overflow:hidden}
.faq-btn{width:100%;text-align:left;background:transparent;border:none;padding:22px 24px;font-size:1rem;font-weight:700;font-family:'Work Sans',sans-serif;cursor:pointer;color:var(--ink);display:flex;justify-content:space-between;align-items:center;gap:16px}
.faq-btn:after{content:'+';font-size:1.5rem;color:var(--primary);font-weight:400;flex:none}
.faq-body{max-height:0;overflow:hidden;transition:max-height .25s ease}
.faq-body p{padding:0 24px 22px;color:var(--muted);font-size:.92rem}
.faq-row.open .faq-btn:after{content:'−'}

.final{background:linear-gradient(135deg,var(--primary) 0%,var(--primary-dark) 55%,var(--ink) 100%);border-radius:36px;padding:64px 40px;text-align:center;color:#fff}
.final h2{color:#fff;font-size:2.2rem;margin-bottom:14px;font-weight:600}
.final p{color:rgba(255,255,255,.85);margin-bottom:26px;font-size:1rem;max-width:540px;margin-left:auto;margin-right:auto}
.final img{max-width:160px;margin:0 auto 24px}
.final .old{text-decoration:line-through;opacity:.7;font-size:1rem}
.final .new{font-family:'Fraunces',serif;font-size:2rem;font-weight:600;margin-bottom:22px}

footer{background:var(--ink);color:rgba(247,241,226,.7);padding:64px 0 30px;font-size:.86rem}
.foot-top{display:grid;grid-template-columns:1.3fr 1fr 1fr;gap:40px;margin-bottom:36px}
@media(max-width:760px){.foot-top{grid-template-columns:1fr}}
.foot-top h5{color:var(--paper);font-size:.82rem;text-transform:uppercase;letter-spacing:.05em;margin-bottom:16px;font-weight:700}
.foot-top ul li{margin-bottom:10px}
.foot-top a{color:rgba(247,241,226,.68);font-weight:500}
.foot-top a:hover{color:var(--primary)}
footer hr{border:none;border-top:1px solid rgba(247,241,226,.12);margin:26px 0}
footer p{margin-bottom:12px;color:rgba(247,241,226,.5);font-size:.78rem;line-height:1.7}
.cr{margin-top:16px;font-size:.78rem;color:rgba(247,241,226,.4);font-weight:500}

.sticky-bar{position:fixed;bottom:0;left:0;right:0;background:var(--card);border-top:1px solid var(--border);padding:14px 20px;display:flex;align-items:center;justify-content:space-between;gap:16px;box-shadow:0 -8px 24px rgba(0,0,0,.1);z-index:70}
.sticky-bar b{font-weight:700;font-size:1.02rem;font-family:'Fraunces',serif}
.sticky-bar small{display:block;color:var(--muted);font-size:.73rem;font-weight:600}
@media(min-width:761px){.sticky-bar{display:none}}
@media(max-width:760px){body{padding-bottom:82px}}
</style>
</head>
<body>

<div class="ticker-wrap"><div class="ticker">
<span>✓ Made In The USA</span><span>✓ __FACT1_NUM__ Named Ingredients — No Proprietary Blends</span><span>✓ FDA-Registered, GMP-Certified Facility</span><span>✓ 60-Day Money-Back Guarantee</span><span>★★★★★ <b>4.8/5</b> — __REVIEW_COUNT__ Verified Reviews</span>
<span>✓ Made In The USA</span><span>✓ __FACT1_NUM__ Named Ingredients — No Proprietary Blends</span><span>✓ FDA-Registered, GMP-Certified Facility</span><span>✓ 60-Day Money-Back Guarantee</span><span>★★★★★ <b>4.8/5</b> — __REVIEW_COUNT__ Verified Reviews</span>
</div></div>

<nav><div class="wrap">
<a class="logo" href="index.html"><svg viewBox="0 0 24 24" fill="none"><path d="M12 2C8 6 4 9 4 14a8 8 0 0016 0c0-5-4-8-8-12z" style="fill:var(--primary-dark)"/><path d="M12 6c-2 3-4 5-4 8a4 4 0 008 0c0-3-2-5-4-8z" style="fill:var(--primary)"/></svg>__BRAND__</a>
<ul class="navlinks">
<li><a href="how-it-works.html">How It Works</a></li>
<li><a href="ingredients.html">Ingredients</a></li>
<li><a href="benefits.html">Benefits</a></li>
<li><a href="reviews.html">Reviews</a></li>
<li><a href="blog/index.html">Blog</a></li>
<li><a href="index.html#pricing">Pricing</a></li>
<li><a class="nav-cta" href="__AFFILIATE__">__CTA_HEADER__</a></li>
</ul>
</div></nav>

<header class="hero"><div class="wrap hero-grid">
<div>
<span class="eyebrow">__PILL_TEXT__</span>
<h1>__HERO_H1__</h1>
<p class="lede">__HERO_DESC__</p>
<div class="rating-row"><span class="stars">★★★★★</span><span>4.8 / 5 average — __REVIEW_COUNT__ verified reviews</span></div>
<div class="hero-actions">
<a class="btn" href="__AFFILIATE__">Shop __BRAND__ — From __PRICE_FROM__<span class="btn-sub">Official Site · Secure Checkout</span></a>
<a class="btn-ghost" href="#how-it-works">See How It Works ↓</a>
</div>
<ul class="hero-checks">
<li>__CHECK1__</li>
<li>__CHECK2__</li>
<li>__CHECK3__</li>
<li>__CHECK4__</li>
</ul>
</div>
<div class="orbit">
<div class="orbit-ring"></div>
<div class="orbit-ring r2"></div>
<div class="chip c1">__ORBIT1__</div>
<div class="chip c2">__ORBIT2__</div>
<div class="chip c3">__ORBIT3__</div>
<div class="chip c4">__ORBIT4__</div>
<div class="hero-frame"><img src="assets/images/hero.png" alt="__BRAND__ product" id="hero-img"></div>
</div>
</div></header>

<section class="trust"><div class="wrap">
<div class="tcard"><div class="ic"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 2l3 6 7 1-5 5 1 7-6-3-6 3 1-7-5-5 7-1z"/></svg></div><b>Made In The USA</b><span>Manufactured under strict quality control</span></div>
<div class="tcard"><div class="ic"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M8 4v16M3 9h5"/></svg></div><b>FDA-Registered Facility</b><span>Produced under registered oversight</span></div>
<div class="tcard"><div class="ic"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 2l8 4v6c0 5-3.5 8-8 10-4.5-2-8-5-8-10V6z"/></svg></div><b>GMP Certified</b><span>Good Manufacturing Practice standards</span></div>
<div class="tcard"><div class="ic"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 2C8 6 4 9 4 14a8 8 0 0016 0c0-5-4-8-8-12z"/></svg></div><b>Naturally Sourced</b><span>Thoughtfully selected ingredients</span></div>
</div></section>

<section id="symptoms-section"><div class="wrap">
<div class="head"><span class="eyebrow">The Real Issue</span><h2>What __BRAND__ was formulated to address</h2><p>Not a mystery — just specific, everyday problems worth naming directly.</p></div>
<div class="grid g3">
__SYMPTOM_CARD_TEMPLATE__
</div>
</div></section>

<section class="trust" id="what-is"><div class="wrap split">
<div class="statcard">
<div class="big">__FACT1_NUM__</div>
<div class="lbl">Named ingredients — zero proprietary blends</div>
<hr>
<div class="statrow"><span>Daily serving</span><b>__SERVING_DAILY__</b></div>
<div class="statrow"><span>Per bottle</span><b>__SERVING_PER_BOTTLE__</b></div>
<div class="statrow"><span>Manufacturing</span><b>USA · GMP-Certified</b></div>
<div class="statrow"><span>Guarantee</span><b>60 Days</b></div>
</div>
<div>
<span class="eyebrow">What This Actually Is</span>
<h2>What is __BRAND__, honestly?</h2>
<p>__WHATIS_P1__</p>
<div class="callout"><b>Straight talk:</b> __WHATIS_CALLOUT__</div>
<div class="chiprow"><span>__CHIP1__</span><span>__CHIP2__</span><span>__CHIP3__</span><span>__CHIP4__</span></div>
</div>
</div></section>

<section class="dark" id="how-it-works"><div class="wrap">
<div class="head"><span class="eyebrow">The Mechanism</span><h2>How Does __BRAND__ Work?</h2><p>__HIW_INTRO__</p></div>
<div class="grid g4">
__HIW_CARD_TEMPLATE__
</div>
</div></section>

<section id="ingredients"><div class="wrap">
<div class="head"><span class="eyebrow">Inside Every Serving</span><h2>__ING_HEADING__</h2><p>Every ingredient named — no proprietary blend hiding amounts.</p></div>
<div class="grid g3">
__ING_CARD_TEMPLATE__
</div>
</div></section>

<section id="benefits"><div class="wrap">
<div class="head"><span class="eyebrow">Key Benefits</span><h2>What __BRAND__ is formulated to support</h2><p>Supportive wellness benefits — not promised medical outcomes.</p></div>
<div class="grid g4">
__BENEFIT_CARD_TEMPLATE__
</div>
</div></section>

<section class="trust"><div class="wrap">
<div class="head"><span class="eyebrow">The Difference</span><h2>The typical approach vs. the __BRAND__ approach</h2><p>Most __CATEGORY__ products hide what's actually inside. Here's what's different.</p></div>
<div class="tblwrap">
<table class="cmp">
<tr><th>&nbsp;</th><th>Typical Formula</th><th class="hl">__BRAND__</th></tr>
<tr><td>Ingredient transparency</td><td class="bad">Hides amounts behind a "proprietary blend"</td><td class="good">All __FACT1_NUM__ ingredients named, with amounts and roles explained</td></tr>
<tr><td>What's actually inside</td><td class="bad">Filler-heavy, generic formulations</td><td class="good">A formula built specifically around __CATEGORY__</td></tr>
<tr><td>Manufacturing</td><td class="bad">Unclear or unverified origin</td><td class="good">FDA-registered, GMP-certified USA facility</td></tr>
<tr><td>Guarantee</td><td class="bad">Often none, or under 30 days</td><td class="good">Full 60-day money-back guarantee</td></tr>
<tr><td>Customer reviews</td><td class="bad">Hard to verify, easy to fake</td><td class="good">__REVIEW_COUNT__ verified reviews at 4.8/5</td></tr>
</table>
</div>
</div></section>

<section id="reviews"><div class="wrap">
<div class="head"><span class="eyebrow">Real Reviews</span><h2>What __BRAND__ customers report</h2><p>Individual experiences vary. These reflect personal opinions, not guaranteed outcomes.</p></div>
<div class="grid g3">
__REVIEW_CARD_TEMPLATE__
</div>
<div class="rev-board">
<div><b>4.8</b><span>Average Rating</span></div>
<div><b>__REVIEW_COUNT__</b><span>Verified Reviews</span></div>
<div><b>60-Day</b><span>Money-Back Guarantee</span></div>
</div>
</div></section>

<section id="blog-teaser"><div class="wrap">
<div class="head"><span class="eyebrow">Learn More</span><h2>__BRAND__ Guides &amp; Articles</h2><p>Dig deeper into ingredients, usage tips and honest answers on our blog.</p></div>
<div class="grid g3">
<div class="card"><h4>What To Know Before Trying __BRAND__</h4><p>A clear look at ingredients, dosage and what to realistically expect.</p></div>
<div class="card"><h4>How To Read A Supplement Label</h4><p>Understanding ingredient blends, serving sizes and common label claims.</p></div>
<div class="card"><h4>__BRAND__: An Honest Review</h4><p>Strengths, limitations and who should consider this product.</p></div>
</div>
<div style="text-align:center;margin-top:32px"><a class="btn-dark" href="blog/index.html">Visit The __BRAND__ Blog</a></div>
</div></section>

<section id="pricing"><div class="wrap">
<div class="head"><span class="eyebrow">Pick Your Pack</span><h2>Choose your __BRAND__ package</h2><p>Larger bundles reduce the cost per bottle.</p></div>
<div class="plans">
__PLAN_CARD_TEMPLATE__
</div>
<p class="plan-note">__PRICING_NOTE__</p>
</div></section>

__BONUS_SECTION__

<section class="trust"><div class="wrap">
<div class="guar">
<div class="seal">60<br>Days</div>
<div><span class="eyebrow">Zero Risk</span><h3>A real 60-day guarantee</h3><p>__GUARANTEE_TEXT__</p></div>
</div>
</div></section>

<section id="faq"><div class="wrap">
<div class="head"><span class="eyebrow">Common Questions</span><h2>__BRAND__ FAQ, answered honestly</h2></div>
<div class="faq">
__FAQ_ROW_TEMPLATE__
</div>
</div></section>

<section><div class="wrap">
<div class="final">
<h2>Ready to try __BRAND__?</h2>
<p>__FINAL_TEXT__</p>
<img src="assets/images/bottle-6.png" alt="__BRAND__ six bottle pack">
<div class="old">Regular: __PRICE_HIGH__ / bottle</div>
<div class="new">Today from __PRICE_LOW__ / bottle</div>
<a class="btn-dark" href="__AFFILIATE__">__CTA_CLOSING__</a>
</div>
</div></section>

<footer><div class="wrap">
<div class="foot-top">
<div>
<a class="logo" href="index.html" style="color:var(--paper);margin-bottom:14px"><svg viewBox="0 0 24 24" fill="none" width="22" height="22"><path d="M12 2C8 6 4 9 4 14a8 8 0 0016 0c0-5-4-8-8-12z" style="fill:var(--primary-dark)"/><path d="M12 6c-2 3-4 5-4 8a4 4 0 008 0c0-3-2-5-4-8z" style="fill:var(--primary)"/></svg>__BRAND__</a>
<p>A daily __CATEGORY__ formula built around transparent, named ingredients.</p>
</div>
<div><h5>Explore</h5><ul>
<li><a href="what-is-product.html">What Is __BRAND__</a></li>
<li><a href="how-it-works.html">How It Works</a></li>
<li><a href="ingredients.html">Ingredients</a></li>
<li><a href="benefits.html">Benefits</a></li>
<li><a href="reviews.html">Reviews</a></li>
</ul></div>
<div><h5>Legal</h5><ul>
<li><a href="terms.html">Terms of Use</a></li>
<li><a href="privacy-policy.html">Privacy Policy</a></li>
<li><a href="disclaimer.html">Disclaimer</a></li>
<li><a href="refund-policy.html">Refund Policy</a></li>
<li><a href="contact.html">Contact Us</a></li>
</ul></div>
</div>
<hr>
<p><b>Who this is for:</b> __BRAND__ is a dietary supplement for adults aged 18 and over interested in general nutritional support. It is not a substitute for medical treatment.</p>
<p><b>FDA Compliance:</b> These statements have not been evaluated by the U.S. Food &amp; Drug Administration. __BRAND__ is a dietary supplement, not a drug, and is not intended to diagnose, treat, cure or prevent any disease.</p>
<p><b>Affiliate Disclosure:</b> This website may earn a commission on purchases made through links to the official __BRAND__ store, at no additional cost to you.</p>
<div class="cr">© __YEAR__ __BRAND__ — All Rights Reserved</div>
</div></footer>

<div class="sticky-bar"><div><b>__PRICE_LOW__ / bottle</b><small>Best value pack</small></div><a class="btn" href="__AFFILIATE__">__CTA_STICKY__</a></div>

<script>
document.querySelectorAll('.faq-btn').forEach(function(btn){
 btn.addEventListener('click',function(){
  var row=btn.closest('.faq-row');
  var body=row.querySelector('.faq-body');
  var wasOpen=row.classList.contains('open');
  document.querySelectorAll('.faq-row.open').forEach(function(r){
   r.classList.remove('open');
   r.querySelector('.faq-body').style.maxHeight=null;
  });
  if(!wasOpen){
   row.classList.add('open');
   body.style.maxHeight=body.scrollHeight+'px';
  }
 });
});
</script>
</body></html>
