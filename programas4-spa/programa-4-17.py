import nltk
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk.tokenize import RegexpTokenizer
from nltk import FreqDist
import codecs

segmentador= nltk.data.load("spanish-mod.pickle")
tokenizador=RegexpTokenizer('\w+|[^\w\s]+')

corpus = PlaintextCorpusReader(".", 'DOGC-2015-spa.txt',word_tokenizer=tokenizador,sent_tokenizer=segmentador)

frecuencia=FreqDist(corpus.words())

salida=codecs.open("frecuencias.txt","w",encoding="utf-8")

for mc in frecuencia.most_common():
    palabra=mc[0]
    frecuencia_absoluta=mc[1]
    frecuencia_relativa=frecuencia.freq(palabra)
    cadena=str(frecuencia_absoluta)+"\t"+str(frecuencia_relativa)+"\t"+palabra
    salida.write(cadena+"\n")


