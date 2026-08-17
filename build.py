#!/usr/bin/env python3
"""Build the Sphynx Motion card into two outputs from the files in assets/:
   - sphynx-card.html : self-contained single file (offline / claude.ai artifact)
   - index.html       : same card wrapped as an installable PWA (GitHub Pages)
Run: python3 build.py
"""
import base64, pathlib

ROOT = pathlib.Path(__file__).parent
A = ROOT / "assets"

fonts    = (A / "fonts-embedded.css").read_text()
logo_b64 = base64.b64encode((A / "logo.png").read_bytes()).decode()
av_b64   = base64.b64encode((A / "avatar-cropped.jpg").read_bytes()).decode()
qr_card  = (A / "qr-card.svg").read_text()      # hero QR -> the card's own public URL
qr_vcard = (A / "qr-contact.svg").read_text()   # save-contact vCard QR

CHEV = ('<span class="go" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" '
        'stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
        '<path d="M9 6l6 6-6 6"/></svg></span>')

STYLE = f"""<style>
{fonts}
:root{{
  --bg:#08080A; --bg2:#0C0C10; --surface:#111114; --surface-el:#1A1A1F;
  --border:rgba(255,255,255,.06); --border-2:rgba(255,255,255,.12);
  --text:#F0EDE8; --muted:#6B6872; --muted-2:#4A4852;
  --accent:#E8181E; --accent-2:#FF6B6E;
  --paper:#F0EDE8; --paper-ink:#0B0B0D;
  --display:'Fraunces',Georgia,serif; --ui:'Plus Jakarta Sans',system-ui,sans-serif;
}}
*{{box-sizing:border-box}}
html{{-webkit-text-size-adjust:100%}}
body{{margin:0;min-height:100dvh;background:var(--bg);color:var(--text);
  font-family:var(--ui);-webkit-font-smoothing:antialiased;
  display:flex;align-items:safe center;justify-content:center;
  padding:26px 16px;position:relative;overflow-x:hidden}}
.atmos{{position:fixed;inset:0;z-index:0;pointer-events:none;overflow:hidden}}
.glow{{position:absolute;border-radius:50%;filter:blur(90px);will-change:transform}}
.glow.a{{width:460px;height:460px;top:-180px;left:50%;margin-left:-230px;
  background:radial-gradient(circle,rgba(232,24,30,.16),transparent 68%);animation:drift 26s ease-in-out infinite}}
.glow.b{{width:420px;height:420px;bottom:-200px;right:-160px;background:radial-gradient(circle,rgba(232,24,30,.07),transparent 70%)}}
.grain{{position:absolute;inset:0;opacity:.04;mix-blend-mode:soft-light;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='140' height='140'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}}
@keyframes drift{{0%,100%{{transform:translate(0,0)}}50%{{transform:translate(-30px,30px)}}}}

.card{{position:relative;z-index:1;width:100%;max-width:404px;
  background:linear-gradient(180deg,var(--surface),var(--bg2));
  border:1px solid var(--border);border-radius:24px;padding:30px 28px 24px;
  box-shadow:0 1px 0 rgba(255,255,255,.04) inset,0 40px 90px -40px rgba(0,0,0,.95),0 0 0 1px rgba(0,0,0,.5);
  opacity:0;transform:translateY(14px);animation:rise .85s cubic-bezier(.2,.7,.2,1) .05s forwards}}
@keyframes rise{{to{{opacity:1;transform:none}}}}

.logo{{display:block;height:26px;width:auto;margin:2px auto 22px;opacity:.96}}
.hero{{display:flex;flex-direction:column;align-items:center;text-align:center}}
.avatar{{width:104px;height:104px;border-radius:50%;object-fit:cover;border:1px solid var(--border-2);
  box-shadow:0 0 0 4px rgba(232,24,30,.14),0 16px 34px -14px rgba(0,0,0,.9)}}
.name{{font-family:var(--display);font-weight:560;font-optical-sizing:auto;font-size:31px;line-height:1.08;letter-spacing:-.015em;margin:16px 0 6px;text-wrap:balance}}
.role{{font-size:11px;font-weight:600;letter-spacing:.22em;text-transform:uppercase;color:var(--muted);margin:0}}
.role .dot{{color:var(--accent)}}
.rule{{height:1px;margin:22px 0;background:linear-gradient(to right,transparent,var(--accent),transparent);opacity:.6}}

.qr-wrap{{background:var(--paper);border-radius:16px;padding:16px 16px 14px;display:flex;flex-direction:column;align-items:center;gap:11px;box-shadow:0 16px 40px -20px rgba(0,0,0,.85);position:relative}}
.qr-wrap::before{{content:"";position:absolute;top:0;left:22%;right:22%;height:2px;background:var(--accent);border-radius:2px}}
.qr{{width:172px;height:172px;color:var(--paper-ink);display:block}}
.qr svg{{width:100%;height:100%;display:block}}
.qr-cap{{display:flex;align-items:center;gap:7px;font-size:10.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:#3a3833}}
.qr-cap svg{{width:13px;height:13px;color:var(--accent)}}
.qr-url{{font-size:12px;color:#6f6a60;letter-spacing:.01em;font-weight:500}}

.links{{display:flex;flex-direction:column;gap:8px}}
.link{{display:flex;align-items:center;gap:13px;padding:12px 14px;border-radius:13px;text-decoration:none;color:var(--text);width:100%;text-align:left;font-family:var(--ui);font-size:inherit;cursor:pointer;
  background:linear-gradient(135deg,var(--surface-el),var(--surface));border:1px solid var(--border);
  transition:border-color .22s,transform .12s,box-shadow .22s,background .22s}}
.ic{{width:38px;height:38px;border-radius:10px;flex:none;display:grid;place-items:center;color:var(--text);background:rgba(255,255,255,.04);border:1px solid var(--border);transition:color .22s,background .22s,border-color .22s}}
.ic svg{{width:19px;height:19px;display:block}}
.lt{{display:flex;flex-direction:column;line-height:1.25;min-width:0}}
.lt .k{{font-size:14px;font-weight:600}}
.lt .v{{font-size:12px;color:var(--muted);overflow:hidden;text-overflow:ellipsis;white-space:nowrap;transition:color .22s}}
.go{{margin-left:auto;color:var(--muted-2);flex:none;transition:color .22s,transform .28s ease}}
.go svg{{width:16px;height:16px;display:block}}

.link:hover,.link:active,.link.primary{{
  background:linear-gradient(135deg,rgba(255,58,63,.96),rgba(214,16,22,.96));
  border-color:rgba(255,255,255,.38);
  box-shadow:0 12px 34px -12px rgba(232,24,30,.62),inset 0 1px 0 rgba(255,255,255,.4),inset 0 0 0 1px rgba(255,255,255,.06);
  transform:translateY(-1px)}}
.link.primary{{transform:none}}
.link:hover .lt .k,.link:active .lt .k,.link.primary .lt .k,
.link:hover .lt .v,.link:active .lt .v,.link.primary .lt .v,
.link:hover .go,.link:active .go,.link.primary .go{{color:#fff}}
.link:hover .ic,.link:active .ic,.link.primary .ic{{color:#fff;background:rgba(255,255,255,.20);border-color:rgba(255,255,255,.5);box-shadow:inset 0 1px 0 rgba(255,255,255,.5)}}
.link:focus-visible{{outline:2px solid #fff;outline-offset:2px}}
.link.primary:focus-visible{{outline:2px solid var(--accent-2)}}
.link.primary[aria-expanded="true"] .go{{transform:rotate(90deg)}}

.savepanel{{overflow:hidden;max-height:0;opacity:0;transition:max-height .42s cubic-bezier(.2,.7,.2,1),opacity .3s ease,margin-top .3s ease;margin-top:0}}
.savepanel.open{{max-height:360px;opacity:1;margin-top:8px}}
.savecard{{background:var(--paper);border-radius:14px;padding:16px;display:flex;flex-direction:column;align-items:center;gap:9px;position:relative}}
.savecard::before{{content:"";position:absolute;top:0;left:26%;right:26%;height:2px;background:var(--accent);border-radius:2px}}
.savecard .qr{{width:186px;height:186px}}
.savecard .cap{{font-size:11px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#3a3833;text-align:center}}
.savecard .sub{{font-size:11.5px;color:#6f6a60;text-align:center;font-weight:500}}

footer{{margin-top:20px;text-align:center;font-size:10px;letter-spacing:.2em;text-transform:uppercase;color:var(--muted-2)}}
footer b{{color:var(--muted);font-weight:600}}

@media (max-width:360px){{.card{{padding:26px 20px 20px}}.name{{font-size:28px}}.qr{{width:154px;height:154px}}}}
@media (prefers-reduced-motion:reduce){{.glow{{animation:none}}.card{{animation:none;opacity:1;transform:none}}.savepanel{{transition:none}}}}
</style>"""

BODY = f"""<div class="atmos" aria-hidden="true"><div class="glow a"></div><div class="glow b"></div><div class="grain"></div></div>

<main class="card">
  <img class="logo" alt="Sphynx Motion" src="data:image/png;base64,{logo_b64}">
  <div class="hero">
    <img class="avatar" alt="Davies Bassey A." src="data:image/jpeg;base64,{av_b64}">
    <h1 class="name">Davies Bassey A.</h1>
    <p class="role">Cinematic Motion <span class="dot">&middot;</span> Brand Film</p>
  </div>

  <div class="rule"></div>

  <div class="qr-wrap">
    <div class="qr">{qr_card}</div>
    <div class="qr-cap"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><path d="M14 14h3v3M20 14v.01M14 20v.01M20 20v.01M17 17h.01"/></svg> Scan to open my card</div>
    <div class="qr-url">Contact &middot; links &middot; socials</div>
  </div>

  <div class="rule"></div>

  <div class="links">
    <button class="link primary" id="saveBtn" type="button" aria-expanded="false" aria-controls="savePanel">
      <span class="ic" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H7a4 4 0 0 0-4 4v2"/><circle cx="9.5" cy="7" r="4"/><path d="M19 8v6M22 11h-6"/></svg></span>
      <span class="lt"><span class="k">Save contact</span><span class="v">Scan to add me to your phone</span></span>
      {CHEV}
    </button>

    <div class="savepanel" id="savePanel">
      <div class="savecard">
        <div class="qr" style="color:var(--paper-ink)">{qr_vcard}</div>
        <div class="cap">Point your camera here</div>
        <div class="sub">Davies Bassey A. &middot; Sphynx Motion</div>
      </div>
    </div>

    <a class="link" href="https://wa.me/27721830433" target="_blank" rel="noopener">
      <span class="ic" aria-hidden="true"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2 22l5.25-1.38c1.45.79 3.08 1.21 4.79 1.21 5.46 0 9.91-4.45 9.91-9.91C21.95 6.45 17.5 2 12.04 2zm5.8 14.02c-.24.68-1.2 1.26-1.97 1.42-.53.11-1.22.2-3.56-.76-2.99-1.24-4.91-4.27-5.06-4.47-.15-.2-1.21-1.61-1.21-3.07 0-1.46.77-2.18 1.04-2.48.27-.3.59-.37.79-.37.2 0 .39.01.56.02.18 0 .42-.07.66.5.24.58.83 2.01.9 2.16.07.15.12.32.02.52-.09.2-.14.32-.28.5-.14.17-.29.38-.42.51-.14.14-.28.29-.12.57.16.27.72 1.19 1.55 1.93 1.06.95 1.96 1.24 2.24 1.38.27.14.43.12.59-.07.16-.2.68-.79.86-1.06.18-.27.36-.22.61-.13.24.09 1.55.73 1.82.86.27.14.45.2.51.31.06.11.06.64-.18 1.32z"/></svg></span>
      <span class="lt"><span class="k">WhatsApp</span><span class="v">+27 72 183 0433</span></span>
      {CHEV}
    </a>

    <a class="link" href="mailto:info@sphynxmotion.com">
      <span class="ic" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="M4 7l8 6 8-6"/></svg></span>
      <span class="lt"><span class="k">Email</span><span class="v">info@sphynxmotion.com</span></span>
      {CHEV}
    </a>

    <a class="link" href="https://www.sphynxmotion.com" target="_blank" rel="noopener">
      <span class="ic" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.5 3.8 5.7 3.8 9s-1.3 6.5-3.8 9c-2.5-2.5-3.8-5.7-3.8-9S9.5 5.5 12 3z"/></svg></span>
      <span class="lt"><span class="k">Website</span><span class="v">sphynxmotion.com</span></span>
      {CHEV}
    </a>

    <a class="link" href="https://instagram.com/davies.bassey" target="_blank" rel="noopener">
      <span class="ic" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.4" cy="6.6" r="1.1" fill="currentColor" stroke="none"/></svg></span>
      <span class="lt"><span class="k">Instagram</span><span class="v">@davies.bassey</span></span>
      {CHEV}
    </a>

    <a class="link" href="https://www.tiktok.com/@daviesbassey" target="_blank" rel="noopener">
      <span class="ic" aria-hidden="true"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M16.5 3c.3 2.1 1.6 3.6 3.5 3.9v2.6c-1.3.05-2.5-.32-3.6-1v5.9c0 3.4-2.7 5.9-5.9 5.6-2.7-.25-4.8-2.5-4.8-5.2 0-3.2 3-5.6 6.1-4.9v2.7c-.4-.13-.85-.18-1.3-.1-1.1.18-1.9 1.1-1.9 2.2 0 1.3 1.1 2.3 2.4 2.2 1.2-.1 2.1-1.1 2.1-2.4V3h3.4z"/></svg></span>
      <span class="lt"><span class="k">TikTok</span><span class="v">@daviesbassey</span></span>
      {CHEV}
    </a>

    <a class="link" href="https://www.youtube.com/@sphynx-motion" target="_blank" rel="noopener">
      <span class="ic" aria-hidden="true"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M22 8.2a3 3 0 0 0-2.1-2.1C18.1 5.6 12 5.6 12 5.6s-6.1 0-7.9.5A3 3 0 0 0 2 8.2 31 31 0 0 0 1.7 12 31 31 0 0 0 2 15.8a3 3 0 0 0 2.1 2.1c1.8.5 7.9.5 7.9.5s6.1 0 7.9-.5a3 3 0 0 0 2.1-2.1c.3-1.25.3-3.8.3-3.8s0-2.55-.3-3.8zM10 15V9l5.2 3z"/></svg></span>
      <span class="lt"><span class="k">YouTube</span><span class="v">@sphynx-motion</span></span>
      {CHEV}
    </a>

    <a class="link" href="https://x.com/Larochelle_smit" target="_blank" rel="noopener">
      <span class="ic" aria-hidden="true"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.5 3h3l-6.6 7.6L21.8 21h-5.9l-4.3-5.6L6.6 21H3.5l7-8L2.6 3h6l3.9 5.2L17.5 3zm-1 16h1.6L7.5 4.7H5.8L16.5 19z"/></svg></span>
      <span class="lt"><span class="k">X (Twitter)</span><span class="v">@Larochelle_smit</span></span>
      {CHEV}
    </a>
  </div>

  <footer><b>Sphynx&nbsp;Motion</b> &nbsp;&middot;&nbsp; Scan &middot; Tap &middot; Connect</footer>
</main>

<script>
(function(){{
  var btn=document.getElementById("saveBtn"),panel=document.getElementById("savePanel");
  if(btn&&panel){{btn.addEventListener("click",function(){{
    var open=panel.classList.toggle("open");
    btn.setAttribute("aria-expanded",open?"true":"false");
    if(open)panel.scrollIntoView({{block:"nearest",behavior:"smooth"}});
  }});}}
}})();
</script>"""

# 1) self-contained single file (artifact / offline)
standalone = f"<title>Sphynx Motion Card</title>\n{STYLE}\n\n{BODY}\n"
(ROOT / "sphynx-card.html").write_text(standalone)

# 2) installable PWA for GitHub Pages
head_extra = """<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Davies Bassey A. — Sphynx Motion. Cinematic motion & brand film.">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#08080A">
<link rel="manifest" href="manifest.webmanifest">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Sphynx">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
<link rel="icon" type="image/png" sizes="512x512" href="icons/icon-512.png">
<style>html,body{background:#08080A}</style>"""
pwa = ("<!doctype html>\n<html lang=\"en\">\n<head>\n<title>Sphynx Motion Card</title>\n"
       + head_extra + "\n" + STYLE + "\n</head>\n<body>\n" + BODY + "\n</body>\n</html>\n")
(ROOT / "index.html").write_text(pwa)

print("wrote sphynx-card.html and index.html")
