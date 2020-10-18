import nltk
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk.tokenize import RegexpTokenizer

segmentador= nltk.data.load("catalan.pickle")
tokenitzador=RegexpTokenizer('[ldsmLDSM]\'|\w+|[^\w\s]+')

corpus = PlaintextCorpusReader(".", 'DOGC-2015-cat.txt',word_tokenizer=tokenitzador,sent_tokenizer=segmentador)

ocurrencies=corpus.words()
tipus=set(ocurrencies)
riquesalexica=len(ocurrencies)/len(tipus)

print("OCURRENCIES:",len(ocurrencies))
print("TIPUS:",len(tipus))
print("RIQUESA LÊXICA:",round(riquesalexica,2))
