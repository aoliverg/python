import codecs
import nltk

entrada=codecs.open("catalanTagged_0_5000-utf-8.txt","r",encoding="utf-8")

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

unigram_tagger=nltk.UnigramTagger(tagged_sents)
bigram_tagger=nltk.BigramTagger(tagged_sents,backoff=unigram_tagger)
trigram_tagger=nltk.TrigramTagger(tagged_sents,backoff=bigram_tagger)
oracio="l'àcid desoxiribonucleic (ADN o DNA) és un àcid nucleic que conté les instruccions genètiques utilitzades en el desenvolupament i funcionament de tots els éssers vius coneguts, així com en alguns virus, des d'un punt de vista químic, l'ADN es compon de dos llargs polímers d'unitats simples anomenades nucleòtids, amb un tronc compost de sucres i grups fosfats units per enllaços èster"
tokenitzador=nltk.tokenize.RegexpTokenizer('[ldsmLDSM]\'|\w+|[^\w\s]+')
tokens=tokenitzador.tokenize(oracio)
analisi=trigram_tagger.tag(tokens)
print(analisi)
