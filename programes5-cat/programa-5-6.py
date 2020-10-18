import nltk
oracio="They refuse to permit us to obtain the refuse permit"
paraules = nltk.tokenize.word_tokenize(oracio)
analisi=nltk.pos_tag(paraules)
print(analisi)
