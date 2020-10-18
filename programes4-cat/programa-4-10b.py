from nltk.tokenize import RegexpTokenizer

oracio="El Sr. Martínez arribarà demà d'Alacant amb la R.E.N.F.E. a les 22.30 h. i s'haurà d'allotjar a l'hotel de l'estació."
tokenitzador=RegexpTokenizer('Sr\.|h\.|R\.E\.N\.F\.E\.|[ldsmLDSM]\'|\w+|[^\w\s]+')
tokens=tokenitzador.tokenize(oracio)
print(tokens)
