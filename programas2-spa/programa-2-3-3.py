import codecs
entrada=codecs.open("archivo.txt","r",encoding="utf-8")
for linea in entrada:
    linea=linea.rstrip()
    print(linea)
