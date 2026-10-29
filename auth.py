"""Access control for the hosted version of the generator.

Enabled only when ADMIN_PASSWORD is set, so running locally (gui.py / python
app.py) behaves exactly as before. When enabled:

* the owner logs in with ADMIN_PASSWORD and can open /admin
* friends log in with an access code the owner creates in /admin; each code
  carries an expiry date and an optional per-day generation limit
* codes are signed (stateless), so no database is needed on a free host
* a code can be revoked early by adding its id to the REVOKED_CODES env var
"""
import os,time,hmac,hashlib,secrets
from datetime import datetime,timezone,timedelta
from flask import (Blueprint,request,session,redirect,render_template,
                   jsonify,url_for,g)
from itsdangerous import URLSafeSerializer,BadSignature

ADMIN_PASSWORD=os.getenv('ADMIN_PASSWORD','').strip()
ENABLED=bool(ADMIN_PASSWORD)
HOSTED=ENABLED or os.getenv('HOSTED','')=='1'

bp=Blueprint('auth',__name__)

PUBLIC_ENDPOINTS={'auth.landing','auth.login','auth.logout','auth.healthz','static'}
# Endpoints that spend the owner's AI credit and therefore count toward a
# friend's daily limit. Phase 2 (/api/generate) reuses phase 1's content and
# only calls the AI when the browser didn't send it, so counting phase 1 is
# the accurate measure of "one website".
METERED_ENDPOINTS={'generate_content'}

_attempts={}   # ip -> [timestamps] for login throttling
_usage={}      # (code id, YYYY-MM-DD) -> count; best effort, resets on restart


def _secret():
    return (os.getenv('SECRET_KEY','').strip()
            or hashlib.sha256(('affgen:'+ADMIN_PASSWORD).encode()).hexdigest())


def init(app):
    app.secret_key=_secret()
    app.config.update(
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_SAMESITE='Lax',
        SESSION_COOKIE_SECURE=os.getenv('COOKIE_SECURE','1' if HOSTED else '0')=='1',
    )
    if HOSTED:
        app.config['MAX_CONTENT_LENGTH']=int(os.getenv('MAX_UPLOAD_MB','40'))*1024*1024
    if HOSTED:
        from werkzeug.middleware.proxy_fix import ProxyFix
        app.wsgi_app=ProxyFix(app.wsgi_app,x_for=1,x_proto=1,x_host=1)
    app.jinja_env.filters['datetimeformat']=lambda ts:datetime.fromtimestamp(ts,timezone.utc).strftime('%d %b %Y')
    app.register_blueprint(bp)
    app.before_request(_gate)


def _signer():
    return URLSafeSerializer(_secret(),salt='friend-access')


def _revoked():
    return {x.strip() for x in os.getenv('REVOKED_CODES','').split(',') if x.strip()}


TEMPLATES={}   # set by app.py; {design id: {'name':...}}


def make_code(name,days,daily_cap,designs=()):
    exp=int((datetime.now(timezone.utc)+timedelta(days=days)).timestamp())
    cid=secrets.token_hex(3)
    return _signer().dumps({'i':cid,'n':name,'e':exp,'c':daily_cap,'d':list(designs)}),cid,exp


def allowed_designs():
    """Design ids the current user may use, or None for no restriction."""
    u=current()
    if not ENABLED or not u or u['role']=='admin':
        return None
    return u.get('d') or None


def current():
    """The logged-in user as a dict, or None. Re-validates expiry/revocation
    on every request so a revoked or expired friend is cut off immediately."""
    if not ENABLED:
        return {'role':'admin','name':'local'}
    u=session.get('u')
    if not u:
        return None
    if u['role']=='friend':
        if u['e']<time.time() or u['i'] in _revoked():
            session.clear()
            return None
    return u


def is_admin():
    u=current()
    return bool(u and u['role']=='admin')


def _client_ip():
    return request.remote_addr or '?'


def _throttled():
    now=time.time()
    hits=[t for t in _attempts.get(_client_ip(),[]) if now-t<300]
    _attempts[_client_ip()]=hits
    return len(hits)>=8


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
    if request.endpoint=='admin' or (request.endpoint or '').startswith('auth.admin'):
        if u['role']!='admin':
            return redirect(url_for('index'))
    if u['role']=='friend' and request.method=='POST' and request.endpoint=='generate':
        allowed=u.get('d')
        if allowed and request.form.get('design','1') not in allowed:
            return jsonify(error='This design is not included in your access. Pick one of your allowed designs.'),403
    if u['role']=='friend' and request.method=='POST' and request.endpoint in METERED_ENDPOINTS:
        cap=u.get('c') or 0
        if cap:
            key=(u['i'],datetime.now(timezone.utc).strftime('%Y-%m-%d'))
            if _usage.get(key,0)>=cap:
                return jsonify(error=f'Daily limit reached ({cap} websites per day). Try again tomorrow.'),429
            _usage[key]=_usage.get(key,0)+1
    return None


@bp.get('/')
def landing():
    if not ENABLED:
        return redirect(url_for('index'))
    if current():
        return redirect(url_for('index'))
    return render_template('landing.html')


@bp.get('/healthz')
def healthz():
    return 'ok'


@bp.route('/login',methods=['GET','POST'])
def login():
    if not ENABLED:
        return redirect(url_for('index'))
    error=''
    if request.method=='POST':
        if _throttled():
            error='Too many attempts. Wait a few minutes and try again.'
        else:
            code=request.form.get('code','').strip()
            _attempts.setdefault(_client_ip(),[]).append(time.time())
            if code and hmac.compare_digest(code.encode(),ADMIN_PASSWORD.encode()):
                session.clear()
                session['u']={'role':'admin','name':'Owner'}
                session.permanent=True
                return redirect(request.args.get('next') or url_for('index'))
            try:
                d=_signer().loads(code)
                if d['e']<time.time():
                    error='This access code has expired. Ask the owner for a new one.'
                elif d['i'] in _revoked():
                    error='This access code has been revoked.'
                else:
                    session.clear()
                    session['u']={'role':'friend','name':d['n'],'i':d['i'],'e':d['e'],'c':d.get('c',0),'d':d.get('d',[])}
                    session.permanent=True
                    return redirect(url_for('index'))
            except (BadSignature,KeyError,TypeError):
                error='Invalid access code.'
    return render_template('login.html',error=error)


@bp.post('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.landing'))


@bp.route('/admin',methods=['GET','POST'])
def admin():
    if not is_admin():
        return redirect(url_for('auth.login'))
    created=None
    if request.method=='POST':
        name=(request.form.get('name','').strip() or 'Friend')[:40]
        try:days=max(1,min(int(request.form.get('days','7')),365))
        except ValueError:days=7
        try:cap=max(0,min(int(request.form.get('cap','3')),100))
        except ValueError:cap=3
        picked=[k for k in request.form.getlist('designs') if k in TEMPLATES]
        code,cid,exp=make_code(name,days,cap,picked)
        created={'name':name,'code':code,'id':cid,'days':days,'cap':cap,
                 'designs':[TEMPLATES[k]['name'] for k in picked],
                 'expires':datetime.fromtimestamp(exp,timezone.utc).strftime('%d %b %Y'),
                 'link':request.url_root.rstrip('/')+url_for('auth.login')}
    return render_template('admin.html',created=created,revoked=sorted(_revoked()),templates=TEMPLATES)
