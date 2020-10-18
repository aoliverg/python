import codecs
import nltk
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk.tokenize import RegexpTokenizer

diccionari={}
arxiu_diccionari=codecs.open("diccionari-cat.txt","r",encoding="utf-8")

for entrada in arxiu_diccionari:
    entrada=entrada.rstrip()
    camps=entrada.split(" ")
    forma=camps[0]
    lema=camps[1]
    etiqueta=camps[2]
    if forma in diccionari:
        diccionari[forma]=diccionari.get(forma,"")+" "+lema+" "+etiqueta
    else:
        diccionari[forma]=lema+" "+etiqueta

segmentador= nltk.data.load("catalan-mod.pickle")
tokenitzador=RegexpTokenizer('[ldsmLDSM]\'|\w+|[^\w\s]+')

corpus = PlaintextCorpusReader(".", 'noticia.txt',word_tokenizer=tokenitzador,sent_tokenizer=segmentador)

for forma in corpus.words():
    if forma in diccionari:
        info=diccionari[forma]
    else:
        info="DESCONEGUDA"
    print(forma+" "+info)
