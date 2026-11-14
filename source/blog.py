import sys, re, os, json, html
sys.path.insert(0, "/home/claude/web")
from posts import POSTS
from posts_pt import PT as POSTS_PT
for _p in POSTS: _p['pt']=POSTS_PT[_p['slug']]

SITE = "https://matiassilvaph.com"
tpl = open("/home/claude/web/template.html").read()
CSS = re.search(r"<style>(.*?)</style>", tpl, re.S).group(1)
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400;0,6..96,500;1,6..96,400&family=Work+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">'

GUIA_CTA = {
 "es": '''<aside class="guia-cta"><p class="eyebrow">Guía gratuita</p><h2>Empezar a fotografiar</h2><p>Trece páginas para dejar el modo automático: exposición, modos, histograma, enfoque, composición y un plan de práctica de cuatro semanas. Sirve para cualquier cámara.</p><a class="btn" href="/guia/">Descargar la guía</a></aside>''',
 "en": '''<aside class="guia-cta"><p class="eyebrow">Free guide</p><h2>Start taking photographs</h2><p>Thirteen pages to leave auto mode: exposure, modes, histogram, focus, composition and a four-week practice plan. It works with any camera.</p><a class="btn" href="/en/guia/">Download the guide</a></aside>''',
 "pt": '''<aside class="guia-cta"><p class="eyebrow">Guia gratuito</p><h2>Começar a fotografar</h2><p>Treze páginas para deixar o modo automático: exposição, modos, histograma, focagem, composição e um plano de prática de quatro semanas. Serve para qualquer câmara.</p><a class="btn" href="/pt/guia/">Descarregar o guia</a></aside>'''}

POP_T = {
 "es": dict(form="guia", ok="/guia/gracias/", img="/img/guia-tapa.jpg", ey="Guía gratuita · PDF", h="Empezar a fotografiar",
            p="Trece páginas para dejar el modo automático. Sirve para cualquier cámara.", name="Tu nombre", mail="Tu correo",
            chk="Quiero recibir novedades. Sin spam.", btn="Descargar gratis", close="Cerrar"),
 "en": dict(form="guia-en", ok="/en/guia/gracias/", img="/img/guia-tapa-en.jpg", ey="Free guide · PDF", h="Start taking photographs",
            p="Thirteen pages to leave auto mode. It works with any camera.", name="Your name", mail="Your email",
            chk="I would like to receive updates. No spam.", btn="Download free", close="Close"),
 "pt": dict(form="guia-pt", ok="/pt/guia/gracias/", img="/img/guia-tapa-pt.jpg", ey="Guia gratuito · PDF", h="Começar a fotografar",
            p="Treze páginas para deixar o modo automático. Serve para qualquer câmara.", name="O teu nome", mail="O teu e-mail",
            chk="Quero receber novidades. Sem spam.", btn="Descarregar grátis", close="Fechar"),
}
def popup(lang):
    t = POP_T[lang]
    return f"""<div class="gp" id="gp" hidden role="dialog" aria-modal="false" aria-labelledby="gp-h">
  <button class="gp-x" type="button" aria-label="{t['close']}">×</button>
  <img src="{t['img']}" alt="" width="120" height="170" loading="lazy">
  <div class="gp-b">
    <p class="eyebrow">{t['ey']}</p><p class="gp-h" id="gp-h">{t['h']}</p><p class="gp-p">{t['p']}</p>
    <form name="{t['form']}" method="POST" action="{t['ok']}" data-netlify="true" netlify-honeypot="empresa">
      <input type="hidden" name="form-name" value="{t['form']}"><p hidden><input name="empresa"></p>
      <input type="text" name="nombre" placeholder="{t['name']}" required autocomplete="given-name">
      <input type="email" name="email" placeholder="{t['mail']}" required autocomplete="email">
      <label><input type="checkbox" name="novedades" value="si"> {t['chk']}</label>
      <button type="submit">{t['btn']}</button>
    </form>
  </div>
</div>
<script>
(function(){{
  var K='gpHide',p=document.getElementById('gp');if(!p)return;
  function get(){{try{{return localStorage.getItem(K)}}catch(e){{return null}}}}
  function set(v){{try{{localStorage.setItem(K,v)}}catch(e){{}}}}
  var v=get();if(v==='done'||(v&&Date.now()<+v))return;
  var shown=false;
  function show(){{if(shown)return;shown=true;p.hidden=false;requestAnimationFrame(function(){{p.classList.add('on')}});}}
  function close(){{p.classList.remove('on');setTimeout(function(){{p.hidden=true}},300);set(String(Date.now()+30*864e5));}}
  window.addEventListener('scroll',function(){{var h=document.documentElement;if((h.scrollTop+innerHeight)/h.scrollHeight>0.5)show();}},{{passive:true}});
  p.querySelector('.gp-x').addEventListener('click',close);
  document.addEventListener('keydown',function(e){{if(e.key==='Escape'&&shown)close();}});
  p.querySelector('form').addEventListener('submit',function(e){{
    e.preventDefault();var f=this;f.querySelector('button').disabled=true;set('done');
    var go=function(){{location.href='{t['ok']}';}};
    fetch('/',{{method:'POST',headers:{{'Content-Type':'application/x-www-form-urlencoded'}},body:new URLSearchParams(new FormData(f)).toString()}}).then(go,go);
    setTimeout(go,4000);
  }});
}})();
</script>"""
POP_CSS = """
.gp{position:fixed;z-index:60;right:24px;bottom:24px;width:min(440px,calc(100vw - 32px));background:#131a1f;border:1px solid var(--accent);box-shadow:0 20px 60px rgba(0,0,0,.6);display:flex;gap:18px;padding:22px;transform:translateY(24px);opacity:0;transition:transform .3s,opacity .3s}
.gp.on{transform:none;opacity:1}
.gp img{width:96px;height:auto;align-self:flex-start;box-shadow:0 8px 20px rgba(0,0,0,.5)}
.gp-b{flex:1;min-width:0}
.gp .eyebrow{margin:0 0 4px}
.gp-h{font:400 1.45rem/1.1 var(--display);margin:0 0 6px;color:var(--fg)}
.gp-p{font-size:.88rem;color:var(--muted);margin:0 0 12px}
.gp form{display:flex;flex-direction:column;gap:8px}
.gp input[type=text],.gp input[type=email]{background:#0b0f12;border:1px solid var(--line);color:var(--fg);font:.95rem var(--body);padding:10px;width:100%;box-sizing:border-box}
.gp label{font-size:.78rem;color:var(--muted);display:flex;gap:6px;align-items:flex-start}
.gp button[type=submit]{background:var(--accent);color:#0b0f12;border:0;font:500 .95rem var(--body);padding:11px;cursor:pointer}
.gp-x{position:absolute;top:6px;right:8px;background:none;border:0;color:var(--muted);font-size:1.6rem;line-height:1;cursor:pointer;padding:4px 8px}
@media (max-width:600px){.gp{left:0;right:0;bottom:0;width:auto;border-width:1px 0 0;padding:18px 16px 20px}.gp img{display:none}}
"""
BLOG_CSS = """"""+POP_CSS+""".guia-cta{max-width:68ch;margin-top:28px;padding:26px;border:1px solid var(--accent);background:var(--surface)}
.guia-cta h2{font-family:var(--display);font-weight:400;font-size:1.8rem;margin:6px 0 8px}
.guia-cta p{margin:0 0 16px;color:var(--muted)}
.btn{display:inline-block;background:var(--accent);color:#0b0f12;font:500 .95rem var(--body);padding:12px 20px;text-decoration:none}
.btn:hover{filter:brightness(1.08)}

.crumbs{font:12px var(--mono);color:var(--muted);padding-block:28px 0}
.crumbs a{text-decoration:none}.crumbs a:hover{color:var(--fg)}
.post-head{max-width:820px;padding-block:18px 28px}
.post-head h1{font-family:var(--display);font-weight:400;font-size:clamp(2.2rem,5vw,3.6rem);line-height:1.05;margin:0 0 16px;text-wrap:balance}
.post-meta{font:12px/1.8 var(--mono);color:var(--muted);display:flex;flex-wrap:wrap;gap:4px 16px}
.post-meta .cat{color:var(--accent)}
.post-cover{margin:0 0 36px}
.post-cover img{width:100%;aspect-ratio:21/9;object-fit:cover}
.prose{max-width:68ch;font-size:1.06rem}
.prose .lead{font-family:var(--display);font-size:clamp(1.3rem,2.4vw,1.6rem);line-height:1.4;margin:0 0 1.2em}
.prose h2{font-family:var(--display);font-weight:400;font-size:clamp(1.6rem,3vw,2.1rem);line-height:1.15;margin:2.2em 0 .6em;text-wrap:balance}
.prose p,.prose ul,.prose ol{margin:0 0 1.1em}
.prose li{margin-bottom:.45em}
.prose strong{color:var(--fg);font-weight:600}
.prose a{color:var(--accent)}
.prose .fig{margin:2em 0}
.prose .fig img{width:auto;max-width:100%;max-height:82vh;display:block;margin:0 auto}
.prose .fig figcaption{display:block;font:12px/1.7 var(--mono);color:var(--muted);padding-top:8px}
.table-wrap{overflow-x:auto;margin:0 0 1.4em;border:1px solid var(--line)}
.prose table{border-collapse:collapse;width:100%;font-size:.92rem;font-variant-numeric:tabular-nums}
.prose th,.prose td{text-align:left;padding:10px 12px;border-bottom:1px solid var(--line);vertical-align:top}
.prose th{font:500 11px var(--mono);text-transform:uppercase;letter-spacing:.08em;color:var(--muted);background:var(--surface)}
.prose tr:last-child td{border-bottom:0}
.prose .next{border-top:1px solid var(--line);padding-top:18px;margin-top:2.4em;font-size:.95rem}
.author{display:flex;gap:16px;align-items:center;max-width:68ch;margin-top:40px;padding:18px;border:1px solid var(--line);background:var(--surface)}
.author img{width:64px;height:64px;object-fit:cover;border-radius:50%}
.author p{margin:0;font-size:.92rem;color:var(--muted)}
.author b{color:var(--fg);font-weight:500}
.blog-head{padding-block:40px 24px;border-bottom:1px solid var(--line);margin-bottom:32px}
.blog-head h1{font-family:var(--display);font-weight:400;font-size:clamp(2.6rem,7vw,5rem);line-height:.95;margin:0 0 14px}
.blog-head p{margin:0;color:var(--muted);max-width:60ch}
.cards{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:28px}
.card{text-decoration:none;display:flex;flex-direction:column;gap:12px}
.card img{width:100%;aspect-ratio:16/9;object-fit:cover;transition:filter .3s}
.card:hover img{filter:brightness(1.1)}
.card h2{font-family:var(--display);font-weight:400;font-size:1.6rem;line-height:1.15;margin:0;text-wrap:balance}
.card p{margin:0;color:var(--muted);font-size:.95rem}
@media (max-width:820px){.cards{grid-template-columns:1fr}}
"""

L = {
 "es": dict(home="/", blog="/blog/", nav=[("/#mar","El mar"),("/#pueblo","El pueblo"),("/#luz","La luz"),("/#guia","Guía"),("/blog/","Blog"),("/recursos/","Recursos"),("/sobre/","Quién soy")],
            brand="fotografía", blogtitle="Blog", blogdesc="Artículos sobre fotografía para quienes empiezan: exposición, modos de la cámara, composición y luz. Sirven para cualquier cámara.",
            blogh="Blog", blogp="Lo que voy aprendiendo sobre fotografía, explicado simple. Conceptos que sirven con cualquier cámara, del celular a una sin espejo.",
            read="min de lectura", by="Por Matías Silva", home_l="Inicio",
            author="<b>Matías Silva</b> · Fotógrafo entre San Miguel y Nazaré. Escribo sobre lo que aprendo en cada salida.",
            foot="© 2026 Matías Silva · Todas las fotografías son de autoría propia.", months=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]),
 "pt": dict(home="/pt/", blog="/pt/blog/", nav=[("/pt/#mar","O mar"),("/pt/#pueblo","A vila"),("/pt/#luz","A luz"),("/pt/#guia","Guia"),("/pt/blog/","Blog"),("/pt/recursos/","Recursos"),("/pt/sobre/","Quem sou")],
            brand="fotografia", blogtitle="Blog", blogdesc="Artigos de fotografia para quem está a começar: exposição, modos da câmara, composição e luz. Servem para qualquer câmara.",
            blogh="Blog", blogp="O que vou aprendendo sobre fotografia, explicado de forma simples. Conceitos que servem para qualquer câmara, do telemóvel a uma sem espelho.",
            read="min de leitura", by="Por Matías Silva", home_l="Início",
            author="<b>Matías Silva</b> · Fotógrafo entre San Miguel e a Nazaré. Escrevo sobre o que aprendo em cada saída.",
            foot="© 2026 Matías Silva · Todas as fotografias são de autoria própria.", months=["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]),
 "en": dict(home="/en/", blog="/en/blog/", nav=[("/en/#mar","The sea"),("/en/#pueblo","The town"),("/en/#luz","The light"),("/en/#guia","Guide"),("/en/blog/","Blog"),("/en/recursos/","Resources"),("/en/sobre/","About")],
            brand="photography", blogtitle="Blog", blogdesc="Photography articles for beginners: exposure, camera modes, composition and light. They work with any camera.",
            blogh="Blog", blogp="What I am learning about photography, explained simply. Concepts that work with any camera, from a phone to a mirrorless.",
            read="min read", by="By Matías Silva", home_l="Home",
            author="<b>Matías Silva</b> · Photographer between San Miguel and Nazaré. I write about what I learn on every shoot.",
            foot="© 2026 Matías Silva · All photographs are my own work.", months=["January","February","March","April","May","June","July","August","September","October","November","December"]),
}

def fdate(d, lang):
    y, m, dd = d.split("-")
    mn = L[lang]["months"][int(m)-1]
    return f"{mn} {int(dd)}, {y}" if lang == "en" else f"{int(dd)} de {mn} de {y}"

def mins(body):
    return max(1, round(len(re.sub("<[^>]+>", " ", body).split()) / 200))

def page(lang, title, desc, url, alt_es, alt_en, ld, content, ogimg="familia", alt_pt=None):
    t = L[lang]
    alts = {"es": alt_es, "en": alt_en, "pt": alt_pt}
    nav = "".join(f'<a href="{h}">{n}</a>' for h, n in t["nav"])
    nav += "".join(f'<a class="lang" href="{u}" hreflang="{k}" lang="{k}">{k.upper()}</a>' for k, u in alts.items() if u and k != lang)
    ptlink = f'<link rel="alternate" hreflang="pt-PT" href="{SITE}{alt_pt}">\n' if alt_pt else ""
    return f"""<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{SITE}{url}">
<link rel="alternate" hreflang="es" href="{SITE}{alt_es}">
<link rel="alternate" hreflang="en" href="{SITE}{alt_en}">
{ptlink}<link rel="alternate" hreflang="x-default" href="{SITE}{alt_es}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="{'article' if ld.get('@type')=='BlogPosting' else 'website'}">
<meta property="og:image" content="{SITE}/img/{ogimg}.jpg">
{FONTS}
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<style>{CSS}{BLOG_CSS}</style>
<header class="top">
  <div class="wrap">
    <a class="brand" href="{t['home']}">Matías Silva <i>{t['brand']}</i></a>
    <nav aria-label="{dict(es='Secciones',en='Sections',pt='Secções')[lang]}">{nav}</nav>
  </div>
</header>
<main>
{content}
</main>
<footer class="wrap">{t['foot']}</footer>
"""

out = {}
for lang in ("es", "en", "pt"):
    t = L[lang]
    cards = ""
    for p in reversed(POSTS):
        c = p[lang]
        url = f"{t['blog']}{p['slug']}/"
        alt_es, alt_en, alt_pt = f"/blog/{p['slug']}/", f"/en/blog/{p['slug']}/", f"/pt/blog/{p['slug']}/"
        ld = {"@context": "https://schema.org", "@type": "BlogPosting", "headline": c["title"], "description": c["desc"],
              "inLanguage": ("pt-PT" if lang == "pt" else lang), "datePublished": p["date"], "dateModified": p["date"], "image": f"{SITE}/img/{p['image']}.jpg",
              "author": {"@type": "Person", "@id": SITE + "/#matias-silva", "name": "Matías Silva", "url": SITE + t["home"], "image": SITE + "/img/matias.jpg"},
              "publisher": {"@type": "Person", "name": "Matías Silva"}, "mainEntityOfPage": SITE + url}
        content = f"""<div class="wrap">
  <p class="crumbs"><a href="{t['home']}">{t['home_l']}</a> / <a href="{t['blog']}">Blog</a></p>
  <header class="post-head">
    <h1>{c['title']}</h1>
    <div class="post-meta"><span class="cat">{c['cat']}</span><span>{t['by']}</span><span>{fdate(p['date'], lang)}</span><span>{mins(c['body'])} {t['read']}</span></div>
  </header>
  <figure class="post-cover"><img src="/img/{p['image']}.jpg" alt="" width="1440" height="960" fetchpriority="high"></figure>
  <article class="prose">{c['body']}</article>
  <aside class="author"><img src="/img/matias.jpg" alt="Matías Silva" width="96" height="96" loading="lazy"><p>{t['author']}</p></aside>
  {GUIA_CTA[lang]}
</div>
{popup(lang)}
<div hidden>
</div>"""
        out[f"{lang}/{p['slug']}"] = (url, page(lang, c["title"] + " · Matías Silva", c["desc"], url, alt_es, alt_en, ld, content, p["image"], alt_pt))
        cards += f"""<a class="card" href="{url}"><img src="/img/{p['image']}-s.jpg" alt="" loading="lazy" width="760" height="507">
<div class="post-meta"><span class="cat">{c['cat']}</span><span>{fdate(p['date'], lang)}</span><span>{mins(c['body'])} {t['read']}</span></div>
<h2>{c['title']}</h2><p>{c['desc']}</p></a>"""
    ld = {"@context": "https://schema.org", "@type": "Blog", "name": "Blog · Matías Silva", "inLanguage": ("pt-PT" if lang == "pt" else lang), "url": SITE + t["blog"],
          "author": {"@type": "Person", "name": "Matías Silva"}}
    content = f"""<div class="wrap">
  <header class="blog-head"><p class="eyebrow">Matías Silva</p><h1>{t['blogh']}</h1><p>{t['blogp']}</p></header>
  <div class="cards">{cards}</div>
</div>"""
    out[f"{lang}/index"] = (t["blog"], page(lang, "Blog · Matías Silva " + dict(es="Fotografía", en="Photography", pt="Fotografia")[lang], t["blogdesc"], t["blog"], "/blog/", "/en/blog/", ld, content, alt_pt="/pt/blog/"))

for k, (url, pg) in out.items():
    path = "/home/claude/web/site" + url + "index.html"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w").write(pg)
print("\n".join(v[0] for v in out.values()))
