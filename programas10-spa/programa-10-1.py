import codecs

entrada=codecs.open("catalog.xml","r",encoding="utf-8")
salida=codecs.open("catalog.txt","w",encoding="utf-8")
artist=""
title=""
year=""
for linia in entrada:
    linia=linia.rstrip().lstrip()
    if linia.startswith("</cd>"):
        if not artist=="" and not title=="" and not year=="":
            cadena=artist+"\t"+title+"\t"+year
            print(cadena)
            salida.write(cadena+"\n")
    if linia.startswith("<title>") and linia.endswith("</title>"):
        title=linia[7:-8]
    elif linia.startswith("<artist>") and linia.endswith("</artist>"):
        artist=linia[8:-9]
    elif linia.startswith("<year>") and linia.endswith("</year>"):
        year=linia[6:-7] 
