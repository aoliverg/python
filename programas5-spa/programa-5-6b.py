import nltk
oracion="They refuse to permit us to obtain the refuse permit"
palabras = nltk.tokenize.word_tokenize(oracion)
analisis=nltk.pos_tag(palabras)

for ana in analisis:
    forma=ana[0]
    etiqueta=ana[1]
    universal=nltk.tag.mapping.map_tag('en-ptb', 'universal', etiqueta)
    print(forma,etiqueta,universal)
