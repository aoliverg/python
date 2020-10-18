import nltk.data

parrafo="Today Mr. Smith and Ms. Johanson will meet at St. Patrick church."

segmentador=nltk.data.load("tokenizers/punkt/PY3/english.pickle")
segmentos=segmentador.tokenize(parrafo)
print(segmentos)

