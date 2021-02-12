import sys
import chardet
import codecs

fitxer_entrada=sys.argv[1]
raw_data=open(fitxer_entrada,"rb").read()
codificacio=chardet.detect(raw_data)
print("Archivo:",fitxer_entrada,"Codificación:",codificacio)
print(codificacio["encoding"])
codificacio=codificacio["encoding"]
if codificacio=="utf-8":
    print("Ya está en utf-8")
else:
    fitxer_sortida=fitxer_entrada+".utf8"
    entrada=codecs.open(fitxer_entrada,"r",encoding=codificacio)
    sortida=codecs.open(fitxer_sortida,"w",encoding="utf-8")

    for linia in entrada:
        sortida.write(linia)
