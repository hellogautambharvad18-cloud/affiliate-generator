#!/usr/bin/env python3
"""
Affiliate Website Generator — Desktop GUI
Run: python gui.py
"""
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import threading, json, os, sys, subprocess, time, shutil, tempfile
from pathlib import Path

SCRIPT_DIR  = Path(__file__).resolve().parent
CONFIG_FILE = SCRIPT_DIR / '.aff_config.json'
FLASK_PORT  = 5000
FLASK_URL   = f'http://127.0.0.1:{FLASK_PORT}'

# ── Light, modern palette ──
BG       = '#F5F7FB'
CARD     = '#FFFFFF'
BORDER   = '#E3E8F0'
TEXT     = '#1F2937'
MUTED    = '#6B7280'
PRIMARY  = '#2563EB'
PRIMARY_D= '#1D4ED8'
SUCCESS  = '#16A34A'
WARNING  = '#F59E0B'
ERROR    = '#DC2626'

FONT_FAMILY = 'Segoe UI'

DESIGNS = [
    ('1','Design 1 — BloodPril Editorial','Reference'),
    ('2','Design 2 — JellyTide Premium','Reference'),
    ('3','Design 3 — VapoCept Editorial','Reference'),
    ('4','Design 4 — BreathiZen Premium','Reference'),
    ('5','Design 5 — Gelagen Editorial','Reference'),
    ('6','Design 6 — Aurora (Auto-Themed)','Native'),
    ('7','Design 7 — MemoVolt Structured','Reference'),
    ('8','Design 8 — Clarity (Auto-Themed)','Native'),
    ('9','Design 9 — Bold (Auto-Themed)','Native'),
    ('10','Design 10 — Playful (Auto-Themed)','Native'),
    ('11','Design 11 — Surge (Auto-Themed)','Native'),
    ('12','Design 12 — Terra (Auto-Themed)','Native'),
    ('13','Design 13 — Verdict (Auto-Themed)','Native'),
    ('14','Design 14 — Teal Classic (Auto-Themed)','Native'),
]

# A small color per design just so the picker cards aren't all identical —
# purely decorative (no real per-design screenshot thumbnails exist to show).
_SWATCH = {
    '1':'#8B5CF6','2':'#7C3AED','3':'#0EA5E9','4':'#3B82F6','5':'#EC4899',
    '6':'#10B981','7':'#6366F1','8':'#06B6D4','9':'#F97316','10':'#F43F5E',
    '11':'#8B5CF6','12':'#65A30D','13':'#0F766E','14':'#0F6E7E',
}

# ── Image slot requirements, shared across every design — every design's
# generated HTML is built from the same MANUAL_SLOTS vocabulary in app.py
# (hero/bottle-2/3/6 always rendered in the pricing cards; the rest are
# optional sections/badges that each design shows IF an upload fills them,
# and otherwise either falls back automatically — reviewer photos become
# initials avatars, bonus/how-it-works sections are simply omitted — server
# side already, with no GUI action needed) or, for badges/guarantee/
# credit-cards on a NATIVE design specifically, has no bundled fallback at
# all and 404s without an upload — which is what the GUI's own fallback
# (badges/guarantee/credit-cards -> generated here) exists to prevent. ──
REQUIRED_IMAGES = {
    'required': ['hero', 'bottle-2', 'bottle-3', 'bottle-6'],
    'optional': ['how-it-works', 'reviewer-1', 'reviewer-2', 'reviewer-3',
                 'bonus-1', 'bonus-2', 'badge-fda', 'badge-gmp', 'badge-usa',
                 'badge-natural', 'guarantee', 'credit-cards', 'favicon'],
}
SLOT_HINTS = {
    'hero':'Main product shot (front of pricing/hero section)',
    'bottle-2':'2-bottle pack photo',
    'bottle-3':'3-bottle pack photo',
    'bottle-6':'6-bottle pack photo',
    'how-it-works':'Mechanism/how-it-works illustration (optional — falls back to a generated numbered-steps graphic)',
    'reviewer-1':'Reviewer 1 photo (optional — falls back to an initials avatar)',
    'reviewer-2':'Reviewer 2 photo (optional — falls back to an initials avatar)',
    'reviewer-3':'Reviewer 3 photo (optional — falls back to an initials avatar)',
    'bonus-1':'Bonus #1 cover image',
    'bonus-2':'Bonus #2 cover image',
    'badge-fda':'FDA-registered-facility badge',
    'badge-gmp':'GMP-certified badge',
    'badge-usa':'Made-in-USA badge',
    'badge-natural':'Natural-ingredients badge',
    'guarantee':'Money-back guarantee seal',
    'credit-cards':'Accepted payment methods strip',
    'favicon':'Browser-tab icon (falls back to a generated brand-letter icon)',
}
# Fallback chain — ONLY ever pulled from the publisher's own other uploads,
# never a template/bundled or different-product image.
BOTTLE_FALLBACK = {
    'bottle-2': ['bottle-3', 'bottle-6'],
    'bottle-3': ['bottle-2', 'bottle-6'],
    'bottle-6': ['bottle-3', 'bottle-2'],
}
HERO_FALLBACK = ['bottle-3', 'bottle-2', 'bottle-6']
# Slots the server already handles gracefully with no upload at all — no
# fallback FILE is ever needed for these, just a log line explaining what
# happens instead.
NO_FILE_NEEDED = {
    'reviewer-1':'initials avatar', 'reviewer-2':'initials avatar', 'reviewer-3':'initials avatar',
    'bonus-1':'bonus section omitted', 'bonus-2':'bonus section omitted',
    'how-it-works':'generated numbered-steps graphic (from the product\'s own how-it-works text)',
}
# Slots with no safe same-product fallback image — the SERVER generates one
# instead (generic badge/seal/payment-strip graphics, a brand-letter
# favicon, or a numbered-steps how-it-works infographic), the same way
# app.py's own make_fda_registered_badge()/generate_how_it_works_image() do.
GENERATED_FALLBACK = {'badge-fda','badge-gmp','badge-usa','badge-natural',
                       'guarantee','credit-cards','favicon','how-it-works'}


class PlaceholderEntry(tk.Entry):
    """Entry with placeholder text — .get() always returns real value."""
    def __init__(self, master, placeholder='', show_ch='', **kw):
        self._ph    = placeholder
        self._show  = show_ch
        self._empty = True
        super().__init__(master, **kw)
        self.config(fg=MUTED)
        if placeholder:
            self.insert(0, placeholder)
        self.bind('<FocusIn>',  self._on_in)
        self.bind('<FocusOut>', self._on_out)

    def _on_in(self, _=None):
        if self._empty:
            self.delete(0, 'end')
            self.config(fg=TEXT, show=self._show)
            self._empty = False

    def _on_out(self, _=None):
        if not super().get().strip():
            self._empty = True
            self.config(show='')
            self.delete(0, 'end')
            self.insert(0, self._ph)
            self.config(fg=MUTED)

    def get(self):
        return '' if self._empty else super().get().strip()

    def set(self, value):
        """Set value programmatically (for loading saved config)."""
        self.delete(0, 'end')
        if value:
            self._empty = False
            self.config(fg=TEXT, show=self._show)
            self.insert(0, value)
        else:
            self._empty = True
            self.config(fg=MUTED, show='')
            if self._ph:
                self.insert(0, self._ph)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Affiliate Website Generator')
        self.geometry('1060x900')
        self.minsize(860, 640)
        self.configure(bg=BG)
        self._flask_proc   = None
        self._imgfiles     = []
        self._fallback_tmp = []   # temp files created for auto-fill, cleaned up after each run
        self._cfg          = self._load_cfg()
        self._build()
        self.protocol('WM_DELETE_WINDOW', self._on_close)

    # ── Config ────────────────────────────────────────────────
    def _load_cfg(self):
        try:
            if CONFIG_FILE.exists():
                return json.loads(CONFIG_FILE.read_text(encoding='utf-8'))
        except Exception:
            pass
        return {}

    def _save_cfg(self):
        try:
            CONFIG_FILE.write_text(json.dumps({
                'anthropic_key': self.e_ant.get(),
                'openai_key':    self.e_oai.get(),
                'deepseek_key':  self.e_ds.get(),
                'serpapi_key':   self.e_serp.get(),
                'ai_provider':   self.v_prov.get(),
                'design':        self.v_design.get(),
                'image_source':  self.v_imgsrc.get(),
            }, indent=2), encoding='utf-8')
        except Exception:
            pass

    # ── Build UI ───────────────────────────────────────────────
    def _build(self):
        # Header
        hdr = tk.Frame(self, bg=CARD, pady=14, highlightthickness=1,
                        highlightbackground=BORDER)
        hdr.pack(fill='x')
        tk.Label(hdr, text='Affiliate Website Generator',
                 bg=CARD, fg=TEXT, font=(FONT_FAMILY,16,'bold')).pack(anchor='w', padx=24)
        tk.Label(hdr, text='Smart image placement  ·  Anthropic + OpenAI + DeepSeek  ·  Auto-save keys',
                 bg=CARD, fg=MUTED, font=(FONT_FAMILY,9)).pack(anchor='w', padx=24)

        body = tk.Frame(self, bg=BG)
        body.pack(fill='both', expand=True)

        # ── Left sidebar: steps (informational — the form below is one
        # continuous flow, these just orient the user on where they are) ──
        side = tk.Frame(body, bg=BG, width=190)
        side.pack(side='left', fill='y', padx=(16,8), pady=16)
        side.pack_propagate(False)
        tk.Label(side, text='STEPS', bg=BG, fg=MUTED,
                 font=(FONT_FAMILY,8,'bold')).pack(anchor='w', padx=4, pady=(0,6))
        self._step_labels = []
        for i, step in enumerate(['Product', 'Design', 'Images', 'Links & Keys', 'Generate']):
            f = tk.Frame(side, bg=BG)
            f.pack(fill='x', pady=3)
            dot = tk.Label(f, text=str(i+1), bg=BORDER, fg=TEXT, width=2,
                            font=(FONT_FAMILY,9,'bold'))
            dot.pack(side='left', padx=(2,8))
            lbl = tk.Label(f, text=step, bg=BG, fg=TEXT, font=(FONT_FAMILY,10), anchor='w')
            lbl.pack(side='left', fill='x', expand=True)
            self._step_labels.append((dot, lbl))

        # ── Right: scrollable main content ──
        outer = tk.Frame(body, bg=BG)
        outer.pack(side='left', fill='both', expand=True, padx=(8,16), pady=16)
        self._canvas = tk.Canvas(outer, bg=BG, highlightthickness=0)
        sb = ttk.Scrollbar(outer, orient='vertical', command=self._canvas.yview)
        self._canvas.configure(yscrollcommand=sb.set)
        sb.pack(side='right', fill='y')
        self._canvas.pack(side='left', fill='both', expand=True)
        self._frame = tk.Frame(self._canvas, bg=BG)
        self._cwin  = self._canvas.create_window((0,0), window=self._frame, anchor='nw')
        self._frame.bind('<Configure>', self._on_frame_cfg)
        self._canvas.bind('<Configure>', self._on_canvas_cfg)
        self.bind_all('<MouseWheel>',  self._on_wheel)
        self.bind_all('<Button-4>',    self._on_wheel)
        self.bind_all('<Button-5>',    self._on_wheel)

        P = self._frame

        # ── 01 Product ──
        c1 = self._card(P, '01  Product Details')
        r = self._row(c1)
        self._lbl(r, 'Product Name')
        self.e_product = self._entry(r, placeholder='e.g. ProDentim')
        rh = self._row(c1)
        self._lbl(rh, 'Description')
        self.e_hint = self._entry(rh, placeholder='e.g. Male vitality supplement with 7 botanicals (optional)')
        tk.Label(c1, text='Helps the AI when the product name alone doesn\'t indicate the category',
                 bg=CARD, fg=MUTED, font=(FONT_FAMILY,8)).pack(anchor='w', padx=(128,0), pady=(0,4))

        # ── 02 Design (thumbnail-card grid) ──
        c2 = self._card(P, '02  Design')
        self.v_design = tk.StringVar(value=self._cfg.get('design','1'))
        grid = tk.Frame(c2, bg=CARD)
        grid.pack(fill='x', pady=(4,0))
        self._design_cards = {}
        for i, (key, name, kind) in enumerate(DESIGNS):
            card = self._design_card(grid, key, name, kind)
            card.grid(row=i//3, column=i%3, padx=6, pady=6, sticky='nsew')
            self._design_cards[key] = card
        for col in range(3):
            grid.grid_columnconfigure(col, weight=1)
        self._refresh_design_cards()

        # ── 03 Images ──
        c3 = self._card(P, '03  Images')
        r7 = self._row(c3)
        self._lbl(r7, 'Image Source')
        self.v_imgsrc = tk.StringVar(value=self._cfg.get('image_source','both'))
        ttk.Combobox(r7, textvariable=self.v_imgsrc, state='readonly', width=20,
            values=['both','manual','serp','none']).pack(side='left', padx=(0,20))

        r8 = self._row(c3)
        self._lbl(r8, 'Upload Images')
        self._img_lbl = tk.Label(r8, text='No files selected', bg=BG,
                                  fg=MUTED, font=(FONT_FAMILY,9), padx=8, pady=5,
                                  anchor='w', width=28, highlightthickness=1,
                                  highlightbackground=BORDER)
        self._img_lbl.pack(side='left', padx=(0,8))
        self._btn(r8, 'Browse...', self._browse, primary=False).pack(side='left')
        self._btn(r8, 'Clear', self._clear_imgs, primary=False).pack(side='left', padx=(6,0))

        # Per-theme image requirements panel — rebuilt whenever the design
        # selection changes (see _refresh_requirements_panel).
        self._req_panel = tk.Frame(c3, bg=CARD)
        self._req_panel.pack(fill='x', pady=(10,0))
        self._refresh_requirements_panel()

        # ── 04 Links & Keys ──
        c4 = self._card(P, '04  Affiliate Link, Domain & AI Keys')
        r2 = self._row(c4)
        self._lbl(r2, 'Affiliate Link')
        self.e_affiliate = self._entry(r2, placeholder='https://...')
        rd = self._row(c4)
        self._lbl(rd, 'Your Domain')
        self.e_domain = self._entry(rd, placeholder='https://yoursite.com')

        r3 = self._row(c4)
        self._lbl(r3, 'AI Provider')
        self.v_prov = tk.StringVar(value=self._cfg.get('ai_provider','auto'))
        ttk.Combobox(r3, textvariable=self.v_prov, state='readonly', width=20,
            values=['auto','anthropic','openai','deepseek']).pack(side='left', padx=(0,20))

        r4 = self._row(c4)
        self._lbl(r4, 'Anthropic Key')
        self.e_ant  = self._entry(r4, placeholder='sk-ant-...', show='*')
        r5 = self._row(c4)
        self._lbl(r5, 'OpenAI Key')
        self.e_oai  = self._entry(r5, placeholder='sk-...', show='*')
        r6 = self._row(c4)
        self._lbl(r6, 'DeepSeek Key')
        self.e_ds   = self._entry(r6, placeholder='sk-...', show='*')
        r6b = self._row(c4)
        self._lbl(r6b, 'SerpAPI Key')
        self.e_serp = self._entry(r6b, placeholder='serpapi.com key', show='*')

        for entry, key in [(self.e_ant,'anthropic_key'),(self.e_oai,'openai_key'),
                           (self.e_ds,'deepseek_key'),(self.e_serp,'serpapi_key')]:
            val = self._cfg.get(key,'')
            if val:
                entry.set(val)
        tk.Label(c4, text='✓ Keys auto-saved — no need to re-enter each time',
                 bg=CARD, fg=SUCCESS, font=(FONT_FAMILY,9)).pack(anchor='w', padx=(128,0), pady=(4,0))

        # ── 05 Generate ──
        c5 = self._card(P, '05  Generate')
        self.btn = self._btn(c5, '⚡  Generate Website ZIP', self._generate, primary=True)
        self.btn.pack(fill='x', pady=(4,8))
        self.bar = ttk.Progressbar(c5, mode='indeterminate')
        self.bar.pack(fill='x')

        # ── Log ──
        c6 = self._card(P, 'Log')
        self.log = scrolledtext.ScrolledText(c6, bg='#F1F5F9', fg=TEXT,
                                              font=('Consolas',9), height=12,
                                              relief='flat', wrap='word',
                                              state='disabled', highlightthickness=1,
                                              highlightbackground=BORDER)
        self.log.pack(fill='both', expand=True, pady=(4,0))
        self.log.tag_config('ok',   foreground=SUCCESS)
        self.log.tag_config('err',  foreground=ERROR)
        self.log.tag_config('warn', foreground=WARNING)
        self.log.tag_config('dim',  foreground=MUTED)
        self._log('Ready — fill in details above and click Generate.', 'dim')

    # ── Scroll helpers ─────────────────────────────────────────
    def _on_frame_cfg(self, _):
        self._canvas.configure(scrollregion=self._canvas.bbox('all'))

    def _on_canvas_cfg(self, e):
        self._canvas.itemconfig(self._cwin, width=e.width)

    def _on_wheel(self, e):
        if e.num == 4:
            self._canvas.yview_scroll(-1, 'units')
        elif e.num == 5:
            self._canvas.yview_scroll(1, 'units')
        else:
            self._canvas.yview_scroll(-1*(e.delta//120), 'units')

    # ── Widget helpers ─────────────────────────────────────────
    def _card(self, p, title):
        wrap = tk.Frame(p, bg=BG)
        wrap.pack(fill='x', pady=(0,14))
        tk.Label(wrap, text=title, bg=BG, fg=TEXT,
                 font=(FONT_FAMILY,11,'bold')).pack(anchor='w', pady=(0,6))
        f = tk.Frame(wrap, bg=CARD, padx=18, pady=16, highlightthickness=1,
                     highlightbackground=BORDER)
        f.pack(fill='x')
        return f

    def _row(self, p):
        f = tk.Frame(p, bg=CARD)
        f.pack(fill='x', pady=4)
        return f

    def _lbl(self, p, text):
        tk.Label(p, text=text+':', bg=CARD, fg=MUTED,
                 font=(FONT_FAMILY,9), width=16, anchor='w').pack(side='left')

    def _entry(self, p, placeholder='', show=''):
        e = PlaceholderEntry(p, placeholder=placeholder, show_ch=show,
                             bg=BG, fg=TEXT, insertbackground=TEXT,
                             relief='flat', font=(FONT_FAMILY,10), width=34,
                             highlightthickness=1, highlightbackground=BORDER,
                             highlightcolor=PRIMARY)
        e.pack(side='left', padx=(0,16), ipady=6)
        return e

    def _btn(self, p, text, command, primary=True):
        if primary:
            b = tk.Button(p, text=text, bg=PRIMARY, fg='#FFFFFF', relief='flat',
                          activebackground=PRIMARY_D, activeforeground='#FFFFFF',
                          font=(FONT_FAMILY,11,'bold'), pady=10, padx=14,
                          cursor='hand2', command=command, bd=0)
        else:
            b = tk.Button(p, text=text, bg=BG, fg=TEXT, relief='flat',
                          activebackground=BORDER, font=(FONT_FAMILY,9), pady=6,
                          padx=10, cursor='hand2', command=command, bd=0,
                          highlightthickness=1, highlightbackground=BORDER)
        return b

    def _design_card(self, p, key, name, kind):
        selected = (self.v_design.get() == key)
        f = tk.Frame(p, bg=CARD, highlightthickness=2,
                     highlightbackground=(PRIMARY if selected else BORDER),
                     cursor='hand2')
        swatch = tk.Frame(f, bg=_SWATCH.get(key, PRIMARY), height=36)
        swatch.pack(fill='x')
        body = tk.Frame(f, bg=CARD, padx=8, pady=6)
        body.pack(fill='x')
        tk.Label(body, text=name, bg=CARD, fg=TEXT, font=(FONT_FAMILY,9,'bold'),
                 wraplength=180, justify='left').pack(anchor='w')
        tk.Label(body, text=kind, bg=BORDER, fg=MUTED, font=(FONT_FAMILY,8),
                 padx=6, pady=1).pack(anchor='w', pady=(4,0))
        for w in (f, swatch, body, *body.winfo_children()):
            w.bind('<Button-1>', lambda e, k=key: self._select_design(k))
        return f

    def _select_design(self, key):
        self.v_design.set(key)
        self._refresh_design_cards()
        self._refresh_requirements_panel()

    def _refresh_design_cards(self):
        cur = self.v_design.get()
        for key, card in self._design_cards.items():
            card.config(highlightbackground=(PRIMARY if key == cur else BORDER))

    def _log(self, msg, tag=''):
        self.log.config(state='normal')
        self.log.insert('end', msg+'\n', tag)
        self.log.see('end')
        self.log.config(state='disabled')

    def _clear_log(self):
        self.log.config(state='normal')
        self.log.delete('1.0','end')
        self.log.config(state='disabled')

    # ── Image requirements panel ────────────────────────────────
    def _uploaded_stems(self):
        return {Path(f).stem.lower() for f in self._imgfiles}

    def _refresh_requirements_panel(self):
        for w in self._req_panel.winfo_children():
            w.destroy()
        req = REQUIRED_IMAGES
        have = self._uploaded_stems()
        tk.Label(self._req_panel, text='Images this theme uses', bg=CARD, fg=TEXT,
                 font=(FONT_FAMILY,9,'bold')).pack(anchor='w', pady=(0,4))
        for slot in req['required'] + req['optional']:
            is_required = slot in req['required']
            got = slot in have
            if got:
                icon, color = '✓', SUCCESS
            elif is_required:
                icon, color = '⚠', ERROR
            else:
                icon, color = '○', MUTED
            row = tk.Frame(self._req_panel, bg=CARD)
            row.pack(fill='x', pady=1)
            tk.Label(row, text=icon, bg=CARD, fg=color, font=(FONT_FAMILY,9,'bold'),
                     width=2).pack(side='left')
            tk.Label(row, text=f'{slot}.*', bg=CARD, fg=TEXT, font=('Consolas',9),
                     width=16, anchor='w').pack(side='left')
            tag = 'required' if is_required else 'optional'
            tk.Label(row, text=f'({tag}) {SLOT_HINTS.get(slot,"")}', bg=CARD, fg=MUTED,
                     font=(FONT_FAMILY,8), anchor='w').pack(side='left', fill='x', expand=True)

    # ── Images ────────────────────────────────────────────────
    def _browse(self):
        files = filedialog.askopenfilenames(
            title='Select product images',
            filetypes=[('Images','*.jpg *.jpeg *.png *.webp *.gif'),('All','*.*')])
        if files:
            self._imgfiles = list(files)
            names = [Path(f).name for f in files]
            display = ', '.join(names[:3]) + (f'  +{len(names)-3} more' if len(names)>3 else '')
            self._img_lbl.config(text=display, fg=TEXT)
            self._log(f'Images selected: {", ".join(names)}', 'dim')
            if self.v_imgsrc.get() == 'none':
                self.v_imgsrc.set('manual')
                self._log('Image Source was "none" — switched to "manual" since you selected files.', 'warn')
            self._refresh_requirements_panel()

    def _clear_imgs(self):
        self._imgfiles = []
        self._img_lbl.config(text='No files selected', fg=MUTED)
        self._refresh_requirements_panel()

    # ── Auto-fill fallback (only from the publisher's own uploads, or a
    # freshly generated generic graphic for badge/guarantee/credit-cards/
    # favicon — never a template/bundled or different-product image) ──
    def _build_fallback_plan(self):
        have = self._uploaded_stems()
        missing_required = [s for s in REQUIRED_IMAGES['required'] if s not in have]
        if not missing_required:
            return []
        plan = []  # (slot, action, detail)
        path_by_stem = {Path(f).stem.lower(): f for f in self._imgfiles}
        for slot in missing_required:
            if slot == 'hero':
                src = next((path_by_stem[s] for s in HERO_FALLBACK if s in path_by_stem), None)
                if src:
                    plan.append((slot, 'copy', src))
                    continue
            if slot in BOTTLE_FALLBACK:
                src = next((path_by_stem[s] for s in BOTTLE_FALLBACK[slot] if s in path_by_stem), None)
                if src:
                    plan.append((slot, 'copy', src))
                    continue
            if self._imgfiles:
                plan.append((slot, 'copy', self._imgfiles[0]))
            else:
                plan.append((slot, 'none', None))
        return plan

    def _apply_fallback_plan(self, plan):
        """Materialize the plan as real temp files named for their slot, so
        the server's own filename-based slot matching picks them up exactly
        like a real upload would. Returns the summary lines for the log."""
        summary = []
        for slot, action, detail in plan:
            if action == 'copy' and detail:
                ext = Path(detail).suffix or '.jpg'
                tmp = Path(tempfile.gettempdir()) / f'{slot}_fallback_{os.getpid()}{ext}'
                try:
                    shutil.copy2(detail, tmp)
                    self._imgfiles.append(str(tmp))
                    self._fallback_tmp.append(tmp)
                    summary.append(f'  {slot}.* <- fallback from {Path(detail).name}')
                except Exception as e:
                    summary.append(f'  {slot}.* <- fallback FAILED ({e})')
            else:
                summary.append(f'  {slot}.* <- no uploads available to fall back to; section will be omitted')
        return summary

    def _cleanup_fallback_tmp(self):
        for p in self._fallback_tmp:
            try: p.unlink(missing_ok=True)
            except Exception: pass
        self._fallback_tmp = []

    def _log_image_summary(self):
        have = self._uploaded_stems()
        user_slots = [s for s in REQUIRED_IMAGES['required']+REQUIRED_IMAGES['optional'] if s in have]
        if user_slots:
            self._log(f'Images from your uploads: {", ".join(user_slots)}', 'dim')
        for slot, note in NO_FILE_NEEDED.items():
            if slot not in have:
                self._log(f'  {slot}.* not supplied -> {note}', 'dim')

    # ── Generate ──────────────────────────────────────────────
    def _generate(self):
        product   = self.e_product.get()
        hint      = self.e_hint.get()
        affiliate = self.e_affiliate.get()
        domain    = self.e_domain.get()

        if not product:
            messagebox.showerror('Missing', 'Enter Product Name'); return
        if not affiliate or not affiliate.startswith('http'):
            messagebox.showerror('Missing', 'Affiliate Link must start with http://'); return
        if not domain or not domain.startswith('http'):
            messagebox.showerror('Missing', 'Domain must start with http://'); return

        ant  = self.e_ant.get()
        oai  = self.e_oai.get()
        ds   = self.e_ds.get()
        serp = self.e_serp.get()

        if not ant and not oai and not ds:
            messagebox.showerror('API Key',
                'Enter at least one AI key:\nAnthropic, OpenAI, or DeepSeek'); return

        if self._imgfiles and self.v_imgsrc.get() == 'none':
            self.v_imgsrc.set('manual')

        # Required-image check — offer to auto-fill from the publisher's own
        # other uploads before generating, rather than silently shipping a
        # broken/missing pricing-card image.
        plan = self._build_fallback_plan()
        if plan:
            missing_names = ', '.join(s for s, _, _ in plan)
            if not messagebox.askyesno('Missing images',
                    f'{missing_names} missing — auto-fill from your other uploads?'):
                return
            fallback_summary = self._apply_fallback_plan(plan)
        else:
            fallback_summary = []

        self._save_cfg()
        self.btn.config(state='disabled', text='⏳  Generating...', bg=BORDER, fg=TEXT)
        self.bar.start(8)
        self._clear_log()
        design_name = next(n for k,n,_ in DESIGNS if k == self.v_design.get())
        self._log(f'Product: {product}')
        self._log(f'Design: {design_name}')
        self._log(f'Images: {self.v_imgsrc.get()} | Files: {len(self._imgfiles)}', 'dim')
        for line in fallback_summary:
            self._log(line, 'warn')
        self._log_image_summary()

        imgfiles = list(self._imgfiles)
        design   = self.v_design.get()
        imgsrc   = self.v_imgsrc.get()
        prov     = self.v_prov.get()

        threading.Thread(
            target=self._worker,
            args=(product, hint, affiliate, domain, ant, oai, ds, serp, prov, design, imgsrc, imgfiles),
            daemon=True).start()

    def _worker(self, product, hint, affiliate, domain, ant, oai, ds, serp,
                prov, design, imgsrc, imgfiles):
        try:
            # 1. Ensure Flask running
            self._start_flask()

            import requests as req

            # 2. Build request
            data = {
                'product_name':      product,
                'product_hint':      hint,
                'affiliate_link':    affiliate,
                'domain':            domain,
                'ai_provider':       prov,
                'anthropic_api_key': ant,
                'openai_api_key':    oai,
                'deepseek_api_key':  ds,
                'serp_api_key':      serp,
                'design':            design,
                'image_source':      imgsrc,
            }

            file_handles = []
            files_arg    = []
            for fp in imgfiles:
                fh = open(fp, 'rb')
                file_handles.append(fh)
                files_arg.append(('images', (Path(fp).name, fh, 'image/jpeg')))

            self.after(0, lambda: self._log('Calling AI & building pages...', 'dim'))

            r = req.post(f'{FLASK_URL}/api/generate',
                         data=data,
                         files=files_arg if files_arg else None,
                         timeout=360)

            for fh in file_handles:
                fh.close()
            self._cleanup_fallback_tmp()

            if r.status_code != 200:
                try:   err = r.json().get('error', r.text[:200])
                except Exception: err = r.text[:200]
                self.after(0, lambda err=err: self._show_err(err))
                return

            # 3. Save file — must happen on main thread (filedialog)
            content = r.content
            fname   = f'{product.lower().replace(" ","-")}-affiliate-site.zip'
            self.after(0, lambda: self._save_result(content, fname))

        except Exception as ex:
            self._cleanup_fallback_tmp()
            msg = str(ex)
            self.after(0, lambda msg=msg: self._show_err(msg))

    def _save_result(self, content, fname):
        """Called on main thread — shows save dialog."""
        path = filedialog.asksaveasfilename(
            defaultextension='.zip',
            initialfile=fname,
            filetypes=[('ZIP file','*.zip')],
            title='Save generated website ZIP')
        if path:
            try:
                Path(path).write_bytes(content)
                self._log(f'✅ Saved: {path}', 'ok')
                messagebox.showinfo('Done!', f'ZIP saved:\n{path}')
            except Exception as e:
                self._show_err(str(e))
        else:
            self._log('Save cancelled.', 'warn')
        self._done()

    def _show_err(self, msg):
        self._log(f'❌ {msg}', 'err')
        messagebox.showerror('Error', msg)
        self._done()

    def _done(self):
        self.bar.stop()
        self.btn.config(state='normal', text='⚡  Generate Website ZIP', bg=PRIMARY, fg='#FFFFFF')

    # ── Flask ─────────────────────────────────────────────────
    def _start_flask(self):
        import requests as req
        try:
            req.get(FLASK_URL, timeout=2); return
        except Exception:
            pass
        self.after(0, lambda: self._log('Starting Flask server...', 'dim'))
        self._flask_proc = subprocess.Popen(
            [sys.executable, str(SCRIPT_DIR/'app.py')],
            cwd=str(SCRIPT_DIR),
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL)
        for _ in range(20):
            time.sleep(1)
            try:
                req.get(FLASK_URL, timeout=1)
                self.after(0, lambda: self._log('Flask ready.', 'dim'))
                return
            except Exception:
                pass
        raise RuntimeError(
            'Flask server did not start.\n'
            'Run "python app.py" in terminal first, then try again.')

    def _on_close(self):
        self._cleanup_fallback_tmp()
        if self._flask_proc:
            try: self._flask_proc.terminate()
            except Exception: pass
        self.destroy()


if __name__ == '__main__':
    root = App()
    # Apply ttk styles after Tk is created
    st = ttk.Style(root)
    try:    st.theme_use('clam')
    except Exception: pass
    st.configure('TCombobox',      fieldbackground=CARD, background=CARD,
                 foreground=TEXT, selectbackground=PRIMARY, selectforeground='#FFFFFF')
    st.configure('TScrollbar',     background=BORDER, troughcolor=BG, arrowcolor=MUTED)
    st.configure('TProgressbar',   troughcolor=BORDER, background=PRIMARY)
    st.map('TCombobox', fieldbackground=[('readonly', CARD)],
           foreground=[('readonly', TEXT)])
    root.mainloop()
