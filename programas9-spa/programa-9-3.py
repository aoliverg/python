import codecs
entrada=codecs.open("noticia-cat.txt","r",encoding="utf-8")
salida=codecs.open("noticia3-cat.txt","w",encoding="iso-8859-1")
for linia in entrada:
    salida.write(linia)
