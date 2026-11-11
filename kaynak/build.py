import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
KEY = "AIzaSyBJROHUjjSM37FhW92hZVYnmry7ptE6g6U"
s = open(os.path.join(HERE, "template.html"), encoding='utf-8').read()
r = open(os.path.join(HERE, "routes.json"), encoding='utf-8').read().replace('</', '<\\/'); bm = open(os.path.join(HERE, "basemap.json"), encoding='utf-8').read().replace('</', '<\\/')
s = s.replace('/*ROUTES*/', r).replace('/*BASEMAP*/', bm)
open(os.path.join(HERE, "onizleme.html"), "w", encoding='utf-8').write(s)                       # Claude önizlemesi (anahtarsız)
open(os.devnull, "w", encoding='utf-8').write(max(re.findall(r'<script>([\s\S]*?)</script>', s), key=len))
i = s.index('<div class="app">')
site = s.replace('window.MAPS_KEY = window.MAPS_KEY || "";', 'window.MAPS_KEY = window.MAPS_KEY || "%s";' % KEY)
i = site.index('<div class="app">')
page = ('<!doctype html>\n<html lang="tr">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        '<meta name="robots" content="noindex, nofollow">\n'
        '<meta name="description" content="Ankara otobüs filosu için filo konsolu sunum prototipi (örnek veri).">\n'
        '<style>html{color-scheme:light}body{margin:0;-webkit-font-smoothing:antialiased}img{max-width:100%}[hidden]{display:none!important}</style>\n'
        + site[:i] + '\n</head>\n<body>\n' + site[i:] + '\n</body>\n</html>\n')
open(sys.argv[1], 'w', encoding='utf-8').write(page)
print('ok', len(page.encode()))
