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
s=open('/home/claude/web/site/index.html').read()
i=s.index('<header class="top">')
head,body=s[:i],s[i:]
page=('<!doctype html>\n<html lang="es">\n<head>\n'+GA4+GTM_HEAD+'<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
      + head.replace('<meta name="claude:viewport-fit-sides" content="cover">\n','') +
      '<style>[hidden]{display:none!important}</style>\n</head>\n<body>\n'+GTM_BODY + body + '\n</body>\n</html>\n')
open('/home/claude/matiassilvaph-web/index.html','w').write(page)
