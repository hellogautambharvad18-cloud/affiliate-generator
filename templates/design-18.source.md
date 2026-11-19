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
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@700;800;900&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
:root{--primary:__COLOR_PRIMARY__;--primary-dark:__COLOR_DARK__;--primary-light:__COLOR_LIGHT__;--accent:__COLOR_ACCENT__;--on-primary:__COLOR_ON_PRIMARY__;--cta:#ff6a00;--cta-dark:#e55e00;--ink:#0f172a;--muted:#475569;--border:#0f172a;--soft:#f8fafc;--gold:#ffc107;--green:#16a34a}
*{box-sizing:border-box}
html{font-size:20px;scroll-behavior:smooth}
body{margin:0;font-family:'Inter',system-ui,-apple-system,Segoe UI,Roboto,sans-serif;color:var(--ink);background:#fff;line-height:1.6}
h1,h2,h3,h4,.logo,.plan-price,.plan-ttl{font-family:'Archivo',sans-serif;line-height:1.05;letter-spacing:-.02em}
a{color:var(--primary)}
img{max-width:100%;height:auto}
.wrap{max-width:1120px;margin:0 auto;padding:0 24px}
.container{max-width:1120px;margin:0 auto;padding:0 24px}
/* Top urgency bar */
.topbar{background:var(--ink);color:#fff;text-align:center;padding:10px 16px;font-weight:800;font-size:.9rem;letter-spacing:.02em}
.topbar strong{color:var(--gold)}
.topbar #d18-count{color:var(--gold);font-variant-numeric:tabular-nums}
/* Nav */
nav.site{position:sticky;top:0;z-index:100;background:#fff;border-bottom:3px solid var(--ink)}
nav.site .wrap{display:flex;align-items:center;gap:20px;padding-top:12px;padding-bottom:12px}
.logo{font-size:1.35rem;font-weight:900;text-transform:uppercase;text-decoration:none;color:var(--ink)}
.logo span{color:var(--primary)}
.nav-links{display:flex;gap:18px;margin-left:auto;flex-wrap:wrap}
.nav-links a,.nav-link-c{color:var(--ink);text-decoration:none;font-weight:700;font-size:.92rem}
.nav-links a:hover{color:var(--primary);text-decoration:underline}
.btn,.btn-cta,.btn-big{display:inline-block;background:var(--cta);color:#fff!important;font-weight:900;text-decoration:none;padding:16px 28px;border-radius:12px;border:3px solid var(--ink);box-shadow:5px 5px 0 var(--ink);font-size:1.05rem;line-height:1.2;text-align:center;transition:transform .15s ease,box-shadow .15s ease}
.btn:hover,.btn-cta:hover,.btn-big:hover{transform:translate(-2px,-2px);box-shadow:8px 8px 0 var(--ink)}
.btn:active{transform:translate(2px,2px);box-shadow:2px 2px 0 var(--ink)}
.nav-cta{padding:10px 18px!important;font-size:.95rem;box-shadow:3px 3px 0 var(--ink)}
/* Hero */
header.hero{background:var(--primary-light);border-bottom:3px solid var(--ink);padding:56px 0 64px}
.hero .wrap{display:grid;grid-template-columns:1.05fr .95fr;gap:48px;align-items:center}
.pill{display:inline-block;background:#fff;border:2px solid var(--ink);border-radius:999px;padding:6px 14px;font-weight:800;font-size:.82rem;box-shadow:3px 3px 0 var(--ink)}
.hero h1{font-size:3.1rem;font-weight:900;margin:18px 0 16px;text-transform:uppercase}
.hero h1 em{font-style:normal;color:var(--primary);box-shadow:inset 0 -14px 0 var(--gold)}
.hero-sub{font-size:1.18rem;color:var(--muted);margin:0 0 22px}
.hero-checks{display:grid;gap:10px;margin:0 0 24px;font-weight:700}
.hero-checks div:before{content:"✓ ";color:var(--green);font-weight:900}
.hero-cta-row{display:flex;gap:16px;align-items:center;flex-wrap:wrap}
.hero-price{font-weight:900;font-size:1.25rem}
.hero-price small{display:block;font-size:.85rem;color:var(--muted);font-weight:700}
.hero-note{font-size:.85rem;color:var(--muted);margin-top:12px}
.hero-media{position:relative}
.hero-media img{width:100%;border:3px solid var(--ink);border-radius:20px;box-shadow:10px 10px 0 var(--ink);background:#fff}
.hero-badge{position:absolute;top:-14px;right:-10px;background:var(--gold);border:3px solid var(--ink);border-radius:999px;padding:10px 16px;font-weight:900;box-shadow:4px 4px 0 var(--ink);transform:rotate(3deg)}
.hero-facts{display:flex;gap:16px;flex-wrap:wrap;margin-top:22px}
.hero-facts div{background:#fff;border:2px solid var(--ink);border-radius:12px;padding:10px 14px;text-align:center;min-width:110px;box-shadow:3px 3px 0 var(--ink)}
.hero-facts b{display:block;font-family:'Archivo',sans-serif;font-size:1.25rem}
.hero-facts span{font-size:.78rem;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:.05em}
/* Sections */
.sec{padding:64px 0}
.sec.soft{background:var(--soft)}
.sec.teal{background:var(--primary);color:#fff}
.sec.teal h2,.sec.teal h3{color:#fff}
.sec.teal p{color:rgba(255,255,255,.92)}
.head{max-width:760px;margin:0 auto 36px;text-align:center}
.head h2{font-size:2.2rem;font-weight:900;text-transform:uppercase;margin:0 0 12px}
.head h2:after{content:"";display:block;width:72px;height:6px;background:var(--cta);margin:16px auto 0;border-radius:3px}
.head p{color:var(--muted);font-size:1.08rem;margin:0}
.eyebrow{display:inline-block;background:var(--gold);border:2px solid var(--ink);padding:4px 12px;border-radius:999px;font-weight:900;font-size:.78rem;letter-spacing:.08em;text-transform:uppercase;margin-bottom:12px}
.grid{display:grid;gap:20px}
.g1{grid-template-columns:1fr}
.g2{grid-template-columns:repeat(2,1fr)}
.g3{grid-template-columns:repeat(3,1fr)}
.g4{grid-template-columns:repeat(4,1fr)}
/* Cards - shared markup from build_native_page */
.card,.pcard,.ing-card,.rev-card,.trust-card,.science-col,.step-card{background:#fff;border:3px solid var(--ink);border-radius:16px;padding:24px;box-shadow:6px 6px 0 var(--ink)}
.card h4,.pcard h4,.ing-card h4,.step-card h4{margin:0 0 8px;font-size:1.2rem}
.card p,.pcard p,.ing-card p,.step-card p,.rev-card p{color:var(--muted);margin:0}
.pcard .num{font-family:'Archivo',sans-serif;font-size:2rem;font-weight:900;color:var(--primary)}
.ing-card{display:flex;gap:16px}
.ing-num,.ing-num-circle{flex:none;width:44px;height:44px;border-radius:50%;background:var(--primary);color:var(--on-primary);display:flex;align-items:center;justify-content:center;font-weight:900;font-family:'Archivo',sans-serif}
.step-card .step-num{width:48px;height:48px;border-radius:12px;background:var(--ink);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:1.3rem;margin-bottom:14px}
.rev-card .rev-head{display:flex;gap:12px;align-items:center;margin-bottom:10px}
.rev-card .rev-head img{width:46px;height:46px;border-radius:50%;object-fit:cover;border:2px solid var(--ink)}
.rev-name{font-weight:800}
.rev-sub{font-size:.82rem;color:var(--muted)}
.rev-stars{color:#f59e0b;font-size:1.1rem;letter-spacing:.1em;margin-bottom:8px}
/* Trust strip */
section.trust{border-bottom:3px solid var(--ink);padding:22px 0;background:#fff}
section.trust .wrap{display:flex;gap:28px;justify-content:center;flex-wrap:wrap;font-weight:800;text-align:center}
section.trust span:before{content:"★ ";color:#f59e0b}
/* What-is / chips */
.chips{display:flex;gap:10px;flex-wrap:wrap;margin:20px 0}
.chips span{background:var(--primary-light);border:2px solid var(--ink);border-radius:999px;padding:6px 14px;font-weight:800;font-size:.85rem}
.callout,.note{background:#fffbeb;border:3px solid var(--ink);border-left:10px solid var(--gold);border-radius:12px;padding:18px 20px;font-weight:600;box-shadow:5px 5px 0 var(--ink)}
/* Pricing */
.plans{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;align-items:stretch}
.plan{position:relative;background:#fff;border:3px solid var(--ink);border-radius:18px;padding:28px 22px;text-align:center;box-shadow:6px 6px 0 var(--ink);display:flex;flex-direction:column}
.plan.top{background:var(--ink);color:#fff;transform:scale(1.04);box-shadow:8px 8px 0 var(--cta)}
.plan.top .plan-ttl,.plan.top .plan-price{color:#fff}
.plan.top .plan-sub,.plan.top .plan-tot,.plan.top .plan-ship{color:rgba(255,255,255,.85)}
.plan-badge{position:absolute;top:-14px;left:50%;transform:translateX(-50%);background:var(--cta);color:#fff;border:2px solid var(--ink);border-radius:999px;padding:6px 14px;font-weight:900;font-size:.82rem;white-space:nowrap}
.plan img{max-width:220px;margin:10px auto;display:block}
.plan-ttl{font-size:1.4rem;font-weight:900;text-transform:uppercase}
.plan-sub{font-weight:700;color:var(--muted)}
.plan-price{font-size:2.4rem;font-weight:900;margin:12px 0 4px}
.plan-price small{font-size:1rem}
.plan-tot,.plan-ship{font-weight:700}
.plan ul{list-style:none;padding:0;margin:16px 0;text-align:left}
.plan ul li{padding:6px 0 6px 28px;position:relative;font-weight:600}
.plan ul li:before{content:"✓";position:absolute;left:0;color:var(--green);font-weight:900}
.plan .btn{margin-top:auto}
/* Guarantee */
.guarantee{background:#fff;border:3px solid var(--ink);border-radius:18px;padding:28px;box-shadow:6px 6px 0 var(--ink);text-align:center}
.guarantee img{max-width:180px}
/* FAQ */
.faq-row{border:3px solid var(--ink);border-radius:14px;margin-bottom:12px;background:#fff;overflow:hidden;box-shadow:4px 4px 0 var(--ink)}
.faq-btn{width:100%;text-align:left;background:#fff;border:0;padding:18px 20px;font-family:'Archivo',sans-serif;font-weight:800;font-size:1.05rem;cursor:pointer;display:flex;justify-content:space-between;gap:16px;align-items:center}
.faq-btn:after{content:"+";font-size:1.6rem;font-weight:900}
.faq-row.open .faq-btn:after{content:"–"}
.faq-body{display:none;padding:0 20px 18px;color:var(--muted)}
.faq-row.open .faq-body{display:block}
/* Final CTA */
section.final{background:var(--ink);color:#fff;text-align:center}
section.final h2{font-size:2.4rem;text-transform:uppercase}
section.final p{color:rgba(255,255,255,.85);max-width:680px;margin:0 auto 24px}
.auto-cta-trust{color:rgba(255,255,255,.8)!important}
footer{background:#fff;border-top:3px solid var(--ink);padding:36px 0;text-align:center;color:var(--muted)}
footer a{color:var(--ink);font-weight:700;text-decoration:none;margin:0 8px}
footer a:hover{text-decoration:underline}
/* Sticky CTA injected by app.py */
.auto-sticky-cta-btn{background:var(--cta)!important;border:3px solid var(--ink)!important;box-shadow:4px 4px 0 var(--ink)!important}
@media(max-width:900px){.hero .wrap{grid-template-columns:1fr}.hero h1{font-size:2.3rem}.g3,.g4,.plans{grid-template-columns:1fr}.g2{grid-template-columns:1fr}.plan.top{transform:none}.nav-links{display:none}}
</style>
</head>
<body>
<div class="topbar">🔥 <strong>LIMITED-TIME OFFER</strong> — <strong>STOCK LOW</strong> — Today only: prices from <strong>__PRICE_FROM__</strong> per bottle &nbsp;·&nbsp; Ends in <span id="d18-count">23:59:59</span></div>
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
<div class="hero-facts">
<div><b>__FACT1_NUM__</b><span>__FACT1_LABEL__</span></div>
<div><b>__FACT2_NUM__</b><span>__FACT2_LABEL__</span></div>
<div><b>__FACT3_NUM__</b><span>__FACT3_LABEL__</span></div>
<div><b>__FACT4_NUM__</b><span>__FACT4_LABEL__</span></div>
</div>
</div>
<div class="hero-media">
<div class="hero-badge">SAVE BIG TODAY</div>
<img id="hero-img" src="assets/images/hero.png" alt="__BRAND__ __CATEGORY__ supplement bottle" width="640" height="640" fetchpriority="high">
</div>
</div></header>
<section class="trust"><div class="wrap"><span>__REVIEW_COUNT__ Verified Reviews</span><span>60-Day Guarantee</span><span>Made In USA</span><span>Secure Checkout</span></div></section>
<section class="sec" id="symptoms"><div class="wrap">
<div class="head"><span class="eyebrow">Does this sound familiar?</span><h2>Stop Ignoring The Signs</h2><p>If any of these sound like your day-to-day, __BRAND__ was made for you.</p></div>
<div class="grid g3">__SYMPTOM_CARD_TEMPLATE__</div>
</div></section>
<section class="sec soft" id="what-is"><div class="wrap">
<div class="head"><span class="eyebrow">What is __BRAND__?</span><h2>The Straight Answer</h2></div>
<p style="font-size:1.15rem;max-width:820px;margin:0 auto 16px;text-align:center">__WHATIS_P1__</p>
<div class="callout" style="max-width:820px;margin:0 auto">__WHATIS_CALLOUT__</div>
<div class="chips" style="justify-content:center"><span>__CHIP1__</span><span>__CHIP2__</span><span>__CHIP3__</span><span>__CHIP4__</span></div>
<div style="text-align:center;margin-top:28px"><a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_AFTER_WHATIS__</a></div>
</div></section>
<section class="sec" id="how-it-works"><div class="wrap">
<div class="head"><span class="eyebrow">Simple by design</span><h2>How __BRAND__ Works</h2><p>__HIW_INTRO__</p></div>
<div style="text-align:center;margin-bottom:28px"><img src="assets/images/feature-shot.png" alt="How __BRAND__ works" style="max-width:680px;border:3px solid var(--ink);border-radius:16px;box-shadow:6px 6px 0 var(--ink)"></div>
<div class="grid g2">__HIW_CARD_TEMPLATE__</div>
<div style="text-align:center;margin-top:28px"><a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_AFTER_HIW__</a></div>
</div></section>
<section class="sec soft" id="benefits"><div class="wrap">
<div class="head"><span class="eyebrow">Why people choose it</span><h2>Benefits That Matter Daily</h2><p>Real, everyday support — no hype, no promises it cannot keep.</p></div>
<div class="grid g3">__BENEFIT_CARD_TEMPLATE__</div>
<ul style="max-width:720px;margin:28px auto 0;font-weight:700;line-height:2">__BAL_PROS_TEMPLATE__</ul>
<div style="text-align:center;margin-top:28px"><a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_AFTER_BENEFITS__</a></div>
</div></section>
<section class="sec" id="ingredients"><div class="wrap">
<div class="head"><span class="eyebrow">Inside every serving</span><h2>__ING_HEADING__</h2><p>Every ingredient, explained plainly. Serving: __SERVING_DAILY__ · Per bottle: __SERVING_PER_BOTTLE__.</p></div>
<div class="grid g3" id="ing-grid">__ING_CARD_TEMPLATE__</div>
<div style="text-align:center;margin-top:28px"><a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_AFTER_INGREDIENTS__</a></div>
</div></section>
<section class="sec soft" id="pricing"><div class="wrap">
<div class="head"><span class="eyebrow">Choose your package</span><h2>Pick The Best Value For You</h2><p>__PRICING_NOTE__</p></div>
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
<h2 style="font-size:2rem;text-transform:uppercase;margin:12px 0">60-Day Money-Back Guarantee</h2>
<p style="color:var(--muted);max-width:680px;margin:0 auto">__GUARANTEE_TEXT__</p>
</div></div></section>
<section class="sec" id="faq"><div class="wrap">
<div class="head"><span class="eyebrow">Got questions?</span><h2>Frequently Asked Questions</h2></div>
__FAQ_ROW_TEMPLATE__
<div style="text-align:center;margin-top:28px"><a class="btn btn-big" href="__AFFILIATE__" target="_blank" rel="nofollow sponsored noopener">__CTA_AFTERFAQ__</a></div>
</div></section>
<section class="sec final"><div class="wrap">
<h2>Ready To Start Today?</h2>
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
var el=document.getElementById('d18-count');
function tick(){if(!el)return;var n=new Date();var end=new Date(n);end.setHours(23,59,59,999);var s=Math.max(0,Math.floor((end-n)/1000));var h=Math.floor(s/3600),m=Math.floor(s%3600/60),sec=s%60;el.textContent=(h<10?'0'+h:h)+':'+(m<10?'0'+m:m)+':'+(sec<10?'0'+sec:sec);}
tick();setInterval(tick,1000);
})();
</script>
</body>
</html>
