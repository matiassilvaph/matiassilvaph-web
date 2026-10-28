GTM_HEAD="""<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-PZMCM3XP');</script>
<!-- End Google Tag Manager -->
"""
GA4="""<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-PRT487HS08"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-PRT487HS08');
</script>
"""
GTM_BODY="""<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-PZMCM3XP"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
"""
import os
def wrap(src,out,lang):
    s=open(src).read()
    i=s.index('<header class="top">')
    head,body=s[:i],s[i:]
    page=('<!doctype html>\n<html lang="'+lang+'">\n<head>\n'+GA4+GTM_HEAD+'<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
          + head.replace('<meta name="claude:viewport-fit-sides" content="cover">\n','') +
          '<style>[hidden]{display:none!important}</style>\n</head>\n<body>\n'+GTM_BODY + body + '\n</body>\n</html>\n')
    os.makedirs(os.path.dirname(out),exist_ok=True)
    open(out,'w').write(page)
R='/home/claude/matiassilvaph-web/'
wrap('/home/claude/web/site/index.html',R+'index.html','es')
wrap('/home/claude/web/site/en/index.html',R+'en/index.html','en')
import posts
pairs=[("/","/en/"),("/blog/","/en/blog/")]+[(f"/blog/{x['slug']}/",f"/en/blog/{x['slug']}/") for x in posts.POSTS]
for es,en in pairs[1:]:
    wrap('/home/claude/web/site'+es+'index.html',R+es.lstrip('/')+'index.html','es')
    wrap('/home/claude/web/site'+en+'index.html',R+en.lstrip('/')+'index.html','en')
B="https://matiassilvaph.netlify.app"
urls=""
for es,en in pairs:
    for u in (es,en):
        urls+=f"""  <url>
    <loc>{B}{u}</loc>
    <xhtml:link rel="alternate" hreflang="es" href="{B}{es}"/>
    <xhtml:link rel="alternate" hreflang="en" href="{B}{en}"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{B}{es}"/>
    <lastmod>2026-10-28</lastmod>
  </url>
"""
open(R+'sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'+urls+'</urlset>\n')

