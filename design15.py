"""Design 15: a native design that re-rolls its look for every generated site.

It reuses Design 14's proven markup (so every placeholder and content mapping
keeps working) and applies a random "recipe" on top: fonts, colour mode,
corner radius, card / button / header / hero styles, which sections are
shown in which order, grid column counts, and animations. The recipe is
created once per generation and stored in data['_d15'], so every page of that
site (home, sub-pages, blog, legal) shares the same look.
"""
import random
from bs4 import BeautifulSoup

# (family, css2 weights, heading weight, generic)
HEAD_FONTS=[
 ('Playfair Display','wght@600;700;800',700,'serif'),
 ('Poppins','wght@600;700;800',700,'sans-serif'),
 ('Space Grotesk','wght@500;600;700',700,'sans-serif'),
 ('Outfit','wght@600;700;800',700,'sans-serif'),
 ('Sora','wght@600;700;800',700,'sans-serif'),
 ('Montserrat','wght@600;700;800',800,'sans-serif'),
 ('Merriweather','wght@700;900',700,'serif'),
 ('Lora','wght@600;700',700,'serif'),
 ('Rubik','wght@600;700;800',700,'sans-serif'),
 ('Manrope','wght@600;700;800',800,'sans-serif'),
 ('DM Serif Display','',400,'serif'),
 ('Fraunces','wght@600;700;800',700,'serif'),
 ('Plus Jakarta Sans','wght@600;700;800',800,'sans-serif'),
]
BODY_FONTS=[
 ('Inter','wght@400;500;600','sans-serif'),
 ('DM Sans','wght@400;500;600','sans-serif'),
 ('Nunito Sans','wght@400;600;700','sans-serif'),
 ('Source Sans 3','wght@400;600;700','sans-serif'),
 ('Open Sans','wght@400;600;700','sans-serif'),
 ('Lato','wght@400;700','sans-serif'),
 ('Work Sans','wght@400;500;600','sans-serif'),
 ('Karla','wght@400;500;700','sans-serif'),
]
# (soft, strong, text-on-button) — every pair is light enough for dark text
CTA_PAIRS=[
 ('#FFF197','#F5C242','#0f172a'),('#FFD6A5','#FF9F43','#1a1208'),('#B8F2E6','#2DD4BF','#06231f'),
 ('#FFFFFF','#E2E8F0','#0f172a'),('#FFB4A2','#FF7A59','#2a0d06'),('#D9F99D','#A3E635','#14210a'),
 ('#FBCFE8','#F472B6','#2a0a1a'),('#C7D2FE','#818CF8','#0b1030'),
]
MODES={
 'light':dict(bg='#ffffff',surface='#ffffff',soft='#F8FAFC',text='#1E293B',muted='#64748B',border='#E2E8F0'),
 'cream':dict(bg='#FBF6EE',surface='#FFFDF9',soft='#F4ECDF',text='#2A2118',muted='#7A6B5A',border='#E6DAC8'),
 'tint':dict(bg='#ffffff',surface='#ffffff',soft='#F1F5F9',text='#1E293B',muted='#64748B',border='#E2E8F0'),
 'dark':dict(bg='#0c1322',surface='#141d33',soft='#0f182c',text='#e6ecf8',muted='#9fb0cc',border='#25324f'),
}
# Valid page flows (hero is always first, the closing CTA always last). Each
# keeps pricing after the product has been explained.
FLOWS=[
 ['trust','symptoms','what-is','how','benefits','ingredients','pricing','glance','reviews','guarantee','faq'],
 ['trust','reviews','what-is','benefits','how','ingredients','glance','pricing','guarantee','symptoms','faq'],
 ['symptoms','what-is','benefits','ingredients','how','reviews','pricing','guarantee','glance','trust','faq'],
 ['what-is','how','ingredients','benefits','glance','reviews','symptoms','pricing','guarantee','trust','faq'],
 ['benefits','what-is','ingredients','how','trust','reviews','pricing','guarantee','glance','symptoms','faq'],
 ['trust','what-is','symptoms','ingredients','benefits','how','reviews','glance','pricing','guarantee','faq'],
]
SWAPS=[('benefits','ingredients'),('glance','reviews'),('symptoms','what-is'),('guarantee','faq'),('how','benefits')]


def new_recipe(rng=None):
    r=rng or random.SystemRandom()
    hf=r.choice(HEAD_FONTS)
    bf=r.choice(BODY_FONTS)
    mode=r.choices(['light','cream','tint','dark'],[4,2,2,2])[0]
    flow=list(r.choice(FLOWS))
    for a,b in r.sample(SWAPS,r.randint(0,2)):
        i,j=flow.index(a),flow.index(b)
        flow[i],flow[j]=flow[j],flow[i]
    light_mode=mode!='dark'
    return {
     'mode':mode,
     'head_font':list(hf),'body_font':list(bf),
     'radius':r.choice([0,6,12,18,26]),
     'card':r.choice(['soft','flat','brutal','glass','topbar','tint']),
     'head':r.choice(['center','center-bar','left','kicker']),
     'btn':r.choice(['pill','round','square','gradient']),
     'cta':list(r.choice(CTA_PAIRS)),
     'header':r.choice(['solid','light','glass']) if light_mode else r.choice(['solid','glass']),
     'topbar':r.choice(['default','accent','hidden']),
     'hero':r.choice(['split','split-left','center']),
     'hero_bg':r.choice(['gradient','animated','pattern','solid']),
     'hero_light':light_mode and r.random()<0.25,
     'hero_shape':r.choice(['flat','slant','curve']),
     'h1_size':r.choice([2.4,2.7,3.0,3.3]),
     'flow':flow,
     'cols':{'symptoms':r.choice([2,3,4]),'benefits':r.choice([2,3,4]),'ingredients':r.choice([2,3,4]),'reviews':r.choice([1,2,3])},
     'steps':r.choice(['two','four','one']),
     'teal_how':r.random()<0.7,
     'anim':r.choice(['fade-up','slide','zoom','flip','blur']),
     'stagger':r.choice([50,80,110]),
     'hover':r.choice(['lift','tilt','glow','scale']),
     'hero_anim':r.choice(['up','zoom','left','blur']),
     'extras':r.sample(['float','pulse','progress'],r.randint(1,3)),
    }


def _font_href(rc):
    def part(fam,weights):
        return 'family='+fam.replace(' ','+')+((':'+weights) if weights else '')
    hf,bf=rc['head_font'],rc['body_font']
    return ('https://fonts.googleapis.com/css2?'+part(hf[0],hf[1])+'&'+part(bf[0],bf[1])+'&display=swap')


def build_css(rc):
    m=MODES[rc['mode']]
    dark=rc['mode']=='dark'
    hf,bf=rc['head_font'],rc['body_font']
    cta_soft,cta_strong,cta_ink=rc['cta']
    r=rc['radius']
    css=[]
    a=css.append
    a(f"body{{--text:{m['text']};--muted:{m['muted']};--border:{m['border']};--soft:{m['soft']};"
      f"--surface:{m['surface']};--r:{r}px;--gold-soft:{cta_soft};--gold:{cta_strong};--cta-ink:{cta_ink};"
      f"--d15-stg:{rc['stagger']}ms;background:{m['bg']};color:var(--text);font-family:'{bf[0]}',{bf[2]}}}")
    if rc['mode']=='tint':
        a("@supports (background:color-mix(in srgb,red,blue)){body{--soft:color-mix(in srgb,var(--primary-light) 55%,#fff);background:color-mix(in srgb,var(--primary-light) 22%,#fff)}}")
    a(f"h1,h2,h3,h4,.logo,.foot-logo,.plan-price,.plan-ttl{{font-family:'{hf[0]}',{hf[3]};font-weight:{hf[2]}}}")
    a(f".hero h1{{font-size:{rc['h1_size']}rem}}@media(max-width:991px){{.hero h1{{font-size:{max(1.9,rc['h1_size']-0.6):.1f}rem}}}}")
    # ---- surfaces (cards etc. must follow the colour mode) ----
    a(".pcard,.card,.trust-card,.ing-card,.plan,.science-col,.rev-card,.faq-row,.faq-btn{background:var(--surface)}")
    a(".pcard,.card,.trust-card,.ing-card,.plan,.science-col,.rev-card,.faq-row,.guarantee,.note{border-radius:var(--r)}")
    a(".plan{border-radius:calc(var(--r) + 6px)}.btn-cta{border-radius:var(--r)}")
    if dark:
        a(".ing-card{border-color:var(--border)}.sec:not(.teal) .head h2,.sec:not(.teal) h2[style],.faq-btn,.plan-price,.plan-ttl,.science-col li i{color:var(--primary-light)!important}"
          ".plan-ship{color:var(--primary-light)}.trust{border-bottom-color:var(--border)}.hero-note{opacity:.8}"
          ".auto-quick-facts{background:var(--surface)!important;border:1px solid var(--border)!important;color:var(--text)!important}"
          ".auto-quick-facts th{color:var(--muted)!important}.auto-quick-facts td,.auto-quick-facts h3{color:var(--text)!important}"
          ".auto-cta-trust{color:var(--muted)!important}")
    else:
        # primary can be a light colour, so section titles use the darker shade
        a(".sec:not(.teal) .head h2,.sec:not(.teal) h2[style]{color:var(--primary-dark)!important}")
    # ---- card style ----
    c=rc['card']
    cards=".pcard,.card,.ing-card,.rev-card,.science-col,.trust-card"
    if c=='flat':
        a(f"{cards}{{border:1.5px solid var(--border);box-shadow:none}}")
    elif c=='brutal':
        a(f"{cards}{{border:2px solid var(--text);box-shadow:5px 5px 0 var(--text)}}"
          f".pcard:hover,.card:hover,.ing-card:hover,.rev-card:hover,.trust-card:hover{{transform:translate(-2px,-2px);box-shadow:8px 8px 0 var(--text)}}")
    elif c=='glass':
        a(f"{cards}{{background:color-mix(in srgb,var(--surface) 72%,transparent);backdrop-filter:blur(10px);border:1px solid color-mix(in srgb,var(--border) 70%,#fff)}}")
    elif c=='topbar':
        a(f"{cards}{{border-top:4px solid var(--accent,var(--primary))}}.ing-card:before{{display:none}}")
    elif c=='tint':
        a(f"{cards}{{background:var(--primary-light);border-color:transparent;box-shadow:none}}"
          ".pcard p,.card p,.ing-card p,.rev-card p,.trust-card p{color:var(--primary-dark)}"
          ".pcard h4,.card h4,.ing-card h4,.rev-card .rev-name,.trust-card h3{color:var(--primary-dark)}")
    # ---- hover ----
    hv={'lift':'transform:translateY(-6px);box-shadow:0 14px 32px rgba(0,0,0,.14)',
        'tilt':'transform:translateY(-4px) rotate(-.7deg);box-shadow:0 12px 28px rgba(0,0,0,.14)',
        'glow':'box-shadow:0 0 0 2px var(--primary),0 14px 36px rgba(0,0,0,.18)',
        'scale':'transform:scale(1.03);box-shadow:0 14px 32px rgba(0,0,0,.14)'}[rc['hover']]
    if c!='brutal':
        a(f".pcard:hover,.card:hover,.ing-card:hover,.rev-card:hover,.trust-card:hover,.science-col:hover{{{hv}}}")
    # ---- headings ----
    h=rc['head']
    if h=='left':
        a(".head{text-align:left;margin-left:0;margin-right:auto;max-width:760px}")
    elif h=='center-bar':
        a(".head h2{position:relative;padding-bottom:16px}.head h2:after{content:'';position:absolute;left:50%;bottom:0;transform:translateX(-50%);width:64px;height:4px;border-radius:4px;background:var(--accent,var(--primary))}")
    elif h=='kicker':
        a(".head h2{font-size:1.75rem;text-transform:uppercase;letter-spacing:.07em}.head p{margin-top:6px}")
    # ---- buttons ----
    b=rc['btn']
    radius={'pill':'999px','round':'12px','square':'2px','gradient':'14px'}[b]
    a(f".btn-big,.btn-cta,.plan .btn{{border-radius:{radius};color:var(--cta-ink)!important}}")
    if b=='gradient':
        a(".btn-big,.btn-cta,.plan .btn{background:linear-gradient(135deg,var(--gold-soft),var(--gold));border-color:transparent}")
    # ---- header / top bar ----
    hd=rc['header']
    if hd=='light':
        a("nav.site{background:var(--surface);box-shadow:0 1px 0 var(--border)}.logo,.nav-link-c{color:var(--primary)!important}"
          ".nav-link-c:hover{color:var(--accent,var(--primary-dark))!important}.navbar-toggler-icon{filter:invert(1)}")
    elif hd=='glass':
        a("@supports (background:color-mix(in srgb,red,blue)){nav.site{background:color-mix(in srgb,var(--primary) 82%,transparent);backdrop-filter:blur(14px)}}")
    tb=rc['topbar']
    if tb=='hidden':a(".topbar{display:none}")
    elif tb=='accent':a(".topbar{background:var(--primary-dark);color:var(--on-primary)}.topbar i{color:var(--gold)}")
    # ---- hero ----
    hero=rc['hero']
    if hero=='split-left':
        a("@media(min-width:992px){.hero .row{flex-direction:row-reverse}}")
    elif hero=='center':
        a(".hero .row{justify-content:center;text-align:center}.hero .col-lg-7,.hero .col-lg-5{flex:0 0 auto;width:100%;max-width:880px}"
          ".hero-checks{max-width:640px;margin:0 auto 26px;text-align:left}#hero-img{max-height:340px!important}")
    bg=rc['hero_bg']
    if bg=='animated':
        # same two colours the original hero uses, so the text contrast is unchanged
        a("@media(prefers-reduced-motion:no-preference){.hero{background:linear-gradient(120deg,var(--primary),var(--primary-dark),var(--primary));background-size:300% 300%;animation:d15-grad 16s ease infinite}}")
    elif bg=='pattern':
        a(".hero{background-image:radial-gradient(rgba(255,255,255,.14) 1.5px,transparent 1.6px),linear-gradient(135deg,var(--primary),var(--primary-dark));background-size:24px 24px,auto}")
    elif bg=='solid':
        a(".hero{background:var(--primary)}")
    if rc['hero_light']:
        a(".hero{background:var(--primary-light)!important;animation:none!important}.hero,.hero h1,.hero-sub,.hero-checks div,.hero-note{color:var(--text)!important}"
          ".hero-badge{background:var(--surface);border-color:var(--border);color:var(--text)}.hero-checks i{color:var(--primary)}")
    shape=rc['hero_shape']
    if shape=='slant':
        a(".hero{padding-bottom:110px;clip-path:polygon(0 0,100% 0,100% 93%,0 100%)}")
    elif shape=='curve':
        a(".hero{padding-bottom:100px;border-radius:0 0 50% 50%/0 0 46px 46px}")
    # ---- steps ----
    st=rc['steps']
    if st=='four':
        a("@media(min-width:992px){.steps{grid-template-columns:repeat(4,1fr)}}")
    elif st=='one':
        a(".steps{grid-template-columns:1fr;max-width:760px;margin:0 auto}")
    a(".sec:not(.teal) .step-card{background:var(--surface);border-color:var(--border);color:var(--text)}"
      ".sec:not(.teal) .step-card h4{color:var(--text)}.sec:not(.teal) .step-card p{color:var(--muted)}"
      ".sec:not(.teal) .step-card .step-num{background:var(--primary);color:var(--on-primary)}")
    a(".g1{grid-template-columns:1fr;max-width:760px;margin:0 auto}")
    # ---- motion (everything inside no-preference) ----
    reveal={'fade-up':'transform:translateY(28px)',
            'slide':'transform:translateX(-38px)',
            'zoom':'transform:scale(.92)',
            'flip':'transform:perspective(800px) rotateX(14deg) translateY(20px)',
            'blur':'filter:blur(10px);transform:translateY(12px)'}[rc['anim']]
    a("@media(prefers-reduced-motion:no-preference){")
    a(".d15-js .d15-r{opacity:0;"+reveal+";transition:opacity .7s ease,transform .7s cubic-bezier(.2,.7,.2,1),filter .7s ease;"
      "transition-delay:calc(var(--d15-i,0)*var(--d15-stg))}")
    if rc['anim']=='slide':
        a(".d15-js .d15-r:nth-child(even){transform:translateX(38px)}")
    a(".d15-js .d15-r.d15-in{opacity:1;transform:none;filter:none}")
    ha=rc['hero_anim']
    kf={'up':'from{opacity:0;transform:translateY(26px)}','zoom':'from{opacity:0;transform:scale(.9)}',
        'left':'from{opacity:0;transform:translateX(-34px)}','blur':'from{opacity:0;filter:blur(12px)}'}[ha]
    a("@keyframes d15-in{"+kf+"to{opacity:1;transform:none;filter:none}}")
    a("@keyframes d15-grad{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}")
    a("@keyframes d15-float{0%,100%{transform:translateY(0)}50%{transform:translateY(-12px)}}")
    a("@keyframes d15-pulse{0%{box-shadow:0 0 0 0 rgba(255,255,255,.5)}70%{box-shadow:0 0 0 16px rgba(255,255,255,0)}100%{box-shadow:0 0 0 0 rgba(255,255,255,0)}}")
    a(".hero .col-lg-7>*,.hero .col-lg-5{animation:d15-in .85s cubic-bezier(.2,.7,.2,1) both}")
    for i in range(1,7):
        a(f".hero .col-lg-7>*:nth-child({i}){{animation-delay:{.08*i:.2f}s}}")
    a(".hero .col-lg-5{animation-delay:.25s}")
    if 'float' in rc['extras']:
        a("#hero-img{animation:d15-float 5s ease-in-out infinite}")
    if 'pulse' in rc['extras']:
        a(".hero .btn-big{animation:d15-pulse 2.4s infinite}")
    a("}")
    a("#d15-progress{position:fixed;top:0;left:0;height:3px;width:0;background:var(--gold);z-index:2000}")
    return '\n'.join(css)


_JS="""(function(){
var d=document.documentElement;
var bar=document.getElementById('d15-progress');
if(bar){window.addEventListener('scroll',function(){var h=d.scrollHeight-innerHeight;bar.style.width=(h>0?scrollY/h*100:0)+'%'},{passive:true});}
if(matchMedia('(prefers-reduced-motion:reduce)').matches||!('IntersectionObserver' in window))return;
var sel='.head,.pcard,.card,.ing-card,.rev-card,.plans,.step-card,.trust-card,.science-col,.guarantee,.faq-row,#what-is .row>div';
var els=[].slice.call(document.querySelectorAll(sel));
els.forEach(function(el){
 var i=[].indexOf.call(el.parentNode.children,el);
 el.classList.add('d15-r');el.style.setProperty('--d15-i',Math.min(i,6));
});
d.classList.add('d15-js');
var io=new IntersectionObserver(function(es){es.forEach(function(e){
 if(!e.isIntersecting)return;var el=e.target;io.unobserve(el);el.classList.add('d15-in');
 var done=function(ev){if(ev.propertyName!=='opacity')return;el.classList.remove('d15-r','d15-in');el.style.removeProperty('--d15-i');el.removeEventListener('transitionend',done)};
 el.addEventListener('transitionend',done);
})},{threshold:.1,rootMargin:'0px 0px -5% 0px'});
els.forEach(function(el){io.observe(el)});
})();"""


def _find_block(soup,key):
    if key=='trust':return soup.find('section',class_='trust')
    ids={'symptoms':'symptoms-section','what-is':'what-is','how':'how-it-works','benefits':'benefits',
         'ingredients':'ingredients','pricing':'pricing','reviews':'reviews','faq':'faq'}
    if key in ids:return soup.find('section',id=ids[key])
    if key=='glance':
        n=soup.find(class_='science-col')
        return n.find_parent('section') if n else None
    if key=='guarantee':
        n=soup.find(class_='guarantee')
        return n.find_parent('section') if n else None
    return None


def _classes(tag):
    return list(tag.get('class') or [])


def _reorder_and_restyle(soup,rc):
    final=soup.find('section',class_='final')
    if not final:return
    blocks={}
    for key in rc['flow']:
        node=_find_block(soup,key)
        if node is not None and node is not final:
            blocks[key]=node
    bonus=soup.find('div',class_='bonus-block')
    order=[k for k in rc['flow'] if k in blocks]
    for key in order:
        final.insert_before(blocks[key])
        if key=='pricing' and bonus is not None:
            final.insert_before(bonus)
    # alternate backgrounds in the new order; one or two coloured sections
    # Only the how-it-works section is ever coloured: its step cards are built
    # for it, while other sections' cards would lose their titles on a coloured
    # background.
    teal=set()
    if rc.get('teal_how',True) and 'how' in blocks:teal.add('how')
    n=0
    for key in order:
        tag=blocks[key]
        cls=_classes(tag)
        if 'sec' not in cls:continue
        cls=[c for c in cls if c not in ('soft','teal')]
        if key in teal:cls.append('teal')
        else:
            if n%2==1:cls.append('soft')
            n+=1
        tag['class']=cls
    # grid column counts per section
    for key,sec_key in (('symptoms','symptoms'),('benefits','benefits'),('ingredients','ingredients'),('reviews','reviews')):
        sec=blocks.get(sec_key)
        if sec is None:continue
        grid=sec.find('div',class_='grid')
        if grid is None:continue
        cls=[c for c in _classes(grid) if c not in ('g1','g2','g3','g4')]
        cls.append('g'+str(rc['cols'][key]))
        grid['class']=cls


def apply(soup,rc,filename='index.html',page_kind='index'):
    """Apply the recipe to a built native page (a BeautifulSoup tree)."""
    if not rc or soup.head is None or soup.body is None:
        return
    fonts=soup.new_tag('link',rel='stylesheet',href=_font_href(rc))
    pre1=soup.new_tag('link',rel='preconnect',href='https://fonts.googleapis.com')
    pre2=soup.new_tag('link',rel='preconnect',href='https://fonts.gstatic.com',crossorigin='')
    for t in (pre1,pre2,fonts):soup.head.append(t)
    style=soup.new_tag('style',id='d15-style')
    style.string=build_css(rc)
    soup.head.append(style)
    cls=_classes(soup.body)+['d15']+(['d15-dark'] if rc['mode']=='dark' else [])
    soup.body['class']=cls
    if filename=='index.html' and page_kind=='index':
        _reorder_and_restyle(soup,rc)
    if 'progress' in rc['extras']:
        soup.body.insert(0,BeautifulSoup('<div id="d15-progress" aria-hidden="true"></div>','html.parser'))
    js=soup.new_tag('script')
    js.string=_JS
    soup.body.append(js)
