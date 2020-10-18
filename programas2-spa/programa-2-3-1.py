import codecs
entrada=codecs.open("archivo.txt","r",encoding="utf-8")
while 1:
    linea=entrada.readline()
    linea=linea.rstrip()
    if not linea:
        break
    print(linea)
entrada.close()
