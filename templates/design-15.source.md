<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>__TITLE__</title>
<meta name="description" content="__META_DESC__">
<link rel="canonical" href="__CANONICAL__">
<meta name="theme-color" content="__COLOR_PRIMARY__">
<link rel="preconnect" href="https://cdn.jsdelivr.net">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css">
<link rel="preload" as="style" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css" onload="this.onload=null;this.rel='stylesheet'">
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" onload="this.onload=null;this.rel='stylesheet'">
<noscript>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap">
</noscript>
<style>
:root{
 --primary:__COLOR_PRIMARY__;
 --primary-dark:__COLOR_DARK__;
 --primary-light:__COLOR_LIGHT__;
 --accent:__COLOR_ACCENT__;
 --on-primary:__COLOR_ON_PRIMARY__;
 --gold:#F5C242;
 --gold-soft:#FFF197;
 --soft:#F8FAFC;
 --text:#1E293B;
 --muted:#64748B;
 --border:#E2E8F0;
}
*{box-sizing:border-box}
body{font-family:'Inter',system-ui,-apple-system,sans-serif;color:var(--text);background:#fff;line-height:1.6;overflow-x:hidden}
h1,h2,h3,h4{font-weight:800;line-height:1.2;color:var(--text)}
a{text-decoration:none}
img{max-width:100%}
.sec{padding:80px 0}
.sec.soft{background:var(--soft)}
.sec.teal{background:var(--primary);color:var(--on-primary)}
.sec.teal h2,.sec.teal h3,.sec.teal h4{color:var(--on-primary)}
@media(max-width:767px){.sec{padding:52px 0}}

.topbar{background:#0a0f12;color:#fff;font-size:.86rem;font-weight:600;letter-spacing:.4px;padding:8px 0;text-align:center}
.topbar i{color:var(--gold);margin-right:6px}

header.site{background:var(--primary);position:sticky;top:0;z-index:1030;box-shadow:0 4px 15px rgba(0,0,0,.15)}
.logo{font-size:1.9rem;font-weight:900;color:var(--on-primary)!important;letter-spacing:-.5px;display:flex;align-items:center}
.nav-link-c{color:var(--on-primary)!important;font-weight:600;padding:8px 16px!important;display:inline-flex;align-items:center;gap:8px}
.nav-link-c:hover{color:var(--gold-soft)!important}
.btn-cta{background:var(--gold-soft);color:#0f172a!important;font-weight:800;border-radius:8px;padding:10px 24px;border:none;display:inline-flex;align-items:center;gap:6px;box-shadow:0 4px 12px rgba(0,0,0,.18);transition:all .2s}
.btn-cta:hover{background:var(--gold);transform:scale(1.03)}
.btn-big{display:inline-block;background:var(--gold-soft);color:#0f172a;font-weight:800;font-size:1.2rem;padding:16px 34px;border-radius:50px;border:2px solid #fff;box-shadow:0 8px 25px rgba(0,0,0,.2);transition:all .25s}
.btn-big:hover{background:#fff;color:var(--primary-dark);transform:translateY(-3px)}

.hero{background:linear-gradient(135deg,var(--primary),var(--primary-dark));color:var(--on-primary);padding:60px 0 80px}
.hero-badge{display:inline-block;background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.25);border-radius:12px;padding:12px 18px;font-weight:700;margin-bottom:22px;backdrop-filter:blur(8px)}
.hero-badge i{color:var(--gold);margin-right:8px}
.hero h1{font-size:2.7rem;color:var(--on-primary);margin-bottom:18px}
.hero-sub{font-size:1.15rem;color:var(--on-primary);opacity:.94;margin-bottom:24px}
.hero-checks{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:26px}
.hero-checks div{display:flex;align-items:flex-start;gap:9px;font-weight:600;color:var(--on-primary)}
.hero-checks i{color:var(--gold);margin-top:3px}
.hero-note{font-size:.85rem;opacity:.75;margin:16px 0 0}
@media(max-width:991px){.hero h1{font-size:2.1rem}.btn-big{width:100%;text-align:center}.hero-checks{grid-template-columns:1fr}}

.trust{background:var(--soft);border-bottom:1px solid var(--border);padding:44px 0}
.trust-card{background:#fff;border:1px solid var(--border);border-radius:16px;padding:22px;text-align:center;height:100%;box-shadow:0 10px 25px rgba(0,0,0,.04);transition:all .25s}
.trust-card:hover{transform:translateY(-5px);border-color:var(--primary)}
.trust-card img{max-height:78px;object-fit:contain;margin-bottom:12px}
.trust-card h3{font-size:1rem;margin-bottom:2px}
.trust-card p{font-size:.82rem;color:var(--muted);margin:0}

.head{text-align:center;max-width:780px;margin:0 auto 46px}
.head h2{font-size:2.2rem;color:var(--primary);margin-bottom:12px}
.head p{font-size:1.1rem;color:var(--muted);margin:0}
.sec.teal .head h2{color:var(--on-primary)}
.sec.teal .head p{color:var(--on-primary);opacity:.88}
.pill{display:inline-block;background:var(--primary);color:var(--on-primary);font-weight:700;font-size:.8rem;border-radius:999px;padding:7px 16px;margin-bottom:14px}
.lead-p{font-size:1.12rem;font-weight:500;color:var(--text)}
.note{background:var(--soft);border-left:4px solid var(--primary);border-radius:8px;padding:16px 20px;font-size:.92rem;color:var(--muted)}

/* Generic grids that wrap the generator's card markup */
.grid{display:grid;gap:22px}
.g2{grid-template-columns:repeat(2,1fr)}
.g3{grid-template-columns:repeat(3,1fr)}
.g4{grid-template-columns:repeat(4,1fr)}
@media(max-width:991px){.g3,.g4{grid-template-columns:repeat(2,1fr)}}
@media(max-width:640px){.g2,.g3,.g4{grid-template-columns:1fr}}

.pcard,.card{background:#fff;border:1px solid var(--border);border-radius:14px;padding:24px;height:100%;box-shadow:0 4px 15px rgba(0,0,0,.03);transition:all .25s}
.pcard:hover,.card:hover{transform:translateY(-4px);border-color:var(--primary);box-shadow:0 10px 25px rgba(0,0,0,.08)}
.pcard .num{width:46px;height:46px;border-radius:50%;background:var(--primary-light);color:var(--primary-dark);display:flex;align-items:center;justify-content:center;font-weight:900;margin-bottom:14px}
.pcard h4,.card h4{font-size:1.05rem;margin-bottom:8px}
.pcard p,.card p{color:var(--muted);font-size:.92rem;margin:0}
.card{border-top:4px solid var(--primary)}

.ing-card{position:relative;overflow:hidden;display:flex;gap:14px;background:#fff;border:1px solid #eef2f6;border-radius:16px;padding:22px 22px 22px 26px;box-shadow:0 6px 18px rgba(0,0,0,.04);transition:all .25s}
.ing-card:before{content:'';position:absolute;left:0;top:0;width:5px;height:100%;background:var(--primary)}
.ing-card:hover{transform:translateY(-5px);box-shadow:0 12px 30px rgba(0,0,0,.08)}
.ing-num{flex:none;width:34px;height:34px;border-radius:50%;background:var(--primary-light);color:var(--primary-dark);font-weight:800;font-size:.85rem;display:flex;align-items:center;justify-content:center}
.ing-card h4{font-size:1.02rem;margin-bottom:6px}
.ing-card p{color:var(--muted);font-size:.88rem;margin:0}

.steps{display:grid;grid-template-columns:repeat(2,1fr);gap:22px}
@media(max-width:767px){.steps{grid-template-columns:1fr}}
.step-card{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:14px;padding:24px;color:var(--on-primary)}
.step-card .step-num{width:42px;height:42px;border-radius:50%;background:var(--gold-soft);color:#0f172a;font-weight:900;display:flex;align-items:center;justify-content:center;margin-bottom:14px}
.step-card h4{color:var(--on-primary);font-size:1.08rem;margin-bottom:8px}
.step-card p{color:var(--on-primary);opacity:.88;font-size:.92rem;margin:0}

.plans{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;align-items:stretch}
@media(max-width:991px){.plans{grid-template-columns:1fr;max-width:420px;margin:0 auto}}
.plan{position:relative;display:flex;flex-direction:column;text-align:center;background:#fff;border:2px solid var(--border);border-radius:20px;padding:34px 22px 26px;box-shadow:0 10px 30px rgba(0,0,0,.05)}
.plan.top{border-color:var(--primary);box-shadow:0 15px 40px rgba(0,0,0,.14);transform:scale(1.03)}
@media(max-width:991px){.plan.top{transform:none}}
.plan-badge{position:absolute;top:-15px;left:50%;transform:translateX(-50%);background:var(--primary);color:var(--on-primary);font-size:.78rem;font-weight:800;letter-spacing:1px;text-transform:uppercase;padding:6px 20px;border-radius:20px;white-space:nowrap}
.plan img{max-height:170px;object-fit:contain;margin:6px auto 10px}
.plan-ttl{font-size:1.3rem;font-weight:800}
.plan-sub{color:var(--muted);font-size:.85rem;font-weight:600;margin-bottom:8px}
.plan-price{font-size:2.9rem;font-weight:900;color:var(--primary);line-height:1.05}
.plan-price small{font-size:.95rem;color:var(--muted);font-weight:600}
.plan-tot{font-weight:800;margin-top:6px}
.plan-ship{font-weight:700;color:var(--primary-dark);font-size:.88rem;margin-bottom:8px}
.plan ul{list-style:none;padding:0;margin:10px 0 6px;text-align:left}
.plan li{font-size:.86rem;color:var(--muted);padding:3px 0 3px 22px;position:relative}
.plan li:before{content:'\2713';position:absolute;left:0;color:var(--primary);font-weight:900}
.plan .btn{display:block;margin-top:auto;background:var(--gold-soft);color:#0f172a;font-weight:800;font-size:1.1rem;padding:14px 18px;border-radius:12px;border:1px solid rgba(0,0,0,.1);box-shadow:0 4px 15px rgba(0,0,0,.12)}
.plan .btn:hover{background:var(--gold)}
.plan.top .btn{background:var(--gold)}

.bonus-block{max-width:900px;margin:0 auto}

.science-col{background:#fff;border:1px solid var(--border);border-radius:18px;padding:30px;box-shadow:0 8px 24px rgba(0,0,0,.05);height:100%}
.science-col h3{font-size:1.1rem;margin-bottom:14px;color:var(--text)}
.science-col ul{list-style:none;padding:0;margin:0}
.science-col li{display:flex;gap:10px;padding:9px 0;border-bottom:1px solid var(--border);font-size:.92rem;color:var(--muted)}
.science-col li:last-child{border-bottom:none}
.science-col li i{color:var(--primary);margin-top:3px}
.science-col .serving-line{font-size:.88rem;color:var(--muted);margin:14px 0 0}

.rev-card{background:#fff;border:1px solid var(--border);border-radius:16px;padding:28px;box-shadow:0 6px 20px rgba(0,0,0,.04);height:100%}
.rev-head{display:flex;align-items:center;gap:14px;margin-bottom:12px}
.rev-head img{width:68px;height:68px;border-radius:50%;object-fit:cover;border:3px solid var(--primary)}
.rev-name{font-weight:800}
.rev-sub{font-size:.78rem;color:var(--muted)}
.rev-stars{color:var(--gold);letter-spacing:2px;margin-bottom:10px}
.rev-card p{color:var(--muted);font-size:.93rem;margin:0}

.guarantee{background:linear-gradient(135deg,var(--primary),var(--primary-dark));border-radius:24px;padding:48px 40px;color:var(--on-primary);box-shadow:0 15px 35px rgba(0,0,0,.2)}
.guarantee h2{color:var(--on-primary);margin-bottom:14px}
.guarantee p{color:var(--on-primary);opacity:.92}
.guarantee img{max-height:220px}
@media(max-width:767px){.guarantee{padding:34px 22px}}

.faq{max-width:860px;margin:0 auto}
.faq-row{border:1px solid var(--border);border-radius:12px;margin-bottom:14px;background:#fff;overflow:hidden;box-shadow:0 2px 8px rgba(0,0,0,.02)}
.faq-btn{width:100%;text-align:left;background:#fff;border:none;padding:19px 24px;font-size:1.04rem;font-weight:700;color:var(--primary);cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:16px;font-family:inherit}
.faq-btn:after{content:'+';font-size:1.5rem;font-weight:400;flex:none}
.faq-row.open .faq-btn{background:var(--primary-light);color:var(--primary-dark)}
.faq-row.open .faq-btn:after{content:'\2212'}
.faq-body{max-height:0;overflow:hidden;transition:max-height .25s ease}
.faq-body p{padding:16px 24px 20px;color:var(--muted);margin:0}

.final{background:linear-gradient(135deg,var(--primary),var(--primary-dark));text-align:center;color:var(--on-primary);padding:70px 0}
.final h2{color:var(--on-primary);font-size:2.2rem;margin-bottom:12px}
.final p{color:var(--on-primary);opacity:.9;max-width:560px;margin:0 auto 22px}
.final img{max-width:170px;margin:0 auto 18px;border-radius:10px}

footer.site{background:#111827;color:#e2e8f0;border-top:4px solid var(--primary);padding:56px 0 28px;font-size:.92rem}
footer .foot-logo{font-size:1.5rem;font-weight:900;color:#fff;display:block;margin-bottom:10px}
footer h5{color:#fff;font-size:1.02rem;font-weight:700;margin-bottom:16px}
footer ul{list-style:none;padding:0;margin:0}
footer li{margin-bottom:8px}
footer a{color:#cbd5e1}
footer a:hover{color:var(--gold-soft)}
footer p{color:#94a3b8;font-size:.82rem;line-height:1.6}
footer hr{border-color:#334155;margin:24px 0}

.sticky-bar{position:fixed;left:0;right:0;bottom:0;background:#0f172a;border-top:1px solid #334155;padding:12px 16px;display:none;align-items:center;justify-content:space-between;gap:14px;z-index:70}
.sticky-bar b{color:#fff;font-size:.95rem;font-weight:800}
.sticky-bar small{color:#94a3b8;font-size:.7rem;display:block}
@media(max-width:767px){.sticky-bar{display:flex}body{padding-bottom:78px}}
</style>
</head>
<body>

<div class="topbar"><div class="container"><i class="bi bi-truck"></i> Official pricing: larger bundles ship free and cost less per bottle &mdash; __CATEGORY__ support backed by a 60-day guarantee</div></div>

<header class="site">
<div class="container">
<nav class="navbar navbar-dark navbar-expand-lg py-2">
<a class="logo navbar-brand" href="index.html">__BRAND__</a>
<button class="navbar-toggler border-0" type="button" data-bs-toggle="collapse" data-bs-target="#mainNav" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
<div class="collapse navbar-collapse" id="mainNav">
<ul class="navbar-nav mx-auto mb-2 mb-lg-0">
<li class="nav-item"><a class="nav-link nav-link-c" href="what-is-product.html"><i class="bi bi-info-circle"></i> About</a></li>
<li class="nav-item"><a class="nav-link nav-link-c" href="ingredients.html"><i class="bi bi-flower1"></i> Ingredients</a></li>
<li class="nav-item"><a class="nav-link nav-link-c" href="benefits.html"><i class="bi bi-heart-pulse"></i> Benefits</a></li>
<li class="nav-item"><a class="nav-link nav-link-c" href="reviews.html"><i class="bi bi-star"></i> Reviews</a></li>
<li class="nav-item"><a class="nav-link nav-link-c" href="blog/index.html"><i class="bi bi-journal-text"></i> Blog</a></li>
<li class="nav-item"><a class="nav-link nav-link-c" href="index.html#faq"><i class="bi bi-question-circle"></i> FAQs</a></li>
</ul>
<a class="btn-cta" href="__AFFILIATE__">__CTA_HEADER__ <i class="bi bi-arrow-right"></i></a>
</div>
</nav>
</div>
</header>

<header class="hero">
<div class="container">
<div class="row align-items-center gy-5">
<div class="col-lg-7">
<div class="hero-badge"><i class="bi bi-shield-check"></i> __PILL_TEXT__</div>
<h1>__HERO_H1__</h1>
<p class="hero-sub">__HERO_DESC__</p>
<div class="hero-checks">
<div><i class="bi bi-check-circle-fill"></i><span>__CHECK1__</span></div>
<div><i class="bi bi-check-circle-fill"></i><span>__CHECK2__</span></div>
<div><i class="bi bi-check-circle-fill"></i><span>__CHECK3__</span></div>
<div><i class="bi bi-check-circle-fill"></i><span>__CHECK4__</span></div>
</div>
<a class="btn-big" href="__AFFILIATE__">__CTA_HERO__ <i class="bi bi-cart3 ms-2"></i></a>
<p class="hero-note"><i class="bi bi-lock me-1"></i> Secure checkout on the official store &middot; 60-day money-back guarantee</p>
</div>
<div class="col-lg-5 text-center">
<img src="assets/images/hero.png" alt="__BRAND__ product" id="hero-img" width="600" height="600" style="max-height:440px;width:auto;border-radius:16px">
</div>
</div>
</div>
</header>

<section class="trust"><div class="container">
<div class="row g-4">
<div class="col-6 col-md-3"><div class="trust-card"><img src="assets/images/badge-usa.png" alt="Made in the USA" width="78" height="78" loading="lazy"><h3>Made In USA</h3><p>Formulated under strict standards</p></div></div>
<div class="col-6 col-md-3"><div class="trust-card"><img src="assets/images/badge-natural.png" alt="Natural ingredients" width="78" height="78" loading="lazy"><h3>Natural Ingredients</h3><p>Every ingredient named</p></div></div>
<div class="col-6 col-md-3"><div class="trust-card"><img src="assets/images/badge-gmp.png" alt="GMP certified" width="78" height="78" loading="lazy"><h3>GMP Certified</h3><p>Good Manufacturing Practice</p></div></div>
<div class="col-6 col-md-3"><div class="trust-card"><img src="assets/images/badge-fda.png" alt="FDA-registered facility" width="78" height="78" loading="lazy"><h3>FDA-Registered Facility</h3><p>Manufactured in a registered facility</p></div></div>
</div>
</div></section>

<section class="sec" id="symptoms-section"><div class="container">
<div class="head"><h2>What __BRAND__ Was Formulated To Address</h2><p>Specific, everyday concerns worth naming directly.</p></div>
<div class="grid g3">
__SYMPTOM_CARD_TEMPLATE__
</div>
</div></section>

<section class="sec soft" id="what-is"><div class="container">
<div class="row align-items-center gy-5">
<div class="col-lg-6 text-center"><img src="assets/images/hero.png" alt="__BRAND__ overview" id="whatis-img" width="600" height="600" loading="lazy" style="max-height:420px;width:auto;border-radius:16px;box-shadow:0 15px 35px rgba(0,0,0,.12)"></div>
<div class="col-lg-6">
<span class="pill">Comprehensive Overview</span>
<h2 style="color:var(--primary);margin-bottom:18px">What Is __BRAND__?</h2>
<p class="lead-p">__WHATIS_P1__</p>
<div class="note mt-3">__WHATIS_CALLOUT__</div>
<p class="mt-4"><a class="btn-cta" href="what-is-product.html">Read The Full __BRAND__ Explainer <i class="bi bi-chevron-right"></i></a></p>
</div>
</div>
</div></section>

<section class="sec teal" id="how-it-works"><div class="container">
<div class="head"><h2>How Does __BRAND__ Work?</h2><p>__HIW_INTRO__</p></div>
<div class="steps">
__HIW_CARD_TEMPLATE__
</div>
</div></section>

<section class="sec" id="benefits"><div class="container">
<div class="head"><h2>Key Benefits Of __BRAND__</h2><p>Every benefit below is supportive, not a promised medical outcome.</p></div>
<div class="grid g4">
__BENEFIT_CARD_TEMPLATE__
</div>
</div></section>

<section class="sec soft" id="ingredients"><div class="container">
<div class="head"><h2>__ING_HEADING__</h2><p>Each ingredient is listed individually so you can see exactly what is inside.</p></div>
<div class="grid g3" id="ing-grid">
__ING_CARD_TEMPLATE__
</div>
</div></section>

<section class="sec" id="pricing"><div class="container">
<div class="head"><span class="pill">Official Pricing</span><h2>Choose Your __BRAND__ Package</h2><p>One-time payment &middot; No subscription &middot; No hidden charges</p></div>
<div class="plans">
__PLAN_CARD_TEMPLATE__
</div>
<p class="text-center mt-4" style="font-size:.9rem;color:var(--muted)"><strong>Note:</strong> __PRICING_NOTE__</p>
</div></section>

<div class="bonus-block">__BONUS_SECTION__</div>

<section class="sec soft"><div class="container">
<div class="head"><h2>At A Glance</h2><p>The key facts about __BRAND__, straight from the label.</p></div>
<div class="row g-4 justify-content-center">
<div class="col-lg-6"><div class="science-col"><h3><i class="bi bi-clipboard-check me-2" style="color:var(--primary)"></i>Key Facts</h3>
<ul>
<li><i class="bi bi-check-circle-fill"></i><span><strong>__FACT1_NUM__</strong> __FACT1_LABEL__ named on the label</span></li>
<li><i class="bi bi-check-circle-fill"></i><span><strong>__FACT2_NUM__</strong> __FACT2_LABEL__ per day (__SERVING_DAILY__)</span></li>
<li><i class="bi bi-check-circle-fill"></i><span><strong>__FACT3_NUM__</strong> __FACT3_LABEL__</span></li>
<li><i class="bi bi-check-circle-fill"></i><span>Made in the <strong>__FACT4_NUM__</strong></span></li>
</ul>
<p class="serving-line">Each bottle contains __SERVING_PER_BOTTLE__.</p></div></div>
<div class="col-lg-6"><div class="science-col"><h3><i class="bi bi-hand-thumbs-up me-2" style="color:var(--primary)"></i>What It Is Formulated To Support</h3>
<ul id="bal-pros">
__BAL_PROS_TEMPLATE__
</ul></div></div>
</div>
</div></section>

<section class="sec" id="reviews"><div class="container">
<div class="head"><h2>Customer Reviews For __BRAND__</h2><p>Individual experiences shared with the brand. Results vary, and nothing here is a guarantee of outcome.</p></div>
<div class="grid g3">
__REVIEW_CARD_TEMPLATE__
</div>
</div></section>

<section class="sec soft"><div class="container">
<div class="guarantee"><div class="row align-items-center gy-4">
<div class="col-lg-4 text-center"><img src="assets/images/guarantee.png" alt="60-day money-back guarantee" width="220" height="220" loading="lazy"></div>
<div class="col-lg-8">
<h2>The 60-Day Money-Back Guarantee</h2>
<p>__GUARANTEE_TEXT__</p>
<a class="btn-big mt-2" href="__AFFILIATE__" style="font-size:1.05rem">Order Risk-Free <i class="bi bi-shield-check ms-2"></i></a>
</div>
</div></div>
</div></section>

<section class="sec" id="faq"><div class="container">
<div class="head"><h2>Frequently Asked Questions About __BRAND__</h2><p>Quick answers on serving, safety, shipping and the guarantee.</p></div>
<div class="faq">
__FAQ_ROW_TEMPLATE__
</div>
</div></section>

<section class="final"><div class="container">
<h2>Ready To Try __BRAND__?</h2>
<p>__FINAL_TEXT__</p>
<img src="assets/images/bottle-6.png" alt="__BRAND__ six bottle pack" width="170" height="170" loading="lazy">
<div style="text-decoration:line-through;opacity:.7">Regular: __PRICE_HIGH__ / bottle</div>
<div style="font-size:1.8rem;font-weight:900;margin-bottom:18px">Today From __PRICE_LOW__ / bottle</div>
<a class="btn-big" href="__AFFILIATE__">__CTA_CLOSING__ <i class="bi bi-cart3 ms-2"></i></a>
</div></section>

<footer class="site"><div class="container">
<div class="row g-4">
<div class="col-lg-4">
<span class="foot-logo">__BRAND__</span>
<p>__BRAND__ is a dietary supplement formulated with named ingredients to support everyday wellness. Always read the label and follow the directions.</p>
</div>
<div class="col-6 col-lg-4"><h5>Explore</h5><ul>
<li><a href="what-is-product.html">What Is __BRAND__</a></li>
<li><a href="how-it-works.html">How It Works</a></li>
<li><a href="ingredients.html">Ingredients</a></li>
<li><a href="benefits.html">Benefits</a></li>
<li><a href="reviews.html">Reviews</a></li>
<li><a href="faq.html">FAQ</a></li>
</ul></div>
<div class="col-6 col-lg-4"><h5>Legal</h5><ul>
<li><a href="terms.html">Terms of Use</a></li>
<li><a href="privacy-policy.html">Privacy Policy</a></li>
<li><a href="disclaimer.html">Disclaimer</a></li>
<li><a href="refund-policy.html">Refund Policy</a></li>
<li><a href="contact.html">Contact Us</a></li>
</ul></div>
</div>
<hr>
<p><b>FDA Disclaimer:</b> These statements have not been evaluated by the U.S. Food &amp; Drug Administration. __BRAND__ is a dietary supplement, not a drug, and is not intended to diagnose, treat, cure or prevent any disease. Consult a healthcare professional before use, especially if you are pregnant, nursing, taking medication or managing a medical condition.</p>
<p><b>Affiliate Disclosure:</b> This website may earn a commission on purchases made through links to the official __BRAND__ store, at no additional cost to you.</p>
<p style="text-align:center;margin-top:18px">&copy; __YEAR__ __BRAND__ &mdash; All Rights Reserved</p>
</div></footer>

<div class="sticky-bar"><div><b>__PRICE_LOW__ / bottle</b><small>Best value pack</small></div><a class="btn-cta" href="__AFFILIATE__">__CTA_STICKY__</a></div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
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
