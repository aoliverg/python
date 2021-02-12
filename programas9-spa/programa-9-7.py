import codecs
entrada=codecs.open("cdlconsulteca.txt","r",encoding="utf-8")
salida=codecs.open("cdlconsulteca-mod.txt","w",encoding="utf-8")

for linea in entrada:
    linea=linea.rstrip()
    campos=linea.split("\t")
    cadena=campos[3]+"\t"+campos[2]+"\t"+campos[4]
    print(cadena)
    salida.write(cadena+"\n")
