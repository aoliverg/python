import codecs
import nltk

entrada=codecs.open("diccionari-cat.txt","r",encoding="utf-8")

tagged_words=[]
tagged_sents=[]
cont=0
for linia in entrada:
    cont+=1
    if cont==10000:
        break
    linia=linia.rstrip()
    camps=linia.split(" ")
    forma=camps[0]
    lema=camps[1]
    etiqueta=camps[2]
    tupla=(forma,etiqueta)
    tagged_words.append(tupla)
tagged_sents.append(tagged_words)

affix_tagger=nltk.AffixTagger(tagged_sents, affix_length=-3, min_stem_length=2)
