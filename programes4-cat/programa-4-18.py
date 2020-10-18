import nltk
from nltk.corpus import cess_cat
import re
import codecs

paraules=cess_cat.words()
freqdist=nltk.FreqDist(paraules)
sortida=codecs.open("sortida.txt","w", encoding="utf-8")

posicio=0
p = re.compile('\w+')
for mc in freqdist.most_common(50):
    if p.match(mc[0]):
        posicio+=1
        freq=mc[1]
        fxr=posicio*freq
        sortida.write(mc[0]+"\t"+str(freq)+"\t"+str(posicio)+"\t"+str(fxr)+"\n")
