"""Niche registry.

Every niche has a `kind` that decides how the AI is told to treat the product:
  supplement  - the original behaviour (capsules, ingredients, bottles)
  digital     - courses, software, ebooks, memberships, information products
  physical    - physical consumer products that are not supplements
  service     - bookings, subscriptions and other services

To add a niche, add one entry to NICHES. `subs` are only autocomplete
suggestions; the user can type any sub-niche. `warn` is shown under the
selector and is meant for categories with legal or advertising restrictions.
"""

DEFAULT_NICHE='health-fitness'

NICHES={
 'health-fitness':{'name':'Health & Fitness','kind':'supplement',
   'subs':['Weight loss','Men\'s health','Women\'s health','Joint & pain','Blood sugar','Brain & memory','Sleep','Fitness programs'],
   'warn':'Health claims must be accurate and supportable. Avoid disease treatment or cure claims.'},
 'arts-entertainment':{'name':'Arts & Entertainment','kind':'digital',
   'subs':['Music','Drawing & painting','Photography','Film & video','Writing','Dance','Crafts']},
 'betting-systems':{'name':'Betting Systems','kind':'digital',
   'subs':['Sports betting','Casino & poker','Lottery','Horse racing'],
   'warn':'Gambling promotion is illegal or heavily restricted in many countries and on most ad platforms. Check the law where you publish and where your visitors live.'},
 'business-investing':{'name':'Business / Investing','kind':'digital',
   'subs':['Stocks & trading','Crypto','Real estate','Small business','Personal finance','Forex'],
   'warn':'Do not promise income or returns. Financial and income claims need clear disclaimers.'},
 'computers-internet':{'name':'Computers / Internet','kind':'digital',
   'subs':['Security & privacy','Web design','Programming','Hosting','Online tools']},
 'cooking-food-wine':{'name':'Cooking, Food & Wine','kind':'digital',
   'subs':['Recipes','Diets & meal plans','Baking','Wine & drinks','BBQ & grilling']},
 'e-business-marketing':{'name':'E-Business & E-Marketing','kind':'digital',
   'subs':['Affiliate marketing','SEO & traffic','Email marketing','Social media','Dropshipping']},
 'e-commerce':{'name':'E-Commerce','kind':'physical',
   'subs':['Online stores','Dropshipping','Amazon FBA','Print on demand']},
 'education':{'name':'Education','kind':'digital',
   'subs':['Test prep','Online courses','Homeschooling','Study skills','Career skills']},
 'employment-jobs':{'name':'Employment & Jobs','kind':'digital',
   'subs':['Resumes & interviews','Work from home','Freelancing','Career change'],
   'warn':'Do not promise jobs or specific earnings.'},
 'games':{'name':'Games','kind':'digital',
   'subs':['Video game guides','Board & card games','Puzzles','Cheats & tips']},
 'green-products':{'name':'Green Products','kind':'physical',
   'subs':['Solar & energy','Recycling','Organic products','Water & air','Eco living']},
 'home-garden':{'name':'Home & Garden','kind':'physical',
   'subs':['Gardening','DIY & woodworking','Decor','Pest control','Home improvement']},
 'languages':{'name':'Languages','kind':'digital',
   'subs':['English','Spanish','French','German','Other languages']},
 'parenting-families':{'name':'Parenting & Families','kind':'digital',
   'subs':['Pregnancy','Babies & toddlers','Teens','Family activities','Relationships']},
 'politics-current-events':{'name':'Politics / Current Events','kind':'digital',
   'subs':['Preparedness','News & analysis','Civic topics'],
   'warn':'Political content has special advertising and election rules on many platforms and countries.'},
 'reference':{'name':'Reference','kind':'digital',
   'subs':['Guides & manuals','Genealogy','Directories','Research']},
 'self-help':{'name':'Self-Help','kind':'digital',
   'subs':['Motivation','Dating & relationships','Confidence','Stress & anxiety','Productivity'],
   'warn':'Avoid guaranteed life or mental-health outcomes.'},
 'software-services':{'name':'Software & Services','kind':'digital',
   'subs':['Apps','Business software','Web services','Utilities','AI tools']},
 'spirituality':{'name':'Spirituality, New Age & Alternative Beliefs','kind':'digital',
   'subs':['Meditation','Astrology','Manifestation','Alternative healing']},
 'sports':{'name':'Sports','kind':'digital',
   'subs':['Golf','Fishing & hunting','Team sports','Martial arts','Running & cycling']},
 'travel':{'name':'Travel','kind':'service',
   'subs':['Travel deals','Cruises','Hotels','Travel guides','Visas & documents']},
}

_KIND_GUIDE={
 'digital':(
  'This is a DIGITAL product (course, software, ebook, programme, membership or information product), '
  'NOT a physical item or a supplement. Never mention bottles, capsules, servings, doses, FDA or GMP. '
  'Use the "ingredients" array for the product\'s main components (modules, lessons, features, tools or bonuses '
  'actually included), with "role" describing what each one does for the buyer. '
  'For pricing, list the real packages/plans sold; set "bottles" to the number of licences, seats or months '
  'in that package (1 if it is a single purchase) and use the package name in "label". '
  'Describe benefits as outcomes a buyer can reasonably expect, without income, result or success guarantees.'),
 'physical':(
  'This is a PHYSICAL consumer product that is NOT a dietary supplement. Never mention capsules, servings, '
  'FDA or GMP unless they truly apply. Use the "ingredients" array for the product\'s key features, materials '
  'or components, with "role" describing what each does. For pricing, list the real bundles or quantities sold '
  'and set "bottles" to the number of units in that bundle.'),
 'service':(
  'This is a SERVICE or booking/subscription offer, NOT a physical item or a supplement. Never mention bottles, '
  'capsules, servings, FDA or GMP. Use the "ingredients" array for what is included in the service, with "role" '
  'describing each element. For pricing, list the real plans or packages and set "bottles" to the number of '
  'units (people, nights or months) in that plan, 1 if it is a single purchase.'),
}


def get_niche(niche_id):
    return NICHES.get(niche_id) or NICHES[DEFAULT_NICHE]


def valid_niche(niche_id):
    return niche_id in NICHES


def build_hint(niche_id,sub,user_hint):
    """Fold the niche into the 'publisher description' that the content prompt
    already treats as ground truth. The default niche adds nothing beyond a
    label, so existing supplement behaviour is unchanged."""
    n=get_niche(niche_id)
    parts=[]
    if niche_id!=DEFAULT_NICHE or (sub or '').strip():
        label=n['name']+(f' > {sub.strip()}' if (sub or '').strip() else '')
        parts.append(f'Niche: {label}.')
    if niche_id!=DEFAULT_NICHE and n['kind'] in _KIND_GUIDE:
        parts.append(_KIND_GUIDE[n['kind']])
    if (user_hint or '').strip():
        parts.append(user_hint.strip())
    return ' '.join(parts)
