import nltk
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk.tokenize import RegexpTokenizer
from nltk import FreqDist
segmentador= nltk.data.load("catalan.pickle")
tokenitzador=RegexpTokenizer('[ldsmLDSM]\'|\w+|[^\w\s]+')

corpus = PlaintextCorpusReader(".", 'DOGC-2015-cat.txt',word_tokenizer=tokenitzador,sent_tokenizer=segmentador)

frequencia=FreqDist(corpus.words())

for mc in frequencia.most_common():
    print(mc)


