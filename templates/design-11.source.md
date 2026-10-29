<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>__TITLE__</title>
<meta name="description" content="__META_DESC__">
<link rel="canonical" href="__CANONICAL__">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
:root{
 --primary:__COLOR_PRIMARY__;
 --primary-dark:__COLOR_DARK__;
 --primary-light:__COLOR_LIGHT__;
 --accent:__COLOR_ACCENT__;
 --on-primary:__COLOR_ON_PRIMARY__;
 --ink:#f3f5fb;
 --muted:#8991a8;
 --bg:#090b11;
 --bg-alt:#10131c;
 --card:#12151f;
 --border:rgba(255,255,255,.08);
 --radius:20px;
}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Inter',system-ui,sans-serif;color:var(--ink);background:var(--bg);line-height:1.65}
h1,h2,h3,h4{font-family:'Space Grotesk',system-ui,sans-serif;font-weight:700;line-height:1.15;letter-spacing:-.01em;color:var(--ink)}
.wrap{max-width:1140px;margin:0 auto;padding:0 24px}
a{color:inherit;text-decoration:none}
img{max-width:100%;display:block}

/* ═══ Marquee ticker ═══ */
.ticker{background:var(--bg-alt);border-bottom:1px solid var(--border);padding:10px 0;overflow:hidden;white-space:nowrap}
.ticker-track{display:inline-flex;gap:0;animation:ticker 26s linear infinite}
.ticker-track span{display:inline-flex;align-items:center;gap:10px;font-size:.78rem;font-weight:700;letter-spacing:.03em;text-transform:uppercase;color:var(--muted);padding:0 28px;white-space:nowrap}
.ticker-track span b{color:var(--primary)}
@keyframes ticker{from{transform:translateX(0)}to{transform:translateX(-50%)}}

/* ═══ Nav ═══ */
nav{padding:18px 0;position:sticky;top:0;background:rgba(9,11,17,.85);backdrop-filter:blur(10px);z-index:50;border-bottom:1px solid var(--border)}
nav .wrap{display:flex;align-items:center;justify-content:space-between;gap:20px}
.logo{font-weight:700;font-size:1.35rem;color:var(--ink)}
.logo em{font-style:normal;color:var(--primary)}
.navlinks{display:flex;align-items:center;gap:26px;list-style:none;flex-wrap:wrap}
.navlinks a{font-size:.9rem;font-weight:600;color:var(--muted)}
.navlinks a:hover{color:var(--ink)}
.nav-btn{background:var(--primary);color:var(--on-primary)!important;padding:11px 24px;border-radius:999px;font-weight:700!important;font-size:.85rem!important;box-shadow:0 0 0 1px color-mix(in srgb, var(--primary) 50%, transparent),0 8px 24px -8px var(--primary)}

/* ═══ Buttons ═══ */
.btn{display:inline-block;background:var(--primary);color:var(--on-primary);padding:17px 34px;border-radius:999px;font-weight:700;font-size:1rem;border:none;cursor:pointer;transition:transform .18s,box-shadow .18s;box-shadow:0 0 0 1px color-mix(in srgb, var(--primary) 45%, transparent),0 0 32px -6px var(--primary)}
.btn:hover{transform:translateY(-3px);box-shadow:0 0 0 1px color-mix(in srgb, var(--primary) 60%, transparent),0 0 44px -4px var(--primary)}
.btn-outline{display:inline-block;background:transparent;color:var(--ink);padding:15px 30px;border-radius:999px;font-weight:700;border:1.5px solid var(--border)}
.btn-outline:hover{border-color:var(--primary);color:var(--primary)}
.btn-sub{display:block;font-size:.72rem;font-weight:500;opacity:.85;margin-top:3px}

/* ═══ Hero — glow blobs + pulsing product ring ═══ */
.hero{position:relative;padding:64px 0 74px;overflow:hidden}
.hero:before,.hero:after{content:'';position:absolute;width:520px;height:520px;border-radius:50%;filter:blur(120px);opacity:.28;z-index:0;animation:drift 14s ease-in-out infinite alternate}
.hero:before{background:var(--primary);top:-220px;left:-160px}
.hero:after{background:var(--accent);bottom:-260px;right:-180px;animation-delay:2s}
@keyframes drift{from{transform:translate(0,0) scale(1)}to{transform:translate(40px,30px) scale(1.12)}}
.hero-grid{display:grid;grid-template-columns:1.05fr .95fr;gap:56px;align-items:center;position:relative;z-index:2}
.pill{display:inline-flex;align-items:center;gap:8px;background:color-mix(in srgb, var(--primary) 16%, transparent);border:1px solid color-mix(in srgb, var(--primary) 40%, transparent);color:var(--primary-light);font-size:.8rem;font-weight:700;padding:8px 18px;border-radius:999px;margin-bottom:20px}
.hero h1{font-size:3rem;margin-bottom:18px;background:linear-gradient(100deg,var(--ink) 30%,var(--primary) 65%,var(--accent) 100%);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.hero .lede{font-size:1.08rem;color:var(--muted);margin-bottom:24px;max-width:520px}
.rating{display:flex;align-items:center;gap:10px;margin-bottom:22px;font-size:.9rem;color:var(--muted);font-weight:600}
.stars{color:var(--primary);letter-spacing:2px;font-size:1.05rem;text-shadow:0 0 16px color-mix(in srgb, var(--primary) 70%, transparent)}
.factrow{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin:24px 0}
.factrow div{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:14px 8px;text-align:center;transition:border-color .2s}
.factrow div:hover{border-color:color-mix(in srgb, var(--primary) 50%, transparent)}
.factrow b{display:block;font-size:1.35rem;color:var(--primary);font-weight:700;font-family:'Space Grotesk',sans-serif}
.factrow span{font-size:.68rem;color:var(--muted);font-weight:600;text-transform:uppercase;letter-spacing:.04em}
.checks{list-style:none;margin:20px 0 28px}
.checks li{position:relative;padding-left:30px;margin-bottom:12px;font-size:.95rem;color:var(--ink);font-weight:500}
.checks li:before{content:'⚡';position:absolute;left:0;top:-2px;width:22px;height:22px;background:color-mix(in srgb, var(--primary) 18%, transparent);color:var(--primary);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:.68rem}
.hero-actions{display:flex;gap:16px;flex-wrap:wrap;margin-bottom:16px}
.trustline{font-size:.8rem;color:var(--muted);font-weight:500}
.hero-img{position:relative;text-align:center}
.hero-img:before{content:'';position:absolute;inset:8%;border-radius:50%;background:radial-gradient(circle,color-mix(in srgb, var(--primary) 55%, transparent),transparent 70%);filter:blur(6px);animation:pulseGlow 3.2s ease-in-out infinite}
@keyframes pulseGlow{0%,100%{opacity:.55;transform:scale(.94)}50%{opacity:.95;transform:scale(1.04)}}
.hero-img img{position:relative;max-width:72%;margin:0 auto;filter:drop-shadow(0 28px 48px rgba(0,0,0,.55))}

/* ═══ Trust badge strip ═══ */
.trust-strip{background:var(--bg-alt);padding:30px 0;border-bottom:1px solid var(--border)}
.trust-row{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.trust-item{display:flex;flex-direction:column;align-items:center;gap:10px;text-align:center;font-size:.82rem;font-weight:600;color:var(--muted)}
.trust-item img{width:40px;height:40px;object-fit:contain}

section{padding:78px 0}
.section-alt{background:var(--bg-alt)}
.head{text-align:center;max-width:660px;margin:0 auto 46px}
.eyebrow{display:inline-block;color:var(--primary);font-weight:700;font-size:.74rem;letter-spacing:.06em;text-transform:uppercase;margin-bottom:12px;background:color-mix(in srgb, var(--primary) 14%, transparent);padding:6px 16px;border-radius:999px;border:1px solid color-mix(in srgb, var(--primary) 30%, transparent)}
.head h2{font-size:2.2rem;margin-bottom:12px}
.head p{color:var(--muted);font-size:1.02rem}

.grid{display:grid;gap:20px}
.g2{grid-template-columns:repeat(2,1fr)}
.g3{grid-template-columns:repeat(3,1fr)}
.g4{grid-template-columns:repeat(4,1fr)}
.card{background:var(--card);border:1px solid var(--border);border-radius:var(--radius);padding:26px;transition:transform .18s,border-color .18s,box-shadow .18s}
.card:hover{transform:translateY(-4px);border-color:color-mix(in srgb, var(--primary) 45%, transparent);box-shadow:0 16px 40px -20px var(--primary)}
.card h4{font-size:1.05rem;margin-bottom:10px}
.card p{color:var(--muted);font-size:.92rem}

.split{display:grid;grid-template-columns:1fr 1.1fr;gap:56px;align-items:center}
.split-reverse{display:grid;grid-template-columns:1.1fr 1fr;gap:56px;align-items:center}
.split-reverse img{order:2}
.split img,.split-reverse img{border-radius:24px;border:1px solid var(--border)}
.callout{background:var(--card);border-left:3px solid var(--primary);border-radius:0 16px 16px 0;padding:18px 22px;margin:22px 0;font-size:.95rem;color:var(--ink)}
.factchip{display:inline-flex;gap:10px;flex-wrap:wrap;margin-top:18px}
.factchip span{background:var(--card);border:1px solid var(--border);color:var(--ink);border-radius:999px;padding:8px 18px;font-size:.8rem;font-weight:600}

.ing-card{display:flex;gap:18px;background:var(--card);border:1px solid var(--border);border-radius:var(--radius);padding:24px;transition:transform .18s,border-color .18s,box-shadow .18s}
.ing-card:hover{transform:translateY(-4px);border-color:color-mix(in srgb, var(--primary) 45%, transparent);box-shadow:0 16px 40px -20px var(--primary)}
.ing-num{flex:none;width:42px;height:42px;border-radius:12px;background:linear-gradient(135deg,var(--primary),var(--accent));color:var(--on-primary);display:flex;align-items:center;justify-content:center;font-weight:700;font-family:'Space Grotesk',sans-serif}
.ing-card h4{font-size:1.02rem;margin-bottom:6px}
.ing-card p{color:var(--muted);font-size:.9rem}

.step-card{background:var(--card);border:1px solid var(--border);border-radius:var(--radius);padding:24px;position:relative}
.step-card:hover{border-color:color-mix(in srgb, var(--primary) 45%, transparent)}
.step-num{width:34px;height:34px;border-radius:10px;background:linear-gradient(135deg,var(--primary),var(--accent));color:var(--on-primary);display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.9rem;margin-bottom:14px;font-family:'Space Grotesk',sans-serif}
.step-card h4{font-size:1rem;margin-bottom:8px}
.step-card p{color:var(--muted);font-size:.9rem}

.rev-card{background:var(--card);border:1px solid var(--border);border-radius:var(--radius);padding:26px;position:relative}
.rev-card:before{content:'"';position:absolute;top:14px;right:22px;font-family:'Space Grotesk',sans-serif;font-size:3.4rem;color:color-mix(in srgb, var(--primary) 25%, transparent);line-height:1}
.rev-head{display:flex;align-items:center;gap:14px;margin-bottom:12px}
.rev-head img{width:48px;height:48px;border-radius:50%;object-fit:cover;border:2px solid var(--border)}
.rev-name{font-weight:700;font-size:.95rem;color:var(--ink)}
.rev-sub{font-size:.78rem;color:var(--muted);font-weight:500}
.rev-card p{color:var(--ink)!important;font-size:.92rem;position:relative;z-index:1}
.rev-stars{color:var(--primary);margin-bottom:10px;font-size:1rem;text-shadow:0 0 14px color-mix(in srgb, var(--primary) 60%, transparent)}
.rev-board{display:flex;justify-content:center;gap:60px;margin-top:40px;text-align:center;flex-wrap:wrap}
.rev-board b{display:block;font-size:1.9rem;font-weight:700;color:var(--primary);font-family:'Space Grotesk',sans-serif}
.rev-board span{font-size:.78rem;color:var(--muted);font-weight:600;text-transform:uppercase}

.plans{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;align-items:start}
.plan{background:var(--card);border:1px solid var(--border);border-radius:22px;padding:30px 24px;text-align:center;position:relative;transition:transform .18s}
.plan.top{border-color:color-mix(in srgb, var(--primary) 55%, transparent);animation:planGlow 2.6s ease-in-out infinite}
@keyframes planGlow{0%,100%{box-shadow:0 0 0 1px color-mix(in srgb, var(--primary) 40%, transparent),0 0 26px -8px var(--primary)}50%{box-shadow:0 0 0 1px color-mix(in srgb, var(--primary) 65%, transparent),0 0 46px -4px var(--primary)}}
.plan-badge{position:absolute;top:-15px;left:50%;transform:translateX(-50%);background:linear-gradient(135deg,var(--primary),var(--accent));color:var(--on-primary);font-size:.72rem;font-weight:700;padding:7px 18px;border-radius:999px;white-space:nowrap}
.plan img{max-width:128px;margin:12px auto 18px;filter:drop-shadow(0 12px 20px rgba(0,0,0,.4))}
.plan-ttl{font-weight:700;font-size:1.18rem;margin-bottom:2px;font-family:'Space Grotesk',sans-serif}
.plan-sub{font-size:.78rem;color:var(--muted);margin-bottom:16px;font-weight:500}
.plan-price{font-size:2.1rem;font-weight:700;color:var(--ink);font-family:'Space Grotesk',sans-serif}
.plan-price small{font-size:.85rem;font-weight:500;color:var(--muted)}
.plan-tot{font-size:.85rem;color:var(--muted);margin:6px 0 2px}
.plan-ship{font-size:.82rem;color:var(--primary);font-weight:700;margin-bottom:18px}
.plan ul{list-style:none;text-align:left;margin-bottom:20px}
.plan ul li{font-size:.86rem;padding:6px 0 6px 26px;position:relative;color:var(--ink)}
.plan ul li:before{content:'✓';position:absolute;left:0;color:var(--primary);font-weight:700}
.plan .btn{width:100%;padding:15px}
.flag{background:var(--card);border:1px solid var(--border);border-radius:16px;padding:18px 22px;margin-top:30px;font-size:.9rem;text-align:center;max-width:780px;margin-left:auto;margin-right:auto;color:var(--muted)}

.guar{display:flex;align-items:center;gap:44px;background:var(--card);border:1px solid var(--border);border-radius:28px;padding:44px}
.guar img{width:140px;flex:none}
.guar h3{font-size:1.5rem;margin-bottom:12px}
.guar p{color:var(--muted);margin-bottom:8px}

.faq{max-width:780px;margin:0 auto}
.faq-row{border:1px solid var(--border);border-radius:16px;margin-bottom:14px;overflow:hidden;background:var(--card)}
.faq-btn{width:100%;text-align:left;background:transparent;border:none;padding:20px 22px;font-size:1rem;font-weight:700;cursor:pointer;color:var(--ink);display:flex;justify-content:space-between;align-items:center;font-family:'Space Grotesk',sans-serif}
.faq-btn:after{content:'+';font-size:1.5rem;color:var(--primary);font-weight:700}
.faq-body{padding:0 22px 20px;color:var(--muted);font-size:.94rem;display:none}
.faq-row.open{border-color:color-mix(in srgb, var(--primary) 40%, transparent)}
.faq-row.open .faq-body{display:block}
.faq-row.open .faq-btn:after{content:'−'}

footer{background:var(--bg-alt);color:var(--muted);padding:60px 0 32px;font-size:.86rem;border-top:1px solid var(--border)}
.foot-nav{display:flex;flex-wrap:wrap;gap:24px;list-style:none;margin-bottom:20px}
.foot-nav a{color:var(--ink);font-weight:600}
.foot-nav a:hover{color:var(--primary)}
.foot-legal{display:flex;flex-wrap:wrap;gap:18px;list-style:none;margin-bottom:26px;font-size:.8rem}
.foot-legal a{color:var(--muted)}
footer hr{border:none;border-top:1px solid var(--border);margin:24px 0}
footer p{margin-bottom:12px;font-size:.78rem;line-height:1.7}
.cr{margin-top:18px;font-size:.78rem;color:#565f75}

.sticky-bar{position:fixed;bottom:0;left:0;right:0;background:var(--bg-alt);border-top:1px solid var(--border);padding:14px 20px;display:flex;align-items:center;justify-content:space-between;gap:16px;box-shadow:0 -8px 24px rgba(0,0,0,.4);z-index:60}
.sticky-bar b{font-weight:700;font-size:1.05rem;color:var(--ink)}
.sticky-bar small{display:block;color:var(--muted);font-size:.75rem}

.final{background:linear-gradient(135deg,color-mix(in srgb, var(--primary) 22%, var(--bg-alt)),var(--bg-alt));border:1px solid color-mix(in srgb, var(--primary) 35%, transparent);color:var(--ink);border-radius:32px;padding:60px 44px;text-align:center}
.final h2{margin-bottom:14px;font-size:2.1rem}
.final p{color:var(--muted);margin-bottom:26px}
.final img{max-width:170px;margin:0 auto 26px;filter:drop-shadow(0 20px 36px rgba(0,0,0,.5))}
.final .old{text-decoration:line-through;opacity:.6;font-size:1rem;color:var(--muted)}
.final .new{font-size:2rem;font-weight:700;margin-bottom:22px;color:var(--primary);font-family:'Space Grotesk',sans-serif}

@media(max-width:860px){
 .hero-grid,.split,.split-reverse{grid-template-columns:1fr}
 .split-reverse img{order:0}
 .g4{grid-template-columns:repeat(2,1fr)}
 .g3,.g2{grid-template-columns:1fr}
 .plans{grid-template-columns:1fr}
 .factrow{grid-template-columns:repeat(2,1fr)}
 .trust-row{grid-template-columns:repeat(2,1fr)}
 .navlinks{display:none}
 .guar{flex-direction:column;text-align:center}
 .rev-board{gap:32px}
 body{padding-bottom:78px}
 .hero h1{font-size:2.1rem}
 .hero:before,.hero:after{display:none}
}
</style>
</head>
<body>

<div class="ticker"><div class="ticker-track">
<span>⚡ <b>__BRAND__</b> — __FACT1_NUM__ Named Ingredients</span><span>✓ Made In The USA</span><span>✓ 60-Day Guarantee</span><span>✓ __REVIEW_COUNT__ Reviews</span>
<span>⚡ <b>__BRAND__</b> — __FACT1_NUM__ Named Ingredients</span><span>✓ Made In The USA</span><span>✓ 60-Day Guarantee</span><span>✓ __REVIEW_COUNT__ Reviews</span>
</div></div>

<nav><div class="wrap">
<a class="logo" href="index.html">__BRAND__</a>
<ul class="navlinks">
<li><a href="how-it-works.html">How It Works</a></li>
<li><a href="ingredients.html">Ingredients</a></li>
<li><a href="benefits.html">Benefits</a></li>
<li><a href="reviews.html">Reviews</a></li>
<li><a href="blog/index.html">Blog</a></li>
<li><a href="index.html#pricing">Pricing</a></li>
<li><a class="nav-btn" href="__AFFILIATE__">__CTA_HEADER__</a></li>
</ul>
</div></nav>

<header class="hero"><div class="wrap hero-grid">
<div>
<span class="pill">__PILL_TEXT__</span>
<h1>__HERO_H1__</h1>
<p class="lede">__HERO_DESC__</p>
<div class="rating"><span class="stars">★★★★★</span> <b>4.8 / 5</b> from __REVIEW_COUNT__ reviews</div>
<div class="factrow">
<div><b>__FACT1_NUM__</b><span>__FACT1_LABEL__</span></div>
<div><b>__FACT2_NUM__</b><span>__FACT2_LABEL__</span></div>
<div><b>__FACT3_NUM__</b><span>__FACT3_LABEL__</span></div>
<div><b>__FACT4_NUM__</b><span>__FACT4_LABEL__</span></div>
</div>
<ul class="checks">
<li>__CHECK1__</li>
<li>__CHECK2__</li>
<li>__CHECK3__</li>
<li>__CHECK4__</li>
</ul>
<div class="hero-actions">
<a class="btn" href="__AFFILIATE__">Get __BRAND__ — __PRICE_FROM__<span class="btn-sub">Official Site • Secure Checkout</span></a>
<a class="btn-outline" href="what-is-product.html">What Is __BRAND__?</a>
</div>
<div class="trustline">Made in USA • GMP Certified • 60-Day Guarantee</div>
</div>
<div class="hero-img"><img src="assets/images/hero.png" alt="__BRAND__ product" id="hero-img"></div>
</div></header>

<div class="trust-strip"><div class="wrap trust-row">
<div class="trust-item"><img src="assets/images/badge-usa.png" alt="Made in USA">Made In The USA</div>
<div class="trust-item"><img src="assets/images/badge-fda.png" alt="FDA registered">FDA-Registered Facility</div>
<div class="trust-item"><img src="assets/images/badge-gmp.png" alt="GMP certified">GMP Certified</div>
<div class="trust-item"><img src="assets/images/badge-natural.png" alt="Natural">Naturally Sourced</div>
</div></div>

<section class="section-alt" id="what-is"><div class="wrap split-reverse">
<img src="assets/images/feature-shot.png" alt="__BRAND__ overview" id="whatis-img">
<div>
<span class="eyebrow">What This Actually Is</span>
<h2>What Is __BRAND__?</h2>
<p>__WHATIS_P1__</p>
<div class="callout"><b>Straight talk:</b> __WHATIS_CALLOUT__</div>
<div class="factchip">
<span>__CHIP1__</span><span>__CHIP2__</span><span>__CHIP3__</span><span>__CHIP4__</span>
</div>
</div>
</div></section>

<section id="ingredients"><div class="wrap">
<div class="head"><span class="eyebrow">Inside Every Serving</span><h2>__ING_HEADING__</h2><p>Each ingredient explained individually below.</p></div>
<div class="grid g3" id="ing-grid">
__ING_CARD_TEMPLATE__
</div>
</div></section>

<section class="section-alt" id="how-it-works"><div class="wrap">
<div class="head"><span class="eyebrow">The Mechanism</span><h2>How Does __BRAND__ Work?</h2><p>__HIW_INTRO__</p></div>
<div class="grid g4" id="hiw-grid">
__HIW_CARD_TEMPLATE__
</div>
</div></section>

<section id="benefits"><div class="wrap">
<div class="head"><span class="eyebrow">Key Benefits</span><h2>What __BRAND__ Is Formulated To Support</h2><p>Supportive wellness benefits — not promised medical outcomes.</p></div>
<div class="grid g4" id="benefits-grid">
__BENEFIT_CARD_TEMPLATE__
</div>
</div></section>

<section class="section-alt" id="reviews"><div class="wrap">
<div class="head"><span class="eyebrow">Real Reviews</span><h2>What __BRAND__ Customers Report</h2><p>Individual experiences vary. These reflect personal opinions, not guaranteed outcomes.</p></div>
<div class="grid g3" id="rev-grid">
__REVIEW_CARD_TEMPLATE__
</div>
<div class="rev-board">
<div><b>4.8</b><span>Average Rating</span></div>
<div><b>__REVIEW_COUNT__</b><span>Customer Reviews</span></div>
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
<div style="text-align:center;margin-top:32px"><a class="btn-outline" href="blog/index.html">Visit The __BRAND__ Blog</a></div>
</div></section>

<section class="section-alt" id="pricing"><div class="wrap">
<div class="head"><span class="eyebrow">Pick Your Pack</span><h2>Choose Your __BRAND__ Package</h2><p>Larger bundles reduce the cost per bottle.</p></div>
<div class="plans" id="plans-grid">
__PLAN_CARD_TEMPLATE__
</div>
<div class="flag">__PRICING_NOTE__</div>
</div></section>

__BONUS_SECTION__

<section><div class="wrap">
<div class="guar">
<img src="assets/images/guarantee.png" alt="Money back guarantee">
<div><span class="eyebrow">Zero Risk</span><h3>A Real 60-Day Guarantee</h3><p>__GUARANTEE_TEXT__</p></div>
</div>
</div></section>

<section class="section-alt" id="faq"><div class="wrap">
<div class="head"><span class="eyebrow">Common Questions</span><h2>__BRAND__ FAQ, Answered Honestly</h2></div>
<div class="faq" id="faq-list">
__FAQ_ROW_TEMPLATE__
</div>
</div></section>

<section><div class="wrap">
<div class="final">
<h2>Ready To Try __BRAND__?</h2>
<p>__FINAL_TEXT__</p>
<img src="assets/images/bottle-6.png" alt="__BRAND__ six bottle pack">
<div class="old">Regular: __PRICE_HIGH__ / bottle</div>
<div class="new">Today from __PRICE_LOW__ / bottle</div>
<a class="btn" href="__AFFILIATE__">__CTA_CLOSING__</a>
</div>
</div></section>

<footer><div class="wrap">
<ul class="foot-nav">
<li><a href="index.html">Home</a></li>
<li><a href="what-is-product.html">What Is __BRAND__</a></li>
<li><a href="how-it-works.html">How It Works</a></li>
<li><a href="ingredients.html">Ingredients</a></li>
<li><a href="benefits.html">Benefits</a></li>
<li><a href="reviews.html">Reviews</a></li>
<li><a href="__AFFILIATE__">__CTA_AFTERFAQ__</a></li>
</ul>
<ul class="foot-legal">
<li><a href="terms.html">Terms of Use</a></li>
<li><a href="privacy-policy.html">Privacy Policy</a></li>
<li><a href="disclaimer.html">Disclaimer</a></li>
<li><a href="refund-policy.html">Refund Policy</a></li>
<li><a href="contact.html">Contact Us</a></li>
</ul>
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
  var wasOpen=row.classList.contains('open');
  document.querySelectorAll('.faq-row.open').forEach(function(r){r.classList.remove('open')});
  if(!wasOpen)row.classList.add('open');
 });
});
if('IntersectionObserver' in window){
 var io=new IntersectionObserver(function(entries){
  entries.forEach(function(en){
   if(!en.isIntersecting)return;
   io.unobserve(en.target);
   var el=en.target,full=el.textContent,m=full.match(/^(\d+)(.*)$/);
   if(!m)return;
   var target=parseInt(m[1],10),suffix=m[2];
   if(isNaN(target)||target<=0||target>9999)return;
   var t0=null,dur=700;
   function step(ts){
    if(!t0)t0=ts;
    var p=Math.min(1,(ts-t0)/dur);
    el.textContent=Math.floor(p*target)+suffix;
    if(p<1)requestAnimationFrame(step);else el.textContent=full;
   }
   requestAnimationFrame(step);
  });
 },{threshold:.4});
 document.querySelectorAll('.factrow b').forEach(function(el){io.observe(el)});
}
</script>
</body></html>
