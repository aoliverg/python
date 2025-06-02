import urllib.request
import codecs
f = urllib.request.urlopen("https://www.ara.cat/esports/barca/resultats-observatori-blaugrana-febrer-2018_0_1954004729.html")
web=f.read().decode('utf-8')

sortida=codecs.open("noticia.html","w",encoding="utf-8")
sortida.write(web)
