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
def soon(ph,tag,title,desc):
    return f'<div class="r-card soon"><div class="ph">{ph}</div><div class="b"><span class="tag">{tag}</span><h3>{title}</h3><p>{desc}</p></div></div>'
T={
 "es":dict(url="/recursos/",ey="Recursos",h1="Recursos de fotografía",p="Guías, materiales y herramientas para aprender a fotografiar y editar con criterio. Algunos son gratuitos y otros van a ser de pago, siempre a precios accesibles.",fr="Gratuitos",sn="Próximamente",ph="Próximamente",
  free=[("/guia/","/img/guia-tapa.jpg","Gratis · PDF","Empezar a fotografiar","Trece páginas para dejar el modo automático: exposición, modos, histograma, enfoque, composición y un plan de práctica.","Descargar"),
        ("/blog/temporada-de-olas-en-nazare/","/img/praia-norte-arriba-s.jpg","Gratis · Artículo","Guía de las olas de Nazaré","Cuándo ir, cómo leer el pronóstico y dónde pararse para ver y fotografiar las olas grandes.","Leer")],
  paid=[("Presets · Lightroom","Presets Nazaré","Mi edición oscura y fría, lista para aplicar en Lightroom móvil y de escritorio."),("Guía puntual · PDF","Fotografiar olas grandes","Equipo, ajustes y lugares para fotografiar surf y mar grande."),("Guía puntual · PDF","Retrato con luz natural","Cómo ubicar a la persona, leer la luz y dirigir la expresión.")],
  title="Recursos de fotografía · Matías Silva",desc="Guías gratuitas y recursos de fotografía de Matías Silva: exposición, edición, presets y guías puntuales para aprender a fotografiar."),
 "en":dict(url="/en/recursos/",ey="Resources",h1="Photography resources",p="Guides, materials and tools to learn to photograph and edit with judgement. Some are free and others will be paid, always at accessible prices.",fr="Free",sn="Coming soon",ph="Coming soon",
  free=[("/en/guia/","/img/guia-tapa-en.jpg","Free · PDF","Start taking photographs","Thirteen pages to leave auto mode: exposure, modes, histogram, focus, composition and a practice plan.","Download"),
        ("/en/blog/temporada-de-olas-en-nazare/","/img/praia-norte-arriba-s.jpg","Free · Article","Nazaré wave guide","When to go, how to read the forecast and where to stand to watch and photograph the big waves.","Read")],
  paid=[("Presets · Lightroom","Nazaré presets","My dark, cool edit, ready to apply in Lightroom mobile and desktop."),("Focused guide · PDF","Photographing big waves","Gear, settings and spots for photographing surf and big seas."),("Focused guide · PDF","Natural light portraits","How to place the person, read the light and direct the expression.")],
  title="Photography resources · Matías Silva",desc="Free guides and photography resources by Matías Silva: exposure, editing, presets and focused guides to learn photography."),
 "pt":dict(url="/pt/recursos/",ey="Recursos",h1="Recursos de fotografia",p="Guias, materiais e ferramentas para aprender a fotografar e editar com critério. Alguns são gratuitos e outros vão ser pagos, sempre a preços acessíveis.",fr="Gratuitos",sn="Brevemente",ph="Brevemente",
  free=[("/pt/guia/","/img/guia-tapa-pt.jpg","Grátis · PDF","Começar a fotografar","Treze páginas para deixar o modo automático: exposição, modos, histograma, focagem, composição e um plano de prática.","Descarregar"),
        ("/pt/blog/temporada-de-olas-en-nazare/","/img/praia-norte-arriba-s.jpg","Grátis · Artigo","Guia das ondas da Nazaré","Quando ir, como ler a previsão e onde ficar para ver e fotografar as ondas grandes.","Ler")],
  paid=[("Presets · Lightroom","Presets Nazaré","A minha edição escura e fria, pronta a aplicar no Lightroom móvel e no computador."),("Guia temático · PDF","Fotografar ondas grandes","Equipamento, ajustes e lugares para fotografar surf e mar grande."),("Guia temático · PDF","Retrato com luz natural","Como posicionar a pessoa, ler a luz e dirigir a expressão.")],
  title="Recursos de fotografia · Matías Silva",desc="Guias gratuitos e recursos de fotografia de Matías Silva: exposição, edição, presets e guias temáticos para aprender fotografia."),
}
for lang,t in T.items():
    free="".join(card(*c) for c in t["free"]); paid="".join(soon(t["ph"],*c) for c in t["paid"])
    content=f"""<div class="wrap">
  <header class="r-head"><p class="eyebrow">{t['ey']}</p><h1>{t['h1']}</h1><p>{t['p']}</p></header>
  <section class="r-sec"><h2>{t['fr']}</h2><div class="r-grid">{free}</div></section>
  <section class="r-sec"><h2>{t['sn']}</h2><div class="r-grid">{paid}</div></section>
</div>"""
    ld={"@context":"https://schema.org","@type":"CollectionPage","name":t["title"],"inLanguage":("pt-PT" if lang=="pt" else lang),"url":SITE+t["url"]}
    pg=blog.page(lang,t["title"],t["desc"],t["url"],"/recursos/","/en/recursos/",ld,content,"familia",alt_pt="/pt/recursos/").replace("</style>",CSS+"</style>",1)
    os.makedirs("/home/claude/web/site"+t["url"],exist_ok=True)
    open("/home/claude/web/site"+t["url"]+"index.html","w").write(pg)
print("recursos ok x3")
