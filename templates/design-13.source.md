<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>__TITLE__</title>
<meta name="description" content="__META_DESC__">
<link rel="canonical" href="__CANONICAL__">
<meta name="theme-color" content="__COLOR_DARK__">
<link rel="preconnect" href="https://cdn.jsdelivr.net">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css">
<link rel="preload" as="style" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css" onload="this.onload=null;this.rel='stylesheet'">
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Anton&family=Barlow:wght@400;500;600;700;800;900&display=swap" onload="this.onload=null;this.rel='stylesheet'">
<noscript>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anton&family=Barlow:wght@400;500;600;700;800;900&display=swap">
</noscript>
<style>
:root{
 --primary:__COLOR_PRIMARY__;
 --primary-dark:__COLOR_DARK__;
 --primary-light:__COLOR_LIGHT__;
 --accent:__COLOR_ACCENT__;
 --on-primary:__COLOR_ON_PRIMARY__;
 --ink:#0d0c0b;
 --ink2:#191715;
 --paper:#f7f5f1;
 --card:#ffffff;
 --text:#1c1b19;
 --muted:#6a655f;
 --border:#e6e2d9;
 --border-dark:#2a2724;
 --red:#c23b2f;
}
*{box-sizing:border-box}
body{font-family:'Barlow',system-ui,sans-serif;color:var(--text);background:var(--paper);line-height:1.65}
h1,h2,h3,h4{font-family:'Anton',Impact,sans-serif;font-weight:400;text-transform:uppercase;letter-spacing:.01em;line-height:1.08;color:var(--ink)}
a{color:inherit;text-decoration:none}
img{max-width:100%}
.sec{padding:88px 0}
.sec.paper{background:var(--paper)}
.sec.dark{background:var(--ink);color:var(--paper)}
.sec.dark h2,.sec.dark h3,.sec.dark h4{color:var(--paper)}
.sec.dark .kick{color:var(--primary)}
@media(max-width:767px){.sec{padding:56px 0}}

.brand{display:inline-flex;align-items:center;gap:9px;font-family:'Anton',sans-serif;font-size:1.3rem;color:var(--ink);text-transform:uppercase}
.bolt{width:10px;height:10px;border-radius:50%;background:var(--primary);display:inline-block}
nav.navbar{background:rgba(247,245,241,.94)!important;backdrop-filter:blur(10px);border-bottom:1px solid var(--border);padding:14px 0}
.navbar-nav .nav-link{font-weight:700;font-size:.86rem;text-transform:uppercase;letter-spacing:.02em;color:var(--ink)!important;padding:8px 14px!important}
.navbar-nav .nav-link:hover{color:var(--primary)!important}

.btn-ember{background:var(--primary);color:var(--on-primary);border:none;font-weight:800;text-transform:uppercase;letter-spacing:.02em;padding:14px 26px;border-radius:4px}
.btn-ember:hover{background:var(--primary-dark);color:var(--on-primary)}
.btn-out{display:inline-flex;align-items:center;gap:6px;border:2px solid var(--ink);color:var(--ink);font-weight:800;padding:11px 20px;border-radius:4px;text-transform:uppercase;font-size:.85rem;letter-spacing:.02em}
.btn-out:hover{background:var(--ink);color:var(--paper)}
.btn-out-l{display:inline-flex;align-items:center;gap:6px;border:2px solid rgba(247,245,241,.35);color:var(--paper);font-weight:800;padding:11px 20px;border-radius:4px;text-transform:uppercase;font-size:.85rem;letter-spacing:.02em}
.btn-out-l:hover{border-color:var(--paper)}

.hero{background:var(--ink);color:var(--paper);padding:76px 0}
.flag{display:inline-flex;align-items:center;gap:8px;background:var(--primary);color:var(--on-primary);font-weight:800;font-size:.76rem;text-transform:uppercase;letter-spacing:.03em;padding:8px 16px;border-radius:999px;margin-bottom:20px}
.hero h1{font-size:2.7rem;color:var(--paper)}
.hero h1 span{color:var(--primary)}
.hero-sub{color:rgba(247,245,241,.7);font-size:1.05rem;margin:20px 0 26px;font-weight:500}
.hero-sub strong{color:var(--paper)}
.ticks{display:flex;flex-direction:column;gap:11px;margin-bottom:28px}
.ticks div{display:flex;align-items:flex-start;gap:10px;font-weight:600;font-size:.92rem;color:rgba(247,245,241,.85)}
.ticks i{color:var(--primary);margin-top:3px}
.hero-btns{display:flex;flex-wrap:wrap;gap:14px;margin-bottom:22px}
.hero-rate{font-size:.88rem;color:rgba(247,245,241,.6);font-weight:600}
.hero-rate .stars{color:var(--primary);letter-spacing:1px}
.hero-pack{border-radius:8px}

.eeat{background:var(--ink2);border-top:1px solid var(--border-dark);border-bottom:1px solid var(--border-dark);padding:13px 0}
.eeat .in{display:flex;flex-wrap:wrap;justify-content:center;gap:10px 26px;font-size:.76rem;font-weight:600;color:rgba(247,245,241,.6)}
.eeat .in span{display:flex;align-items:center;gap:7px}
.eeat strong{color:rgba(247,245,241,.9)}

.head{max-width:680px;margin:0 auto 46px;text-align:center}
.kick{display:inline-block;font-size:.78rem;font-weight:800;letter-spacing:.05em;text-transform:uppercase;color:var(--primary-dark);margin-bottom:10px}
.head h2{font-size:2rem;margin-bottom:10px}
.head p{color:var(--muted);font-size:1rem}

.card-x{background:var(--card);border:1px solid var(--border);border-radius:8px;padding:28px 22px;height:100%}
.card-x .ic{width:48px;height:48px;border-radius:10px;background:var(--primary-light);color:var(--primary-dark);display:flex;align-items:center;justify-content:center;font-size:1.3rem;margin-bottom:16px}
.card-x .ic.dark{background:var(--ink);color:var(--primary)}
.card-x h3{font-size:1rem;margin-bottom:8px}
.card-x p{color:var(--muted);font-size:.88rem;margin:0}

.fig{border-radius:8px}
.lead-p{font-size:1.08rem;font-weight:600;color:var(--ink)}
.note{border-radius:8px;padding:18px 20px;font-size:.9rem;border-left:4px solid var(--primary)}
.sec.paper .note{background:var(--card);border:1px solid var(--border)}

.steps{counter-reset:stp;max-width:820px;margin:0 auto;list-style:none;padding:0}
.steps li{display:flex;gap:20px;padding:22px 0;border-bottom:1px solid var(--border)}
.sec.dark .steps li{border-bottom:1px solid var(--border-dark)}
.steps li:last-child{border-bottom:none}
.step-num{counter-increment:stp;flex:none;width:42px;height:42px;border-radius:50%;background:var(--primary);color:var(--on-primary);display:flex;align-items:center;justify-content:center;font-family:'Anton',sans-serif;font-size:1.1rem}
.step-num:before{content:counter(stp)}
.steps h3{font-size:1rem;margin-bottom:8px;text-transform:none}
.steps p{color:var(--muted);font-size:.9rem;margin:0}
.sec.dark .steps p{color:rgba(247,245,241,.6)}

.pack{background:var(--card);border:1px solid var(--border);border-radius:10px;overflow:hidden;text-align:center;height:100%;display:flex;flex-direction:column}
.pack.top{border-color:var(--primary);border-width:2px}
.pack-bar{background:var(--ink);color:var(--paper);padding:15px 10px;font-weight:800;text-transform:uppercase;letter-spacing:.03em;font-size:.92rem}
.pack.top .pack-bar{background:var(--primary);color:var(--on-primary)}
.pack-body{padding:24px 22px 0}
.pack-name{font-family:'Anton',sans-serif;font-size:1.15rem;margin-top:4px}
.pack-supply{color:var(--muted);font-size:.8rem;text-transform:uppercase;letter-spacing:.02em;font-weight:700;margin-bottom:14px}
.pack img{max-width:150px;margin:0 auto 16px}
.pack-price-row{display:flex;align-items:baseline;justify-content:center;gap:6px;margin-bottom:16px}
.pack-price-big{font-family:'Anton',sans-serif;font-size:2.3rem;color:var(--ink)}
.pack-price-sub{color:var(--muted);font-size:.9rem;font-weight:600}
.pack-badges{display:flex;flex-direction:column;gap:8px;margin-bottom:20px}
.pack-badge-pill{display:flex;align-items:center;justify-content:center;gap:8px;background:var(--paper);border-radius:999px;padding:9px 14px;font-size:.78rem;font-weight:800;color:var(--ink)}
.pack-badge-pill i{color:var(--primary)}
.pack-badge-pill.accent{background:var(--primary);color:var(--on-primary)}
.pack-badge-pill.accent i{color:var(--on-primary)}
.pack-buy{margin-bottom:18px}
.pack-total{font-size:.86rem;color:var(--muted);font-weight:700;text-transform:uppercase;letter-spacing:.02em;margin-bottom:4px}
.pack-total .pack-was{text-decoration:line-through;opacity:.6;font-weight:500;margin-right:6px}
.pack-total b{color:var(--ink);font-size:1rem}
.pack-ship{font-size:.82rem;color:var(--primary-dark);font-weight:700;margin-bottom:20px}
.pack-pay{margin-top:auto;padding:14px 16px;border-top:1px solid var(--border)}
.pack-pay img{max-height:26px;margin:0 auto}

.ing{background:var(--card);border:1px solid var(--border);border-radius:8px;padding:22px;height:100%}
.ing-top{display:flex;align-items:flex-start;gap:14px;margin-bottom:10px}
.ing-ic{width:38px;height:38px;flex:none;border-radius:8px;background:var(--primary-light);color:var(--primary-dark);display:flex;align-items:center;justify-content:center}
.ing-top h3{font-size:.98rem;text-transform:none;margin-bottom:4px}
.ing-role{display:inline-block;font-size:.68rem;font-weight:800;text-transform:uppercase;letter-spacing:.02em;color:var(--primary-dark);background:var(--primary-light);padding:2px 8px;border-radius:4px}
.ing p{color:var(--muted);font-size:.87rem;margin:0}
.med{background:var(--card);border:1px solid var(--border);border-left:4px solid var(--red);border-radius:0 8px 8px 0;padding:18px 20px;font-size:.88rem;color:var(--text)}

.badges .badge-tile{text-align:center}
.badge-img{width:64px;height:64px;object-fit:contain;margin:0 auto 12px}
.badge-cap{font-size:.82rem;font-weight:700;text-transform:uppercase;letter-spacing:.01em}
.warranty-img{max-width:190px;margin:0 auto}

.gain{background:var(--card);border:1px solid var(--border);border-radius:8px;padding:20px 24px;margin-bottom:14px}
.gain h3{font-size:.98rem;text-transform:none;margin-bottom:6px}
.gain p{color:var(--muted);font-size:.88rem;margin:0}

.cols{background:var(--card);border:1px solid var(--border);border-radius:10px;height:100%}
.cols h3{display:flex;align-items:center;gap:10px;font-size:1.05rem;text-transform:none;padding:20px 24px;border-bottom:1px solid var(--border);margin:0}
.cols.plus{border-top:4px solid var(--primary)}
.cols.minus{border-top:4px solid var(--ink)}
.cols ul{list-style:none;padding:18px 24px;margin:0}
.cols li{display:flex;gap:10px;padding:8px 0;font-size:.9rem}
.cols.plus li i{color:var(--primary)}
.cols.minus li i{color:var(--red)}

.said{background:var(--card);border:1px solid var(--border);border-radius:8px;padding:24px;height:100%}
.said img{width:56px;height:56px;border-radius:50%;object-fit:cover;margin-bottom:12px}
.said h3{font-size:.96rem;text-transform:none;margin-bottom:2px}
.said-stars{color:var(--primary);font-size:.9rem;margin-bottom:10px}
.said-ok{color:var(--muted);font-weight:600;font-size:.76rem;text-transform:none}
.said p{font-size:.9rem;color:var(--text);margin:0}

.warranty{background:var(--primary);color:var(--on-primary);border-radius:16px;padding:44px 40px}
.warranty .kick{color:var(--on-primary);opacity:.8}
.warranty h2{color:var(--on-primary)}
.warranty p{color:var(--on-primary);opacity:.88;margin:0}

.bonus-wrap{background:var(--card);border:1px solid var(--border);border-radius:10px;overflow:hidden;max-width:900px;margin:0 auto}
.bonus-bar{background:var(--ink);color:var(--paper);text-align:center;padding:18px 20px;font-family:'Anton',sans-serif;font-size:1.2rem;text-transform:uppercase;letter-spacing:.02em}
.bonus-rows{display:flex;flex-direction:column}
.bonus-row{display:flex;gap:24px;align-items:center;flex-wrap:wrap;padding:26px 28px;border-bottom:1px solid var(--border)}
.bonus-row:last-child{border-bottom:none}
.bonus-row img{width:130px;flex:none;border-radius:6px;box-shadow:0 10px 24px rgba(0,0,0,.12)}
.bonus-row h4{font-size:1.05rem;text-transform:none;margin-bottom:6px}
.bonus-price{color:var(--primary-dark);font-weight:800;font-size:.8rem;text-transform:uppercase;letter-spacing:.02em;margin-bottom:8px}
.bonus-price s{opacity:.6;font-weight:500;text-transform:none}
.bonus-row p:last-child{color:var(--muted);font-size:.9rem;margin:0}

.fit{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:26px}
.fit h3{display:flex;align-items:center;gap:9px;font-size:1rem;text-transform:none;margin-bottom:14px}
.fit ul{list-style:none;padding:0;margin:0}
.fit li{display:flex;gap:10px;padding:7px 0;font-size:.88rem}
.fit.yes li i{color:var(--primary)}
.fit.no li i{color:var(--red)}

.rev-board{display:flex;justify-content:center;gap:56px;flex-wrap:wrap;margin-top:44px;text-align:center}
.rev-board b{display:block;font-family:'Anton',sans-serif;font-size:1.8rem;color:var(--primary)}
.rev-board span{font-size:.76rem;color:var(--muted);font-weight:700;text-transform:uppercase;letter-spacing:.02em}

.faq{max-width:800px;margin:0 auto}
.faq-row{border:1px solid var(--border);border-radius:8px;margin-bottom:12px;background:var(--card);overflow:hidden}
.faq-btn{width:100%;text-align:left;background:transparent;border:none;padding:18px 20px;font-size:.96rem;font-weight:700;font-family:'Barlow',sans-serif;cursor:pointer;color:var(--ink);display:flex;justify-content:space-between;align-items:center;gap:16px}
.faq-btn:after{content:'+';font-size:1.4rem;color:var(--primary);font-weight:400;flex:none}
.faq-body{max-height:0;overflow:hidden;transition:max-height .25s ease}
.faq-body p{padding:0 20px 18px;color:var(--muted);font-size:.88rem;margin:0}
.faq-row.open .faq-btn:after{content:'−'}

.final{background:linear-gradient(135deg,var(--primary),var(--primary-dark));border-radius:16px;padding:56px 36px;text-align:center;color:#fff}
.final h2{color:#fff;margin-bottom:12px;font-size:2rem}
.final p{color:rgba(255,255,255,.85);max-width:520px;margin:0 auto 22px}
.final img{max-width:150px;margin:0 auto 20px;border-radius:8px}
.final .old{text-decoration:line-through;opacity:.7}
.final .new{font-family:'Anton',sans-serif;font-size:1.8rem;margin-bottom:18px}

footer{background:var(--ink);color:rgba(247,245,241,.65);padding:56px 0 26px;font-size:.85rem;border-top:1px solid var(--border-dark)}
footer .foot-logo{font-family:'Anton',sans-serif;font-size:1.15rem;color:var(--paper);text-transform:uppercase;display:block;margin-bottom:10px}
footer h5{color:var(--paper);font-size:.76rem;text-transform:uppercase;letter-spacing:.04em;margin-bottom:12px;font-weight:800}
footer ul{list-style:none;padding:0}
footer li{margin-bottom:8px}
footer a{color:rgba(247,245,241,.6);font-weight:500}
footer a:hover{color:var(--primary)}
footer hr{border-color:var(--border-dark);margin:20px 0}
footer p{color:rgba(247,245,241,.42);font-size:.76rem;margin-bottom:10px}

.sticky-bar{position:fixed;bottom:0;left:0;right:0;background:var(--ink);border-top:1px solid var(--border-dark);padding:12px 18px;display:none;align-items:center;justify-content:space-between;gap:16px;z-index:70}
.sticky-bar b{color:var(--paper);font-family:'Anton',sans-serif;font-size:.95rem}
.sticky-bar small{color:rgba(247,245,241,.5);font-size:.7rem;display:block}
@media(max-width:767px){.sticky-bar{display:flex}body{padding-bottom:76px}}
</style>
</head>
<body>

<div class="eeat"><div class="container"><div class="in">
<span><i class="bi bi-pencil-square"></i>Written by the <strong>__BRAND__ Editorial Desk</strong></span>
<span><i class="bi bi-clipboard-check"></i>Checked Against The Current Label</span>
<span><i class="bi bi-arrow-repeat"></i>Updated <strong>__YEAR__</strong></span>
<span><i class="bi bi-shield-check"></i>Independently Reviewed</span>
</div></div></div>

<nav class="navbar navbar-expand-lg sticky-top">
<div class="container">
<a class="brand navbar-brand" href="index.html"><span class="bolt"></span>__BRAND__</a>
<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#mainNav" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
<div class="collapse navbar-collapse" id="mainNav">
<ul class="navbar-nav ms-auto align-items-lg-center">
<li class="nav-item"><a class="nav-link" href="how-it-works.html">How It Works</a></li>
<li class="nav-item"><a class="nav-link" href="ingredients.html">Ingredients</a></li>
<li class="nav-item"><a class="nav-link" href="index.html#pricing">Pricing</a></li>
<li class="nav-item"><a class="nav-link" href="reviews.html">Reviews</a></li>
<li class="nav-item"><a class="nav-link" href="blog/index.html">Blog</a></li>
<li class="nav-item"><a class="nav-link" href="index.html#faq">FAQ</a></li>
<li class="nav-item ms-lg-2"><a class="btn btn-ember btn-sm" href="__AFFILIATE__"><i class="bi bi-bag-check me-1"></i> Order Now</a></li>
</ul>
</div>
</div>
</nav>

<header class="hero">
<div class="container">
<div class="row align-items-center g-5">
<div class="col-lg-6">
<span class="flag"><i class="bi bi-patch-check-fill"></i> __PILL_TEXT__</span>
<h1>__HERO_H1__</h1>
<p class="hero-sub">__HERO_DESC__</p>
<div class="ticks">
<div><i class="bi bi-check-circle-fill"></i><span>__CHECK1__</span></div>
<div><i class="bi bi-check-circle-fill"></i><span>__CHECK2__</span></div>
<div><i class="bi bi-check-circle-fill"></i><span>__CHECK3__</span></div>
<div><i class="bi bi-check-circle-fill"></i><span>__CHECK4__</span></div>
</div>
<div class="hero-btns">
<a class="btn btn-ember btn-lg" href="__AFFILIATE__"><i class="bi bi-bag-check me-1"></i> Get __BRAND__ — From __PRICE_FROM__</a>
<a class="btn btn-out-l" href="#how-it-works">See How It Works</a>
</div>
<p class="hero-rate"><span class="stars">★★★★★</span> <strong>4.8 / 5</strong> average rating &nbsp;·&nbsp; __REVIEW_COUNT__ verified reviews</p>
</div>
<div class="col-lg-6 text-center">
<img src="assets/images/hero.png" alt="__BRAND__ product" class="hero-pack" id="hero-img" width="600" height="600">
</div>
</div>
</div>
</header>

<section class="sec" id="symptoms-section"><div class="container">
<div class="head"><span class="kick">The Real Issue</span><h2>What __BRAND__ Was Formulated To Address</h2><p>Not a mystery — specific, everyday problems worth naming directly.</p></div>
<div class="row g-4">
__SYMPTOM_CARD_TEMPLATE__
</div>
</div></section>

<section class="sec paper" id="what-is"><div class="container">
<div class="row align-items-center g-5">
<div class="col-12 col-lg-5 text-center">
<img src="assets/images/hero.png" alt="__BRAND__ overview" class="fig" id="whatis-img" width="600" height="600" loading="lazy">
</div>
<div class="col-12 col-lg-7">
<span class="kick">About The Product</span>
<h2>What Is __BRAND__?</h2>
<p class="lead-p">__WHATIS_P1__</p>
<div class="note mt-3">__WHATIS_CALLOUT__</div>
<p class="mt-3"><a class="btn-out" href="what-is-product.html">Read The Full __BRAND__ Explainer <i class="bi bi-arrow-right"></i></a></p>
</div>
</div>
</div></section>

<section class="sec dark" id="how-it-works"><div class="container">
<div class="head"><span class="kick">The Mechanism</span><h2>How Does __BRAND__ Work?</h2><p>__HIW_INTRO__</p></div>
<ol class="steps">
__HIW_CARD_TEMPLATE__
</ol>
</div></section>

<section class="sec" id="pricing"><div class="container">
<div class="head"><span class="kick">Official Pricing</span><h2>Just Click Below To Select Your Package!</h2>
<p style="margin-bottom:4px">The order you place today is a one-time payment</p>
<p style="margin-bottom:0;font-weight:800;color:var(--ink)">NO Subscription &nbsp;·&nbsp; NO Hidden Charges</p></div>
<div class="row g-4 justify-content-center">
__PLAN_CARD_TEMPLATE__
</div>
<p class="text-center mt-4" style="font-size:.88rem;color:var(--muted)"><strong>Note:</strong> __PRICING_NOTE__</p>
</div></section>

__BONUS_SECTION__

<section class="sec paper" id="ingredients"><div class="container">
<div class="head"><span class="kick">Inside The Bottle</span><h2>__ING_HEADING__</h2><p>Every ingredient named — no proprietary blend hiding amounts.</p></div>
<div class="row g-4">
__ING_CARD_TEMPLATE__
</div>
</div></section>

<section class="sec badges"><div class="container">
<div class="head"><span class="kick">Quality You Can Trust</span><h2>Made To A Higher Standard</h2></div>
<div class="row g-4 justify-content-center text-center">
<div class="col-6 col-lg-3 badge-tile"><img src="assets/images/badge-usa.png" alt="Made in the USA" class="badge-img" width="64" height="64" loading="lazy"><div class="badge-cap">Made In The USA</div></div>
<div class="col-6 col-lg-3 badge-tile"><img src="assets/images/badge-natural.png" alt="Natural ingredients" class="badge-img" width="64" height="64" loading="lazy"><div class="badge-cap">Natural Ingredients</div></div>
<div class="col-6 col-lg-3 badge-tile"><img src="assets/images/badge-gmp.png" alt="GMP certified" class="badge-img" width="64" height="64" loading="lazy"><div class="badge-cap">GMP Certified</div></div>
<div class="col-6 col-lg-3 badge-tile"><img src="assets/images/badge-fda.png" alt="FDA-registered facility" class="badge-img" width="64" height="64" loading="lazy"><div class="badge-cap">FDA-Registered Facility</div></div>
</div>
</div></section>

<section class="sec paper" id="benefits"><div class="container">
<div class="head"><span class="kick">What It Supports</span><h2>The Benefits Of __BRAND__</h2><p>Every benefit below is supportive, not a promised medical outcome.</p></div>
<div class="row justify-content-center"><div class="col-12 col-lg-10">
__BENEFIT_CARD_TEMPLATE__
</div></div>
</div></section>

<section class="sec"><div class="container">
<div class="head"><span class="kick">Balanced View</span><h2>Both Sides, Stated Plainly</h2><p>A page that only lists upsides is not worth reading.</p></div>
<div class="row g-4 justify-content-center">
<div class="col-12 col-lg-6"><div class="cols plus"><h3><i class="bi bi-hand-thumbs-up-fill"></i> What Works Well</h3><ul id="bal-pros">__BAL_PROS_TEMPLATE__</ul></div></div>
<div class="col-12 col-lg-6"><div class="cols minus"><h3><i class="bi bi-exclamation-triangle-fill"></i> What To Be Realistic About</h3><ul>
<li><i class="bi bi-dash-lg"></i><span>Individual results vary — __BRAND__ is general nutritional support, not a guaranteed outcome for everyone.</span></li>
<li><i class="bi bi-dash-lg"></i><span>Consistent daily use over several weeks is generally needed to fairly judge a formula like this.</span></li>
<li><i class="bi bi-dash-lg"></i><span>__BRAND__ is designed to work alongside a healthy diet, sleep and lifestyle — not to replace them.</span></li>
<li><i class="bi bi-dash-lg"></i><span>The smallest package costs more per bottle than the larger bundles.</span></li>
</ul></div></div>
</div>
</div></section>

<section class="sec paper" id="reviews"><div class="container">
<div class="head"><span class="kick">Customer Voices</span><h2>Real __BRAND__ Reviews</h2><p>Individual experiences shared with the brand. Results vary, and nothing here is a guarantee of outcome.</p></div>
<div class="row g-4 justify-content-center">
__REVIEW_CARD_TEMPLATE__
</div>
<div class="rev-board">
<div><b>4.8</b><span>Average Rating</span></div>
<div><b>__REVIEW_COUNT__</b><span>Verified Reviews</span></div>
<div><b>60-Day</b><span>Guarantee</span></div>
</div>
</div></section>

<section class="sec"><div class="container">
<div class="warranty"><div class="row align-items-center g-4">
<div class="col-12 col-lg-4 text-center"><img src="assets/images/guarantee.png" alt="60-day money-back guarantee" class="warranty-img" width="190" height="190" loading="lazy"></div>
<div class="col-12 col-lg-8">
<span class="kick">Risk-Free Ordering</span>
<h2>The 60-Day Money-Back Guarantee</h2>
<p>__GUARANTEE_TEXT__</p>
</div>
</div></div>
</div></section>

<section class="sec paper"><div class="container">
<div class="head"><span class="kick">Suitability</span><h2>Who __BRAND__ Is For — And Who It Isn't</h2><p>An honest look before you order.</p></div>
<div class="row g-4">
<div class="col-12 col-lg-6"><div class="fit yes"><h3><i class="bi bi-check-circle-fill" style="color:var(--primary)"></i> Likely A Good Fit</h3><ul>
<li><i class="bi bi-check-lg"></i><span>Adults aged 18 and over interested in general nutritional support</span></li>
<li><i class="bi bi-check-lg"></i><span>Comfortable taking a daily capsule consistently for 8-12 weeks</span></li>
<li><i class="bi bi-check-lg"></i><span>Want every ingredient named, not hidden in a proprietary blend</span></li>
<li><i class="bi bi-check-lg"></i><span>Prefer a one-time purchase with no forced subscription</span></li>
</ul></div></div>
<div class="col-12 col-lg-6"><div class="fit no"><h3><i class="bi bi-x-circle-fill" style="color:var(--red)"></i> Consider Waiting</h3><ul>
<li><i class="bi bi-dash-lg"></i><span>Pregnant, nursing, or under the age of 18</span></li>
<li><i class="bi bi-dash-lg"></i><span>Currently on prescription medication without medical clearance</span></li>
<li><i class="bi bi-dash-lg"></i><span>Looking for an overnight fix rather than a daily routine</span></li>
<li><i class="bi bi-dash-lg"></i><span>Managing a diagnosed medical condition without a doctor's input</span></li>
</ul></div></div>
</div>
</div></section>

<section class="sec" id="faq"><div class="container">
<div class="head"><span class="kick">Common Questions</span><h2>__BRAND__ FAQ, Answered Honestly</h2></div>
<div class="faq">
__FAQ_ROW_TEMPLATE__
</div>
</div></section>

<section class="sec paper"><div class="container">
<div class="final">
<h2>Ready To Try __BRAND__?</h2>
<p>__FINAL_TEXT__</p>
<img src="assets/images/bottle-6.png" alt="__BRAND__ six bottle pack" width="150" height="150" loading="lazy">
<div class="old">Regular: __PRICE_HIGH__ / bottle</div>
<div class="new">Today From __PRICE_LOW__ / bottle</div>
<a class="btn btn-ember btn-lg" href="__AFFILIATE__"><i class="bi bi-bag-check me-1"></i> Claim Your __BRAND__ Discount</a>
</div>
</div></section>

<footer><div class="container">
<div class="row g-4 mb-4">
<div class="col-12 col-lg-5">
<span class="foot-logo">__BRAND__</span>
<p>An evidence-transparent daily formula built around named ingredients and an honest, balanced view.</p>
</div>
<div class="col-6 col-lg-3"><h5>Explore</h5><ul>
<li><a href="what-is-product.html">What Is __BRAND__</a></li>
<li><a href="how-it-works.html">How It Works</a></li>
<li><a href="ingredients.html">Ingredients</a></li>
<li><a href="benefits.html">Benefits</a></li>
<li><a href="reviews.html">Reviews</a></li>
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
<p><b>Who This Is For:</b> __BRAND__ is a dietary supplement for adults aged 18 and over interested in general nutritional support. It is not a substitute for medical treatment.</p>
<p><b>FDA Compliance:</b> These statements have not been evaluated by the U.S. Food &amp; Drug Administration. __BRAND__ is a dietary supplement, not a drug, and is not intended to diagnose, treat, cure or prevent any disease.</p>
<p><b>Affiliate Disclosure:</b> This website may earn a commission on purchases made through links to the official __BRAND__ store, at no additional cost to you.</p>
<p style="margin-top:16px;color:rgba(247,245,241,.35)">© __YEAR__ __BRAND__ — All Rights Reserved</p>
</div></footer>

<div class="sticky-bar"><div><b>__PRICE_LOW__ / bottle</b><small>Best value pack</small></div><a class="btn btn-ember btn-sm" href="__AFFILIATE__">__CTA_STICKY__</a></div>

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
