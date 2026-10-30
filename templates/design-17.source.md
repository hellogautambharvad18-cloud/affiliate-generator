<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>__TITLE__</title>
<meta name="description" content="__META_DESC__">
<link rel="canonical" href="__CANONICAL__">
<meta name="theme-color" content="__COLOR_PRIMARY__">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Epilogue:wght@600;700;800;900&family=Hind:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>

:root{
  --lu-ink:#16203a;--lu-txt:#2b3550;--lu-mut:#5b6580;--lu-line:#e3e8f4;
  --primary:__COLOR_PRIMARY__;--primary-dark:__COLOR_DARK__;--primary-light:__COLOR_LIGHT__;--accent:__COLOR_ACCENT__;--on-primary:__COLOR_ON_PRIMARY__;
  --lu-cob:__COLOR_DARK__;--lu-cobD:color-mix(in srgb,__COLOR_DARK__ 78%,#000);--lu-sky:__COLOR_LIGHT__;
  --lu-apr:__COLOR_ACCENT__;--lu-aprD:color-mix(in srgb,__COLOR_ACCENT__ 78%,#000);--lu-peach:color-mix(in srgb,__COLOR_ACCENT__ 11%,#fff);
  --lu-leaf:#3e9a55;--lu-mint:#eef8f0;
  --lu-hd:"Epilogue",system-ui,sans-serif;--lu-bd:"Hind",system-ui,sans-serif;
  --lu-w:1220px;
}
*,*::before,*::after{box-sizing:border-box}
html{font-size:19px;-webkit-text-size-adjust:100%;scroll-behavior:smooth}
body{margin:0;background:#fff;color:var(--lu-txt);font:400 1.08rem/1.75 var(--lu-bd);overflow-x:hidden}
img{max-width:100%;height:auto;display:block}
a{color:var(--lu-cob);text-underline-offset:3px}
h1,h2,h3,h4{font-family:var(--lu-hd);color:var(--lu-ink);line-height:1.18;letter-spacing:-.01em}
h2{font-size:clamp(1.75rem,3.2vw,2.5rem);font-weight:800;margin:0 0 .8rem}
h3{font-size:1.3rem;font-weight:700;margin:0 0 .5rem}
p{margin:0 0 1rem}
.lu-skip{position:absolute;left:-999px;top:0;background:var(--lu-ink);color:#fff;padding:.6rem 1rem;z-index:99}
.lu-skip:focus{left:8px}
.lu-wrap{max-width:var(--lu-w);margin:0 auto;padding:0 28px}

/* scroll-math reveal: JS writes --sy on <html> and --at on each block; CSS does the rest */
.lu-math [data-in]{--k:clamp(0,calc((var(--sy,99999) - var(--at,0) + 70) / 150),1);opacity:var(--k);transform:translateY(calc((1 - var(--k)) * 28px))}
@media (prefers-reduced-motion:reduce){.lu-math [data-in]{opacity:1;transform:none}}

/* header */
.lu-head{position:sticky;top:0;z-index:50;background:rgba(255,255,255,.94);backdrop-filter:blur(10px);box-shadow:0 1px 0 var(--lu-line)}
.lu-bar{max-width:1440px;margin:0 auto;padding:12px 28px;display:flex;align-items:center;gap:22px}
.lu-brand{display:flex;align-items:center;gap:10px;text-decoration:none;font:800 1.35rem/1 var(--lu-hd);color:var(--lu-ink);flex:none}
.lu-brand i{font-style:normal;color:var(--lu-cob)}
.lu-links{display:flex;gap:4px;margin-left:auto}
.lu-links a{text-decoration:none;color:var(--lu-ink);font-weight:600;font-size:1rem;padding:.45rem .6rem;border-radius:8px;white-space:nowrap}
.lu-links a:hover,.lu-links a[aria-current]{color:var(--lu-cob);background:var(--lu-sky)}
.lu-go{display:inline-flex;align-items:center;justify-content:center;gap:.5rem;text-decoration:none;background:var(--lu-apr);color:#fff;font:700 1.02rem/1 var(--lu-hd);padding:1rem 1.5rem;border-radius:999px;white-space:nowrap;box-shadow:0 10px 24px -12px color-mix(in srgb,var(--lu-apr) 90%,transparent);transition:transform .2s,background .2s}
.lu-go:hover{background:var(--lu-aprD);transform:translateY(-2px)}
.lu-bar>.lu-go{flex:none}
.lu-go.lu-xl{font-size:1.15rem;padding:1.15rem 2rem}
.lu-go.lu-blue{background:var(--lu-cob);box-shadow:0 10px 24px -12px color-mix(in srgb,var(--lu-cob) 90%,transparent)}
.lu-go.lu-blue:hover{background:var(--lu-cobD)}
.lu-go.lu-full{display:flex;width:100%}
.lu-burger{display:none;margin-left:auto;width:50px;height:50px;border:0;border-radius:50%;background:var(--lu-sky);color:var(--lu-cob);cursor:pointer;place-items:center}
.lu-burger .x{display:none}
.lu-burger[aria-pressed="true"] .x{display:block}
.lu-burger[aria-pressed="true"] .m{display:none}
/* circle-reveal drawer opened by aria-pressed via :has() */
.lu-drawer{position:fixed;inset:74px 0 0 0;z-index:49;background:#fff;overflow-y:auto;padding:22px 28px 40px;clip-path:circle(0 at calc(100% - 52px) -30px);visibility:hidden;transition:clip-path .55s cubic-bezier(.6,0,.2,1),visibility 0s .55s}
body:has(.lu-burger[aria-pressed="true"]) .lu-drawer{clip-path:circle(160vmax at calc(100% - 52px) -30px);visibility:visible;transition:clip-path .55s cubic-bezier(.6,0,.2,1),visibility 0s}
body:has(.lu-burger[aria-pressed="true"]){overflow:hidden}
.lu-drawer nav{display:grid;grid-template-columns:1fr 1fr;gap:4px 18px;max-width:640px;margin:0 auto}
.lu-drawer nav a{color:var(--lu-ink);text-decoration:none;font:600 1.12rem/1.3 var(--lu-hd);padding:.85rem 0;border-bottom:1px solid var(--lu-line)}
.lu-drawer .lu-go{grid-column:1/-1;margin-top:1.2rem;color:#fff;border:0}

/* hero */
.lu-hero{background:radial-gradient(900px 500px at 85% 10%,color-mix(in srgb,var(--lu-cob) 13%,#fff) 0,rgba(230,237,255,0) 70%),radial-gradient(700px 420px at 0% 100%,var(--lu-peach) 0,rgba(255,244,234,0) 70%),#fff;padding:56px 0 72px}
.lu-hgrid{display:grid;grid-template-columns:1.08fr .92fr;grid-template-areas:"say bottle" "say hub";grid-template-rows:auto 1fr;gap:28px 56px;align-items:start}
.lu-say{grid-area:say}
.lu-bottle{grid-area:bottle;position:relative;min-height:440px;display:grid;place-items:center}
.lu-hub{grid-area:hub}
.lu-chip{display:inline-flex;align-items:center;gap:.5rem;background:var(--lu-mint);color:var(--lu-leaf);font-weight:700;padding:.4rem .95rem;border-radius:999px;font-size:.98rem}
.lu-say h1{font-size:clamp(2.3rem,4.6vw,3.6rem);font-weight:900;margin:.9rem 0 1rem;line-height:1.08}
.lu-say h1 span{display:block;color:var(--lu-cob);font-weight:800}
.lu-intro{font-size:1.2rem;color:var(--lu-mut);margin-bottom:1.6rem}
.lu-qf{margin:0 0 1.5rem;padding:1.4rem 1.6rem;background:#fff;border-radius:22px;box-shadow:0 24px 60px -40px rgba(22,32,58,.55);display:grid;grid-template-columns:1fr 1fr;gap:.9rem 1.6rem}
.lu-qf-h{grid-column:1/-1;font:800 1.15rem/1 var(--lu-hd);color:var(--lu-ink);display:flex;align-items:center;gap:.55rem}
.lu-qf-h::before{content:"";width:12px;height:12px;border-radius:50%;background:var(--lu-apr);box-shadow:0 0 0 5px var(--lu-peach)}
.lu-qf dt{font-size:.82rem;text-transform:uppercase;letter-spacing:.08em;color:var(--lu-cob);font-weight:700}
.lu-qf dd{margin:0;font-weight:600;color:var(--lu-ink);line-height:1.45}
.lu-ticks{list-style:none;padding:0;margin:0 0 1.7rem;display:grid;grid-template-columns:1fr 1fr;gap:.55rem 1.2rem}
.lu-ticks li{position:relative;padding-left:2rem;font-weight:600;color:var(--lu-ink)}
.lu-ticks li::before{content:"";position:absolute;left:0;top:.32em;width:1.25rem;height:1.25rem;border-radius:50%;background:var(--lu-leaf) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='3.2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='m6 12 4 4 8-8'/%3E%3C/svg%3E") center/70% no-repeat}
.lu-btns{display:flex;flex-wrap:wrap;gap:14px;align-items:center}
.lu-ghost{display:inline-flex;align-items:center;font:700 1.02rem/1 var(--lu-hd);color:var(--lu-cob);text-decoration:none;padding:1rem 1.4rem;border-radius:999px;background:var(--lu-sky)}
.lu-ghost:hover{background:color-mix(in srgb,var(--lu-cob) 16%,#fff)}
.lu-nums{list-style:none;padding:0;margin:2rem 0 0;display:flex;flex-wrap:wrap;gap:2.4rem}
.lu-nums b{display:block;font:900 2rem/1 var(--lu-hd);color:var(--lu-ink)}
.lu-nums b em{font-style:normal;color:var(--lu-apr)}
.lu-nums span{color:var(--lu-mut);font-size:.98rem}
.lu-bottle::before{content:"";position:absolute;width:min(420px,88%);aspect-ratio:1;border-radius:50%;background:radial-gradient(circle,#fff 0 38%,color-mix(in srgb,var(--lu-cob) 15%,#fff) 39% 100%);box-shadow:0 0 0 18px color-mix(in srgb,var(--lu-cob) 15%,transparent),0 0 0 36px color-mix(in srgb,var(--lu-cob) 8%,transparent)}
.lu-bottle>img{position:relative;width:min(400px,84%);filter:drop-shadow(0 28px 34px rgba(22,32,58,.22));animation:lu-float 6s ease-in-out infinite}
@keyframes lu-float{50%{transform:translateY(-12px)}}
.lu-waves{position:absolute;inset:0;pointer-events:none}
.lu-waves path{fill:none;stroke:var(--lu-cob);stroke-width:2;stroke-linecap:round;opacity:.28;stroke-dasharray:8 14;animation:lu-flow 5s linear infinite}
.lu-waves path:nth-child(2){stroke:var(--lu-apr);animation-duration:7s}
.lu-waves path:nth-child(3){stroke:var(--lu-leaf);animation-duration:9s}
@keyframes lu-flow{to{stroke-dashoffset:-220}}
.lu-pins{position:absolute;inset:0}
.lu-pin{position:absolute;display:flex;align-items:center;gap:.6rem;background:#fff;padding:.6rem .95rem .6rem .6rem;border-radius:16px;box-shadow:0 16px 36px -20px rgba(22,32,58,.55);line-height:1.2;animation:lu-bob 5s ease-in-out infinite}
.lu-pin i{width:38px;height:38px;border-radius:12px;display:grid;place-items:center;background:var(--lu-sky);color:var(--lu-cob);flex:none}
.lu-pin b{display:block;font-family:var(--lu-hd);color:var(--lu-ink);font-size:1rem}
.lu-pin small{color:var(--lu-mut);font-size:.86rem}
.lu-p1{top:4%;left:0}
.lu-p2{top:16%;right:0;animation-delay:-1.2s}
.lu-p2 i{background:var(--lu-peach);color:var(--lu-apr)}
.lu-p3{bottom:20%;left:-2%;animation-delay:-2.4s}
.lu-p3 i{background:var(--lu-mint);color:var(--lu-leaf)}
.lu-p4{bottom:4%;right:4%;background:var(--lu-cob);animation-delay:-3.4s}
.lu-p4 b,.lu-p4 small{color:#fff}
.lu-p4 i{background:rgba(255,255,255,.18);color:#fff}
@keyframes lu-bob{50%{transform:translateY(-7px)}}
.lu-hub{position:relative;background:#fff;border-radius:26px;padding:2.1rem 1.4rem 1.2rem;box-shadow:0 30px 70px -46px rgba(22,32,58,.6);text-align:center}
.lu-ribbon{position:absolute;top:-16px;right:22px;background:var(--lu-leaf);color:#fff;font:800 .9rem/1 var(--lu-hd);padding:.62rem 1rem;border-radius:10px 10px 10px 0;box-shadow:0 10px 20px -10px rgba(62,154,85,.9)}
.lu-hub h3{font-size:1.25rem;margin:0 0 .4rem}
.lu-fan{width:100%;max-width:440px;margin:0 auto;display:block}
.lu-fan .arc{fill:none;stroke:color-mix(in srgb,var(--lu-cob) 17%,#fff);stroke-width:2;stroke-dasharray:4 7}
.lu-fan .ray{stroke:var(--lu-cob);stroke-width:2.5;stroke-dasharray:6 6;animation:lu-flow 4s linear infinite}
.lu-fan .mid{fill:var(--lu-cob)}
.lu-fan .mid2{fill:none;stroke:var(--lu-cob);stroke-width:2;opacity:.35;transform-origin:220px 236px;animation:lu-ping 2.8s ease-out infinite}
@keyframes lu-ping{from{transform:scale(1);opacity:.5}to{transform:scale(1.5);opacity:0}}
.lu-fan .leafnode{fill:#fff;stroke-width:3}
.lu-fan .n1{stroke:var(--lu-leaf)}
.lu-fan .n2{stroke:var(--lu-apr)}
.lu-fan .n3{stroke:#d9b310}
.lu-fan .nm{font:800 16px var(--lu-hd);fill:var(--lu-ink)}
.lu-fan .rl{font:500 11.5px var(--lu-bd);fill:var(--lu-mut)}
.lu-fan .ct{font:800 14px var(--lu-hd);fill:#fff;letter-spacing:.04em}
.lu-cap{font-size:.9rem;font-style:italic;color:var(--lu-mut);margin:.4rem 0 0}

/* trust strip */
.lu-trust{padding:26px 0;border-bottom:1px solid var(--lu-line)}
.lu-trust .lu-wrap{display:flex;align-items:center;justify-content:center;flex-wrap:wrap;gap:22px 40px}
.lu-trust img{width:140px}
.lu-trust p{max-width:360px;margin:0;color:var(--lu-mut);font-size:.98rem}
.lu-seal{width:112px;height:112px;flex:none}
.lu-seal .o{fill:var(--lu-apr)}
.lu-seal .i{fill:#fff}
.lu-seal .t1{font:900 30px var(--lu-hd);fill:var(--lu-ink)}
.lu-seal .t2{font:800 10.5px var(--lu-hd);fill:var(--lu-ink);letter-spacing:.06em}
.lu-seal .t3{font:700 9px var(--lu-hd);fill:#fff;letter-spacing:.1em}
.lu-seal .spin{transform-origin:60px 60px;animation:lu-turn 26s linear infinite}
@keyframes lu-turn{to{transform:rotate(360deg)}}

/* sections */
.lu-sec{padding:88px 0}
.lu-ice{background:var(--lu-sky)}
.lu-warm{background:var(--lu-peach)}
.lu-fresh{background:var(--lu-mint)}
.lu-head2{max-width:780px;margin:0 0 2.6rem}
.lu-head2.lu-mid{margin:0 auto 2.6rem;text-align:center}
.lu-eyebrow{display:block;font:800 .86rem/1 var(--lu-hd);letter-spacing:.14em;text-transform:uppercase;color:var(--lu-apr);margin-bottom:.8rem}
.lu-head2 p{color:var(--lu-mut);font-size:1.14rem;margin:0}
.lu-split{display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:center}
.lu-split>*{min-width:0}
.lu-roundimg{border-radius:28px}
.lu-link{font:700 1.02rem/1 var(--lu-hd);margin-top:1.4rem}
.lu-link a{text-decoration:none}
.lu-link a::after{content:"  \2192"}

/* wave divider */
.lu-breath{display:block;width:100%;height:56px}
.lu-breath path{fill:none;stroke-width:2.5;stroke-linecap:round;stroke-dasharray:10 12;animation:lu-flow 6s linear infinite}
.lu-breath .w1{stroke:var(--lu-cob);opacity:.4}
.lu-breath .w2{stroke:var(--lu-apr);opacity:.45;animation-direction:reverse}

/* herbs */
.lu-herbs{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(3,1fr);gap:34px}
.lu-herbs>li{min-width:0}
.lu-herbs a{display:block;text-decoration:none;color:inherit}
.lu-herbs img{border-radius:50% 50% 24px 24px;aspect-ratio:1;object-fit:cover;width:100%}
.lu-herbs .no{display:inline-block;margin:1.1rem 0 .3rem;font:800 .85rem/1 var(--lu-hd);letter-spacing:.1em;color:var(--lu-cob);text-transform:uppercase}
.lu-herbs h3{font-size:1.45rem}
.lu-herbs p{color:var(--lu-mut);margin:0}
.lu-herbs .rd{display:inline-block;margin-top:.7rem;font-weight:700;color:var(--lu-cob)}

/* serving grid: 100 dots = 100 servings */
.lu-dose{display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:center;margin-top:72px}
.lu-dose>*{min-width:0}
.lu-dots{display:grid;grid-template-columns:repeat(10,1fr);gap:9px;max-width:400px}
.lu-dots span{aspect-ratio:1;border-radius:50%;background:color-mix(in srgb,var(--lu-cob) 18%,#fff);animation:lu-fill .5s both}
.lu-dots span:nth-child(-n+30){background:var(--lu-cob)}
.lu-dots span:nth-child(n+31):nth-child(-n+60){background:color-mix(in srgb,var(--lu-cob) 70%,#fff)}
@keyframes lu-fill{from{transform:scale(.2);opacity:0}}
.lu-dkey{display:flex;flex-wrap:wrap;gap:.6rem 1.4rem;margin-top:1rem;color:var(--lu-mut);font-size:.95rem}
.lu-dkey i{display:inline-block;width:14px;height:14px;border-radius:50%;margin-right:.4rem;vertical-align:-2px}
.lu-facts img{border-radius:18px;box-shadow:0 20px 50px -36px rgba(22,32,58,.6)}

/* routine */
.lu-routine{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(4,1fr);gap:26px;counter-reset:lr}
.lu-routine>li{counter-increment:lr;position:relative;padding-top:4.4rem;min-width:0}
.lu-routine>li::before{content:counter(lr);position:absolute;top:0;left:0;width:3.3rem;height:3.3rem;border-radius:50%;display:grid;place-items:center;background:var(--lu-cob);color:#fff;font:900 1.35rem/1 var(--lu-hd)}
.lu-routine>li:nth-child(even)::before{background:var(--lu-apr)}
.lu-routine>li::after{content:"";position:absolute;top:1.65rem;left:4rem;right:-14px;border-top:2px dashed color-mix(in srgb,var(--lu-cob) 22%,#fff)}
.lu-routine>li:last-child::after{display:none}
.lu-routine p{color:var(--lu-mut);margin:0}

/* timeline curve */
.lu-curve{margin-top:64px}
.lu-curve svg{width:100%;height:auto;display:block}
.lu-curve .base{stroke:var(--lu-line);stroke-width:2}
.lu-curve .area{fill:url(#lu-g)}
.lu-curve .ln{fill:none;stroke:var(--lu-cob);stroke-width:4;stroke-linecap:round;stroke-dasharray:900;stroke-dashoffset:900;animation:lu-draw 2.8s ease forwards}
@keyframes lu-draw{to{stroke-dashoffset:0}}
.lu-curve .dot{fill:#fff;stroke:var(--lu-apr);stroke-width:4}
.lu-curve .wk{font:800 15px var(--lu-hd);fill:var(--lu-ink)}
.lu-curve .ds{font:500 13.5px var(--lu-bd);fill:var(--lu-mut)}
.lu-curve .ax{font:600 12.5px var(--lu-bd);fill:var(--lu-mut)}
.lu-phase{display:none;list-style:none;padding:0;margin:0}
.lu-phase li{padding:.8rem 0 .8rem 1.4rem;border-left:3px solid var(--lu-cob);margin-left:.4rem}
.lu-phase b{display:block;font-family:var(--lu-hd);color:var(--lu-ink)}
.lu-small{font-size:.92rem;color:var(--lu-mut);font-style:italic}

/* benefits */
.lu-gains{display:grid;grid-template-columns:repeat(3,1fr);gap:40px 44px}
.lu-gains>div{min-width:0}
.lu-gains .ic{width:56px;height:56px;border-radius:18px;display:grid;place-items:center;background:#fff;color:var(--lu-cob);box-shadow:0 14px 30px -20px color-mix(in srgb,var(--lu-cob) 70%,transparent);margin-bottom:1rem}
.lu-gains>div:nth-child(3n+2) .ic{color:var(--lu-apr)}
.lu-gains>div:nth-child(3n) .ic{color:var(--lu-leaf)}
.lu-gains p{color:var(--lu-mut);margin:0}
.lu-meterbox{margin-top:64px;display:grid;grid-template-columns:.9fr 1.1fr;gap:48px;align-items:center}
.lu-meterbox>*{min-width:0}
.lu-meterbox img{border-radius:24px}
.lu-axis{list-style:none;padding:0;margin:0;display:grid;gap:1.3rem}
.lu-axis li span{display:flex;justify-content:space-between;font-weight:700;color:var(--lu-ink);margin-bottom:.4rem}
.lu-axis li i{display:block;height:12px;border-radius:12px;background:#fff;overflow:hidden}
.lu-axis li u{display:block;height:100%;width:var(--w);border-radius:12px;background:linear-gradient(90deg,var(--lu-cob),color-mix(in srgb,var(--lu-cob) 70%,#fff));animation:lu-bar 2s cubic-bezier(.2,.8,.2,1) both}
.lu-axis li:nth-child(even) u{background:linear-gradient(90deg,var(--lu-apr),color-mix(in srgb,var(--lu-apr) 60%,#fff))}
@keyframes lu-bar{from{width:0}}

/* reviews */
.lu-voices{display:grid;grid-template-columns:repeat(3,1fr);gap:30px}
.lu-voice{background:#fff;border-radius:26px;padding:1.8rem;box-shadow:0 26px 60px -44px rgba(22,32,58,.6);min-width:0}
.lu-voice .face{width:76px;height:76px;border-radius:50%;object-fit:cover;box-shadow:0 0 0 4px #fff,0 0 0 6px var(--lu-sky)}
.lu-voice .lu-vh{display:flex;gap:1rem;align-items:center;margin-bottom:1rem}
.lu-voice h3{margin:0;font-size:1.2rem}
.lu-voice .st{margin:0;font-size:.92rem;color:var(--lu-leaf);font-weight:700}
.lu-voice blockquote{margin:0;color:var(--lu-txt);font-size:1.08rem}
.lu-star{color:#f2a60c;letter-spacing:.12em;font-size:1.2rem;margin:0 0 .6rem}
.lu-star s{text-decoration:none;color:#d8dce6}
.lu-score{margin-top:42px;display:grid;grid-template-columns:auto 1fr 1fr;gap:44px;align-items:start}
.lu-score>*{min-width:0}
.lu-bigrate{font:900 4.4rem/1 var(--lu-hd);color:var(--lu-ink)}
.lu-score .sm{color:var(--lu-mut);margin:0;max-width:16rem;font-size:.96rem}
.lu-ours{list-style:none;padding:0;margin:1rem 0 0;display:grid;gap:.85rem}
.lu-ours li>span{display:flex;justify-content:space-between;font-weight:600}
.lu-ours li>span b{color:var(--lu-cob)}
.lu-ours li>i{display:block;height:9px;background:#fff;border-radius:9px;overflow:hidden;margin-top:.3rem}
.lu-ours li>i>u{display:block;height:100%;width:var(--w);background:var(--lu-cob);border-radius:9px;animation:lu-bar 1.8s both}
.lu-loves{list-style:none;padding:0;margin:1rem 0 0;display:grid;gap:.6rem}
.lu-loves li{padding-left:1.8rem;position:relative;font-weight:600;color:var(--lu-ink)}
.lu-loves li::before{content:"\2665";position:absolute;left:0;color:var(--lu-apr)}
.lu-cta2{text-align:center;margin-top:52px}
.lu-cta2 h3{font-size:1.6rem;margin-bottom:1.1rem}
.lu-cta2 p{margin:1rem 0 0;font-weight:700}

/* pricing */
.lu-offers{display:grid;grid-template-columns:1fr 1.08fr 1fr;gap:26px;align-items:center}
.lu-offer{position:relative;background:#fff;border-radius:28px;padding:2.2rem 1.6rem 1.8rem;text-align:center;box-shadow:0 26px 60px -44px rgba(22,32,58,.6);min-width:0}
.lu-offer.lu-star6{padding:2.8rem 1.8rem 2.2rem;box-shadow:0 0 0 3px var(--lu-cob),0 36px 80px -40px color-mix(in srgb,var(--lu-cob) 60%,transparent)}
.lu-offer .flag{position:absolute;top:-16px;left:50%;transform:translateX(-50%);background:var(--lu-ink);color:#fff;font:800 .85rem/1 var(--lu-hd);padding:.55rem 1.1rem;border-radius:999px;white-space:nowrap}
.lu-offer.lu-star6 .flag{background:var(--lu-cob)}
.lu-offer h3{font-size:1.6rem;margin:0}
.lu-offer .sup{color:var(--lu-mut);margin:0 0 .6rem}
.lu-offer img{width:min(230px,100%);margin:0 auto .6rem}
.lu-offer .per{font:900 3.3rem/1 var(--lu-hd);color:var(--lu-ink);margin:.3rem 0}
.lu-offer .per small{font-size:1rem;font-weight:600;color:var(--lu-mut)}
.lu-offer .tot{margin:0;font-weight:700}
.lu-offer .tot s{color:var(--lu-mut);font-weight:500;margin-left:.4rem}
.lu-offer .ship{margin:.2rem 0 .4rem;color:var(--lu-leaf);font-weight:700}
.lu-offer .gift{margin:0 0 1.2rem;color:var(--lu-apr);font-weight:700}
.lu-offer .nog{margin:0 0 1.2rem;color:var(--lu-mut)}
.lu-perbar{margin-top:60px;max-width:820px;margin-left:auto;margin-right:auto}
.lu-perbar h3{text-align:center}
.lu-perbar ul{list-style:none;padding:0;margin:1.2rem 0 0;display:grid;gap:.9rem}
.lu-perbar li{display:grid;grid-template-columns:120px 1fr;gap:16px;align-items:center;font-weight:700;color:var(--lu-ink)}
.lu-perbar li i{display:block;height:44px;border-radius:12px;background:var(--lu-sky);overflow:hidden}
.lu-perbar li u{display:flex;align-items:center;height:100%;width:var(--w);padding-left:14px;color:#fff;text-decoration:none;font-style:normal;background:linear-gradient(90deg,var(--lu-cob),color-mix(in srgb,var(--lu-cob) 80%,#fff));border-radius:12px;white-space:nowrap;animation:lu-bar 2.2s cubic-bezier(.2,.8,.2,1) both}
.lu-perbar li:last-child u{background:linear-gradient(90deg,var(--lu-leaf),#68bb7c)}
.lu-center{text-align:center;margin-top:1.2rem}

/* bonuses */
.lu-gifts{display:grid;grid-template-columns:repeat(3,1fr);gap:34px}
.lu-gifts>div{min-width:0}
.lu-book{width:120px;height:150px;display:block;margin-bottom:1.2rem}
.lu-book .cv{fill:var(--lu-cob)}
.lu-book .sp{fill:var(--lu-cobD)}
.lu-book .pg{fill:#fff}
.lu-book .tx{font:800 11px var(--lu-hd);fill:#fff}
.lu-gifts>div:nth-child(2) .cv{fill:var(--lu-apr)}
.lu-gifts>div:nth-child(2) .sp{fill:var(--lu-aprD)}
.lu-gifts>div:nth-child(3) .cv{fill:var(--lu-leaf)}
.lu-gifts>div:nth-child(3) .sp{fill:#2c7340}
.lu-gifts .val{display:inline-block;font-weight:800;color:var(--lu-apr);font-size:.92rem;text-transform:uppercase;letter-spacing:.08em}
.lu-gifts p{color:var(--lu-mut)}

/* guarantee */
.lu-promise{display:grid;grid-template-columns:auto 1fr;gap:56px;align-items:center}
.lu-promise>*{min-width:0}
.lu-promise .lu-seal{width:240px;height:240px}

/* journal */
.lu-posts{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(3,1fr);gap:40px 36px}
.lu-posts>li{min-width:0}
.lu-posts a{display:block;text-decoration:none;color:inherit;padding-top:1.1rem;border-top:3px solid var(--lu-cob)}
.lu-posts>li:nth-child(3n+2) a{border-top-color:var(--lu-apr)}
.lu-posts>li:nth-child(3n) a{border-top-color:var(--lu-leaf)}
.lu-posts .rt{font-size:.9rem;font-weight:700;color:var(--lu-mut);text-transform:uppercase;letter-spacing:.08em}
.lu-posts h3{margin:.4rem 0 .5rem;font-size:1.3rem}
.lu-posts p{color:var(--lu-mut);margin:0}

/* faq */
.lu-qa{max-width:900px}
.lu-qa details{border-bottom:1px solid color-mix(in srgb,var(--lu-cob) 17%,#fff)}
.lu-qa summary{cursor:pointer;list-style:none;font:700 1.18rem/1.4 var(--lu-hd);color:var(--lu-ink);padding:1.25rem 3rem 1.25rem 0;position:relative}
.lu-qa summary::-webkit-details-marker{display:none}
.lu-qa summary::after{content:"+";position:absolute;right:0;top:50%;transform:translateY(-50%);width:2.1rem;height:2.1rem;border-radius:50%;display:grid;place-items:center;background:#fff;color:var(--lu-cob);font-size:1.4rem;transition:transform .3s}
.lu-qa details[open] summary::after{transform:translateY(-50%) rotate(45deg)}
.lu-qa details>div{padding:0 0 1.2rem;color:var(--lu-mut)}
.lu-search{max-width:900px;margin:0 0 1.6rem}
.lu-search label{display:block;font-weight:700;color:var(--lu-ink);margin-bottom:.4rem}
.lu-search input{width:100%;font:inherit;padding:.95rem 1.2rem;border-radius:14px;border:2px solid color-mix(in srgb,var(--lu-cob) 17%,#fff);background:#fff}
.lu-search input:focus{outline:none;border-color:var(--lu-cob)}

/* closing */
.lu-close{padding:96px 0;background:linear-gradient(180deg,#fff 0,var(--lu-sky) 100%)}
.lu-cgrid{display:grid;grid-template-columns:1.1fr .9fr;gap:56px;align-items:center}
.lu-cgrid>*{min-width:0}
.lu-cgrid ul{list-style:none;padding:0;margin:0 0 1.6rem;display:grid;grid-template-columns:1fr 1fr;gap:.6rem 1rem}
.lu-cgrid li{font-weight:700;color:var(--lu-ink);padding-left:1.6rem;position:relative}
.lu-cgrid li::before{content:"";position:absolute;left:0;top:.5em;width:.75rem;height:.75rem;border-radius:3px;background:var(--lu-apr);transform:rotate(45deg)}
.lu-fine{font-size:.92rem;color:var(--lu-mut);margin-top:1rem}
.lu-strip{padding:62px 0;background:var(--lu-cob);background:linear-gradient(120deg,var(--lu-sky),var(--lu-peach))}
.lu-strip .lu-wrap{display:flex;align-items:center;justify-content:space-between;gap:24px;flex-wrap:wrap}
.lu-strip h2{margin:0;font-size:clamp(1.5rem,2.6vw,2.1rem)}

/* inner pages */
.lu-pagehead{padding:56px 0 46px;background:linear-gradient(180deg,var(--lu-sky),#fff)}
.lu-crumbs{font-size:.95rem;color:var(--lu-mut);margin-bottom:1rem}
.lu-crumbs a{color:var(--lu-mut)}
.lu-pagehead h1{font-size:clamp(2.1rem,4vw,3.1rem);font-weight:900;margin:0 0 .6rem}
.lu-pagehead .lede{font-size:1.2rem;color:var(--lu-mut);margin:0;max-width:760px}
.lu-prose{max-width:800px}
.lu-prose h2{font-size:1.7rem;margin:2.2rem 0 .7rem}
.lu-prose h2:first-child{margin-top:0}
.lu-prose ul,.lu-prose ol{padding-left:1.3rem}
.lu-prose li{margin-bottom:.5rem}
.lu-twocol{display:grid;grid-template-columns:1fr 300px;gap:56px;align-items:start}
.lu-twocol>*{min-width:0}
.lu-aside{position:sticky;top:100px;background:var(--lu-sky);border-radius:22px;padding:1.5rem 1.6rem}
.lu-aside h4{margin:0 0 .6rem;font-size:1.05rem}
.lu-aside ul{list-style:none;padding:0;margin:0 0 1.2rem}
.lu-aside li{padding:.35rem 0}
.lu-aside dl{margin:0 0 1.2rem}
.lu-aside dt{font-size:.82rem;text-transform:uppercase;letter-spacing:.08em;color:var(--lu-cob);font-weight:700}
.lu-aside dd{margin:0 0 .7rem;font-weight:600;color:var(--lu-ink)}
.lu-nextprev{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;margin-top:2.6rem;padding-top:1.4rem;border-top:1px solid var(--lu-line)}
.lu-nextprev a{font-weight:700;text-decoration:none}

/* footer */
.lu-foot{padding:70px 0 120px;background:color-mix(in srgb,var(--lu-cob) 4%,#fff);color:var(--lu-mut);font-size:.98rem}
.lu-fgrid{display:grid;grid-template-columns:1.5fr 1fr 1fr 1fr;gap:40px}
.lu-fgrid>*{min-width:0}
.lu-foot h4{margin:0 0 .8rem;font-size:1.05rem}
.lu-foot ul{list-style:none;padding:0;margin:0}
.lu-foot li{padding:.25rem 0}
.lu-foot ul a{color:var(--lu-txt);text-decoration:none}
.lu-foot ul a:hover{color:var(--lu-cob)}
.lu-foot .lu-brand{margin-bottom:1rem}
.lu-legal{margin-top:46px;padding-top:26px;border-top:1px solid var(--lu-line);font-size:.92rem}

/* mobile dock */
.lu-dock{position:fixed;left:12px;right:12px;bottom:12px;z-index:40;display:none;align-items:center;justify-content:space-between;gap:12px;background:#fff;border-radius:18px;padding:.7rem .8rem .7rem 1.1rem;box-shadow:0 20px 50px -20px rgba(22,32,58,.55);transform:translateY(140%);transition:transform .35s}
.lu-dock[data-up]{transform:none}
.lu-dock b{display:block;font-family:var(--lu-hd);color:var(--lu-ink);line-height:1.2}
.lu-dock small{color:var(--lu-mut)}
.lu-dock .lu-go{padding:.85rem 1.2rem}

@media (max-width:1360px){
  .lu-links{display:none}
  .lu-burger{display:grid}
  .lu-bar>.lu-go{margin-left:0}
}
@media (max-width:1060px){
  .lu-hgrid{grid-template-columns:1fr 1fr;gap:28px 36px}
  .lu-ticks{grid-template-columns:1fr}
  .lu-gains,.lu-posts{grid-template-columns:1fr 1fr}
  .lu-routine{grid-template-columns:1fr 1fr;row-gap:40px}
  .lu-routine>li::after{display:none}
  .lu-score{grid-template-columns:1fr 1fr}
  .lu-score>:first-child{grid-column:1/-1}
  .lu-twocol{grid-template-columns:1fr}
  .lu-aside{position:static}
  .lu-fgrid{grid-template-columns:1fr 1fr}
}
@media (max-width:860px){
  html{font-size:18px}
  .lu-hgrid{grid-template-columns:1fr;grid-template-areas:"bottle" "say" "hub"}
  .lu-bottle{min-height:0;padding:10px 0 0}
  .lu-pins{position:static;display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:22px}
  .lu-pin{position:static;animation:none}
  .lu-bottle{display:block}
  .lu-bottle::before{left:50%;top:0;transform:translateX(-50%);width:min(340px,86%)}
  .lu-bottle>img{margin:0 auto;width:min(320px,80%)}
  .lu-split,.lu-dose,.lu-meterbox,.lu-cgrid,.lu-promise{grid-template-columns:1fr;gap:36px}
  .lu-herbs,.lu-voices,.lu-gifts{grid-template-columns:1fr}
  .lu-herbs img{max-width:420px}
  .lu-offers{grid-template-columns:1fr;max-width:460px;margin:0 auto;row-gap:34px}
  .lu-curve svg{display:none}
  .lu-phase{display:block}
  .lu-sec{padding:64px 0}
  .lu-dock{display:flex}
  .lu-promise .lu-seal{width:180px;height:180px}
}
@media (max-width:600px){
  .lu-wrap,.lu-bar{padding-left:16px;padding-right:16px}
  .lu-bar>.lu-go{display:none}
  .lu-drawer{inset:74px 0 0 0;padding:16px}
  .lu-drawer nav{grid-template-columns:1fr}
  .lu-qf{grid-template-columns:1fr;padding:1.2rem}
  .lu-gains,.lu-posts,.lu-routine,.lu-score,.lu-fgrid,.lu-cgrid ul{grid-template-columns:1fr}
  .lu-nums{gap:1.4rem 2rem}
  .lu-perbar li{grid-template-columns:1fr;gap:6px}
  .lu-trust img{width:110px}
  .lu-btns .lu-go,.lu-btns .lu-ghost{width:100%;justify-content:center}
  .lu-strip .lu-go{width:100%}
}

/* ingredient cards (this generator has no per-herb photos) */
.lu-herbs>li{background:#fff;border-radius:26px;padding:1.7rem 1.7rem 1.5rem;box-shadow:0 26px 60px -44px rgba(22,32,58,.6);border-top:4px solid var(--lu-cob)}
.lu-herbs>li:nth-child(3n+2){border-top-color:var(--lu-apr)}
.lu-herbs>li:nth-child(3n){border-top-color:var(--lu-leaf)}
.lu-herbs .no{margin:0 0 .5rem}
.lu-gains h3,.lu-routine h3{font-size:1.25rem}
.lu-routine p{margin:0}
/* generator-added boxes and the shared blog/legal chrome */
.auto-quick-facts{margin-top:32px;padding:20px 24px;background:var(--lu-sky);border-radius:18px;font-style:normal}
.auto-quick-facts h3{font-size:1.2rem}
.wrap{max-width:var(--lu-w);margin:0 auto;padding:0 28px}
.wrap h1,.wrap h2,.wrap h3{margin-top:1.6em}
.wrap ul,.wrap ol{padding-left:1.3rem}
.wrap li{margin-bottom:.45rem}
.grid.g3{display:grid;grid-template-columns:repeat(3,1fr);gap:28px}
.card{background:#fff;border-radius:22px;padding:1.5rem;box-shadow:0 26px 60px -44px rgba(22,32,58,.6);border-top:4px solid var(--lu-cob)}
.card h4{font:700 1.2rem/1.3 var(--lu-hd);color:var(--lu-ink);margin:0 0 .5rem}
.card p{color:var(--lu-mut)}
.lu-bannerx{background:var(--lu-cobD)}
.lu-offer .lu-go{white-space:normal;text-align:center;line-height:1.25;padding:.95rem 1rem}
.lu-btns .lu-go,.lu-cta2 .lu-go{white-space:normal;text-align:center;line-height:1.25}
@media (max-width:860px){.grid.g3{grid-template-columns:1fr}.wrap{padding:0 16px}}

</style>
</head>
<body>
<a class="lu-skip" href="#main">Skip to content</a>
<div class="lu-head"><div class="lu-bar">
<a class="lu-brand" href="index.html" aria-label="__BRAND__ home"><span>__BRAND__</span></a>
<nav class="lu-links" aria-label="Main"><a href="what-is-product.html">What Is __BRAND__</a><a href="how-it-works.html">How It Works</a><a href="ingredients.html">Ingredients</a><a href="benefits.html">Benefits</a><a href="reviews.html">Reviews</a><a href="faq.html">FAQ</a><a href="blog/index.html">Blog</a></nav>
<a class="lu-go" href="__AFFILIATE__" target="_blank" rel="noopener sponsored">__CTA_HEADER__</a>
<button class="lu-burger" type="button" aria-pressed="false" aria-controls="lu-drawer" aria-label="Open menu"><span class="m"><svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg></span><span class="x"><svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg></span></button>
</div></div>
<div class="lu-drawer" id="lu-drawer"><nav aria-label="Mobile"><a href="index.html">Home</a><a href="what-is-product.html">What Is __BRAND__</a><a href="how-it-works.html">How It Works</a><a href="ingredients.html">Ingredients</a><a href="benefits.html">Benefits</a><a href="reviews.html">Reviews</a><a href="faq.html">FAQ</a><a href="blog/index.html">Blog</a><a class="lu-go lu-full" href="__AFFILIATE__" target="_blank" rel="noopener sponsored">__CTA_HEADER__</a></nav></div>

<header class="lu-hero"><div class="lu-wrap lu-hgrid">
<div class="lu-say">
<span class="lu-chip"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 19c0-8 6-14 15-14 0 9-6 15-14 15"/><path d="M5 19 13 11"/></svg> __CATEGORY_TITLE__</span>
<h1>__H1_HTML__</h1>
<p class="lu-intro">__HERO_DESC__</p>
<dl class="lu-qf"><div class="lu-qf-h">Quick Facts</div>
<div><dt>Category</dt><dd>__CATEGORY__</dd></div>
<div><dt>Key Ingredients</dt><dd>__KEY_ING__</dd></div>
<div><dt>Daily Serving</dt><dd>__SERVING_DAILY__</dd></div>
<div><dt>Per Bottle</dt><dd>__SERVING_PER_BOTTLE__</dd></div>
<div><dt>Guarantee</dt><dd>__GUARANTEE_DAYS__ days, money back</dd></div>
<div><dt>Price</dt><dd>From __PRICE_LOW__ per bottle</dd></div></dl>
<ul class="lu-ticks"><li>__CHECK1__</li><li>__CHECK2__</li><li>__CHECK3__</li><li>__CHECK4__</li></ul>
<div class="lu-btns"><a class="lu-go lu-xl" href="__AFFILIATE__" target="_blank" rel="noopener sponsored">__CTA_HERO__</a><a class="lu-ghost" href="how-it-works.html">See how it works</a></div>
<ul class="lu-nums"><li><b>__PRICE_LOW__</b><span>best per bottle</span></li><li><b>__GUARANTEE_DAYS__</b><span>day guarantee</span></li><li><b>__N_ING__</b><span>named ingredients</span></li></ul>
</div>
<div class="lu-bottle"><svg class="lu-waves" viewBox="0 0 500 460" preserveAspectRatio="none" aria-hidden="true"><path d="M0 120 C 120 80, 200 160, 320 110 S 460 90, 500 130"/><path d="M0 250 C 140 210, 220 300, 340 240 S 470 230, 500 270"/><path d="M0 370 C 110 340, 230 410, 330 360 S 460 350, 500 390"/></svg>
<img src="assets/images/hero.png" width="900" height="900" alt="__BRAND__ product" loading="eager">
<div class="lu-pins"><span class="lu-pin lu-p1"><i><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 9h6v12H9z"/><path d="M10 9V6h4v3M12 6V3h4"/><path d="M19 4h.01M21 6h.01M19 8h.01"/></svg></i><span><b>__FACT2_NUM__</b><small>daily serving</small></span></span><span class="lu-pin lu-p2"><i><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 21V4h11l-2 4 2 4H5"/></svg></i><span><b>Made in USA</b><small>quality standards</small></span></span><span class="lu-pin lu-p3"><i><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 19c0-8 6-14 15-14 0 9-6 15-14 15"/><path d="M5 19 13 11"/></svg></i><span><b>__N_ING__ ingredients</b><small>named individually</small></span></span><span class="lu-pin lu-p4"><i><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 6h11v10H3zM14 10h4l3 3v3h-7"/><circle cx="7" cy="18" r="2"/><circle cx="17" cy="18" r="2"/></svg></i><span><b>__GUARANTEE_DAYS__-day</b><small>money-back guarantee</small></span></span></div></div>
<div class="lu-hub"><span class="lu-ribbon">__GUARANTEE_DAYS__-Day Money-Back Guarantee</span><h3>What goes into __BRAND__</h3>__HUB_SVG__<p class="lu-cap">Illustrative layout, not a measurement of results</p></div>
</div></header>

<section class="lu-trust"><div class="lu-wrap"><img src="assets/images/badge-usa.png" width="500" height="300" alt="Made in USA" loading="lazy"><img src="assets/images/badge-gmp.png" width="500" height="300" alt="GMP certified" loading="lazy"><img src="assets/images/badge-natural.png" width="500" height="300" alt="Natural ingredients" loading="lazy"><svg class="lu-seal" viewBox="0 0 120 120" role="img" aria-label="__GUARANTEE_DAYS__-day money-back guarantee"><polygon class="o spin" points="120.0,60.0 112.1,66.9 118.0,75.5 108.5,80.1 112.0,90.0 101.7,92.0 102.4,102.4 92.0,101.7 90.0,112.0 80.1,108.5 75.5,118.0 66.9,112.1 60.0,120.0 53.1,112.1 44.5,118.0 39.9,108.5 30.0,112.0 28.0,101.7 17.6,102.4 18.3,92.0 8.0,90.0 11.5,80.1 2.0,75.5 7.9,66.9 0.0,60.0 7.9,53.1 2.0,44.5 11.5,39.9 8.0,30.0 18.3,28.0 17.6,17.6 28.0,18.3 30.0,8.0 39.9,11.5 44.5,2.0 53.1,7.9 60.0,0.0 66.9,7.9 75.5,2.0 80.1,11.5 90.0,8.0 92.0,18.3 102.4,17.6 101.7,28.0 112.0,30.0 108.5,39.9 118.0,44.5 112.1,53.1"/><circle class="i" cx="60" cy="60" r="44"/><text class="t1" x="60" y="62" text-anchor="middle">__GUARANTEE_DAYS__</text><text class="t2" x="60" y="78" text-anchor="middle">DAY MONEY</text><text class="t2" x="60" y="90" text-anchor="middle">BACK</text></svg><p>Quality badges as stated by the brand, plus a __GUARANTEE_DAYS__-day money-back guarantee on every order.</p></div></section>

<main id="main">
<section class="lu-sec" id="what-is"><div class="lu-wrap"><div class="lu-split">
<div data-in><img class="lu-roundimg" src="assets/images/feature-shot.png" width="1000" height="1000" alt="__BRAND__ overview" loading="lazy"></div>
<div data-in><span class="lu-eyebrow">What is __BRAND__</span><h2>A plain-English overview</h2>
<p>__WHATIS_P1__</p><p>__WHATIS_CALLOUT__</p>
<p class="lu-link"><a href="how-it-works.html">See how it works</a></p></div>
</div></div></section>
<svg class="lu-breath" viewBox="0 0 1440 56" preserveAspectRatio="none" aria-hidden="true"><path class="w1" d="M0 28 L0 28.0 L24 36.2 L48 41.3 L72 41.3 L96 36.2 L120 28.0 L144 19.8 L168 14.7 L192 14.7 L216 19.8 L240 28.0 L264 36.2 L288 41.3 L312 41.3 L336 36.2 L360 28.0 L384 19.8 L408 14.7 L432 14.7 L456 19.8 L480 28.0 L504 36.2 L528 41.3 L552 41.3 L576 36.2 L600 28.0 L624 19.8 L648 14.7 L672 14.7 L696 19.8 L720 28.0 L744 36.2 L768 41.3 L792 41.3 L816 36.2 L840 28.0 L864 19.8 L888 14.7 L912 14.7 L936 19.8 L960 28.0 L984 36.2 L1008 41.3 L1032 41.3 L1056 36.2 L1080 28.0 L1104 19.8 L1128 14.7 L1152 14.7 L1176 19.8 L1200 28.0 L1224 36.2 L1248 41.3 L1272 41.3 L1296 36.2 L1320 28.0 L1344 19.8 L1368 14.7 L1392 14.7 L1416 19.8 L1440 28.0"/><path class="w2" d="M0 28 L0 28.0 L24 22.1 L48 18.5 L72 18.5 L96 22.1 L120 28.0 L144 33.9 L168 37.5 L192 37.5 L216 33.9 L240 28.0 L264 22.1 L288 18.5 L312 18.5 L336 22.1 L360 28.0 L384 33.9 L408 37.5 L432 37.5 L456 33.9 L480 28.0 L504 22.1 L528 18.5 L552 18.5 L576 22.1 L600 28.0 L624 33.9 L648 37.5 L672 37.5 L696 33.9 L720 28.0 L744 22.1 L768 18.5 L792 18.5 L816 22.1 L840 28.0 L864 33.9 L888 37.5 L912 37.5 L936 33.9 L960 28.0 L984 22.1 L1008 18.5 L1032 18.5 L1056 22.1 L1080 28.0 L1104 33.9 L1128 37.5 L1152 37.5 L1176 33.9 L1200 28.0 L1224 22.1 L1248 18.5 L1272 18.5 L1296 22.1 L1320 28.0 L1344 33.9 L1368 37.5 L1392 37.5 L1416 33.9 L1440 28.0"/></svg>
<section class="lu-sec lu-ice" id="ingredients"><div class="lu-wrap">
<div class="lu-head2" data-in><span class="lu-eyebrow">The ingredients</span><h2>__ING_HEADING__</h2><p>Every ingredient is listed individually, with what it is and why it is in the formula.</p></div>
<ul class="lu-herbs">__ING_CARD_TEMPLATE__</ul>
</div></section>

<section class="lu-sec" id="how-it-works"><div class="lu-wrap">
<div class="lu-head2" data-in><span class="lu-eyebrow">How it works</span><h2>How __BRAND__ is designed to work</h2><p>__HIW_INTRO__</p></div>
<ol class="lu-routine">__HIW_CARD_TEMPLATE__</ol>
</div></section>
<svg class="lu-breath" viewBox="0 0 1440 56" preserveAspectRatio="none" aria-hidden="true"><path class="w1" d="M0 28 L0 28.0 L24 36.2 L48 41.3 L72 41.3 L96 36.2 L120 28.0 L144 19.8 L168 14.7 L192 14.7 L216 19.8 L240 28.0 L264 36.2 L288 41.3 L312 41.3 L336 36.2 L360 28.0 L384 19.8 L408 14.7 L432 14.7 L456 19.8 L480 28.0 L504 36.2 L528 41.3 L552 41.3 L576 36.2 L600 28.0 L624 19.8 L648 14.7 L672 14.7 L696 19.8 L720 28.0 L744 36.2 L768 41.3 L792 41.3 L816 36.2 L840 28.0 L864 19.8 L888 14.7 L912 14.7 L936 19.8 L960 28.0 L984 36.2 L1008 41.3 L1032 41.3 L1056 36.2 L1080 28.0 L1104 19.8 L1128 14.7 L1152 14.7 L1176 19.8 L1200 28.0 L1224 36.2 L1248 41.3 L1272 41.3 L1296 36.2 L1320 28.0 L1344 19.8 L1368 14.7 L1392 14.7 L1416 19.8 L1440 28.0"/><path class="w2" d="M0 28 L0 28.0 L24 22.1 L48 18.5 L72 18.5 L96 22.1 L120 28.0 L144 33.9 L168 37.5 L192 37.5 L216 33.9 L240 28.0 L264 22.1 L288 18.5 L312 18.5 L336 22.1 L360 28.0 L384 33.9 L408 37.5 L432 37.5 L456 33.9 L480 28.0 L504 22.1 L528 18.5 L552 18.5 L576 22.1 L600 28.0 L624 33.9 L648 37.5 L672 37.5 L696 33.9 L720 28.0 L744 22.1 L768 18.5 L792 18.5 L816 22.1 L840 28.0 L864 33.9 L888 37.5 L912 37.5 L936 33.9 L960 28.0 L984 22.1 L1008 18.5 L1032 18.5 L1056 22.1 L1080 28.0 L1104 33.9 L1128 37.5 L1152 37.5 L1176 33.9 L1200 28.0 L1224 22.1 L1248 18.5 L1272 18.5 L1296 22.1 L1320 28.0 L1344 33.9 L1368 37.5 L1392 37.5 L1416 33.9 L1440 28.0"/></svg>
<section class="lu-sec lu-warm" id="benefits"><div class="lu-wrap">
<div class="lu-head2" data-in><span class="lu-eyebrow">Benefits</span><h2>What __BRAND__ is made to support</h2><p>The areas this formula is designed to support as part of a daily routine.</p></div>
<div class="lu-gains">__BENEFIT_CARD_TEMPLATE__</div>
</div></section>

<section class="lu-sec lu-fresh" id="reviews"><div class="lu-wrap">
<div class="lu-head2 lu-mid" data-in><span class="lu-eyebrow">Customer reviews</span><h2>What __BRAND__ customers say</h2><p>Experiences shared by people using __BRAND__ daily.</p></div>
<div class="lu-voices">__REVIEW_CARD_TEMPLATE__</div>
<div class="lu-cta2" data-in><h3>Ready to start your own routine?</h3><a class="lu-go lu-xl" href="__AFFILIATE__" target="_blank" rel="noopener sponsored">__CTA_AFTERFAQ__</a></div>
</div></section>

<section class="lu-sec" id="pricing"><div class="lu-wrap">
<div class="lu-head2 lu-mid" data-in><span class="lu-eyebrow">Pricing</span><h2>Choose your __BRAND__ bundle</h2><p>The bigger the bundle, the lower the price per bottle.</p></div>
<div class="lu-offers">__PLAN_CARD_TEMPLATE__</div>
<p class="lu-small lu-center">__PRICING_NOTE__</p>
</div></section>

__BONUS_SECTION__

<section class="lu-sec" id="guarantee"><div class="lu-wrap"><div class="lu-promise">
<div data-in><svg class="lu-seal" viewBox="0 0 120 120" role="img" aria-label="__GUARANTEE_DAYS__-day money-back guarantee"><polygon class="o spin" points="120.0,60.0 112.1,66.9 118.0,75.5 108.5,80.1 112.0,90.0 101.7,92.0 102.4,102.4 92.0,101.7 90.0,112.0 80.1,108.5 75.5,118.0 66.9,112.1 60.0,120.0 53.1,112.1 44.5,118.0 39.9,108.5 30.0,112.0 28.0,101.7 17.6,102.4 18.3,92.0 8.0,90.0 11.5,80.1 2.0,75.5 7.9,66.9 0.0,60.0 7.9,53.1 2.0,44.5 11.5,39.9 8.0,30.0 18.3,28.0 17.6,17.6 28.0,18.3 30.0,8.0 39.9,11.5 44.5,2.0 53.1,7.9 60.0,0.0 66.9,7.9 75.5,2.0 80.1,11.5 90.0,8.0 92.0,18.3 102.4,17.6 101.7,28.0 112.0,30.0 108.5,39.9 118.0,44.5 112.1,53.1"/><circle class="i" cx="60" cy="60" r="44"/><text class="t1" x="60" y="62" text-anchor="middle">__GUARANTEE_DAYS__</text><text class="t2" x="60" y="78" text-anchor="middle">DAY MONEY</text><text class="t2" x="60" y="90" text-anchor="middle">BACK</text></svg></div>
<div data-in><span class="lu-eyebrow">Guarantee</span><h2>__GUARANTEE_DAYS__ days to decide</h2><p>__GUARANTEE_TEXT__</p>
<a class="lu-go" href="__AFFILIATE__" target="_blank" rel="noopener sponsored">__CTA_CLOSING__</a></div>
</div></div></section>
<svg class="lu-breath" viewBox="0 0 1440 56" preserveAspectRatio="none" aria-hidden="true"><path class="w1" d="M0 28 L0 28.0 L24 36.2 L48 41.3 L72 41.3 L96 36.2 L120 28.0 L144 19.8 L168 14.7 L192 14.7 L216 19.8 L240 28.0 L264 36.2 L288 41.3 L312 41.3 L336 36.2 L360 28.0 L384 19.8 L408 14.7 L432 14.7 L456 19.8 L480 28.0 L504 36.2 L528 41.3 L552 41.3 L576 36.2 L600 28.0 L624 19.8 L648 14.7 L672 14.7 L696 19.8 L720 28.0 L744 36.2 L768 41.3 L792 41.3 L816 36.2 L840 28.0 L864 19.8 L888 14.7 L912 14.7 L936 19.8 L960 28.0 L984 36.2 L1008 41.3 L1032 41.3 L1056 36.2 L1080 28.0 L1104 19.8 L1128 14.7 L1152 14.7 L1176 19.8 L1200 28.0 L1224 36.2 L1248 41.3 L1272 41.3 L1296 36.2 L1320 28.0 L1344 19.8 L1368 14.7 L1392 14.7 L1416 19.8 L1440 28.0"/><path class="w2" d="M0 28 L0 28.0 L24 22.1 L48 18.5 L72 18.5 L96 22.1 L120 28.0 L144 33.9 L168 37.5 L192 37.5 L216 33.9 L240 28.0 L264 22.1 L288 18.5 L312 18.5 L336 22.1 L360 28.0 L384 33.9 L408 37.5 L432 37.5 L456 33.9 L480 28.0 L504 22.1 L528 18.5 L552 18.5 L576 22.1 L600 28.0 L624 33.9 L648 37.5 L672 37.5 L696 33.9 L720 28.0 L744 22.1 L768 18.5 L792 18.5 L816 22.1 L840 28.0 L864 33.9 L888 37.5 L912 37.5 L936 33.9 L960 28.0 L984 22.1 L1008 18.5 L1032 18.5 L1056 22.1 L1080 28.0 L1104 33.9 L1128 37.5 L1152 37.5 L1176 33.9 L1200 28.0 L1224 22.1 L1248 18.5 L1272 18.5 L1296 22.1 L1320 28.0 L1344 33.9 L1368 37.5 L1392 37.5 L1416 33.9 L1440 28.0"/></svg>
<section class="lu-sec lu-ice" id="faq"><div class="lu-wrap">
<div class="lu-head2" data-in><span class="lu-eyebrow">FAQ</span><h2>__BRAND__ questions, answered</h2><p>Clear answers to what people ask most.</p></div>
<div class="lu-qa" data-in>__FAQ_ROW_TEMPLATE__</div>
</div></section>

<section class="lu-close"><div class="lu-wrap"><div class="lu-cgrid">
<div data-in><span class="lu-eyebrow">Your next step</span><h2>__BRAND__ in your daily routine</h2><p>__FINAL_TEXT__</p>
<ul><li>__CHIP1__</li><li>__CHIP2__</li><li>__CHIP3__</li><li>__CHIP4__</li></ul>
<div class="lu-btns"><a class="lu-go lu-xl" href="__AFFILIATE__" target="_blank" rel="noopener sponsored">__CTA_CLOSING__</a><a class="lu-ghost" href="index.html#pricing">Compare bundles</a></div>
<p class="lu-fine">One-time purchase. Confirm the final total at checkout.</p></div>
<div data-in><img src="assets/images/bottle-6.png" width="1024" height="1024" alt="__BRAND__ six bottle pack" loading="lazy"></div>
</div></div></section>

<section class="lu-strip"><div class="lu-wrap"><h2>Read the __BRAND__ guides and articles</h2><a class="lu-go lu-blue" href="blog/index.html">Visit the blog</a></div></section>
</main>

<footer class="lu-foot"><div class="lu-wrap">
<div class="lu-fgrid">
<div><a class="lu-brand" href="index.html"><span>__BRAND__</span></a><p>An independent informational resource covering __BRAND__ ingredients, benefits, pricing and reviews for __YEAR__.</p></div>
<div><h4>Learn</h4><ul><li><a href="what-is-product.html">What Is __BRAND__</a></li><li><a href="how-it-works.html">How It Works</a></li><li><a href="ingredients.html">Ingredients</a></li><li><a href="benefits.html">Benefits</a></li></ul></div>
<div><h4>Buy</h4><ul><li><a href="index.html#pricing">Pricing</a></li><li><a href="reviews.html">Reviews</a></li><li><a href="faq.html">FAQ</a></li><li><a href="blog/index.html">Blog</a></li></ul></div>
<div><h4>Legal</h4><ul><li><a href="terms.html">Terms of Use</a></li><li><a href="privacy-policy.html">Privacy Policy</a></li><li><a href="disclaimer.html">Disclaimer</a></li><li><a href="refund-policy.html">Refund Policy</a></li><li><a href="contact.html">Contact Us</a></li></ul></div>
</div>
<div class="lu-legal">
<p><strong>Disclaimer:</strong> *These statements have not been evaluated by the Food and Drug Administration. __BRAND__ is a dietary supplement and is not intended to diagnose, treat, cure or prevent any disease. Individual results vary. Follow the label and talk with your doctor if you take medication or have a health condition.</p>
<p><strong>Affiliate disclosure:</strong> This website may earn a commission on purchases made through links to the official __BRAND__ store, at no additional cost to you. We do not make or sell __BRAND__.</p>
<p>&copy; __YEAR__ __BRAND__. All rights reserved. &middot; <a href="sitemap.xml">Sitemap</a></p>
</div></div></footer>

<div class="lu-dock sticky-bar"><span><b>__BRAND__</b><small>__GUARANTEE_DAYS__-day guarantee</small></span><a class="lu-go" href="__AFFILIATE__" target="_blank" rel="noopener sponsored">Order Now</a></div>
<script>
// breathizen-usa.com: reveal is pure CSS math. JS only writes two numbers:
// --sy on <html> (bottom edge of the viewport in page px) and --at on each [data-in] block (its page top).
// The menu is a circle-clip drawer opened by toggling aria-pressed; CSS :has() does the opening.
(function () {
  var html = document.documentElement;
  var blocks = [].slice.call(document.querySelectorAll("[data-in]"));
  function pageTop(el) { var y = 0; while (el) { y += el.offsetTop; el = el.offsetParent; } return y; }
  function measure() { blocks.forEach(function (b) { b.style.setProperty("--at", pageTop(b)); }); }
  var queued = false;
  function sync() { queued = false; html.style.setProperty("--sy", Math.round(scrollY + innerHeight)); }
  function ask() { if (!queued) { queued = true; requestAnimationFrame(sync); } }
  if (blocks.length) {
    measure(); sync();
    html.classList.add("lu-math");
    addEventListener("scroll", ask, { passive: true });
    addEventListener("resize", function () { measure(); ask(); });
    addEventListener("load", function () { measure(); ask(); });
    if ("ResizeObserver" in window) { var t; new ResizeObserver(function () { clearTimeout(t); t = setTimeout(function () { measure(); ask(); }, 120); }).observe(document.body); }
  }

  var btn = document.querySelector(".lu-burger"), drawer = document.querySelector(".lu-drawer");
  function setMenu(on) {
    if (!btn) return;
    btn.setAttribute("aria-pressed", on ? "true" : "false");
    btn.setAttribute("aria-label", on ? "Close menu" : "Open menu");
    if (drawer) drawer.toggleAttribute("inert", !on);
  }
  if (btn && drawer) {
    setMenu(false);
    btn.addEventListener("click", function () { setMenu(btn.getAttribute("aria-pressed") !== "true"); });
    drawer.addEventListener("click", function (e) { if (e.target.closest("a")) setMenu(false); });
    addEventListener("keydown", function (e) { if (e.key === "Escape") setMenu(false); });
    matchMedia("(min-width:1361px)").addEventListener("change", function (m) { if (m.matches) setMenu(false); });
  }

  var dock = document.querySelector(".lu-dock");
  if (dock) addEventListener("scroll", function () { dock.toggleAttribute("data-up", scrollY > 640); }, { passive: true });

  var q = document.getElementById("lu-find");
  if (q) {
    var rows = [].slice.call(document.querySelectorAll(".lu-qa details")), none = document.getElementById("lu-empty");
    q.addEventListener("input", function () {
      var v = q.value.trim().toLowerCase(), n = 0;
      rows.forEach(function (d) { var ok = !v || d.textContent.toLowerCase().indexOf(v) > -1; d.hidden = !ok; if (ok) n++; });
      if (none) none.hidden = n > 0;
    });
  }
})();

</script>
</body>
</html>
