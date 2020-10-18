import codecs
import nltk

entrada=codecs.open("catalanTagged_0_5000-utf-8.txt","r",encoding="utf-8")

tagged_words=[]
tagged_sents=[]
for linia in entrada:
    linia=linia.rstrip()
    if linia.startswith("<") or len(linia)==0:
        #nova linia
        if len(tagged_words)>0:
            tagged_sents.append(tagged_words)
            tagged_words=[]
    else:
        camps=linia.split(" ")
        forma=camps[0]
        lema=camps[1]
        etiqueta=camps[2]
        tupla=(forma,etiqueta)
        tagged_words.append(tupla)
tags=[]
for ts in tagged_sents:
    for wt in ts:
        tags.append(wt[1])

mft=nltk.FreqDist(tags).most_common(10)
print("Etiqueta més freqüent: ",mft)

default_tagger=nltk.DefaultTagger("NP00000")
