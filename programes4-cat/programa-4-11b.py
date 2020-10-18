from nltk.tokenize import sent_tokenize

paragraf1="Avui fa un dia molt bonic. Demà l'Albert anirà a dinar a casa."

paragraf2="El Sr. Martínez arribarà demà d'Alacant amb la R.E.N.F.E. a les 22.30 h. i s'haurà d'allotjar a l'hotel de l'estació. L'endemà visitarà al Dr. Rovira a l'Av. Tibidabo. La tornada la farà en avió en el vol AF.352."

segments1=sent_tokenize(paragraf1)
print(segments1)
segments2=sent_tokenize(paragraf2)
print(segments2)
