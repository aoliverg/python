import codecs
import nltk

entrada=codecs.open("fragmento-wikicorpus-tagged-spa.txt","r",encoding="utf-8")

tagged_words=[]
tagged_sents=[]
for linia in entrada:
    linia=linia.rstrip()
    if linia.startswith("<") or len(linia)==0:
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

bigram_tagger=nltk.BigramTagger(tagged_sents)
oracio="mañana por la mañana lloverá"
tokens=nltk.tokenize.word_tokenize(oracio)
analisi=bigram_tagger.tag(tokens)
print(analisi)
