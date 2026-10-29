"""Access control for the hosted version of the generator.

Enabled only when ADMIN_PASSWORD is set, so running locally (gui.py / python
app.py) behaves exactly as before. When enabled:

* the owner logs in with ADMIN_EMAIL (default "admin") + ADMIN_PASSWORD and
  manages friends in /admin
* friends log in with the email + password the owner created for them; each
  account has an expiry date, an optional per-day generation limit and an
  optional list of allowed designs
* accounts live in the database named by DATABASE_URL (use a free Neon
  Postgres on Render, whose own disk is wiped on every deploy). Without
  DATABASE_URL a throw-away SQLite file is used and /admin warns about it.
"""
import os,re,time,hmac,hashlib,secrets,tempfile
from datetime import datetime,timezone
from flask import (Blueprint,request,session,redirect,render_template,
                   jsonify,url_for,g)
from werkzeug.security import generate_password_hash,check_password_hash
from sqlalchemy import (create_engine,MetaData,Table,Column,Integer,BigInteger,
                        String,Boolean,Text,select,insert,update,delete,inspect,text)
import niches as nx

ADMIN_PASSWORD=os.getenv('ADMIN_PASSWORD','').strip()
ADMIN_EMAIL=os.getenv('ADMIN_EMAIL','admin').strip().lower()
ENABLED=bool(ADMIN_PASSWORD)
HOSTED=ENABLED or os.getenv('HOSTED','')=='1'
DATABASE_URL=os.getenv('DATABASE_URL','').strip()

bp=Blueprint('auth',__name__)

PUBLIC_ENDPOINTS={'auth.landing','auth.login','auth.logout','auth.healthz','auth.terms','auth.privacy','static'}
# Endpoints that spend the owner's AI credit and count toward a friend's daily
# limit. Phase 2 (/api/generate) reuses phase 1's content, so counting phase 1
# is the accurate measure of "one website".
METERED_ENDPOINTS={'generate_content'}
EMAIL_RE=re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$')

TEMPLATES={}   # set by app.py; {design id: {'name':...}}
_attempts={}   # ip -> [timestamps] for login throttling

meta=MetaData()
users=Table('users',meta,
    Column('id',Integer,primary_key=True),
    Column('email',String(255),unique=True,nullable=False),
    Column('name',String(80)),
    Column('pw_hash',String(255),nullable=False),
    Column('expires_at',BigInteger,nullable=False),
    Column('daily_cap',Integer,default=0),
    Column('designs',String(255),default=''),
    Column('niches',String(1000),default=''),
    Column('active',Boolean,default=True),
    Column('created_at',BigInteger))
errors=Table('errors',meta,
    Column('id',Integer,primary_key=True),
    Column('ts',BigInteger),
    Column('who',String(255)),
    Column('endpoint',String(80)),
    Column('summary',String(500)),
    Column('detail',Text))
usage=Table('usage',meta,
    Column('user_id',Integer,primary_key=True),
    Column('day',String(10),primary_key=True),
    Column('n',Integer,default=0))

_engine=None


def persistent_db():
    return bool(DATABASE_URL)


def _db():
    global _engine
    if _engine is None:
        url=DATABASE_URL
        if url.startswith('postgres://'):
            url='postgresql://'+url[len('postgres://'):]
        if url.startswith('postgresql://'):
            url='postgresql+psycopg2://'+url[len('postgresql://'):]
        if not url:
            url='sqlite:///'+os.path.join(tempfile.gettempdir(),'affgen_users.db')
        _engine=create_engine(url,pool_pre_ping=True,pool_recycle=240)
        meta.create_all(_engine)
        # create_all never adds columns to a table that already exists, so
        # databases created before niches existed get the column here.
        if 'niches' not in {c['name'] for c in inspect(_engine).get_columns('users')}:
            with _engine.begin() as c:
                c.execute(text("ALTER TABLE users ADD COLUMN niches VARCHAR(1000) DEFAULT ''"))
    return _engine


def _secret():
    return (os.getenv('SECRET_KEY','').strip()
            or hashlib.sha256(('affgen:'+ADMIN_PASSWORD).encode()).hexdigest())


def init(app):
    app.secret_key=_secret()
    app.config.update(
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_SAMESITE='Lax',
        SESSION_COOKIE_SECURE=os.getenv('COOKIE_SECURE','1' if HOSTED else '0')=='1',
        PERMANENT_SESSION_LIFETIME=60*60*24*14,
    )
    if HOSTED:
        app.config['MAX_CONTENT_LENGTH']=int(os.getenv('MAX_UPLOAD_MB','40'))*1024*1024
        from werkzeug.middleware.proxy_fix import ProxyFix
        app.wsgi_app=ProxyFix(app.wsgi_app,x_for=1,x_proto=1,x_host=1)
    app.jinja_env.filters['datetimeformat']=lambda ts:datetime.fromtimestamp(ts,timezone.utc).strftime('%d %b %Y')
    @app.context_processor
    def _chrome():
        return {'nav_user':current() if ENABLED else None,'nav_auth':ENABLED,
                'now_year':datetime.now(timezone.utc).year,
                'support_email':os.getenv('SUPPORT_EMAIL','').strip()}
    @app.after_request
    def _headers(resp):
        resp.headers.setdefault('X-Content-Type-Options','nosniff')
        resp.headers.setdefault('X-Frame-Options','DENY')
        resp.headers.setdefault('Referrer-Policy','same-origin')
        if request.path.startswith(('/app','/admin','/api','/login')):
            resp.headers['X-Robots-Tag']='noindex, nofollow'
        return resp
    app.register_blueprint(bp)
    app.before_request(_gate)


def _user_dict(r):
    return {'role':'friend','name':r.name or r.email,'email':r.email,'uid':r.id,
            'e':r.expires_at,'c':r.daily_cap or 0,
            'd':[x for x in (r.designs or '').split(',') if x],
            'n':[x for x in (r.niches or '').split(',') if x]}


def current():
    """The logged-in user as a dict, or None. Friends are re-read from the
    database on every request, so disabling, deleting or expiring an account
    cuts that person off immediately."""
    if not ENABLED:
        return {'role':'admin','name':'local'}
    s=session.get('u')
    if not s:
        return None
    if s['role']=='admin':
        return {'role':'admin','name':'Owner'}
    try:
        with _db().connect() as c:
            r=c.execute(select(users).where(users.c.id==s['uid'])).first()
    except Exception:
        return None
    if not r or not r.active or r.expires_at<time.time():
        session.clear()
        return None
    return _user_dict(r)


def is_admin():
    u=current()
    return bool(u and u['role']=='admin')


def allowed_designs():
    """Design ids the current user may use, or None for no restriction."""
    u=current()
    if not ENABLED or not u or u['role']=='admin':
        return None
    return u.get('d') or None


def allowed_niches():
    """Niche ids the current user may use, or None for no restriction."""
    u=current()
    if not ENABLED or not u or u['role']=='admin':
        return None
    return u.get('n') or None


def _client_ip():
    return request.remote_addr or '?'


def _throttled():
    now=time.time()
    hits=[t for t in _attempts.get(_client_ip(),[]) if now-t<300]
    _attempts[_client_ip()]=hits
    return len(hits)>=8


def _today():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d')


def _use_quota(u):
    """Count one website against a friend's daily cap; False when exhausted."""
    cap=u.get('c') or 0
    if not cap:
        return True
    with _db().begin() as c:
        row=c.execute(select(usage.c.n).where(usage.c.user_id==u['uid'],usage.c.day==_today())).first()
        n=row[0] if row else 0
        if n>=cap:
            return False
        if row:
            c.execute(update(usage).where(usage.c.user_id==u['uid'],usage.c.day==_today()).values(n=n+1))
        else:
            c.execute(insert(usage).values(user_id=u['uid'],day=_today(),n=1))
    return True


def _gate():
    if not ENABLED:
        return None
    if request.endpoint in PUBLIC_ENDPOINTS:
        return None
    u=current()
    if not u:
        if request.path.startswith('/api/'):
            return jsonify(error='Session expired. Please log in again.'),401
        return redirect(url_for('auth.login',next=request.path))
    g.user=u
    if (request.endpoint or '').startswith('auth.admin') and u['role']!='admin':
        return redirect(url_for('index'))
    if u['role']=='friend' and request.method=='POST':
        if request.endpoint in ('generate','generate_content'):
            allowed_n=u.get('n')
            chosen=request.form.get('niche',nx.DEFAULT_NICHE)
            if allowed_n and chosen not in allowed_n:
                return jsonify(error='This niche is not included in your access. Pick one of your allowed niches.'),403
        if request.endpoint=='generate':
            allowed=u.get('d')
            if allowed and request.form.get('design','1') not in allowed:
                return jsonify(error='This design is not included in your access. Pick one of your allowed designs.'),403
        if request.endpoint in METERED_ENDPOINTS and not _use_quota(u):
            return jsonify(error=f'Daily limit reached ({u["c"]} websites per day). Try again tomorrow.'),429
    return None


@bp.get('/')
def landing():
    if not ENABLED or current():
        return redirect(url_for('index'))
    designs=[]
    for k,v in TEMPLATES.items():
        part=v['name'].split('—',1)[-1].strip()
        label='Auto-themed' if 'Auto-Themed' in part else part.split()[-1]
        designs.append((k,label))
    return render_template('landing.html',designs=designs)


@bp.get('/healthz')
def healthz():
    return 'ok'


@bp.get('/terms')
def terms():
    return render_template('terms.html')


@bp.get('/privacy')
def privacy():
    return render_template('privacy.html')


@bp.route('/login',methods=['GET','POST'])
def login():
    if not ENABLED:
        return redirect(url_for('index'))
    error=''
    if request.method=='POST':
        email=request.form.get('email','').strip().lower()
        pw=request.form.get('password','')
        if _throttled():
            error='Too many attempts. Wait a few minutes and try again.'
        else:
            _attempts.setdefault(_client_ip(),[]).append(time.time())
            if email==ADMIN_EMAIL and hmac.compare_digest(pw.encode(),ADMIN_PASSWORD.encode()):
                session.clear()
                session['u']={'role':'admin'}
                session.permanent=True
                return redirect(request.args.get('next') or url_for('index'))
            try:
                with _db().connect() as c:
                    r=c.execute(select(users).where(users.c.email==email)).first()
            except Exception:
                r=None
                error='Login is temporarily unavailable. Try again in a minute.'
            if r and check_password_hash(r.pw_hash,pw):
                if not r.active:
                    error='This account has been disabled. Contact the owner.'
                elif r.expires_at<time.time():
                    error='Your access has expired. Ask the owner to extend it.'
                else:
                    session.clear()
                    session['u']={'role':'friend','uid':r.id}
                    session.permanent=True
                    return redirect(url_for('index'))
            elif not error:
                error='Wrong email or password.'
    return render_template('login.html',error=error)


@bp.post('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.landing'))


MAX_ERROR_ROWS=300


def record_error(endpoint,summary,detail=''):
    """Store a failure for /admin/errors. Never raises."""
    try:
        try:
            u=current()
            who=(u.get('email') or u.get('name') or '?') if u else 'anonymous'
        except Exception:
            who='?'
        with _db().begin() as c:
            c.execute(insert(errors).values(ts=int(time.time()),who=str(who)[:255],
                      endpoint=str(endpoint)[:80],summary=str(summary)[:500],detail=str(detail)[:6000]))
            # keep the table small on a free database
            old=c.execute(select(errors.c.id).order_by(errors.c.id.desc()).offset(MAX_ERROR_ROWS).limit(1)).first()
            if old:
                c.execute(delete(errors).where(errors.c.id<=old[0]))
    except Exception:
        pass


def _recent_error_count():
    try:
        with _db().connect() as c:
            return c.execute(select(text('count(*)')).select_from(errors).where(errors.c.ts>time.time()-86400)).scalar() or 0
    except Exception:
        return 0


def _admin_page(created=None,error=''):
    with _db().connect() as c:
        rows=c.execute(select(users).order_by(users.c.id.desc())).fetchall()
        today={r.user_id:r.n for r in c.execute(select(usage).where(usage.c.day==_today()))}
    now=time.time()
    people=[{'id':r.id,'name':r.name,'email':r.email,'active':bool(r.active),
             'expired':r.expires_at<now,'expires':datetime.fromtimestamp(r.expires_at,timezone.utc).strftime('%d %b %Y'),
             'cap':r.daily_cap or 0,'used':today.get(r.id,0),
             'designs':[TEMPLATES[k]['name'] for k in (r.designs or '').split(',') if k in TEMPLATES] or ['All'],
             'niches':[nx.NICHES[k]['name'] for k in (r.niches or '').split(',') if k in nx.NICHES] or ['All']}
            for r in rows]
    return render_template('admin.html',created=created,error=error,people=people,error_count=_recent_error_count(),
                           templates=TEMPLATES,niche_list=nx.NICHES,persistent=persistent_db(),admin_email=ADMIN_EMAIL)


@bp.get('/admin')
def admin():
    return _admin_page()


@bp.get('/admin/errors')
def admin_errors():
    with _db().connect() as c:
        rows=c.execute(select(errors).order_by(errors.c.id.desc()).limit(100)).fetchall()
    items=[{'when':datetime.fromtimestamp(r.ts,timezone.utc).strftime('%d %b %H:%M UTC'),'who':r.who,
            'endpoint':r.endpoint,'summary':r.summary,'detail':r.detail} for r in rows]
    return render_template('errors.html',items=items)


@bp.post('/admin/errors/clear')
def admin_errors_clear():
    with _db().begin() as c:
        c.execute(delete(errors))
    return redirect(url_for('auth.admin_errors'))


@bp.post('/admin/create')
def admin_create():
    name=(request.form.get('name','').strip() or 'Friend')[:80]
    email=request.form.get('email','').strip().lower()
    pw=request.form.get('password','').strip() or secrets.token_urlsafe(7)
    if not EMAIL_RE.match(email):
        return _admin_page(error='Enter a valid email address.')
    if len(pw)<6:
        return _admin_page(error='Password must be at least 6 characters.')
    try:days=max(1,min(int(request.form.get('days','7')),3650))
    except ValueError:days=7
    try:cap=max(0,min(int(request.form.get('cap','3')),100))
    except ValueError:cap=3
    picked=[k for k in request.form.getlist('designs') if k in TEMPLATES]
    picked_n=[k for k in request.form.getlist('niches') if k in nx.NICHES]
    exp=int(time.time())+days*86400
    try:
        with _db().begin() as c:
            c.execute(insert(users).values(email=email,name=name,pw_hash=generate_password_hash(pw),
                      expires_at=exp,daily_cap=cap,designs=','.join(picked),niches=','.join(picked_n),
                      active=True,created_at=int(time.time())))
    except Exception:
        return _admin_page(error='That email already has an account.')
    return _admin_page(created={'name':name,'email':email,'password':pw,'days':days,'cap':cap,
                       'designs':[TEMPLATES[k]['name'] for k in picked],
                       'niches':[nx.NICHES[k]['name'] for k in picked_n],
                       'expires':datetime.fromtimestamp(exp,timezone.utc).strftime('%d %b %Y'),
                       'link':request.url_root.rstrip('/')+url_for('auth.login')})


@bp.post('/admin/user/<int:uid>/<action>')
def admin_user(uid,action):
    with _db().begin() as c:
        r=c.execute(select(users).where(users.c.id==uid)).first()
        if r:
            if action=='toggle':
                c.execute(update(users).where(users.c.id==uid).values(active=not r.active))
            elif action=='extend':
                try:d=max(1,min(int(request.form.get('days','7')),3650))
                except ValueError:d=7
                base=max(r.expires_at,int(time.time()))
                c.execute(update(users).where(users.c.id==uid).values(expires_at=base+d*86400))
            elif action=='password':
                pw=request.form.get('password','').strip()
                if len(pw)>=6:
                    c.execute(update(users).where(users.c.id==uid).values(pw_hash=generate_password_hash(pw)))
            elif action=='delete':
                c.execute(delete(users).where(users.c.id==uid))
                c.execute(delete(usage).where(usage.c.user_id==uid))
    return redirect(url_for('auth.admin'))
