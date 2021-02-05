import nltk
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk.tokenize import RegexpTokenizer

segmentador= nltk.data.load("catalan.pickle")
tokenitzador=RegexpTokenizer('[ldsmLDSM]\'|\w+|[^\w\s]+')

corpus = PlaintextCorpusReader(".", 'DOGC-2015-cat.txt',word_tokenizer=tokenitzador,sent_tokenizer=segmentador)

ocurrencias=corpus.words()
tipos=set(ocurrencias)
riquezalexica=len(ocurrencias)/len(tipos)

print("OCURRENCIAS:",len(ocurrencias))
print("TIPUS:",len(tipos))
print("RIQUEZA LÊXICA:",round(riquezalexica,2))
