<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>__TITLE__</title>
<meta name="description" content="__META_DESC__">
<link rel="canonical" href="__CANONICAL__">
<meta name="theme-color" content="__COLOR_PRIMARY__">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700;800;900&family=Source+Sans+3:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{
 --primary:__COLOR_PRIMARY__;
 --primary-dark:__COLOR_DARK__;
 --primary-light:__COLOR_LIGHT__;
 --accent:__COLOR_ACCENT__;
 --on-primary:__COLOR_ON_PRIMARY__;
 --bg:#FFFFFF;--bg-soft:#F5F8F8;--chip:#E3EDEC;--text:#111111;--text-secondary:#444444;--border:#D5E2E1;
 --green:#1a7f37;--yellow:#FFD700;--radius:10px;--shadow:0 6px 20px rgba(20,40,45,.14);
 --font-head:'Montserrat',sans-serif;--font-body:'Source Sans 3',sans-serif;
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{font-family:var(--font-body);font-size:20px;line-height:1.8;color:var(--text);background:var(--bg);padding-bottom:76px;overflow-x:hidden;-webkit-font-smoothing:antialiased}
h1,h2,h3,h4{font-family:var(--font-head);font-weight:800;line-height:1.3}
h1{font-size:clamp(30px,4.2vw,44px)}
h2{font-size:clamp(25px,4.2vw,36px);margin-bottom:16px;color:var(--primary-dark)}
h3{font-size:clamp(20px,2.8vw,26px);color:var(--primary-dark)}
p{margin-bottom:1.1em;font-size:20px;line-height:1.85;color:#222}
a{color:var(--primary-dark);text-decoration:none}
img{max-width:100%;height:auto;display:block}
.container{max-width:1200px;margin:0 auto;padding:0 20px}
.section{padding:60px 0}
@media(max-width:768px){body{font-size:18px;padding-bottom:70px}p{font-size:18px}.section{padding:40px 0}.container{padding:0 16px}}
.bg-soft{background:var(--bg-soft)}
.bg-dark{background:linear-gradient(135deg,var(--primary) 0%,var(--primary-dark) 100%);color:var(--on-primary)}
.bg-dark h1,.bg-dark h2,.bg-dark h3,.bg-dark p{color:var(--on-primary)}
.eyebrow{display:inline-block;background:var(--chip);color:var(--primary-dark);padding:6px 16px;border-radius:999px;font-size:15px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;margin-bottom:14px;font-family:var(--font-head)}

.bar-heading{background:var(--primary);text-align:center;padding:28px 20px;margin-bottom:40px;box-shadow:0 4px 12px rgba(0,0,0,.15)}
.bar-heading h2{color:var(--on-primary);margin:0;font-size:clamp(24px,4.2vw,38px);text-transform:capitalize}
.bar-heading p{color:var(--on-primary);opacity:.9;font-size:19px;margin:8px 0 0}

.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;font-family:var(--font-body);font-weight:700;font-size:19px;padding:13px 26px;border-radius:var(--radius);border:2px solid transparent;cursor:pointer;min-height:44px;transition:.2s;text-align:center}
.btn-yellow{background:var(--yellow);color:#000;box-shadow:0 6px 18px rgba(0,0,0,.18)}
.btn-yellow:hover{background:#FFC700;transform:translateY(-1px)}
.btn-solid{background:var(--primary-dark);color:#fff}
.btn-solid:hover{opacity:.9}

nav.sitenav{position:sticky;top:0;background:#fff;z-index:200;box-shadow:0 2px 10px rgba(0,0,0,.08)}
.nav-inner{display:flex;align-items:center;justify-content:space-between;padding:14px 20px;max-width:1200px;margin:0 auto;gap:16px}
.nav-logo{font-family:var(--font-head);font-weight:800;font-size:24px;color:var(--primary-dark);white-space:nowrap}
.nav-links{display:flex;align-items:center;gap:20px;list-style:none}
.nav-links a{font-size:17px;font-weight:600;color:var(--text)}
.nav-links a:hover{color:var(--primary-dark)}
.nav-toggle{display:none;background:none;border:none;font-size:28px;cursor:pointer;color:var(--primary-dark);padding:0 8px;min-height:44px}
@media(max-width:899px){.nav-inner{padding:10px 12px;gap:8px}.nav-logo{font-size:20px}.nav-inner .btn{padding:8px 12px;font-size:15px;min-height:36px}
 .nav-links{position:fixed;top:60px;left:0;right:0;background:#fff;flex-direction:column;padding:20px;gap:16px;display:none;box-shadow:0 8px 16px rgba(0,0,0,.08)}.nav-links.open{display:flex}.nav-toggle{display:block}}
.ticker{background:var(--primary-dark);color:#fff;font-size:16px;font-weight:600;text-align:center;padding:9px 12px}
@media(max-width:640px){.ticker{font-size:14px;padding:8px 10px}}

.hero{padding:70px 0}
.hero-grid{display:grid;gap:40px;align-items:center}
@media(min-width:900px){.hero-grid{grid-template-columns:430px 1fr}}
.hero-img{width:100%;object-fit:contain;border-radius:12px}
.hero h1{margin-bottom:18px;line-height:1.2}
.hero-lead{font-size:21px;line-height:1.7;opacity:.96;margin-bottom:20px}
.hero-checks{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:0 0 22px}
.hero-checks div{display:flex;gap:9px;align-items:flex-start;font-weight:600;font-size:17px;background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.28);padding:10px 14px;border-radius:8px;color:var(--on-primary)}
.hero-checks i{font-style:normal;color:var(--yellow);font-weight:900}
.hero-badges{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;margin:0 0 22px;max-width:480px}
.hero-badges div{background:rgba(255,255,255,.1);padding:9px 14px;border-radius:8px;border:1px solid rgba(255,255,255,.25);font-size:16px;font-weight:600;color:var(--on-primary)}
.hero-note{font-size:15px;opacity:.85;margin:14px 0 0}
@media(max-width:640px){.hero{padding:34px 0}.hero-checks{grid-template-columns:1fr}.btn-hero{width:100%}}

.what-grid{display:grid;gap:40px;align-items:center}
@media(min-width:900px){.what-grid{grid-template-columns:1fr 1.15fr}}
.what-grid img{border-radius:var(--radius);box-shadow:var(--shadow);width:100%;max-width:480px;margin:0 auto}
.auto-quick-facts.callout{font-style:normal}
.auto-quick-facts.callout h3{font-size:22px}
.callout{background:#f9fafb;border-left:5px solid var(--primary-dark);padding:18px 24px;border-radius:0 10px 10px 0;font-style:italic;color:#333;font-size:19px;line-height:1.8;margin-top:10px}
.problems-list{list-style:none;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:15px;margin:36px 0 0}
.problems-list li{background:#fff;border:1px solid var(--border);padding:14px 20px 14px 50px;border-radius:10px;position:relative;font-size:19px;font-weight:600;color:var(--primary-dark);box-shadow:0 2px 8px rgba(0,0,0,.05)}
.problems-list li::before{content:'\2713';position:absolute;left:15px;color:var(--green);font-weight:900;font-size:24px}

.steps16{display:grid;gap:22px;grid-template-columns:repeat(auto-fit,minmax(250px,1fr))}
.step16{background:#fff;border:1px solid var(--border);border-top:5px solid var(--primary);border-radius:12px;padding:26px 22px;box-shadow:0 4px 15px rgba(0,0,0,.05)}
.step16-num{width:46px;height:46px;border-radius:50%;background:var(--primary);color:var(--on-primary);display:flex;align-items:center;justify-content:center;font-family:var(--font-head);font-weight:800;font-size:20px;margin-bottom:14px}
.step16 h3{font-size:21px;margin-bottom:8px}
.step16 p{font-size:17px;color:var(--text-secondary);margin:0}
.section-intro{text-align:center;max-width:860px;margin:0 auto 34px;color:var(--text-secondary)}

.benefit-grid{display:grid;grid-template-columns:1fr;gap:24px}
@media(min-width:700px){.benefit-grid{grid-template-columns:repeat(2,1fr)}}
@media(min-width:1000px){.benefit-grid{grid-template-columns:repeat(3,1fr)}}
.benefit-card{background:#fff;border:1px solid var(--border);border-radius:12px;padding:28px 24px;box-shadow:var(--shadow);transition:.2s}
.benefit-card:hover{transform:translateY(-3px)}
.benefit-icon{font-size:40px;margin-bottom:12px;line-height:1}
.benefit-card h3{margin-bottom:10px;font-size:23px}
.benefit-card p{font-size:18px;color:var(--text-secondary);margin:0}

.testimonial-grid{display:grid;gap:30px;grid-template-columns:1fr}
@media(min-width:900px){.testimonial-grid{grid-template-columns:repeat(3,1fr)}}
.testimonial{background:#fff;border:1px solid var(--border);border-radius:12px;padding:30px 24px;box-shadow:var(--shadow);text-align:center;display:flex;flex-direction:column;align-items:center}
.testi-photo{width:92px;height:92px;border-radius:50%;object-fit:cover;margin-bottom:14px;border:3px solid var(--border);box-shadow:0 4px 10px rgba(0,0,0,.1)}
.testi-initial{width:92px;height:92px;border-radius:50%;background:var(--primary-light);color:var(--primary-dark);display:flex;align-items:center;justify-content:center;font-size:38px;font-weight:800;font-family:var(--font-head);margin-bottom:14px;border:3px solid var(--border)}
.stars{color:#FFB800;font-size:24px;margin-bottom:8px}
.verified{display:inline-flex;align-items:center;gap:6px;font-size:16px;font-weight:700;color:var(--primary-dark);margin-bottom:14px}
.verified span{color:#22c55e;font-size:20px}
.testimonial p{font-size:18px;font-style:italic;color:#333;line-height:1.7;margin-bottom:14px;text-align:left;width:100%}
.testimonial .name{font-weight:800;font-size:19px;color:var(--primary-dark)}
.rev-note{text-align:center;color:var(--text-secondary);font-size:16px;margin-top:26px}

.trust-grid{display:grid;gap:24px;grid-template-columns:repeat(2,1fr)}
@media(min-width:800px){.trust-grid{grid-template-columns:repeat(4,1fr)}}
.trust-card{background:#fff;border:1px solid var(--border);border-radius:12px;padding:24px;text-align:center;box-shadow:0 4px 14px rgba(20,40,45,.05)}
.trust-card img{width:90px;height:90px;object-fit:contain;margin:0 auto 14px}
.trust-card h3{font-size:20px;margin-bottom:8px}
.trust-card p{font-size:16px;color:var(--text-secondary);line-height:1.6;margin:0}

.ing-list{display:flex;flex-direction:column;gap:20px}
.ing-card{background:#fff;border:1px solid var(--border);border-radius:12px;padding:24px;display:flex;gap:20px;align-items:flex-start;box-shadow:0 4px 15px rgba(0,0,0,.05);transition:.2s}
.ing-card:hover{transform:translateY(-2px);box-shadow:0 8px 25px rgba(0,0,0,.1)}
.ing-num-circle{width:48px;height:48px;border-radius:50%;background:var(--primary);color:var(--on-primary);display:flex;align-items:center;justify-content:center;font-family:var(--font-head);font-size:21px;font-weight:800;flex-shrink:0}
.ing-content{flex:1}
.ing-name{font-size:23px;margin-bottom:8px;color:var(--primary-dark)}
.ing-desc p{font-size:18px;color:#333;line-height:1.8;margin:0}
@media(max-width:640px){.ing-card{padding:18px;gap:14px}.ing-num-circle{width:40px;height:40px;font-size:17px}.ing-name{font-size:20px}}

.pros-grid{display:grid;gap:24px;grid-template-columns:1fr}
@media(min-width:800px){.pros-grid{grid-template-columns:1fr 1fr}}
.pros-box{background:#f0fdf4;border:2px solid #bbf7d0;border-radius:16px;padding:28px;box-shadow:0 4px 15px rgba(0,0,0,.05)}
.pros-box h3{color:#166534;margin-bottom:18px;font-size:24px}
.pros-box ul{list-style:none;padding:0;margin:0}
.pros-box li{position:relative;padding-left:32px;margin-bottom:13px;font-size:19px;color:#166534;font-weight:600;line-height:1.55}
.pros-box li::before{content:'\2713';position:absolute;left:0;color:#22c55e;font-weight:900;font-size:22px}
.pros-box.facts{background:#fff;border-color:var(--border)}
.pros-box.facts h3{color:var(--primary-dark)}
.pros-box.facts li{color:#333;font-weight:500}
.pros-box.facts li::before{color:var(--primary)}
.facts .small{font-size:16px;color:var(--text-secondary);margin:14px 0 0}

.pricing-wrap{background:var(--bg-soft)}
.pricing-grid{display:grid;gap:24px;grid-template-columns:1fr;align-items:stretch}
@media(min-width:900px){.pricing-grid{grid-template-columns:repeat(3,1fr)}}
.price-card{background:#fff;border:2px solid var(--border);border-radius:20px;overflow:hidden;display:flex;flex-direction:column;box-shadow:var(--shadow);position:relative;padding-bottom:20px}
.price-card.best-value{transform:translateY(-8px);box-shadow:0 14px 38px rgba(0,0,0,.2);border-color:var(--primary)}
.price-badge{padding:16px;text-align:center;background:var(--bg-soft);border-bottom:1px solid var(--border);font-family:var(--font-head);font-size:22px;font-weight:800;color:var(--primary-dark)}
.price-card.best-value .price-badge{background:var(--primary);color:var(--on-primary);border:none}
.price-img{max-height:150px;width:auto;margin:16px auto 0;object-fit:contain}
.price-amount{text-align:center;padding:16px 20px 4px;font-family:var(--font-head);font-size:60px;font-weight:900;color:var(--primary-dark);line-height:1}
.price-amount span{font-size:28px;vertical-align:top}
.price-per{text-align:center;font-size:17px;color:var(--text-secondary);margin-bottom:6px;font-weight:600}
.price-savings{text-align:center;font-weight:800;color:var(--primary-dark);font-size:15px;letter-spacing:.5px;margin-bottom:12px}
.price-bonus{text-align:center;font-size:15px;color:var(--primary-dark);background:var(--primary-light);margin:0 20px 16px;padding:8px;border-radius:6px;font-weight:700}
.price-btn{display:block;text-align:center;background:var(--yellow);color:#000;font-weight:900;font-size:19px;padding:15px;margin:0 20px 14px;border-radius:10px;letter-spacing:.03em;transition:.2s}
.price-btn:hover{background:#FFC700;transform:translateY(-1px)}
.price-guarantee{text-align:center;font-size:15px;color:var(--primary-dark);font-weight:700;margin-bottom:12px}
.price-pay{margin:0 auto 12px}
.price-pay img{max-height:26px;width:auto;margin:0 auto}
.price-total{text-align:center;font-size:16px;color:var(--text-secondary);padding:14px 20px 4px;border-top:1px dashed var(--border);margin:0 20px}
.price-total s{color:#999;font-size:14px}
.price-total strong{color:var(--primary-dark);font-size:19px;margin-left:5px}
.price-ship{text-align:center;font-size:15px;font-weight:700;color:var(--primary-dark)}
@media(max-width:640px){.price-card.best-value{transform:none}.price-amount{font-size:52px}}
.pricing-note{text-align:center;color:var(--text-secondary);font-size:16px;margin-top:28px}
.bonus-block{max-width:1000px;margin:0 auto}

.guarantee-section{background:linear-gradient(135deg,var(--primary-light) 0%,#ffffff 100%)}
.guarantee-box{display:grid;gap:32px;align-items:center;background:#fff;border-radius:var(--radius);padding:40px;box-shadow:var(--shadow)}
@media(min-width:800px){.guarantee-box{grid-template-columns:auto 1fr}}
.guarantee-seal{width:160px;height:160px;margin:0 auto;border-radius:50%;background:conic-gradient(from 0deg,var(--primary) 0deg 330deg,transparent 330deg 360deg);display:flex;align-items:center;justify-content:center;flex-shrink:0}
.seal-inner{width:140px;height:140px;border-radius:50%;background:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;box-shadow:inset 0 0 0 4px var(--primary);text-align:center}
.seal-num{font-family:var(--font-head);font-size:44px;font-weight:800;color:var(--primary-dark);line-height:1}
.seal-label{font-family:var(--font-head);font-size:14px;font-weight:700;letter-spacing:.16em;color:var(--primary-dark)}
.seal-sub{font-size:11px;font-weight:700;color:var(--text-secondary);letter-spacing:.08em;margin-top:2px}
.guarantee-content h2{font-size:clamp(23px,3.2vw,31px);margin-bottom:12px}
.guarantee-list{list-style:none;margin:14px 0 20px;padding:0}
.guarantee-list li{padding:5px 0;font-size:19px;font-weight:500}
@media(max-width:768px){.guarantee-box{padding:24px 20px;gap:20px}.guarantee-seal{width:120px;height:120px}.seal-inner{width:104px;height:104px}.seal-num{font-size:34px}}

.faq-list{background:#fff;border-radius:var(--radius);box-shadow:var(--shadow);overflow:hidden;max-width:860px;margin:0 auto}
.faq-item{border-bottom:1px solid var(--border)}
.faq-item:last-child{border-bottom:none}
.faq-q{width:100%;text-align:left;background:none;border:none;font-family:var(--font-head);font-size:20px;font-weight:700;cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:14px;color:var(--primary-dark);padding:22px 24px;min-height:64px;line-height:1.4}
.faq-q:hover{background:var(--bg-soft)}
.faq-icon{font-size:28px;font-weight:400;color:var(--primary-dark);flex-shrink:0;transition:transform .3s;line-height:1}
.faq-item.open .faq-icon{transform:rotate(45deg)}
.faq-a{max-height:0;overflow:hidden;transition:max-height .35s ease}
.faq-a p{padding:0 24px 22px;line-height:1.8;color:#333;font-size:18px;margin:0}
.faq-item.open .faq-a{max-height:800px}
@media(max-width:640px){.faq-q{padding:16px 18px;font-size:18px}.faq-a p{padding:0 18px 18px;font-size:17px}}

.final-cta{text-align:center}
.final-cta img{width:340px;max-width:100%;margin:0 auto 24px;border-radius:var(--radius)}
.fcp-regular{font-size:22px;color:var(--text-secondary);margin-bottom:6px}
.fcp-today{font-size:28px;color:var(--text);margin-bottom:22px}
.fcp-today strong{color:var(--primary-dark);font-family:var(--font-head);font-size:36px}
.final-cta-btn{display:inline-block;background:var(--yellow);color:#000;font-weight:900;font-size:24px;padding:18px 40px;border-radius:10px;letter-spacing:.03em;transition:.2s;box-shadow:0 8px 22px rgba(0,0,0,.2);max-width:100%}
.final-cta-btn:hover{background:#FFC700;transform:translateY(-2px)}
@media(max-width:640px){.fcp-today{font-size:22px}.fcp-today strong{font-size:28px}.final-cta-btn{font-size:19px;padding:15px 22px;width:100%}}

footer.sitefoot{background:#111827;color:#e2e8f0;border-top:4px solid var(--primary);padding:54px 0 24px}
footer.sitefoot a{color:#d8e6e8}
footer.sitefoot a:hover{color:#fff;text-decoration:underline}
.footer-grid{display:grid;gap:32px;margin-bottom:30px}
@media(min-width:700px){.footer-grid{grid-template-columns:2fr 1fr 1fr}}
.footer-brand-title{font-family:var(--font-head);font-weight:800;font-size:24px;color:#fff;margin-bottom:12px}
.footer-grid p{font-size:16px;color:#c9dadd;line-height:1.7}
.footer-col-title{font-family:var(--font-head);font-weight:800;font-size:16px;color:#fff;margin-bottom:14px;text-transform:uppercase;letter-spacing:1.2px}
.footer-grid ul{list-style:none;padding:0;margin:0}
.footer-grid li{margin-bottom:9px;font-size:17px}
.footer-legal{font-size:15px;border-top:1px solid rgba(255,255,255,.15);padding-top:20px;line-height:1.7}
.footer-legal p{margin-bottom:10px;color:#a8c1c5;font-size:15px}
.footer-legal strong{color:#fff}

.sticky-bar{position:fixed;left:0;right:0;bottom:0;background:#fff;box-shadow:0 -4px 14px rgba(0,0,0,.12);padding:11px 16px;display:flex;align-items:center;justify-content:space-between;gap:12px;z-index:150}
.sticky-bar b{font-size:17px;color:var(--primary-dark);font-weight:800}
.sticky-bar small{display:block;font-size:12px;color:var(--text-secondary)}
@media(min-width:900px){.sticky-bar{display:none}body{padding-bottom:0}}
.back-to-top{position:fixed;bottom:90px;right:18px;background:var(--primary-dark);color:#fff;width:48px;height:48px;border-radius:50%;display:flex;align-items:center;justify-content:center;box-shadow:var(--shadow);opacity:0;pointer-events:none;transition:.3s;z-index:140;border:none;cursor:pointer;font-size:22px}
.back-to-top.show{opacity:1;pointer-events:auto}
</style>
</head>
<body>

<div class="ticker">Official pricing: larger bundles ship free and cost less per bottle &mdash; __CATEGORY__ support backed by a 60-day guarantee</div>

<nav class="sitenav">
<div class="nav-inner">
<a class="nav-logo" href="index.html">__BRAND__</a>
<ul class="nav-links">
<li><a href="what-is-product.html">About</a></li>
<li><a href="ingredients.html">Ingredients</a></li>
<li><a href="benefits.html">Benefits</a></li>
<li><a href="reviews.html">Reviews</a></li>
<li><a href="blog/index.html">Blog</a></li>
<li><a href="index.html#faq">FAQs</a></li>
</ul>
<a class="btn btn-yellow" href="__AFFILIATE__">__CTA_HEADER__</a>
<button class="nav-toggle" aria-label="Toggle menu" type="button">&#9776;</button>
</div>
</nav>

<header class="hero bg-dark">
<div class="container hero-grid">
<div><img class="hero-img" src="assets/images/hero.png" alt="__BRAND__ product" id="hero-img" width="600" height="600"></div>
<div>
<span class="eyebrow" style="background:rgba(255,255,255,.16);color:var(--on-primary)">__PILL_TEXT__</span>
<h1>__HERO_H1__</h1>
<p class="hero-lead">__HERO_DESC__</p>
<div class="hero-checks">
<div><i>&#10003;</i><span>__CHECK1__</span></div>
<div><i>&#10003;</i><span>__CHECK2__</span></div>
<div><i>&#10003;</i><span>__CHECK3__</span></div>
<div><i>&#10003;</i><span>__CHECK4__</span></div>
</div>
<div class="hero-badges">
<div>Made In USA</div><div>Natural Ingredients</div><div>GMP Certified</div><div>FDA-Registered Facility</div>
</div>
<a class="btn btn-yellow btn-hero" style="font-size:21px;padding:16px 32px;font-weight:900" href="__AFFILIATE__">__CTA_HERO__</a>
<p class="hero-note">Secure checkout on the official store &middot; 60-day money-back guarantee</p>
</div>
</div>
</header>

<section class="section" id="what-is">
<div class="bar-heading"><h2>What Is __BRAND__?</h2></div>
<div class="container">
<div class="what-grid">
<div><img src="assets/images/hero.png" alt="__BRAND__ overview" id="whatis-img" width="600" height="600" loading="lazy"></div>
<div>
<p>__WHATIS_P1__</p>
<div class="callout">__WHATIS_CALLOUT__</div>
<p style="margin-top:22px"><a class="btn btn-solid" href="what-is-product.html">Read The Full __BRAND__ Explainer</a></p>
</div>
</div>
<ul class="problems-list">
__SYMPTOM_CARD_TEMPLATE__
</ul>
</div>
</section>

<section class="section bg-soft" id="how-it-works">
<div class="bar-heading"><h2>How Does __BRAND__ Work?</h2></div>
<div class="container">
<p class="section-intro">__HIW_INTRO__</p>
<div class="steps16">
__HIW_CARD_TEMPLATE__
</div>
</div>
</section>

<section class="section" id="benefits">
<div class="bar-heading"><h2>What Are The Benefits Of __BRAND__?</h2><p>Every benefit below is supportive, not a promised medical outcome.</p></div>
<div class="container">
<div class="benefit-grid">
__BENEFIT_CARD_TEMPLATE__
</div>
</div>
</section>

<section class="section bg-soft" id="reviews">
<div class="bar-heading"><h2>Customer Reviews For __BRAND__</h2></div>
<div class="container">
<div class="testimonial-grid">
__REVIEW_CARD_TEMPLATE__
</div>
<p class="rev-note">Individual experiences shared with the brand. Results vary, and nothing here is a guarantee of outcome.</p>
</div>
</section>

<section class="section" id="why-choose">
<div class="bar-heading"><h2>Why Choose __BRAND__?</h2></div>
<div class="container">
<div class="trust-grid">
<div class="trust-card"><img src="assets/images/badge-usa.png" alt="Made in the USA" width="90" height="90" loading="lazy"><h3>Made In USA</h3><p>Formulated under strict standards</p></div>
<div class="trust-card"><img src="assets/images/badge-natural.png" alt="Natural ingredients" width="90" height="90" loading="lazy"><h3>Natural Ingredients</h3><p>Every ingredient named</p></div>
<div class="trust-card"><img src="assets/images/badge-gmp.png" alt="GMP certified" width="90" height="90" loading="lazy"><h3>GMP Certified</h3><p>Good Manufacturing Practice</p></div>
<div class="trust-card"><img src="assets/images/badge-fda.png" alt="FDA-registered facility" width="90" height="90" loading="lazy"><h3>FDA-Registered Facility</h3><p>Manufactured in a registered facility</p></div>
</div>
</div>
</section>

<section class="section bg-soft" id="ingredients">
<div class="bar-heading"><h2>__ING_HEADING__</h2><p>Each ingredient is listed individually so you can see exactly what is inside.</p></div>
<div class="container">
<div class="ing-list">
__ING_CARD_TEMPLATE__
</div>
</div>
</section>

<section class="section">
<div class="bar-heading"><h2>__BRAND__ At A Glance</h2></div>
<div class="container">
<div class="pros-grid">
<div class="pros-box"><h3>What It Is Formulated To Support</h3><ul>
__BAL_PROS_TEMPLATE__
</ul></div>
<div class="pros-box facts"><h3>Key Facts</h3><ul>
<li><strong>__FACT1_NUM__</strong> __FACT1_LABEL__ named on the label</li>
<li><strong>__FACT2_NUM__</strong> __FACT2_LABEL__ per day (__SERVING_DAILY__)</li>
<li><strong>__FACT3_NUM__</strong> __FACT3_LABEL__</li>
<li>Made in the <strong>__FACT4_NUM__</strong></li>
</ul>
<p class="small">Each bottle contains __SERVING_PER_BOTTLE__.</p></div>
</div>
</div>
</section>

<section class="section pricing-wrap" id="pricing">
<div class="bar-heading"><h2>Choose Your __BRAND__ Package</h2><p>One-time payment &middot; No subscription &middot; No hidden charges</p></div>
<div class="container">
<div class="pricing-grid">
__PLAN_CARD_TEMPLATE__
</div>
<p class="pricing-note"><strong>Note:</strong> __PRICING_NOTE__</p>
</div>
</section>

<div class="bonus-block">__BONUS_SECTION__</div>

<section class="section guarantee-section">
<div class="container">
<div class="guarantee-box">
<div class="guarantee-seal"><div class="seal-inner"><div class="seal-num">60</div><div class="seal-label">DAY</div><div class="seal-sub">MONEY BACK</div></div></div>
<div class="guarantee-content">
<span class="eyebrow">Zero Risk</span>
<h2>The 60-Day Money-Back Guarantee</h2>
<p>__GUARANTEE_TEXT__</p>
<a class="btn btn-solid" href="__AFFILIATE__">Order Risk-Free</a>
</div>
</div>
</div>
</section>

<section class="section bg-soft" id="faq">
<div class="bar-heading"><h2>Frequently Asked Questions About __BRAND__</h2></div>
<div class="container">
<div class="faq-list">
__FAQ_ROW_TEMPLATE__
</div>
</div>
</section>

<section class="section final-cta">
<div class="bar-heading"><h2>Ready To Try __BRAND__?</h2></div>
<div class="container">
<p class="section-intro">__FINAL_TEXT__</p>
<img src="assets/images/bottle-6.png" alt="__BRAND__ six bottle pack" width="340" height="340" loading="lazy">
<div class="fcp-regular">Regular Price: <s>__PRICE_HIGH__ / bottle</s></div>
<div class="fcp-today">Today From: <strong>__PRICE_LOW__ / bottle</strong></div>
<a class="final-cta-btn" href="__AFFILIATE__">__CTA_CLOSING__</a>
</div>
</section>

<footer class="sitefoot"><div class="container">
<div class="footer-grid">
<div>
<div class="footer-brand-title">__BRAND__</div>
<p>__BRAND__ is a dietary supplement formulated with named ingredients to support everyday wellness. Always read the label and follow the directions.</p>
</div>
<div><div class="footer-col-title">Explore</div><ul>
<li><a href="what-is-product.html">What Is __BRAND__</a></li>
<li><a href="how-it-works.html">How It Works</a></li>
<li><a href="ingredients.html">Ingredients</a></li>
<li><a href="benefits.html">Benefits</a></li>
<li><a href="reviews.html">Reviews</a></li>
<li><a href="faq.html">FAQ</a></li>
</ul></div>
<div><div class="footer-col-title">Legal</div><ul>
<li><a href="terms.html">Terms of Use</a></li>
<li><a href="privacy-policy.html">Privacy Policy</a></li>
<li><a href="disclaimer.html">Disclaimer</a></li>
<li><a href="refund-policy.html">Refund Policy</a></li>
<li><a href="contact.html">Contact Us</a></li>
</ul></div>
</div>
<div class="footer-legal">
<p><strong>FDA Disclaimer:</strong> These statements have not been evaluated by the U.S. Food &amp; Drug Administration. __BRAND__ is a dietary supplement, not a drug, and is not intended to diagnose, treat, cure or prevent any disease. Consult a healthcare professional before use, especially if you are pregnant, nursing, taking medication or managing a medical condition.</p>
<p><strong>Affiliate Disclosure:</strong> This website may earn a commission on purchases made through links to the official __BRAND__ store, at no additional cost to you.</p>
<p style="text-align:center;margin-top:16px">&copy; __YEAR__ __BRAND__ &mdash; All Rights Reserved</p>
</div>
</div></footer>

<div class="sticky-bar"><div><b>__PRICE_LOW__ / bottle</b><small>Best value pack</small></div><a class="btn btn-yellow" style="padding:10px 16px;font-size:16px;min-height:40px" href="__AFFILIATE__">__CTA_STICKY__</a></div>
<button class="back-to-top" aria-label="Back to top" type="button">&uarr;</button>

<script>
document.addEventListener('DOMContentLoaded',function(){
 var t=document.querySelector('.nav-toggle'),l=document.querySelector('.nav-links');
 if(t&&l)t.addEventListener('click',function(){l.classList.toggle('open')});
 document.querySelectorAll('.faq-item').forEach(function(item){
  var b=item.querySelector('.faq-q');if(!b)return;
  b.addEventListener('click',function(){
   var was=item.classList.contains('open');
   document.querySelectorAll('.faq-item.open').forEach(function(i){i.classList.remove('open');i.querySelector('.faq-q').setAttribute('aria-expanded','false')});
   if(!was){item.classList.add('open');b.setAttribute('aria-expanded','true')}
  });
 });
 var bt=document.querySelector('.back-to-top');
 if(bt){window.addEventListener('scroll',function(){bt.classList.toggle('show',window.scrollY>500)});bt.addEventListener('click',function(){window.scrollTo({top:0,behavior:'smooth'})})}
});
</script>
</body></html>
