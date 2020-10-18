import nltk.data

paragraf="Today Mr. Smith and Ms. Johanson will meet at St. Patrick church."

segmentador=nltk.data.load("tokenizers/punkt/PY3/english.pickle")
segments=segmentador.tokenize(paragraf)
print(segments)

