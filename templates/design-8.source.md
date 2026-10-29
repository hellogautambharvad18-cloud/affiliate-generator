<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>__TITLE__</title>
<meta name="description" content="__META_DESC__">
<link rel="canonical" href="__CANONICAL__">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Fraunces:wght@500;600;700&display=swap" rel="stylesheet">
<style>
:root{
 --primary:__COLOR_PRIMARY__;
 --primary-dark:__COLOR_DARK__;
 --primary-light:__COLOR_LIGHT__;
 --accent:__COLOR_ACCENT__;
 --on-primary:__COLOR_ON_PRIMARY__;
 --ink:#182236;
 --muted:#5c6b85;
 --bg:#ffffff;
 --bg-alt:#f7f9fc;
 --border:#e4e9f2;
 --radius:14px;
}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Inter',system-ui,sans-serif;color:var(--ink);background:var(--bg);line-height:1.6}
h1,h2,h3,h4{font-family:'Fraunces',Georgia,serif;font-weight:600;line-height:1.2;color:var(--ink)}
.wrap{max-width:1120px;margin:0 auto;padding:0 24px}
a{color:inherit;text-decoration:none}
img{max-width:100%;display:block}

/* Top notice strip */
.strip{background:var(--primary-dark);color:#fff;font-size:.8rem;padding:8px 0;text-align:center}
.strip span{opacity:.92;margin:0 10px}

/* Nav */
nav{border-bottom:1px solid var(--border);padding:16px 0;position:sticky;top:0;background:#fff;z-index:50}
nav .wrap{display:flex;align-items:center;justify-content:space-between;gap:20px}
.logo{font-family:'Fraunces',serif;font-weight:700;font-size:1.3rem;color:var(--ink)}
.logo em{font-style:normal;color:var(--primary)}
.navlinks{display:flex;align-items:center;gap:24px;list-style:none;flex-wrap:wrap}
.navlinks a{font-size:.92rem;font-weight:500;color:var(--muted)}
.navlinks a:hover{color:var(--primary)}
.nav-btn{background:var(--primary);color:var(--on-primary)!important;padding:10px 20px;border-radius:999px;font-weight:600!important;font-size:.85rem!important}

/* Buttons */
.btn{display:inline-block;background:var(--primary);color:var(--on-primary);padding:15px 30px;border-radius:999px;font-weight:700;font-size:1rem;border:none;cursor:pointer;transition:transform .15s,box-shadow .15s;box-shadow:0 8px 20px -6px color-mix(in srgb, var(--primary) 60%, transparent)}
.btn:hover{transform:translateY(-2px)}
.btn-outline{display:inline-block;background:transparent;color:var(--primary);padding:14px 28px;border-radius:999px;font-weight:600;border:2px solid var(--primary)}
.btn-sub{display:block;font-size:.72rem;font-weight:400;opacity:.85;margin-top:2px}

/* Hero */
.hero{background:linear-gradient(180deg,var(--bg-alt),#fff);padding:60px 0 70px}
.hero-grid{display:grid;grid-template-columns:1.1fr 1fr;gap:56px;align-items:center}
.pill{display:inline-flex;align-items:center;gap:8px;background:var(--primary-light);color:var(--primary-dark);font-size:.8rem;font-weight:600;padding:8px 16px;border-radius:999px;margin-bottom:18px}
.hero h1{font-size:2.6rem;margin-bottom:18px}
.hero .lede{font-size:1.08rem;color:var(--muted);margin-bottom:24px}
.rating{display:flex;align-items:center;gap:10px;margin-bottom:20px;font-size:.9rem;color:var(--muted)}
.stars{color:#f5a623;letter-spacing:2px}
.factrow{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin:22px 0}
.factrow div{background:#fff;border:1px solid var(--border);border-radius:12px;padding:12px 8px;text-align:center}
.factrow b{display:block;font-size:1.15rem;color:var(--primary-dark);font-family:'Fraunces',serif}
.factrow span{font-size:.72rem;color:var(--muted)}
.checks{list-style:none;margin:18px 0 26px}
.checks li{position:relative;padding-left:28px;margin-bottom:10px;font-size:.94rem;color:var(--ink)}
.checks li:before{content:'✓';position:absolute;left:0;top:0;color:var(--primary);font-weight:700}
.hero-actions{display:flex;gap:14px;flex-wrap:wrap;margin-bottom:14px}
.trustline{font-size:.8rem;color:var(--muted)}
.hero-img{background:var(--primary-dark);border-radius:24px;padding:40px;text-align:center;position:relative;overflow:hidden}
.hero-img img{max-width:70%;margin:0 auto;filter:drop-shadow(0 24px 40px rgba(0,0,0,.35))}

/* Section shell */
section{padding:64px 0}
.section-alt{background:var(--bg-alt)}
.head{text-align:center;max-width:640px;margin:0 auto 40px}
.eyebrow{display:inline-block;color:var(--primary);font-weight:700;font-size:.78rem;letter-spacing:.08em;text-transform:uppercase;margin-bottom:10px}
.head h2{font-size:2rem;margin-bottom:10px}
.head p{color:var(--muted);font-size:1rem}

/* Grid cards */
.grid{display:grid;gap:20px}
.g2{grid-template-columns:repeat(2,1fr)}
.g3{grid-template-columns:repeat(3,1fr)}
.g4{grid-template-columns:repeat(4,1fr)}
.card{background:#fff;border:1px solid var(--border);border-radius:var(--radius);padding:26px}
.card h4{font-size:1.05rem;margin-bottom:8px}
.card p{color:var(--muted);font-size:.92rem}
.badge-card{text-align:center}
.badge-card img{width:56px;height:56px;object-fit:contain;margin:0 auto 12px}

/* What-is split */
.split{display:grid;grid-template-columns:1fr 1.1fr;gap:52px;align-items:center}
.split img{border-radius:20px}
.callout{background:var(--primary-light);border-left:4px solid var(--primary);border-radius:10px;padding:16px 20px;margin:18px 0;font-size:.92rem}
.factchip{display:inline-flex;gap:8px;flex-wrap:wrap;margin-top:16px}
.factchip span{background:var(--bg-alt);border:1px solid var(--border);border-radius:999px;padding:6px 14px;font-size:.8rem;color:var(--muted)}

/* Ingredients numbered */
.ing-card{display:flex;gap:16px;background:#fff;border:1px solid var(--border);border-radius:var(--radius);padding:22px}
.ing-num{flex:none;width:38px;height:38px;border-radius:50%;background:var(--primary);color:var(--on-primary);display:flex;align-items:center;justify-content:center;font-weight:700;font-family:'Fraunces',serif}

/* How it works dark */
.dark{background:var(--primary-dark);color:#fff}
.dark .head h2,.dark h3{color:#fff}
.dark .head p{color:rgba(255,255,255,.7)}
.step-card{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);border-radius:var(--radius);padding:22px}
.step-card h4{color:#fff}
.step-card p{color:rgba(255,255,255,.72)}
.step-num{width:30px;height:30px;border-radius:8px;background:var(--primary);color:var(--on-primary);display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.85rem;margin-bottom:10px}

/* Reviews */
.rev-card{background:#fff;border:1px solid var(--border);border-radius:var(--radius);padding:24px}
.rev-head{display:flex;align-items:center;gap:12px;margin-bottom:10px}
.rev-head img{width:46px;height:46px;border-radius:50%;object-fit:cover}
.rev-name{font-weight:700;font-size:.94rem;color:var(--ink)}
.rev-card p{color:var(--ink)!important}
.rev-sub{font-size:.78rem;color:var(--muted)}
.rev-stars{color:#f5a623;margin-bottom:8px;font-size:.9rem}
.rev-board{display:flex;justify-content:center;gap:56px;margin-top:36px;text-align:center;flex-wrap:wrap}
.rev-board b{display:block;font-size:1.7rem;font-family:'Fraunces',serif;color:var(--primary-dark)}
.rev-board span{font-size:.8rem;color:var(--muted)}

/* Pricing */
.plans{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;align-items:start}
.plan{background:#fff;border:2px solid var(--border);border-radius:18px;padding:28px 22px;text-align:center;position:relative}
.plan.top{border-color:var(--primary);box-shadow:0 20px 40px -16px color-mix(in srgb, var(--primary) 40%, transparent)}
.plan-badge{position:absolute;top:-13px;left:50%;transform:translateX(-50%);background:var(--primary);color:var(--on-primary);font-size:.7rem;font-weight:700;padding:5px 16px;border-radius:999px;white-space:nowrap}
.plan img{max-width:120px;margin:10px auto 16px}
.plan-ttl{font-family:'Fraunces',serif;font-weight:600;font-size:1.1rem;margin-bottom:2px}
.plan-sub{font-size:.78rem;color:var(--muted);margin-bottom:14px}
.plan-price{font-size:2rem;font-family:'Fraunces',serif;color:var(--primary-dark)}
.plan-price small{font-size:.9rem;font-weight:400;color:var(--muted)}
.plan-tot{font-size:.85rem;color:var(--muted);margin:4px 0 2px}
.plan-ship{font-size:.8rem;color:var(--primary);font-weight:600;margin-bottom:16px}
.plan ul{list-style:none;text-align:left;margin-bottom:18px}
.plan ul li{font-size:.85rem;padding:5px 0 5px 22px;position:relative;color:var(--ink)}
.plan ul li:before{content:'✓';position:absolute;left:0;color:var(--primary);font-weight:700}
.plan .btn{width:100%;padding:13px}
.flag{background:var(--bg-alt);border:1px solid var(--border);border-radius:12px;padding:16px 20px;margin-top:26px;font-size:.88rem;text-align:center;max-width:760px;margin-left:auto;margin-right:auto}

/* Guarantee */
.guar{display:flex;align-items:center;gap:40px;background:var(--bg-alt);border-radius:24px;padding:40px}
.guar img{width:140px;flex:none}
.guar h3{font-size:1.5rem;margin-bottom:10px}
.guar p{color:var(--muted);margin-bottom:8px}

/* FAQ */
.faq{max-width:760px;margin:0 auto}
.faq-row{border-bottom:1px solid var(--border)}
.faq-btn{width:100%;text-align:left;background:none;border:none;padding:18px 4px;font-size:1rem;font-weight:600;cursor:pointer;color:var(--ink);display:flex;justify-content:space-between;align-items:center;font-family:'Inter',sans-serif}
.faq-btn:after{content:'+';font-size:1.4rem;color:var(--primary);font-weight:400}
.faq-body{padding:0 4px 18px;color:var(--muted);font-size:.93rem;display:none}
.faq-row.open .faq-body{display:block}
.faq-row.open .faq-btn:after{content:'−'}

/* Footer */
footer{background:var(--primary-dark);color:rgba(255,255,255,.82);padding:56px 0 30px;font-size:.86rem}
.foot-nav{display:flex;flex-wrap:wrap;gap:22px;list-style:none;margin-bottom:18px}
.foot-nav a{color:rgba(255,255,255,.85)}
.foot-nav a:hover{color:#fff}
.foot-legal{display:flex;flex-wrap:wrap;gap:18px;list-style:none;margin-bottom:24px;font-size:.8rem}
.foot-legal a{color:rgba(255,255,255,.6)}
footer hr{border:none;border-top:1px solid rgba(255,255,255,.15);margin:22px 0}
footer p{margin-bottom:12px;color:rgba(255,255,255,.6);font-size:.78rem;line-height:1.7}
.cr{margin-top:18px;font-size:.78rem;color:rgba(255,255,255,.5)}

/* Sticky bar */
.sticky-bar{position:fixed;bottom:0;left:0;right:0;background:#fff;border-top:1px solid var(--border);padding:12px 20px;display:flex;align-items:center;justify-content:space-between;gap:16px;box-shadow:0 -8px 24px rgba(0,0,0,.08);z-index:60}
.sticky-bar b{font-family:'Fraunces',serif}
.sticky-bar small{display:block;color:var(--muted);font-size:.75rem}

/* Final CTA */
.final{background:var(--primary-dark);color:#fff;border-radius:28px;padding:56px 40px;text-align:center}
.final h2{color:#fff;margin-bottom:12px}
.final p{color:rgba(255,255,255,.75);margin-bottom:24px}
.final img{max-width:160px;margin:0 auto 24px}
.final .old{text-decoration:line-through;opacity:.6;font-size:.95rem}
.final .new{font-size:1.7rem;font-family:'Fraunces',serif;margin-bottom:20px}

@media(max-width:860px){
 .hero-grid,.split{grid-template-columns:1fr}
 .g4{grid-template-columns:repeat(2,1fr)}
 .g3,.g2{grid-template-columns:1fr}
 .plans{grid-template-columns:1fr}
 .factrow{grid-template-columns:repeat(2,1fr)}
 .navlinks{display:none}
 .guar{flex-direction:column;text-align:center}
 .rev-board{gap:28px}
 body{padding-bottom:74px}
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

<section><div class="wrap">
<div class="head"><span class="eyebrow">Why Choose __BRAND__</span><h2>Built On Quality You Can Verify</h2></div>
<div class="grid g4">
<div class="card badge-card"><img src="assets/images/badge-usa.png" alt="Made in USA"><h4>Made In The USA</h4><p>Manufactured under strict quality control procedures.</p></div>
<div class="card badge-card"><img src="assets/images/badge-fda.png" alt="FDA registered"><h4>Registered Facility</h4><p>Produced in an FDA-registered facility.</p></div>
<div class="card badge-card"><img src="assets/images/badge-gmp.png" alt="GMP certified"><h4>GMP Certified</h4><p>Made under Good Manufacturing Practice guidelines.</p></div>
<div class="card badge-card"><img src="assets/images/badge-natural.png" alt="Natural"><h4>Naturally Sourced</h4><p>Thoughtfully selected natural ingredients.</p></div>
</div>
</div></section>

<section class="section-alt" id="what-is"><div class="wrap split">
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
<div style="text-align:center;margin-top:30px"><a class="btn-outline" href="blog/index.html">Visit The __BRAND__ Blog</a></div>
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
