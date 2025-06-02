import codecs
entrada=codecs.open("cdlconsulteca.txt","r",encoding="utf-8")
sortida=codecs.open("cdlconsulteca-mod.txt","w",encoding="utf-8")

for linia in entrada:
    linia=linia.rstrip()
    camps=linia.split("\t")
    cadena=camps[3]+"\t"+camps[1]+"\t"+camps[4]
    print(cadena)
    sortida.write(cadena+"\n")
