import sys, os, shutil
sys.path.insert(0, "/home/claude/web")
import blog
SITE = blog.SITE
CSS = """
.g-wrap{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:48px;align-items:start;padding-block:40px}
.g-cover img{width:100%;max-width:420px;box-shadow:0 20px 60px rgba(0,0,0,.5);display:block}
.g-text h1{font-family:var(--display);font-weight:400;font-size:clamp(2.4rem,6vw,4rem);line-height:1;margin:8px 0 16px}
.g-text .lead{font-size:1.1rem;color:var(--fg);max-width:52ch}
.g-text ul{color:#c9c5be;padding-left:20px;margin:18px 0 26px}
.g-text li{margin-bottom:6px}
.g-form{border:1px solid var(--accent);background:var(--surface);padding:24px;display:flex;flex-direction:column;gap:12px;max-width:460px}
.g-form label{font:12px var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.g-form input[type=text],.g-form input[type=email]{width:100%;background:#0b0f12;border:1px solid var(--line);color:var(--fg);font:1rem var(--body);padding:12px;margin-top:6px;box-sizing:border-box}
.g-form .chk{display:flex;gap:10px;align-items:flex-start;font:.88rem var(--body);text-transform:none;letter-spacing:0;color:var(--muted)}
.g-form button{background:var(--accent);color:#0b0f12;border:0;font:500 1rem var(--body);padding:14px;cursor:pointer}
.g-form .hp{display:none}
.g-note{font-size:.85rem;color:var(--muted);margin-top:10px;max-width:460px}
.g-ok{max-width:640px;padding-block:60px}
.g-ok h1{font-family:var(--display);font-weight:400;font-size:clamp(2.2rem,5vw,3.4rem);margin:0 0 16px}
@media (max-width:820px){.g-wrap{grid-template-columns:1fr}.g-cover img{max-width:300px}}
"""
form = """<form class="g-form" name="guia" method="POST" action="/guia/gracias/" data-netlify="true" netlify-honeypot="empresa">
  <input type="hidden" name="form-name" value="guia">
  <p class="hp"><label>No completar: <input name="empresa"></label></p>
  <label>Nombre<input type="text" name="nombre" required autocomplete="given-name"></label>
  <label>Correo electrónico<input type="email" name="email" required autocomplete="email"></label>
  <label class="chk"><input type="checkbox" name="novedades" value="si"> Quiero recibir novedades: artículos nuevos, el curso y el libro. Sin spam, y te podés dar de baja cuando quieras.</label>
  <button type="submit">Descargar la guía gratis</button>
</form>"""
content = f"""<div class="wrap"><div class="g-wrap">
  <div class="g-cover"><img src="/img/guia-tapa.jpg" alt="Tapa de la guía Empezar a fotografiar, con Matías Silva y su cámara Sony" width="900" height="1272"></div>
  <div class="g-text">
    <p class="eyebrow">Guía gratuita · PDF</p>
    <h1>Empezar a fotografiar</h1>
    <p class="lead">Lo esencial para dejar el modo automático y empezar a decidir tus fotos. Sirve para cualquier cámara, también para el celular.</p>
    <ul>
      <li>La luz y la exposición, explicadas simple</li>
      <li>Modos de la cámara, histograma y enfoque</li>
      <li>Composición y cómo leer la luz</li>
      <li>Cómo configurar tu cámara el primer día</li>
      <li>Un plan de práctica de cuatro semanas</li>
    </ul>
    {form}
    <p class="g-note">Dejá tu nombre y tu correo, y la descarga se abre al instante. Tus datos solo los uso para enviarte novedades de este sitio.</p>
  </div>
</div></div>"""
ld = {"@context": "https://schema.org", "@type": "CreativeWork", "name": "Empezar a fotografiar", "inLanguage": "es", "isAccessibleForFree": True,
      "author": {"@type": "Person", "@id": SITE + "/#matias-silva", "name": "Matías Silva"}, "url": SITE + "/guia/", "image": SITE + "/img/guia-tapa.jpg"}
pg = blog.page("es", "Guía gratuita: Empezar a fotografiar · Matías Silva", "Guía gratuita en PDF para dejar el modo automático: exposición, modos, histograma, enfoque, composición y un plan de práctica de cuatro semanas.", "/guia/", "/guia/", "/en/", ld, content.replace('<div class="wrap"><div class="g-wrap">','<div class="wrap"><p class="crumbs" style="margin-top:24px"><a href="/recursos/">Recursos</a> / Guía gratuita</p><div class="g-wrap" style="padding-top:12px">'), "familia")
pg = pg.replace("</style>", CSS + "</style>", 1)
os.makedirs("/home/claude/web/site/guia/gracias", exist_ok=True)
open("/home/claude/web/site/guia/index.html", "w").write(pg)
ok = """<div class="wrap"><div class="g-ok">
  <p class="eyebrow">Listo</p>
  <h1>Gracias. Tu guía está acá.</h1>
  <p><a class="btn" href="/descargas/Empezar-a-fotografiar_Matias-Silva.pdf" download>Descargar el PDF</a></p>
  <p style="color:var(--muted);margin-top:24px">Mientras tanto, en el <a href="/blog/" style="color:var(--accent)">blog</a> hay artículos completos sobre cada tema, y en Instagram comparto fotos y proceso: <a href="https://www.instagram.com/matiassilva.ph/" style="color:var(--accent)">@matiassilva.ph</a>.</p>
</div></div>"""
pg2 = blog.page("es", "Gracias · Guía Empezar a fotografiar", "Descarga de la guía Empezar a fotografiar.", "/guia/gracias/", "/guia/gracias/", "/en/", {}, ok)
pg2 = pg2.replace("<title>", '<meta name="robots" content="noindex">\n<title>', 1).replace("</style>", CSS + "</style>", 1)
open("/home/claude/web/site/guia/gracias/index.html", "w").write(pg2)
print("guia ok")
