import nltk
oracio="They refuse to permit us to obtain the refuse permit"
paraules = nltk.tokenize.word_tokenize(oracio)
analisi=nltk.pos_tag(paraules)

for ana in analisi:
    forma=ana[0]
    etiqueta=ana[1]
    universal=nltk.tag.mapping.map_tag('en-ptb', 'universal', etiqueta)
    print(forma,etiqueta,universal)
