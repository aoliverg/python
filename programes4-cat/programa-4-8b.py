from nltk.tokenize import WhitespaceTokenizer
oracio="El Sr. Martínez arribarà demà d'Alacant amb la R.E.N.F.E. a les 22.30 h. i s'haurà d'allotjar a l'hotel de l'estació."
tokens=WhitespaceTokenizer().tokenize(oracio)
print(tokens)
