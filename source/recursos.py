import sys, os
sys.path.insert(0, "/home/claude/web")
import blog
SITE = blog.SITE
CSS = """
.r-head{padding-block:40px 28px;border-bottom:1px solid var(--line);margin-bottom:36px;max-width:820px}
.r-head h1{font-family:var(--display);font-weight:400;font-size:clamp(2.4rem,6vw,4.4rem);line-height:1;margin:0 0 16px}
.r-head p{margin:0;color:var(--muted);max-width:62ch;font-size:1.05rem}
.r-sec{margin-bottom:48px}
.r-sec > h2{font-family:var(--display);font-weight:400;font-size:clamp(1.6rem,3vw,2.2rem);margin:0 0 18px}
.r-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px}
.r-card{border:1px solid var(--line);background:var(--surface);display:flex;flex-direction:column;text-decoration:none;color:var(--fg)}
.r-card img{width:100%;aspect-ratio:4/3;object-fit:cover;object-position:center 20%;display:block}
.r-card .b{padding:20px;display:flex;flex-direction:column;gap:8px;flex:1}
.r-card .tag{font:11px var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--accent)}
.r-card h3{font-family:var(--display);font-weight:400;font-size:1.5rem;margin:0}
.r-card p{margin:0;color:var(--muted);font-size:.92rem}
.r-card .go{margin-top:auto;padding-top:8px;font:500 .9rem var(--body);color:var(--accent)}
.r-card.soon{opacity:.6}
.r-card.soon .ph{aspect-ratio:4/3;background:#101519;display:grid;place-items:center;font:12px var(--mono);letter-spacing:.1em;color:var(--muted);text-transform:uppercase}
@media (max-width:860px){.r-grid{grid-template-columns:1fr}}
"""
def card(href,img,tag,title,desc,go):
    return f'<a class="r-card" href="{href}"><img src="{img}" alt="" loading="lazy"><div class="b"><span class="tag">{tag}</span><h3>{title}</h3><p>{desc}</p><span class="go">{go} →</span></div></a>'
def soon(tag,title,desc):
    return f'<div class="r-card soon"><div class="ph">Próximamente</div><div class="b"><span class="tag">{tag}</span><h3>{title}</h3><p>{desc}</p></div></div>'
free = card("/guia/","/img/guia-tapa.jpg","Gratis · PDF","Empezar a fotografiar","Trece páginas para dejar el modo automático: exposición, modos, histograma, enfoque, composición y un plan de práctica.","Descargar") + \
       card("/blog/temporada-de-olas-en-nazare/","/img/praia-norte-arriba-s.jpg","Gratis · Artículo","Guía de las olas de Nazaré","Cuándo ir, cómo leer el pronóstico y dónde pararse para ver y fotografiar las olas grandes.","Leer")
paid = soon("Presets · Lightroom","Presets Nazaré","Mi edición oscura y fría, lista para aplicar en Lightroom móvil y de escritorio.") + \
       soon("Guía puntual · PDF","Fotografiar olas grandes","Equipo, ajustes y lugares para fotografiar surf y mar grande.") + \
       soon("Guía puntual · PDF","Retrato con luz natural","Cómo ubicar a la persona, leer la luz y dirigir la expresión.")
content = f"""<div class="wrap">
  <header class="r-head"><p class="eyebrow">Recursos</p><h1>Recursos de fotografía</h1><p>Guías, materiales y herramientas para aprender a fotografiar y editar con criterio. Algunos son gratuitos y otros van a ser de pago, siempre a precios accesibles.</p></header>
  <section class="r-sec"><h2>Gratuitos</h2><div class="r-grid">{free}</div></section>
  <section class="r-sec"><h2>Próximamente</h2><div class="r-grid">{paid}</div></section>
</div>"""
ld = {"@context":"https://schema.org","@type":"CollectionPage","name":"Recursos de fotografía · Matías Silva","inLanguage":"es","url":SITE+"/recursos/"}
pg = blog.page("es","Recursos de fotografía · Matías Silva","Guías gratuitas y recursos de fotografía de Matías Silva: exposición, edición, presets y guías puntuales para aprender a fotografiar.","/recursos/","/recursos/","/en/",ld,content,"familia")
pg = pg.replace("</style>", CSS+"</style>",1)
os.makedirs("/home/claude/web/site/recursos",exist_ok=True)
open("/home/claude/web/site/recursos/index.html","w").write(pg)
print("recursos ok")
