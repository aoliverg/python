import urllib.request
import codecs
import html2text
f = urllib.request.urlopen("https://www.ara.cat/esports/barca/resultats-observatori-blaugrana-febrer-2018_0_1954004729.html")
web=f.read().decode('utf-8')
text=html2text.html2text(web)
sortida=codecs.open("noticia.txt","w",encoding="utf-8")
sortida.write(text)
