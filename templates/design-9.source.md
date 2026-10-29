<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>__TITLE__</title>
<meta name="description" content="__META_DESC__">
<link rel="canonical" href="__CANONICAL__">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
:root{
 --primary:__COLOR_PRIMARY__;
 --primary-dark:__COLOR_DARK__;
 --primary-light:__COLOR_LIGHT__;
 --accent:__COLOR_ACCENT__;
 --on-primary:__COLOR_ON_PRIMARY__;
 --ink:#0d1117;
 --muted:#5b6472;
 --bg:#ffffff;
 --bg-alt:#0d1117;
 --border:#e8eaed;
 --radius:20px;
}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Manrope',system-ui,sans-serif;color:var(--ink);background:var(--bg);line-height:1.6}
h1,h2,h3,h4{font-family:'Manrope',sans-serif;font-weight:800;line-height:1.08;letter-spacing:-.02em;color:var(--ink)}
.wrap{max-width:1160px;margin:0 auto;padding:0 24px}
a{color:inherit;text-decoration:none}
img{max-width:100%;display:block}

.strip{background:var(--ink);color:#fff;font-size:.78rem;padding:9px 0;text-align:center;font-weight:600;letter-spacing:.02em}
.strip span{opacity:.9;margin:0 12px}

nav{padding:20px 0;position:sticky;top:0;background:#fff;z-index:50;border-bottom:3px solid var(--ink)}
nav .wrap{display:flex;align-items:center;justify-content:space-between;gap:20px}
.logo{font-weight:800;font-size:1.5rem;color:var(--ink);letter-spacing:-.02em}
.navlinks{display:flex;align-items:center;gap:28px;list-style:none;flex-wrap:wrap}
.navlinks a{font-size:.92rem;font-weight:700;color:var(--ink)}
.navlinks a:hover{color:var(--primary)}
.nav-btn{background:var(--primary);color:var(--on-primary)!important;padding:12px 26px;border-radius:999px;font-weight:800!important;font-size:.85rem!important;box-shadow:5px 5px 0 var(--ink)}

.btn{display:inline-block;background:var(--primary);color:var(--on-primary);padding:18px 36px;border-radius:999px;font-weight:800;font-size:1.05rem;border:3px solid var(--ink);cursor:pointer;transition:transform .12s;box-shadow:6px 6px 0 var(--ink)}
.btn:hover{transform:translate(-2px,-2px);box-shadow:8px 8px 0 var(--ink)}
.btn-outline{display:inline-block;background:#fff;color:var(--ink);padding:16px 32px;border-radius:999px;font-weight:800;border:3px solid var(--ink)}
.btn-sub{display:block;font-size:.72rem;font-weight:600;opacity:.85;margin-top:3px}

.hero{background:var(--bg-alt);padding:70px 0 80px;position:relative;overflow:hidden}
.hero-grid{display:grid;grid-template-columns:1.1fr 1fr;gap:56px;align-items:center;position:relative;z-index:2}
.hero-center{text-align:center;max-width:760px;margin:0 auto;position:relative;z-index:2}
.hero-center h1{font-size:3.2rem}
.hero-img-center{margin:36px auto;max-width:340px;background:linear-gradient(135deg,var(--primary),var(--primary-dark));border-radius:28px;padding:32px;box-shadow:12px 12px 0 rgba(255,255,255,.08)}
.hero-img-center img{max-width:100%;filter:drop-shadow(0 20px 34px rgba(0,0,0,.5))}
.checks-row{display:flex;flex-wrap:wrap;justify-content:center;gap:8px 24px;list-style:none;margin:22px 0}
.checks-row li{padding-left:26px}
.pill{display:inline-flex;align-items:center;gap:8px;background:var(--primary);color:var(--on-primary);font-size:.8rem;font-weight:800;padding:10px 20px;border-radius:999px;margin-bottom:20px;transform:rotate(-2deg)}
.hero h1{font-size:3rem;margin-bottom:20px;color:#fff}
.hero .lede{font-size:1.1rem;color:rgba(255,255,255,.75);margin-bottom:26px;font-weight:500}
.rating{display:flex;align-items:center;gap:10px;margin-bottom:22px;font-size:.9rem;color:rgba(255,255,255,.8);font-weight:600}
.stars{color:var(--primary);letter-spacing:2px;font-size:1.1rem}
.factrow{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin:24px 0}
.factrow div{background:rgba(255,255,255,.06);border:2px solid rgba(255,255,255,.15);border-radius:14px;padding:14px 8px;text-align:center}
.factrow b{display:block;font-size:1.3rem;color:var(--primary);font-weight:800}
.factrow span{font-size:.7rem;color:rgba(255,255,255,.6);font-weight:600;text-transform:uppercase;letter-spacing:.04em}
.checks{list-style:none;margin:20px 0 28px}
.checks li{position:relative;padding-left:32px;margin-bottom:12px;font-size:.98rem;color:#fff;font-weight:600}
.checks li:before{content:'✓';position:absolute;left:0;top:0;width:22px;height:22px;background:var(--primary);color:var(--on-primary);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:.75rem;font-weight:800}
.hero-actions{display:flex;gap:16px;flex-wrap:wrap;margin-bottom:16px}
.trustline{font-size:.8rem;color:rgba(255,255,255,.6);font-weight:600}
.hero-img{background:linear-gradient(135deg,var(--primary),var(--primary-dark));border-radius:28px;padding:44px;text-align:center;position:relative;transform:rotate(2deg);box-shadow:10px 10px 0 rgba(255,255,255,.1)}
.hero-img img{max-width:70%;margin:0 auto;filter:drop-shadow(0 24px 40px rgba(0,0,0,.5))}

section{padding:76px 0}
.section-alt{background:var(--bg-alt);color:#fff}
.section-alt h2,.section-alt .head h2{color:#fff}
.section-alt .head p{color:rgba(255,255,255,.65)}
.head{text-align:center;max-width:680px;margin:0 auto 46px}
.eyebrow{display:inline-block;background:var(--ink);color:#fff;font-weight:800;font-size:.75rem;letter-spacing:.06em;text-transform:uppercase;margin-bottom:14px;padding:6px 16px;border-radius:999px}
.section-alt .eyebrow{background:var(--primary);color:var(--on-primary)}
.head h2{font-size:2.3rem;margin-bottom:12px}
.head p{color:var(--muted);font-size:1.05rem;font-weight:500}

.grid{display:grid;gap:22px}
.g2{grid-template-columns:repeat(2,1fr)}
.g3{grid-template-columns:repeat(3,1fr)}
.g4{grid-template-columns:repeat(4,1fr)}
.card{background:#fff;border:3px solid var(--ink);border-radius:var(--radius);padding:28px;box-shadow:6px 6px 0 var(--border)}
.section-alt .card{background:rgba(255,255,255,.05);border:2px solid rgba(255,255,255,.15);box-shadow:none}
.card h4{font-size:1.1rem;margin-bottom:10px;font-weight:800}
.card p{color:var(--muted);font-size:.94rem;font-weight:500}
.section-alt .card p{color:rgba(255,255,255,.65)}
.badge-card{text-align:center}
.badge-card img{width:60px;height:60px;object-fit:contain;margin:0 auto 14px}

.split{display:grid;grid-template-columns:1fr 1.1fr;gap:56px;align-items:center}
.split-reverse{display:grid;grid-template-columns:1.1fr 1fr;gap:56px;align-items:center}
.split-reverse img{order:2}
.split img{border-radius:24px;border:3px solid var(--ink)}
.callout{background:var(--ink);color:#fff;border-radius:16px;padding:20px 24px;margin:22px 0;font-size:.95rem;font-weight:600}
.factchip{display:inline-flex;gap:10px;flex-wrap:wrap;margin-top:18px}
.factchip span{background:var(--ink);color:#fff;border-radius:999px;padding:8px 18px;font-size:.82rem;font-weight:700}

.ing-card{display:flex;gap:18px;background:#fff;border:3px solid var(--ink);border-radius:var(--radius);padding:24px;box-shadow:6px 6px 0 var(--border)}
.ing-num{flex:none;width:42px;height:42px;border-radius:12px;background:var(--primary);color:var(--on-primary);display:flex;align-items:center;justify-content:center;font-weight:800}

.dark{background:var(--ink);color:#fff}
.dark .head h2,.dark h3{color:#fff}
.dark .head p{color:rgba(255,255,255,.6)}
.step-card{background:rgba(255,255,255,.05);border:2px solid rgba(255,255,255,.15);border-radius:var(--radius);padding:24px}
.step-card h4{color:#fff;font-weight:800}
.step-card p{color:rgba(255,255,255,.6)}
.step-num{width:34px;height:34px;border-radius:10px;background:var(--primary);color:var(--on-primary);display:flex;align-items:center;justify-content:center;font-weight:800;font-size:.9rem;margin-bottom:12px}

.rev-card{background:#fff;border:3px solid var(--ink);border-radius:var(--radius);padding:26px;box-shadow:6px 6px 0 var(--border)}
.rev-head{display:flex;align-items:center;gap:14px;margin-bottom:12px}
.rev-head img{width:50px;height:50px;border-radius:50%;object-fit:cover;border:2px solid var(--ink)}
.rev-name{font-weight:800;font-size:.96rem;color:var(--ink)}
.rev-sub{font-size:.78rem;color:var(--muted);font-weight:600}
.rev-card p{color:var(--ink)!important}
.rev-stars{color:var(--primary);margin-bottom:10px;font-size:1rem}
.rev-board{display:flex;justify-content:center;gap:60px;margin-top:40px;text-align:center;flex-wrap:wrap}
.rev-board b{display:block;font-size:2rem;font-weight:800;color:var(--primary)}
.rev-board span{font-size:.78rem;color:var(--muted);font-weight:700;text-transform:uppercase}

.plans{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;align-items:start}
.plan{background:#fff;border:3px solid var(--ink);border-radius:22px;padding:30px 24px;text-align:center;position:relative;box-shadow:6px 6px 0 var(--border)}
.plan.top{border-color:var(--primary);box-shadow:8px 8px 0 var(--primary)}
.plan-badge{position:absolute;top:-16px;left:50%;transform:translateX(-50%);background:var(--primary);color:var(--on-primary);font-size:.72rem;font-weight:800;padding:7px 18px;border-radius:999px;white-space:nowrap;border:2px solid var(--ink)}
.plan img{max-width:130px;margin:12px auto 18px}
.plan-ttl{font-weight:800;font-size:1.2rem;margin-bottom:2px}
.plan-sub{font-size:.78rem;color:var(--muted);margin-bottom:16px;font-weight:600}
.plan-price{font-size:2.2rem;font-weight:800;color:var(--ink)}
.plan-price small{font-size:.9rem;font-weight:600;color:var(--muted)}
.plan-tot{font-size:.86rem;color:var(--muted);margin:6px 0 2px;font-weight:600}
.plan-ship{font-size:.82rem;color:var(--primary);font-weight:800;margin-bottom:18px}
.plan ul{list-style:none;text-align:left;margin-bottom:20px}
.plan ul li{font-size:.86rem;padding:6px 0 6px 26px;position:relative;font-weight:600}
.plan ul li:before{content:'✓';position:absolute;left:0;color:var(--primary);font-weight:800}
.plan .btn{width:100%;padding:15px}
.flag{background:var(--ink);color:#fff;border-radius:16px;padding:18px 22px;margin-top:30px;font-size:.9rem;font-weight:600;text-align:center;max-width:780px;margin-left:auto;margin-right:auto}

.guar{display:flex;align-items:center;gap:44px;background:var(--ink);color:#fff;border-radius:28px;padding:44px}
.guar img{width:150px;flex:none}
.guar h3{font-size:1.6rem;margin-bottom:12px;color:#fff}
.guar p{color:rgba(255,255,255,.7);margin-bottom:8px;font-weight:500}
.guar .eyebrow{background:var(--primary);color:var(--on-primary)}

.faq{max-width:780px;margin:0 auto}
.faq-row{border:3px solid var(--ink);border-radius:16px;margin-bottom:14px;overflow:hidden}
.faq-btn{width:100%;text-align:left;background:#fff;border:none;padding:20px 22px;font-size:1.02rem;font-weight:800;cursor:pointer;color:var(--ink);display:flex;justify-content:space-between;align-items:center;font-family:'Manrope',sans-serif}
.faq-btn:after{content:'+';font-size:1.6rem;color:var(--primary);font-weight:800}
.faq-body{padding:0 22px 20px;color:var(--muted);font-size:.94rem;font-weight:500;display:none;background:#fff}
.faq-row.open .faq-body{display:block}
.faq-row.open .faq-btn:after{content:'−'}

footer{background:var(--ink);color:rgba(255,255,255,.75);padding:60px 0 32px;font-size:.86rem}
.foot-nav{display:flex;flex-wrap:wrap;gap:24px;list-style:none;margin-bottom:20px}
.foot-nav a{color:rgba(255,255,255,.85);font-weight:700}
.foot-nav a:hover{color:var(--primary)}
.foot-legal{display:flex;flex-wrap:wrap;gap:18px;list-style:none;margin-bottom:26px;font-size:.8rem}
.foot-legal a{color:rgba(255,255,255,.55)}
footer hr{border:none;border-top:2px solid rgba(255,255,255,.15);margin:24px 0}
footer p{margin-bottom:12px;color:rgba(255,255,255,.55);font-size:.78rem;line-height:1.7}
.cr{margin-top:18px;font-size:.78rem;color:rgba(255,255,255,.45);font-weight:600}

.sticky-bar{position:fixed;bottom:0;left:0;right:0;background:#fff;border-top:3px solid var(--ink);padding:14px 20px;display:flex;align-items:center;justify-content:space-between;gap:16px;box-shadow:0 -8px 24px rgba(0,0,0,.12);z-index:60}
.sticky-bar b{font-weight:800;font-size:1.1rem}
.sticky-bar small{display:block;color:var(--muted);font-size:.75rem;font-weight:600}

.final{background:linear-gradient(135deg,var(--primary),var(--primary-dark));color:#fff;border-radius:32px;padding:60px 44px;text-align:center;border:4px solid var(--ink)}
.final h2{color:#fff;margin-bottom:14px;font-size:2.2rem}
.final p{color:rgba(255,255,255,.85);margin-bottom:26px;font-weight:600}
.final img{max-width:170px;margin:0 auto 26px}
.final .old{text-decoration:line-through;opacity:.7;font-size:1rem;font-weight:600}
.final .new{font-size:2rem;font-weight:800;margin-bottom:22px}

@media(max-width:860px){
 .hero-grid,.split{grid-template-columns:1fr}
 .g4{grid-template-columns:repeat(2,1fr)}
 .g3,.g2{grid-template-columns:1fr}
 .plans{grid-template-columns:1fr}
 .factrow{grid-template-columns:repeat(2,1fr)}
 .navlinks{display:none}
 .guar{flex-direction:column;text-align:center}
 .rev-board{gap:32px}
 body{padding-bottom:78px}
 .hero h1{font-size:2.2rem}
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

<header class="hero"><div class="wrap hero-center">
<span class="pill">__PILL_TEXT__</span>
<h1>__HERO_H1__</h1>
<p class="lede">__HERO_DESC__</p>
<div class="rating"><span class="stars">★★★★★</span> <b>4.8 / 5</b> from __REVIEW_COUNT__ reviews</div>
<div class="hero-img-center"><img src="assets/images/hero.png" alt="__BRAND__ product" id="hero-img"></div>
<div class="factrow">
<div><b>__FACT1_NUM__</b><span>__FACT1_LABEL__</span></div>
<div><b>__FACT2_NUM__</b><span>__FACT2_LABEL__</span></div>
<div><b>__FACT3_NUM__</b><span>__FACT3_LABEL__</span></div>
<div><b>__FACT4_NUM__</b><span>__FACT4_LABEL__</span></div>
</div>
<div class="hero-actions">
<a class="btn" href="__AFFILIATE__">Get __BRAND__ — __PRICE_FROM__<span class="btn-sub">Official Site • Secure Checkout</span></a>
<a class="btn-outline" href="what-is-product.html">What Is __BRAND__?</a>
</div>
<ul class="checks checks-row">
<li>__CHECK1__</li>
<li>__CHECK2__</li>
<li>__CHECK3__</li>
<li>__CHECK4__</li>
</ul>
<div class="trustline">Made in USA • GMP Certified • 60-Day Guarantee</div>
</div></header>

<section><div class="wrap">
<div class="head"><span class="eyebrow">Why Choose __BRAND__</span><h2>Built On Quality You Can Verify</h2></div>
<div class="grid g4">
<div class="card badge-card"><img src="assets/images/badge-usa.png" alt="Made in USA"><h4>Made In The USA</h4><p>Manufactured under strict quality control procedures.</p></div>
<div class="card badge-card"><img src="assets/images/badge-fda.png" alt="FDA registered"><h4>Registered Facility</h4><p>Produced in an FDA-registered facility.</p></div>
<div class="card badge-card"><img src="assets/images/badge-gmp.png" alt="GMP certified"><h4>GMP Certified</h4><p>Made under Good Manufacturing Practice guidelines.</p></div>
<div class="card badge-card"><img src="assets/images/badge-natural.png" alt="Natural"><h4>Naturally Sourced</h4><p>Thoughtfully selected natural ingredients.</p></div>
</div>
</div></section>

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

<section class="dark" id="how-it-works"><div class="wrap">
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

<section id="pricing"><div class="wrap">
<div class="head"><span class="eyebrow">Pick Your Pack</span><h2>Choose Your __BRAND__ Package</h2><p>Larger bundles reduce the cost per bottle.</p></div>
<div class="plans" id="plans-grid">
__PLAN_CARD_TEMPLATE__
</div>
<div class="flag">__PRICING_NOTE__</div>
</div></section>

__BONUS_SECTION__

<section class="section-alt"><div class="wrap">
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

<section class="section-alt"><div class="wrap">
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
