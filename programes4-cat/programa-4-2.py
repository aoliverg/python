from nltk.corpus.reader.plaintext import PlaintextCorpusReader
corpus = PlaintextCorpusReader(".", 'mobi_dick.txt')

for oracio in corpus.sents():
    print(oracio)
