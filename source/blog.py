import sys, re, os, json, html
sys.path.insert(0, "/home/claude/web")
from posts import POSTS

SITE = "https://matiassilvaph.netlify.app"
tpl = open("/home/claude/web/template.html").read()
CSS = re.search(r"<style>(.*?)</style>", tpl, re.S).group(1)
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400;0,6..96,500;1,6..96,400&family=Work+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">'

BLOG_CSS = """
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
.prose .fig img{width:100%}
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
 "es": dict(home="/", blog="/blog/", nav=[("/#mar","El mar"),("/#pueblo","El pueblo"),("/#luz","La luz"),("/#guia","Guía"),("/blog/","Blog"),("/#quien-soy","Quién soy")],
            brand="fotografía", blogtitle="Blog", blogdesc="Artículos sobre fotografía para quienes empiezan: exposición, modos de la cámara, composición y luz. Sirven para cualquier cámara.",
            blogh="Blog", blogp="Lo que voy aprendiendo sobre fotografía, explicado simple. Conceptos que sirven con cualquier cámara, del celular a una sin espejo.",
            read="min de lectura", by="Por Matías Silva", home_l="Inicio",
            author="<b>Matías Silva</b> · Fotógrafo entre San Miguel y Nazaré. Escribo sobre lo que aprendo en cada salida.",
            foot="© 2026 Matías Silva · Todas las fotografías son de autoría propia.", months=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]),
 "en": dict(home="/en/", blog="/en/blog/", nav=[("/en/#mar","The sea"),("/en/#pueblo","The town"),("/en/#luz","The light"),("/en/#guia","Guide"),("/en/blog/","Blog"),("/en/#quien-soy","About")],
            brand="photography", blogtitle="Blog", blogdesc="Photography articles for beginners: exposure, camera modes, composition and light. They work with any camera.",
            blogh="Blog", blogp="What I am learning about photography, explained simply. Concepts that work with any camera, from a phone to a mirrorless.",
            read="min read", by="By Matías Silva", home_l="Home",
            author="<b>Matías Silva</b> · Photographer between San Miguel and Nazaré. I write about what I learn on every shoot.",
            foot="© 2026 Matías Silva · All photographs are my own work.", months=["January","February","March","April","May","June","July","August","September","October","November","December"]),
}

def fdate(d, lang):
    y, m, dd = d.split("-")
    mn = L[lang]["months"][int(m)-1]
    return f"{int(dd)} de {mn} de {y}" if lang == "es" else f"{mn} {int(dd)}, {y}"

def mins(body):
    return max(1, round(len(re.sub("<[^>]+>", " ", body).split()) / 200))

def page(lang, title, desc, url, alt_es, alt_en, ld, content, ogimg="familia"):
    t = L[lang]
    other = alt_en if lang == "es" else alt_es
    nav = "".join(f'<a href="{h}">{n}</a>' for h, n in t["nav"])
    nav += (f'<a class="lang" href="{other}" hreflang="en" lang="en">EN</a>' if lang == "es" else f'<a class="lang" href="{other}" hreflang="es" lang="es">ES</a>')
    return f"""<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{SITE}{url}">
<link rel="alternate" hreflang="es" href="{SITE}{alt_es}">
<link rel="alternate" hreflang="en" href="{SITE}{alt_en}">
<link rel="alternate" hreflang="x-default" href="{SITE}{alt_es}">
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
    <nav aria-label="{'Secciones' if lang=='es' else 'Sections'}">{nav}</nav>
  </div>
</header>
<main>
{content}
</main>
<footer class="wrap">{t['foot']}</footer>
"""

out = {}
for lang in ("es", "en"):
    t = L[lang]
    cards = ""
    for p in POSTS:
        c = p[lang]
        url = f"{t['blog']}{p['slug']}/"
        alt_es, alt_en = f"/blog/{p['slug']}/", f"/en/blog/{p['slug']}/"
        ld = {"@context": "https://schema.org", "@type": "BlogPosting", "headline": c["title"], "description": c["desc"],
              "inLanguage": lang, "datePublished": p["date"], "dateModified": p["date"], "image": f"{SITE}/img/{p['image']}.jpg",
              "author": {"@type": "Person", "name": "Matías Silva", "url": SITE + t["home"]},
              "publisher": {"@type": "Person", "name": "Matías Silva"}, "mainEntityOfPage": SITE + url}
        content = f"""<div class="wrap">
  <p class="crumbs"><a href="{t['home']}">{t['home_l']}</a> / <a href="{t['blog']}">Blog</a></p>
  <header class="post-head">
    <h1>{c['title']}</h1>
    <div class="post-meta"><span class="cat">{c['cat']}</span><span>{t['by']}</span><span>{fdate(p['date'], lang)}</span><span>{mins(c['body'])} {t['read']}</span></div>
  </header>
  <figure class="post-cover"><img src="/img/{p['image']}.jpg" alt="" width="1440" height="960" fetchpriority="high"></figure>
  <article class="prose">{c['body']}</article>
  <aside class="author"><img src="/img/detras.jpg" alt="" width="96" height="96" loading="lazy"><p>{t['author']}</p></aside>
</div>"""
        out[f"{lang}/{p['slug']}"] = (url, page(lang, c["title"] + " · Matías Silva", c["desc"], url, alt_es, alt_en, ld, content, p["image"]))
        cards += f"""<a class="card" href="{url}"><img src="/img/{p['image']}-s.jpg" alt="" loading="lazy" width="760" height="507">
<div class="post-meta"><span class="cat">{c['cat']}</span><span>{fdate(p['date'], lang)}</span><span>{mins(c['body'])} {t['read']}</span></div>
<h2>{c['title']}</h2><p>{c['desc']}</p></a>"""
    ld = {"@context": "https://schema.org", "@type": "Blog", "name": "Blog · Matías Silva", "inLanguage": lang, "url": SITE + t["blog"],
          "author": {"@type": "Person", "name": "Matías Silva"}}
    content = f"""<div class="wrap">
  <header class="blog-head"><p class="eyebrow">Matías Silva</p><h1>{t['blogh']}</h1><p>{t['blogp']}</p></header>
  <div class="cards">{cards}</div>
</div>"""
    out[f"{lang}/index"] = (t["blog"], page(lang, "Blog · Matías Silva " + ("Fotografía" if lang == "es" else "Photography"), t["blogdesc"], t["blog"], "/blog/", "/en/blog/", ld, content))

for k, (url, pg) in out.items():
    path = "/home/claude/web/site" + url + "index.html"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w").write(pg)
print("\n".join(v[0] for v in out.values()))
