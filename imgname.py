"""Suggest which website slot each uploaded image belongs to.

The generator fills its pages from files with fixed names (hero, bottle-3,
badge-fda, reviewer-1 ...). This module looks at a batch of images and
proposes those names, so people don't have to rename files by hand.

Order of attempts:
  1. a vision model (Anthropic, then OpenAI) when a key is configured
  2. filename keywords, plus a few cheap image checks
Every suggestion carries its source and a confidence so the UI can show what
was a guess. Nothing here renames anything: the user confirms in the UI.
"""
import io,re,json,base64,os
import requests
from PIL import Image

# slot -> what it is, as described to the model
SLOTS={
 'hero':'main product shot: the product pack/bottle, the best front-facing image of the product',
 'bottle-2':'a pack shot showing exactly 2 bottles/boxes together',
 'bottle-3':'a pack shot showing exactly 3 bottles/boxes together',
 'bottle-6':'a pack shot showing exactly 6 bottles/boxes together',
 'badge-fda':'trust badge about FDA (text such as FDA approved / FDA registered)',
 'badge-gmp':'trust badge about GMP / good manufacturing practice certification',
 'badge-usa':'trust badge: made in USA / American-made',
 'badge-natural':'trust badge: 100% natural / non-GMO / natural ingredients',
 'guarantee':'money-back guarantee seal or badge (e.g. 60 day money back)',
 'credit-cards':'row of accepted payment card logos (Visa, Mastercard, Amex...)',
 'stars':'star-rating graphic (five stars)',
 'how-it-works':'infographic or diagram explaining how the product works',
 'reviewer-1':'a portrait photo of a person used for a customer review',
 'bonus-1':'cover of a free bonus (ebook, guide, report)',
 'checkout':'screenshot of an order or checkout page',
 'supplement-facts':'photo or graphic of a supplement-facts / nutrition label',
 'favicon':'small square logo or icon for the browser tab',
}
# slots that may repeat with a number suffix
NUMBERED={'reviewer':6,'bonus':6}
UNUSED='unused'
KEEP='__keep__'
MAX_IMAGES=20
MAX_BYTES=8*1024*1024

_KEYWORDS=[  # (regex on the file stem, slot) - first match wins
 (r'fda','badge-fda'),(r'gmp|good-manufactur','badge-gmp'),(r'(made-?in-?)?usa|american','badge-usa'),
 (r'natural|non-?gmo|organic','badge-natural'),(r'guarantee|money-?back|refund|seal','guarantee'),
 (r'credit|payment|visa|master|amex|cards?$','credit-cards'),(r'stars?|rating','stars'),
 (r'how-?it-?works?|mechanism|diagram|infographic','how-it-works'),(r'checkout|order-?page','checkout'),
 (r'supplement-?facts|nutrition|label','supplement-facts'),(r'favicon|icon|logo','favicon'),
 (r'review|testimonial|customer|portrait|person|member|user','reviewer'),(r'bonus|ebook|e-book|guide|report|cover','bonus'),
 (r'\b6\b|six|6-?(bottle|pack|box)','bottle-6'),(r'\b3\b|three|3-?(bottle|pack|box)','bottle-3'),
 (r'\b2\b|two|2-?(bottle|pack|box)','bottle-2'),
 (r'hero|main|header|front|product|bottle|jar|pack|box','hero'),
]


def _thumb_b64(data,side=640,quality=72):
    im=Image.open(io.BytesIO(data))
    if im.mode in ('RGBA','LA','P'):
        im=im.convert('RGBA'); bg=Image.new('RGB',im.size,(255,255,255)); bg.paste(im,mask=im.split()[-1]); im=bg
    else:
        im=im.convert('RGB')
    im.thumbnail((side,side))
    out=io.BytesIO(); im.save(out,format='JPEG',quality=quality)
    return base64.b64encode(out.getvalue()).decode('ascii')


def _prompt(names):
    slot_lines='\n'.join(f'- {k}: {v}' for k,v in SLOTS.items())
    listing='\n'.join(f'Image {i}: file name "{n}"' for i,n in enumerate(names))
    return f"""You label images for a website generator for a dietary-supplement / product affiliate site.
Assign each image to ONE slot name from this list, or to "unused" when it fits none:
{slot_lines}

Rules:
- Look at the picture itself; the file name is only a hint and may be random.
- Count the bottles/boxes in pack shots to choose bottle-2 / bottle-3 / bottle-6. A single bottle or the best general product shot is hero.
- Use each slot at most once, except people photos (reviewer-1, reviewer-2, ...) and bonus covers (bonus-1, bonus-2, ...), which you may number in order.
- If several images fit the same slot, pick the best one and mark the others "unused".
- Give "confidence": "high" when clearly right, otherwise "low".

{listing}

Answer with JSON only, no other text:
{{"images":[{{"i":0,"slot":"hero","confidence":"high"}}]}}"""


def _extract_json(text):
    text=text.strip()
    m=re.search(r'\{.*\}',text,re.S)
    return json.loads(m.group(0) if m else text)


def _call_anthropic(key,names,thumbs):
    content=[{'type':'text','text':_prompt(names)}]
    for i,(n,b) in enumerate(zip(names,thumbs)):
        content.append({'type':'text','text':f'Image {i}: {n}'})
        content.append({'type':'image','source':{'type':'base64','media_type':'image/jpeg','data':b}})
    r=requests.post('https://api.anthropic.com/v1/messages',
        headers={'x-api-key':key,'anthropic-version':'2023-06-01','content-type':'application/json'},
        json={'model':os.getenv('ANTHROPIC_VISION_MODEL','claude-haiku-5-5'),'max_tokens':1800,
              'messages':[{'role':'user','content':content}]},timeout=120)
    r.raise_for_status()
    return _extract_json(r.json()['content'][0]['text'])


def _call_openai(key,names,thumbs):
    content=[{'type':'text','text':_prompt(names)}]
    for i,(n,b) in enumerate(zip(names,thumbs)):
        content.append({'type':'text','text':f'Image {i}: {n}'})
        content.append({'type':'image_url','image_url':{'url':'data:image/jpeg;base64,'+b,'detail':'low'}})
    r=requests.post('https://api.openai.com/v1/chat/completions',
        headers={'Authorization':'Bearer '+key,'Content-Type':'application/json'},
        json={'model':os.getenv('OPENAI_VISION_MODEL','gpt-4o-mini'),'max_tokens':1800,
              'response_format':{'type':'json_object'},'messages':[{'role':'user','content':content}]},timeout=120)
    r.raise_for_status()
    return _extract_json(r.json()['choices'][0]['message']['content'])


def _stem(name):
    return re.sub(r'[^a-z0-9]+','-',re.sub(r'\.[a-z0-9]+$','',name.lower())).strip('-')


def filename_guess(name,data=None):
    """(slot, confidence) from the file name and, when possible, the image size."""
    s=_stem(name)
    for pat,slot in _KEYWORDS:
        if re.search(pat,s):
            return slot,'low'
    if data:
        try:
            w,h=Image.open(io.BytesIO(data)).size
            if max(w,h)<=256 and abs(w-h)<=max(8,w*0.1):return 'favicon','low'
        except Exception:pass
    return UNUSED,'low'


def _normalise(raw_items,names):
    """Map model output onto valid slots and enforce 'each slot once'."""
    slots=set(SLOTS)|{UNUSED}
    chosen={}
    for it in (raw_items or []):
        try:i=int(it.get('i'))
        except Exception:continue
        if not 0<=i<len(names):continue
        slot=str(it.get('slot','')).strip().lower()
        base=re.sub(r'-\d+$','',slot)
        if slot not in slots and base not in NUMBERED:
            slot=UNUSED
        chosen[i]=(slot,'high' if str(it.get('confidence','')).lower()=='high' else 'low')
    out=[None]*len(names); used=set(); counters={k:0 for k in NUMBERED}
    for i in range(len(names)):
        slot,conf=chosen.get(i,(UNUSED,'low'))
        base=re.sub(r'-\d+$','',slot)
        if base in NUMBERED:
            counters[base]+=1
            n=counters[base]
            slot=f'{base}-{n}' if n<=NUMBERED[base] else UNUSED
        elif slot!=UNUSED:
            if slot in used:slot=UNUSED   # duplicate: first one wins
            else:used.add(slot)
        out[i]=(slot,conf)
    return out


def suggest(files,keys):
    """files: list of (filename, bytes). keys: dict with anthropic/openai.
    Returns {'provider','note','items':[{'index','filename','slot','confidence','source'}]}."""
    files=files[:MAX_IMAGES]
    names=[n for n,_ in files]
    provider='filename'; note=''; result=None
    thumbs=None
    attempts=[]
    if keys.get('anthropic'):attempts.append(('anthropic',_call_anthropic,keys['anthropic']))
    if keys.get('openai'):attempts.append(('openai',_call_openai,keys['openai']))
    if attempts:
        try:thumbs=[_thumb_b64(d) for _,d in files]
        except Exception as e:
            note=f'Could not read an image ({e}). '; attempts=[]
    for prov,fn,key in attempts:
        try:
            raw=fn(key,names,thumbs)
            result=_normalise(raw.get('images'),names); provider=prov; break
        except Exception as e:
            note+=f'{prov} vision failed ({type(e).__name__}). '
    items=[]
    if result is None:
        guesses=[filename_guess(n,d) for n,d in files]
        result=_normalise([{'i':i,'slot':s,'confidence':c} for i,(s,c) in enumerate(guesses)],names)
        if not attempts and not note:
            note='No vision key is set, so these are guesses from the file names. Check each one.'
    for i,(n,_) in enumerate(files):
        slot,conf=result[i]
        items.append({'index':i,'filename':n,'slot':slot,'confidence':conf if provider!='filename' else 'low',
                      'source':'ai' if provider!='filename' else 'filename'})
    return {'provider':provider,'note':note.strip(),'items':items}


def slot_options():
    """All selectable slot names for the UI."""
    opts=list(SLOTS)
    for base,mx in NUMBERED.items():
        opts=[o for o in opts if o!=f'{base}-1']
        opts+= [f'{base}-{n}' for n in range(1,mx+1)]
    return sorted(set(opts))
