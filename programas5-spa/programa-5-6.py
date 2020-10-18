import nltk
oracion="They refuse to permit us to obtain the refuse permit"
palabras = nltk.tokenize.word_tokenize(oracion)
analisis=nltk.pos_tag(palabras)
print(analisis)
