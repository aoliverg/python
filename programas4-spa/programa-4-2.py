from nltk.corpus.reader.plaintext import PlaintextCorpusReader
corpus = PlaintextCorpusReader(".", 'mobi_dick.txt')

for oracion in corpus.sents():
    print(oracion)
