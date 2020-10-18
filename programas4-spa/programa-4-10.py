from nltk.tokenize import RegexpTokenizer

oracion="El Sr. Martínez llegará mañana de Alicante con la R.E.N.F.E. a las 22.30 h. y se alojará en el hotel de la estación."
tokenizador=RegexpTokenizer('\w+|[^\w\s]+')
tokens=tokenizador.tokenize(oracion)
print(tokens)
