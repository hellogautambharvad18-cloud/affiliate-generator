<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>__TITLE__</title>
<meta name="description" content="__META_DESC__">
<link rel="canonical" href="__CANONICAL__">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link crossorigin href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700;800&family=DM+Sans:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">
<style>
:root{
 --primary:__COLOR_PRIMARY__;
 --primary-dark:__COLOR_DARK__;
 --primary-light:__COLOR_LIGHT__;
 --accent:__COLOR_ACCENT__;
 --on-primary:__COLOR_ON_PRIMARY__;
 --ink:#161a23;
 --muted:#666f80;
 --bg:#fdfcfa;
 --bg-alt:#f3f1ec;
 --border:#e7e3da;
 --radius:22px;
}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'DM Sans',system-ui,sans-serif;color:var(--ink);background:var(--bg);line-height:1.65;-webkit-font-smoothing:antialiased}
h1,h2,h3,h4{font-family:'Sora',system-ui,sans-serif;font-weight:700;line-height:1.15;letter-spacing:-.01em;color:var(--ink)}
.wrap{max-width:1160px;margin:0 auto;padding:0 24px}
a{color:inherit;text-decoration:none}
img{max-width:100%;display:block}
ul{list-style:none}

/* Top notice strip */
.strip{background:var(--ink);color:#fff;font-size:.78rem;padding:9px 0;text-align:center;letter-spacing:.02em}
.strip span{opacity:.85;margin:0 12px}

/* Nav */
nav{padding:18px 0;position:sticky;top:0;background:rgba(253,252,250,.92);backdrop-filter:blur(10px);z-index:50;border-bottom:1px solid var(--border)}
nav .wrap{display:flex;align-items:center;justify-content:space-between;gap:20px}
.logo{font-family:'Sora',sans-serif;font-weight:800;font-size:1.35rem;color:var(--ink);display:flex;align-items:center;gap:8px}
.logo:before{content:'';width:10px;height:10px;border-radius:3px;background:var(--primary);display:inline-block;transform:rotate(45deg)}
.navlinks{display:flex;align-items:center;gap:26px}
.navlinks a{font-size:.9rem;font-weight:500;color:var(--muted)}
.navlinks a:hover{color:var(--ink)}
.nav-btn{background:var(--ink);color:#fff!important;padding:11px 22px;border-radius:999px;font-weight:600!important;font-size:.84rem!important}
.nav-btn:hover{background:var(--primary-dark)}

/* Buttons */
.btn{display:inline-flex;align-items:center;justify-content:center;flex-direction:column;background:var(--ink);color:#fff;padding:16px 32px;border-radius:14px;font-weight:700;font-size:1rem;border:none;cursor:pointer;transition:transform .15s,background .15s}
.btn:hover{background:var(--primary-dark);transform:translateY(-2px)}
.btn-outline{display:inline-block;background:transparent;color:var(--ink);padding:14px 28px;border-radius:14px;font-weight:600;border:1.5px solid var(--border)}
.btn-outline:hover{border-color:var(--ink)}
.btn-sub{display:block;font-size:.72rem;font-weight:400;opacity:.75;margin-top:3px}

/* Hero */
.hero{padding:64px 0 40px;overflow:hidden}
.hero-grid{display:grid;grid-template-columns:1.05fr .95fr;gap:60px;align-items:center}
.pill{display:inline-flex;align-items:center;gap:8px;background:var(--primary-light);color:var(--primary-dark);font-size:.78rem;font-weight:700;padding:8px 16px;border-radius:999px;margin-bottom:20px;text-transform:uppercase;letter-spacing:.04em}
.hero h1{font-size:2.7rem;margin-bottom:18px}
.hero .lede{font-size:1.06rem;color:var(--muted);margin-bottom:26px;max-width:46ch}
.rating{display:flex;align-items:center;gap:10px;margin-bottom:22px;font-size:.9rem;color:var(--muted)}
.stars{color:#e8a534;letter-spacing:2px}
.checks{margin:0 0 28px}
.checks li{position:relative;padding-left:30px;margin-bottom:11px;font-size:.95rem;color:var(--ink)}
.checks li:before{content:'';position:absolute;left:0;top:3px;width:18px;height:18px;border-radius:6px;background:var(--primary-light);border:1.5px solid var(--primary)}
.checks li:after{content:'✓';position:absolute;left:3.5px;top:1px;color:var(--primary-dark);font-weight:700;font-size:.72rem}
.hero-actions{display:flex;gap:14px;flex-wrap:wrap;margin-bottom:16px}
.trustline{font-size:.8rem;color:var(--muted);display:flex;gap:16px;flex-wrap:wrap}
.hero-media{position:relative}
.hero-img{background:linear-gradient(155deg,var(--primary-light),var(--bg-alt));border-radius:32px;padding:44px;text-align:center;position:relative}
.hero-img img{max-width:72%;margin:0 auto;filter:drop-shadow(0 30px 44px rgba(0,0,0,.22))}
.float-card{position:absolute;background:#fff;border-radius:16px;padding:14px 18px;box-shadow:0 16px 36px -12px rgba(20,20,30,.22);font-size:.82rem}
.float-card b{display:block;font-family:'Sora',sans-serif;font-size:1.3rem;color:var(--primary-dark)}
.float-card span{color:var(--muted)}
.float-card.fc1{top:14px;left:-18px}
.float-card.fc2{bottom:18px;right:-14px}
@media(max-width:860px){.float-card{position:static;display:inline-block;margin:10px 8px 0 0}}

/* Section shell */
section{padding:70px 0}
.section-alt{background:var(--bg-alt)}
.head{text-align:center;max-width:620px;margin:0 auto 44px}
.eyebrow{display:inline-block;color:var(--primary-dark);font-weight:700;font-size:.76rem;letter-spacing:.1em;text-transform:uppercase;margin-bottom:12px}
.head h2{font-size:2.05rem;margin-bottom:12px}
.head p{color:var(--muted);font-size:1rem}

/* Trust strip badges */
.badge-row{display:flex;justify-content:center;gap:14px;flex-wrap:wrap}
.badge-chip{display:flex;align-items:center;gap:12px;background:#fff;border:1px solid var(--border);border-radius:16px;padding:14px 20px;min-width:190px}
.badge-chip img{width:34px;height:34px;object-fit:contain;flex:none}
.badge-chip h4{font-size:.88rem;margin-bottom:2px}
.badge-chip p{font-size:.74rem;color:var(--muted)}

/* Grid cards */
.grid{display:grid;gap:22px}
.g2{grid-template-columns:repeat(2,1fr)}
.g3{grid-template-columns:repeat(3,1fr)}
.g4{grid-template-columns:repeat(4,1fr)}
.card{background:#fff;border:1px solid var(--border);border-radius:var(--radius);padding:28px}
.card h4{font-size:1.05rem;margin-bottom:8px}
.card p{color:var(--muted);font-size:.92rem}

/* What-is split */
.split{display:grid;grid-template-columns:.95fr 1.1fr;gap:56px;align-items:center}
.split-media{border-radius:28px;overflow:hidden;background:var(--bg-alt);padding:36px}
.split img{border-radius:18px}
.callout{background:var(--ink);color:#fff;border-radius:16px;padding:20px 22px;margin:20px 0;font-size:.92rem}
.callout b{color:var(--primary-light)}
.factchip{display:flex;gap:10px;flex-wrap:wrap;margin-top:18px}
.factchip span{background:var(--bg-alt);border:1px solid var(--border);border-radius:999px;padding:7px 15px;font-size:.8rem;color:var(--muted);font-weight:500}

/* Ingredients numbered */
.ing-card{display:flex;gap:18px;background:#fff;border:1px solid var(--border);border-radius:var(--radius);padding:24px}
.ing-num{flex:none;width:42px;height:42px;border-radius:12px;background:var(--primary-light);color:var(--primary-dark);display:flex;align-items:center;justify-content:center;font-weight:800;font-family:'Sora',sans-serif;font-size:.95rem}

/* How it works dark */
.dark{background:var(--ink);color:#fff}
.dark .head h2,.dark h3{color:#fff}
.dark .eyebrow{color:var(--primary-light)}
.dark .head p{color:rgba(255,255,255,.62)}
.step-card{background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.1);border-radius:var(--radius);padding:24px}
.step-card h4{color:#fff;margin-top:14px}
.step-card p{color:rgba(255,255,255,.62)}
.step-num{width:34px;height:34px;border-radius:10px;background:var(--primary);color:var(--on-primary);display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.82rem}

/* Reviews */
.rev-card{background:#fff;border:1px solid var(--border);border-radius:var(--radius);padding:26px}
.rev-head{display:flex;align-items:center;gap:12px;margin-bottom:12px}
.rev-head img{width:46px;height:46px;border-radius:50%;object-fit:cover}
.rev-name{font-weight:700;font-size:.94rem;color:var(--ink)}
.rev-card p{color:var(--ink)!important}
.rev-sub{font-size:.78rem;color:var(--muted)}
.rev-stars{color:#e8a534;margin-bottom:10px;font-size:.9rem}
.rev-board{display:flex;justify-content:center;gap:60px;margin-top:40px;text-align:center;flex-wrap:wrap}
.rev-board b{display:block;font-size:1.8rem;font-family:'Sora',sans-serif;color:var(--primary-dark)}
.rev-board span{font-size:.8rem;color:var(--muted)}

/* Pricing */
.plans{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;align-items:start}
.plan{background:#fff;border:2px solid var(--border);border-radius:26px;padding:30px 24px;text-align:center;position:relative}
.plan.top{border-color:var(--primary);background:linear-gradient(180deg,var(--primary-light),#fff 40%);transform:translateY(-14px);box-shadow:0 26px 48px -18px color-mix(in srgb, var(--primary) 45%, transparent)}
.plan-badge{position:absolute;top:-14px;left:50%;transform:translateX(-50%);background:var(--ink);color:#fff;font-size:.7rem;font-weight:700;padding:6px 18px;border-radius:999px;white-space:nowrap;letter-spacing:.03em}
.plan img{max-width:120px;margin:12px auto 18px}
.plan-ttl{font-family:'Sora',sans-serif;font-weight:700;font-size:1.1rem;margin-bottom:2px}
.plan-sub{font-size:.78rem;color:var(--muted);margin-bottom:16px}
.plan-price{font-size:2.1rem;font-family:'Sora',sans-serif;font-weight:800;color:var(--ink)}
.plan-price small{font-size:.85rem;font-weight:500;color:var(--muted)}
.plan-tot{font-size:.85rem;color:var(--muted);margin:6px 0 2px}
.plan-ship{font-size:.8rem;color:var(--primary-dark);font-weight:700;margin-bottom:18px}
.plan ul{text-align:left;margin-bottom:20px}
.plan ul li{font-size:.85rem;padding:6px 0 6px 24px;position:relative;color:var(--ink)}
.plan ul li:before{content:'✓';position:absolute;left:0;color:var(--primary-dark);font-weight:700}
.plan .btn{width:100%;padding:14px;border-radius:12px}
.flag{background:#fff;border:1px solid var(--border);border-radius:16px;padding:18px 22px;margin-top:30px;font-size:.88rem;text-align:center;max-width:740px;margin-left:auto;margin-right:auto;color:var(--muted)}

/* Guarantee */
.guar{display:grid;grid-template-columns:auto 1fr;align-items:center;gap:44px;background:var(--bg-alt);border-radius:28px;padding:44px}
.guar img{width:130px;flex:none}
.guar h3{font-size:1.5rem;margin-bottom:10px}
.guar p{color:var(--muted);margin-bottom:8px}
@media(max-width:640px){.guar{grid-template-columns:1fr;text-align:center;justify-items:center}}

/* FAQ */
.faq{max-width:760px;margin:0 auto;display:flex;flex-direction:column;gap:12px}
.faq-row{border:1px solid var(--border);border-radius:16px;background:#fff;overflow:hidden}
.faq-btn{width:100%;text-align:left;background:none;border:none;padding:20px 22px;font-size:1rem;font-weight:600;cursor:pointer;color:var(--ink);display:flex;justify-content:space-between;align-items:center;gap:16px;font-family:'DM Sans',sans-serif}
.faq-btn:after{content:'+';font-size:1.5rem;color:var(--primary-dark);font-weight:400;flex:none}
.faq-body{padding:0 22px 20px;color:var(--muted);font-size:.93rem;display:none}
.faq-row.open .faq-body{display:block}
.faq-row.open .faq-btn:after{content:'−'}

/* Footer */
footer{background:var(--ink);color:rgba(255,255,255,.75);padding:60px 0 30px;font-size:.86rem}
.foot-top{display:flex;justify-content:space-between;flex-wrap:wrap;gap:30px;margin-bottom:30px}
.foot-brand{max-width:320px}
.foot-brand .logo{color:#fff;margin-bottom:10px}
.foot-brand .logo:before{background:var(--primary-light)}
.foot-nav{display:flex;flex-wrap:wrap;gap:22px}
.foot-nav a{color:rgba(255,255,255,.78)}
.foot-nav a:hover{color:#fff}
.foot-legal{display:flex;flex-wrap:wrap;gap:18px;margin-bottom:24px;font-size:.8rem}
.foot-legal a{color:rgba(255,255,255,.55)}
footer hr{border:none;border-top:1px solid rgba(255,255,255,.12);margin:22px 0}
footer p{margin-bottom:12px;color:rgba(255,255,255,.55);font-size:.78rem;line-height:1.7}
.cr{margin-top:18px;font-size:.78rem;color:rgba(255,255,255,.45)}

/* Sticky bar */
.sticky-bar{position:fixed;bottom:0;left:0;right:0;background:#fff;border-top:1px solid var(--border);padding:12px 20px;display:flex;align-items:center;justify-content:space-between;gap:16px;box-shadow:0 -10px 26px rgba(0,0,0,.08);z-index:60}
.sticky-bar b{font-family:'Sora',sans-serif}
.sticky-bar small{display:block;color:var(--muted);font-size:.75rem}

/* Final CTA */
.final{background:linear-gradient(155deg,var(--ink),var(--primary-dark));color:#fff;border-radius:32px;padding:60px 40px;text-align:center}
.final h2{color:#fff;margin-bottom:12px}
.final p{color:rgba(255,255,255,.7);margin-bottom:26px;max-width:52ch;margin-left:auto;margin-right:auto}
.final img{max-width:150px;margin:0 auto 26px;filter:drop-shadow(0 20px 30px rgba(0,0,0,.3))}
.final .old{text-decoration:line-through;opacity:.55;font-size:.95rem}
.final .new{font-size:1.8rem;font-family:'Sora',sans-serif;font-weight:800;margin-bottom:22px}

@media(max-width:860px){
 .hero-grid,.split{grid-template-columns:1fr}
 .g4{grid-template-columns:repeat(2,1fr)}
 .g3,.g2{grid-template-columns:1fr}
 .plans{grid-template-columns:1fr}
 .plan.top{transform:none}
 .navlinks{display:none}
 .rev-board{gap:28px}
 body{padding-bottom:74px}
 .foot-top{flex-direction:column}
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

<header class="hero"><div class="wrap hero-grid">
<div>
<span class="pill">__PILL_TEXT__</span>
<h1>__HERO_H1__</h1>
<div class="rating"><span class="stars">★★★★★</span> <b>4.8 / 5</b> from __REVIEW_COUNT__ reviews</div>
<p class="lede">__HERO_DESC__</p>
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
<div class="trustline"><span>Made in USA</span><span>GMP Certified</span><span>60-Day Guarantee</span></div>
</div>
<div class="hero-media">
<div class="hero-img"><img src="assets/images/hero.png" alt="__BRAND__ product" id="hero-img"></div>
<div class="float-card fc1"><b>__FACT1_NUM__</b><span>__FACT1_LABEL__</span></div>
<div class="float-card fc2"><b>__FACT3_NUM__</b><span>__FACT3_LABEL__</span></div>
</div>
</div></header>

<section><div class="wrap">
<div class="head"><span class="eyebrow">Why Choose __BRAND__</span><h2>Built On Quality You Can Verify</h2></div>
<div class="badge-row">
<div class="badge-chip"><img src="assets/images/badge-usa.png" alt="Made in USA"><div><h4>Made In The USA</h4><p>Strict quality control</p></div></div>
<div class="badge-chip"><img src="assets/images/badge-fda.png" alt="FDA registered"><div><h4>Registered Facility</h4><p>FDA-registered plant</p></div></div>
<div class="badge-chip"><img src="assets/images/badge-gmp.png" alt="GMP certified"><div><h4>GMP Certified</h4><p>Good Manufacturing Practice</p></div></div>
<div class="badge-chip"><img src="assets/images/badge-natural.png" alt="Natural"><div><h4>Naturally Sourced</h4><p>Thoughtfully chosen ingredients</p></div></div>
</div>
</div></section>

<section class="section-alt" id="what-is"><div class="wrap split">
<div class="split-media"><img src="assets/images/feature-shot.png" alt="__BRAND__ overview" id="whatis-img"></div>
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
<div class="foot-top">
<div class="foot-brand"><a class="logo" href="index.html">__BRAND__</a><p style="margin-top:6px">Independent product information to help you make an informed decision.</p></div>
<ul class="foot-nav">
<li><a href="index.html">Home</a></li>
<li><a href="what-is-product.html">What Is __BRAND__</a></li>
<li><a href="how-it-works.html">How It Works</a></li>
<li><a href="ingredients.html">Ingredients</a></li>
<li><a href="benefits.html">Benefits</a></li>
<li><a href="reviews.html">Reviews</a></li>
<li><a href="__AFFILIATE__">__CTA_AFTERFAQ__</a></li>
</ul>
</div>
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
