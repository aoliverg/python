import nltk
from nltk.corpus import cess_esp
import re
import codecs

palabras=cess_esp.words()
frecdist=nltk.FreqDist(palabras)
salida=codecs.open("salida.txt","w", encoding="utf-8")

posicion=0
p = re.compile('\w+')
for mc in frecdist.most_common(50):
    if p.match(mc[0]):
        posicion+=1
        frec=mc[1]
        fxr=posicion*frec
        salida.write(mc[0]+"\t"+str(frec)+"\t"+str(posicion)+"\t"+str(fxr)+"\n")
