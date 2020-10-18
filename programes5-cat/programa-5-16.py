import nltk
import pickle
import nltk

entrada=open('etiquetador-cat.pkl','rb')
etiquetador=pickle.load(entrada)
entrada.close()

oracio="l'àcid desoxiribonucleic (ADN o DNA) és un àcid nucleic que conté les instruccions genètiques utilitzades en el desenvolupament i funcionament de tots els éssers vius coneguts, així com en alguns virus, des d'un punt de vista químic, l'ADN es compon de dos llargs polímers d'unitats simples anomenades nucleòtids, amb un tronc compost de sucres i grups fosfats units per enllaços èster"
tokenitzador=nltk.tokenize.RegexpTokenizer('[ldsmLDSM]\'|\w+|[^\w\s]+')
tokens=tokenitzador.tokenize(oracio)
analisi=etiquetador.tag(tokens)
print(analisi)
