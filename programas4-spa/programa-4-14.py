import nltk.data
import codecs
import pickle
segmentador=nltk.data.load("spanish.pickle")
archivo_abreviaturas=codecs.open("abr-spa.txt","r",encoding="utf-8")
abreviaturas_extra =[]
for abreviatura in archivo_abreviaturas.readlines():
    abreviatura=abreviatura.rstrip()
    abreviaturas_extra.append(abreviatura)
segmentador._params.abbrev_types.update(abreviaturas_extra)
out = open("spanish-mod.pickle","wb")
pickle.dump(segmentador, out)
out.close()
