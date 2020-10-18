import nltk
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk.tokenize import RegexpTokenizer

segmentador= nltk.data.load("spanish-mod.pickle")
tokenizador=RegexpTokenizer('\w+|[^\w\s]+')

corpus = PlaintextCorpusReader(".", 'DOGC-2015-spa.txt',word_tokenizer=tokenizador,sent_tokenizer=segmentador)

frecuencia={}

for palabra in corpus.words():
    frecuencia[palabra]=frecuencia.get(palabra,0)+1

for clave in frecuencia.keys():
    print(frecuencia[clave],clave)
