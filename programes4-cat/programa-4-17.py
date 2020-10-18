import nltk
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk.tokenize import RegexpTokenizer
from nltk import FreqDist
import codecs

segmentador= nltk.data.load("catalan.pickle")
tokenitzador=RegexpTokenizer('[ldsmLDSM]\'|\w+|[^\w\s]+')

corpus = PlaintextCorpusReader(".", 'DOGC-2015-cat.txt',word_tokenizer=tokenitzador,sent_tokenizer=segmentador)

frequencia=FreqDist(corpus.words())

sortida=codecs.open("frequencies.txt","w",encoding="utf-8")

for mc in frequencia.most_common():
    paraula=mc[0]
    frequencia_absoluta=mc[1]
    frequencia_relativa=frequencia.freq(paraula)
    cadena=str(frequencia_absoluta)+"\t"+str(frequencia_relativa)+"\t"+paraula
    sortida.write(cadena+"\n")


