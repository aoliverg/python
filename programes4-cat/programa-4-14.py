import nltk.data
import codecs
import pickle
segmentador=nltk.data.load("catalan.pickle")
fitxer_abreviacions=codecs.open("abreviatures.txt","r",encoding="utf-8")
abreviacions_extra =[]
for abreviacio in fitxer_abreviacions.readlines():
    abreviacio=abreviacio.rstrip()
    abreviacions_extra.append(abreviacio)
segmentador._params.abbrev_types.update(abreviacions_extra)
out = open("catalan-mod.pickle","wb")
pickle.dump(segmentador, out)
out.close()
