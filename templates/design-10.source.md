<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>__TITLE__</title>
<meta name="description" content="__META_DESC__">
<link rel="canonical" href="__CANONICAL__">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@400;500;600;700&family=Quicksand:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{
 --primary:__COLOR_PRIMARY__;
 --primary-dark:__COLOR_DARK__;
 --primary-light:__COLOR_LIGHT__;
 --accent:__COLOR_ACCENT__;
 --on-primary:__COLOR_ON_PRIMARY__;
 --ink:#2b2340;
 --muted:#786f94;
 --bg:#fffbf5;
 --bg-alt:#fff0f5;
 --border:#f0e4f7;
}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Quicksand',system-ui,sans-serif;color:var(--ink);background:var(--bg);line-height:1.65}
h1,h2,h3,h4{font-family:'Baloo 2',sans-serif;font-weight:700;line-height:1.15;color:var(--ink)}
.wrap{max-width:1080px;margin:0 auto;padding:0 24px}
a{color:inherit;text-decoration:none}
img{max-width:100%;display:block}

.strip{background:var(--primary);color:var(--on-primary);font-size:.8rem;padding:10px 0;text-align:center;font-weight:700}
.strip span{opacity:.95;margin:0 12px}

nav{padding:16px 0;position:sticky;top:0;background:#fff;z-index:50;box-shadow:0 2px 16px rgba(120,80,160,.08)}
nav .wrap{display:flex;align-items:center;justify-content:space-between;gap:20px}
.logo{font-weight:700;font-size:1.4rem;color:var(--primary)}
.navlinks{display:flex;align-items:center;gap:22px;list-style:none;flex-wrap:wrap}
.navlinks a{font-size:.9rem;font-weight:600;color:var(--muted)}
.navlinks a:hover{color:var(--primary)}
.nav-btn{background:var(--primary);color:var(--on-primary)!important;padding:10px 22px;border-radius:999px;font-weight:700!important;font-size:.85rem!important}

.btn{display:inline-block;background:var(--primary);color:var(--on-primary);padding:16px 32px;border-radius:999px;font-weight:700;font-size:1rem;border:none;cursor:pointer;box-shadow:0 10px 26px -8px color-mix(in srgb, var(--primary) 65%, transparent)}
.btn-outline{display:inline-block;background:#fff;color:var(--primary);padding:14px 28px;border-radius:999px;font-weight:700;border:2.5px solid var(--primary)}
.btn-sub{display:block;font-size:.7rem;font-weight:500;opacity:.9;margin-top:3px}

/* ═══ HERO — asymmetric with floating blob shapes ═══ */
.hero{position:relative;padding:50px 0 0;overflow:hidden}
.hero-inner{display:grid;grid-template-columns:1fr;text-align:center;position:relative;z-index:2;padding-bottom:0}
.hero-badge{display:inline-flex;align-items:center;gap:8px;background:var(--primary-light);color:var(--primary-dark);font-size:.82rem;font-weight:700;padding:9px 20px;border-radius:999px;margin:0 auto 18px}
.hero h1{font-size:2.5rem;max-width:760px;margin:0 auto 16px}
.hero .lede{font-size:1.05rem;color:var(--muted);max-width:600px;margin:0 auto 26px;font-weight:500}
.hero-cta-row{display:flex;gap:14px;justify-content:center;flex-wrap:wrap;margin-bottom:36px}
.hero-stage{position:relative;background:var(--primary);border-radius:40px 40px 0 0;padding:50px 24px 0;margin-top:10px}
.hero-stage-inner{max-width:920px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:0;align-items:end}
.hero-stat-list{color:#fff;padding-bottom:50px}
.hero-stat-list .rating{display:flex;align-items:center;gap:10px;margin-bottom:22px;font-weight:700}
.hero-stat-list .stars{color:#ffd23b;letter-spacing:2px}
.hero-stat-list ul{list-style:none}
.hero-stat-list li{position:relative;padding-left:28px;margin-bottom:12px;font-weight:600;opacity:.95}
.hero-stat-list li:before{content:'✓';position:absolute;left:0;width:20px;height:20px;background:#fff;color:var(--primary);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:.7rem;font-weight:800;top:1px}
.hero-jar{text-align:center;position:relative}
.hero-jar img{max-width:78%;margin:0 auto;filter:drop-shadow(0 24px 30px rgba(0,0,0,.25))}

/* ═══ Trust badge strip ═══ */
.trust-strip{background:#fff;padding:26px 0;border-bottom:1px solid var(--border)}
.trust-row{display:flex;justify-content:center;gap:44px;flex-wrap:wrap;align-items:center}
.trust-item{display:flex;align-items:center;gap:10px;font-size:.85rem;font-weight:600;color:var(--muted)}
.trust-item img{width:34px;height:34px;object-fit:contain}

section{padding:64px 0}
.head{text-align:center;max-width:640px;margin:0 auto 40px}
.eyebrow{display:inline-block;color:var(--primary);font-weight:700;font-size:.76rem;letter-spacing:.04em;text-transform:uppercase;margin-bottom:10px;background:var(--primary-light);padding:5px 14px;border-radius:999px}
.head h2{font-size:2rem;margin-bottom:10px}
.head p{color:var(--muted);font-size:1rem;font-weight:500}

/* ═══ What-is: big number stat + text (NOT split image) ═══ */
.whatis-band{background:var(--bg-alt)}
.whatis-inner{max-width:780px;margin:0 auto;text-align:center}
.whatis-inner p{font-size:1.05rem;color:var(--ink);font-weight:500;margin-bottom:20px}
.callout{background:#fff;border-radius:20px;padding:20px 26px;margin:24px 0;font-size:.95rem;font-weight:500;box-shadow:0 8px 24px rgba(120,80,160,.08);text-align:left}
.factchip{display:flex;gap:10px;flex-wrap:wrap;justify-content:center;margin-top:20px}
.factchip span{background:#fff;border:2px solid var(--border);border-radius:999px;padding:8px 18px;font-size:.82rem;color:var(--primary-dark);font-weight:700}

/* ═══ Ingredients — accordion/expandable list ═══ */
.ing-list{max-width:780px;margin:0 auto}
.ing-row{display:flex;align-items:center;gap:18px;background:#fff;border-radius:20px;padding:18px 22px;margin-bottom:12px;box-shadow:0 4px 16px rgba(120,80,160,.06)}
.ing-badge{flex:none;width:44px;height:44px;border-radius:14px;background:var(--primary-light);color:var(--primary-dark);display:flex;align-items:center;justify-content:center;font-weight:700;font-family:'Baloo 2',sans-serif}
.ing-row h4{font-size:1.02rem;margin-bottom:3px}
.ing-row p{color:var(--muted);font-size:.88rem;font-weight:500}

/* ═══ How it works — vertical connected timeline ═══ */
.timeline{background:var(--primary);color:#fff;border-radius:36px;padding:50px 40px}
.timeline .head h2,.timeline .head span{color:#fff}
.timeline .head span{background:rgba(255,255,255,.2)}
.timeline .head p{color:rgba(255,255,255,.75)}
.tl-list{max-width:600px;margin:0 auto;position:relative}
.tl-list:before{content:'';position:absolute;left:19px;top:10px;bottom:10px;width:2px;background:rgba(255,255,255,.25)}
.tl-item{display:flex;gap:20px;margin-bottom:30px;position:relative}
.tl-item:last-child{margin-bottom:0}
.tl-num{flex:none;width:40px;height:40px;border-radius:50%;background:#fff;color:var(--primary);display:flex;align-items:center;justify-content:center;font-weight:700;font-family:'Baloo 2',sans-serif;z-index:2}
.tl-item h4{color:#fff;margin-bottom:4px;font-size:1.02rem}
.tl-item p{color:rgba(255,255,255,.8);font-size:.9rem;font-weight:500}

/* ═══ Benefits — icon row list, not grid ═══ */
.benefit-list{max-width:820px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:20px}
.benefit-item{display:flex;gap:16px;align-items:flex-start}
.benefit-dot{flex:none;width:36px;height:36px;border-radius:50%;background:var(--primary);color:var(--on-primary);display:flex;align-items:center;justify-content:center;font-weight:800;font-size:.8rem}
.benefit-item h4{font-size:.98rem;margin-bottom:4px}
.benefit-item p{color:var(--muted);font-size:.86rem;font-weight:500}

/* ═══ Reviews — single spotlight + small list ═══ */
.rev-spotlight{background:#fff;border-radius:28px;padding:36px;text-align:center;max-width:680px;margin:0 auto 30px;box-shadow:0 16px 40px rgba(120,80,160,.1)}
.rev-spotlight .rev-stars{color:#ffb03b;font-size:1.3rem;margin-bottom:14px}
.rev-spotlight p{font-size:1.15rem;font-weight:600;color:var(--ink);margin-bottom:18px;font-family:'Baloo 2',sans-serif;line-height:1.4}
.rev-spotlight .rev-head{justify-content:center}
.rev-mini-row{display:grid;grid-template-columns:repeat(2,1fr);gap:16px;max-width:780px;margin:0 auto}
.rev-mini{background:#fff;border:2px solid var(--border);border-radius:18px;padding:18px}
.rev-head{display:flex;align-items:center;gap:12px;margin-bottom:8px}
.rev-head img{width:42px;height:42px;border-radius:50%;object-fit:cover}
.rev-name{font-weight:700;font-size:.92rem;color:var(--ink)}
.rev-sub{font-size:.76rem;color:var(--muted)}
.rev-mini p{color:var(--ink)!important;font-size:.88rem;font-weight:500}
.rev-board{display:flex;justify-content:center;gap:50px;margin-top:34px;text-align:center;flex-wrap:wrap}
.rev-board b{display:block;font-size:1.6rem;color:var(--primary)}
.rev-board span{font-size:.78rem;color:var(--muted);font-weight:600}

/* ═══ Blog teaser — horizontal scroll cards ═══ */
.blog-row{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.blog-card{background:#fff;border:2px solid var(--border);border-radius:20px;padding:22px}
.blog-card h4{font-size:.98rem;margin-bottom:6px}
.blog-card p{color:var(--muted);font-size:.85rem;font-weight:500}

/* ═══ Pricing — comparison table style, not cards ═══ */
.price-table{max-width:820px;margin:0 auto;background:#fff;border-radius:28px;overflow:hidden;box-shadow:0 16px 40px rgba(120,80,160,.1)}
.price-row{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;align-items:center;padding:20px 26px;border-bottom:1px solid var(--border)}
.price-row:last-child{border-bottom:none}
.price-row.head-row{background:var(--bg-alt);font-weight:700;font-size:.82rem;text-transform:uppercase;letter-spacing:.03em;color:var(--muted)}
.price-row.top{background:var(--primary-light)}
.price-compare{display:flex;align-items:center;justify-content:center;gap:16px;flex-wrap:wrap;margin-bottom:28px;font-weight:700}
.price-was{color:var(--muted);text-decoration:line-through;font-size:1rem}
.price-arrow{color:var(--primary);font-size:1.2rem}
.price-now{background:var(--primary);color:var(--on-primary);padding:8px 20px;border-radius:999px;font-size:1.1rem}
.price-pkg{display:flex;align-items:center;gap:14px}
.price-pkg img{width:52px;height:52px;object-fit:contain}
.price-pkg-name{font-weight:700;font-family:'Baloo 2',sans-serif}
.price-pkg-badge{display:inline-block;background:var(--primary);color:var(--on-primary);font-size:.68rem;font-weight:700;padding:3px 10px;border-radius:999px;margin-top:3px}
.price-val{font-weight:700;color:var(--primary);font-size:1.1rem;text-align:center}
.price-val small{display:block;font-weight:500;color:var(--muted);font-size:.72rem}
.price-buy{text-align:center}
.price-buy .btn{padding:10px 20px;font-size:.85rem}
.flag{background:var(--bg-alt);border-radius:18px;padding:16px 20px;margin-top:24px;font-size:.88rem;text-align:center;max-width:720px;margin-left:auto;margin-right:auto;font-weight:500}

.guar{display:flex;align-items:center;gap:36px;background:var(--bg-alt);border-radius:32px;padding:38px}
.guar img{width:130px;flex:none}
.guar h3{font-size:1.4rem;margin-bottom:10px}
.guar p{color:var(--muted);margin-bottom:8px;font-weight:500}

.faq{max-width:740px;margin:0 auto}
.faq-row{border:2px solid var(--border);border-radius:18px;margin-bottom:12px;overflow:hidden}
.faq-btn{width:100%;text-align:left;background:#fff;border:none;padding:18px 20px;font-size:.98rem;font-weight:700;cursor:pointer;color:var(--ink);display:flex;justify-content:space-between;align-items:center;font-family:'Baloo 2',sans-serif}
.faq-btn:after{content:'+';font-size:1.3rem;color:var(--primary);font-weight:700}
.faq-body{padding:0 20px 16px;color:var(--muted);font-size:.9rem;display:none;font-weight:500}
.faq-row.open .faq-body{display:block}
.faq-row.open .faq-btn:after{content:'−'}

footer{background:var(--ink);color:rgba(255,255,255,.8);padding:50px 0 28px;font-size:.85rem}
.foot-nav{display:flex;flex-wrap:wrap;gap:20px;list-style:none;margin-bottom:16px}
.foot-nav a{color:rgba(255,255,255,.85);font-weight:600}
.foot-legal{display:flex;flex-wrap:wrap;gap:16px;list-style:none;margin-bottom:22px;font-size:.78rem}
.foot-legal a{color:rgba(255,255,255,.55)}
footer hr{border:none;border-top:1px solid rgba(255,255,255,.15);margin:20px 0}
footer p{margin-bottom:10px;color:rgba(255,255,255,.55);font-size:.76rem;line-height:1.7}
.cr{margin-top:16px;font-size:.76rem;color:rgba(255,255,255,.4);font-weight:500}

.sticky-bar{position:fixed;bottom:0;left:0;right:0;background:#fff;border-top:2px solid var(--border);padding:12px 20px;display:flex;align-items:center;justify-content:space-between;gap:16px;box-shadow:0 -8px 24px rgba(0,0,0,.08);z-index:60}
.sticky-bar b{color:var(--primary)}
.sticky-bar small{display:block;color:var(--muted);font-size:.74rem;font-weight:500}

.final{background:var(--primary);color:#fff;border-radius:36px;padding:50px 36px;text-align:center}
.final h2{color:#fff;margin-bottom:10px}
.final p{color:rgba(255,255,255,.85);margin-bottom:22px;font-weight:500}
.final img{max-width:150px;margin:0 auto 22px}
.final .old{text-decoration:line-through;opacity:.7;font-size:.92rem}
.final .new{font-size:1.6rem;margin-bottom:18px}

@media(max-width:820px){
 .hero-stage-inner{grid-template-columns:1fr;text-align:center}
 .hero-stat-list{padding-bottom:20px}
 .hero-stat-list ul{text-align:left;max-width:280px;margin:0 auto}
 .benefit-list,.rev-mini-row,.blog-row{grid-template-columns:1fr}
 .price-row{grid-template-columns:1fr;text-align:center;gap:10px}
 .price-pkg{justify-content:center}
 .navlinks{display:none}
 .guar{flex-direction:column;text-align:center}
 .rev-board{gap:26px}
 body{padding-bottom:74px}
 .hero h1{font-size:2rem}
}
</style>
</head>
<body>

<div class="strip"><span>✓ Independently Written</span><span>✓ Updated __YEAR__</span><span>✓ Every Claim Checked</span></div>

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

<header class="hero"><div class="hero-inner wrap">
<span class="hero-badge">__PILL_TEXT__</span>
<h1>__HERO_H1__</h1>
<p class="lede">__HERO_DESC__</p>
<div class="hero-cta-row">
<a class="btn" href="__AFFILIATE__">__CTA_HERO__</a>
<a class="btn-outline" href="what-is-product.html">What Is __BRAND__?</a>
</div>
</div>
<div class="hero-stage"><div class="hero-stage-inner wrap">
<div class="hero-stat-list">
<div class="rating"><span class="stars">★★★★★</span> 4.8/5 · __REVIEW_COUNT__ reviews</div>
<ul>
<li>__CHECK1__</li>
<li>__CHECK2__</li>
<li>__CHECK3__</li>
<li>__CHECK4__</li>
</ul>
</div>
<div class="hero-jar"><img src="assets/images/hero.png" alt="__BRAND__ product" id="hero-img"></div>
</div></div>
</header>

<div class="trust-strip"><div class="wrap trust-row">
<div class="trust-item"><img src="assets/images/badge-usa.png" alt="USA">Made In The USA</div>
<div class="trust-item"><img src="assets/images/badge-fda.png" alt="FDA">Registered Facility</div>
<div class="trust-item"><img src="assets/images/badge-gmp.png" alt="GMP">GMP Certified</div>
<div class="trust-item"><img src="assets/images/badge-natural.png" alt="Natural">Naturally Sourced</div>
</div></div>

<section class="whatis-band" id="what-is"><div class="wrap whatis-inner">
<span class="eyebrow">What This Actually Is</span>
<h2>What Is __BRAND__?</h2>
<p>__WHATIS_P1__</p>
<div class="callout"><b>Straight talk:</b> __WHATIS_CALLOUT__</div>
<div class="factchip">
<span>__CHIP1__</span><span>__CHIP2__</span><span>__CHIP3__</span><span>__CHIP4__</span>
</div>
</div></section>

<section id="ingredients"><div class="wrap">
<div class="head"><span class="eyebrow">Inside Every Serving</span><h2>__ING_HEADING__</h2><p>Each ingredient explained individually below.</p></div>
<div class="ing-list" id="ing-grid">
__ING_CARD_TEMPLATE__
</div>
</div></section>

<section><div class="wrap">
<div class="timeline">
<div class="head"><span class="eyebrow">The Mechanism</span><h2>How __BRAND__ Actually Works</h2><p>__HIW_INTRO__</p></div>
<div class="tl-list" id="hiw-grid">
__HIW_CARD_TEMPLATE__
</div>
</div>
</div></section>

<section class="whatis-band" id="benefits"><div class="wrap">
<div class="head"><span class="eyebrow">Key Benefits</span><h2>What __BRAND__ Is Formulated To Support</h2><p>Supportive wellness benefits — not promised medical outcomes.</p></div>
<div class="benefit-list" id="benefits-grid">
__BENEFIT_CARD_TEMPLATE__
</div>
</div></section>

<section id="reviews"><div class="wrap">
<div class="head"><span class="eyebrow">Real Reviews</span><h2>What __BRAND__ Customers Report</h2><p>Individual experiences vary. These reflect personal opinions, not guaranteed outcomes.</p></div>
<div id="rev-grid">
__REVIEW_CARD_TEMPLATE__
</div>
<div class="rev-board">
<div><b>4.8</b><span>Average Rating</span></div>
<div><b>__REVIEW_COUNT__</b><span>Customer Reviews</span></div>
<div><b>60-Day</b><span>Money-Back Guarantee</span></div>
</div>
</div></section>

<section id="blog-teaser" class="whatis-band"><div class="wrap">
<div class="head"><span class="eyebrow">Learn More</span><h2>__BRAND__ Guides &amp; Articles</h2><p>Dig deeper into ingredients, usage tips and honest answers on our blog.</p></div>
<div class="blog-row">
<div class="blog-card"><h4>What To Know Before Trying __BRAND__</h4><p>A clear look at ingredients, dosage and what to realistically expect.</p></div>
<div class="blog-card"><h4>How To Read A Supplement Label</h4><p>Understanding ingredient blends, serving sizes and common label claims.</p></div>
<div class="blog-card"><h4>__BRAND__: An Honest Review</h4><p>Strengths, limitations and who should consider this product.</p></div>
</div>
<div style="text-align:center;margin-top:26px"><a class="btn-outline" href="blog/index.html">Visit The __BRAND__ Blog</a></div>
</div></section>

<section class="section-alt"><div class="wrap">
<div class="head"><span class="eyebrow">Before You Click</span><h2>What Happens When You Click "Order Now"?</h2></div>
<div class="grid g3">
<div class="card"><div class="ing-num" style="margin-bottom:14px">1</div><h4>Secure Checkout</h4><p>You'll be taken straight to a secure, encrypted checkout page — no account required.</p></div>
<div class="card"><div class="ing-num" style="margin-bottom:14px">2</div><h4>Enter Your Details</h4><p>Just your shipping and payment info. The whole process takes under a minute.</p></div>
<div class="card"><div class="ing-num" style="margin-bottom:14px">3</div><h4>Confirmation &amp; Shipping</h4><p>You'll get an instant order confirmation by email, with tracking as soon as it ships.</p></div>
</div>
</div></section>

<section id="pricing"><div class="wrap">
<div class="head"><span class="eyebrow">Pick Your Pack</span><h2>Choose Your __BRAND__ Package</h2><p>Larger bundles reduce the cost per bottle.</p></div>
<div class="price-compare"><span class="price-was">Regular Price: __PRICE_HIGH__/bottle</span><span class="price-arrow">→</span><span class="price-now">Today: __PRICE_FROM__/bottle</span></div>
<div class="price-table" id="plans-grid">
<div class="price-row head-row"><div>Package</div><div>Per Bottle</div><div>Total</div><div>Order</div></div>
__PLAN_CARD_TEMPLATE__
</div>
<div class="flag">__PRICING_NOTE__</div>
</div></section>

__BONUS_SECTION__

<section class="whatis-band"><div class="wrap">
<div class="guar">
<img src="assets/images/guarantee.png" alt="Money back guarantee">
<div><span class="eyebrow">Zero Risk</span><h3>A Real 60-Day Guarantee</h3><p>__GUARANTEE_TEXT__</p></div>
</div>
</div></section>

<section id="faq"><div class="wrap">
<div class="head"><span class="eyebrow">Common Questions</span><h2>__BRAND__ FAQ, Answered Honestly</h2></div>
<div class="faq" id="faq-list">
__FAQ_ROW_TEMPLATE__
</div>
</div></section>

<section class="whatis-band"><div class="wrap">
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
</script>
</body></html>
