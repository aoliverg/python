import codecs
import nltk
import pickle

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
        
diccionari=codecs.open("diccionari-cat.txt","r",encoding="utf-8")

tagged_words=[]
tagged_sents=[]
cont=0
for linia in diccionari:
    #cont+=1
    #if cont==10000:
    #    break
    linia=linia.rstrip()
    camps=linia.split(" ")
    forma=camps[0]
    lema=camps[1]
    etiqueta=camps[2]
    tupla=(forma,etiqueta)
    tagged_words.append(tupla)
tagged_sents.append(tagged_words)

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

default_tagger=nltk.DefaultTagger("NP00000")
affix_tagger=nltk.AffixTagger(tagged_sents, affix_length=-3, min_stem_length=2,backoff=default_tagger)
unigram_tagger_diccionari=nltk.UnigramTagger(tagged_sents,backoff=affix_tagger)
unigram_tagger=nltk.UnigramTagger(tagged_sents,backoff=unigram_tagger_diccionari)
bigram_tagger=nltk.BigramTagger(tagged_sents,backoff=unigram_tagger)
trigram_tagger=nltk.TrigramTagger(tagged_sents,backoff=bigram_tagger)

sortida=open('etiquetador-cat.pkl', 'wb')
pickle.dump(trigram_tagger, sortida, -1)
sortida.close()
