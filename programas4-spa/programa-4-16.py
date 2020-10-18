import nltk
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk.tokenize import RegexpTokenizer
from nltk import FreqDist
segmentador= nltk.data.load("spanish-mod.pickle")
tokenizador=RegexpTokenizer('\w+|[^\w\s]+')

corpus = PlaintextCorpusReader(".", 'DOGC-2015-spa.txt',word_tokenizer=tokenizador,sent_tokenizer=segmentador)

frequencia=FreqDist(corpus.words())

for mc in frequencia.most_common():
    print(mc)


