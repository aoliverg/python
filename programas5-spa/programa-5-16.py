import nltk
import pickle
import nltk

entrada=open('etiquetador-spa.pkl','rb')
etiquetador=pickle.load(entrada)
entrada.close()

oracio="Mañana por la mañana lloverá."
tokenitzador=nltk.tokenize.RegexpTokenizer('\w+|[^\w\s]+')
tokens=tokenitzador.tokenize(oracio)
analisis=etiquetador.tag(tokens)
print(analisis)
