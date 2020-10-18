import nltk.tokenize.punkt
import pickle
import codecs
segmentador = nltk.tokenize.punkt.PunktSentenceTokenizer()
texto = codecs.open("DOGC-2015-spa.txt","r","utf8").read()
segmentador.train(texto)
out = open("spanish.pickle","wb")
pickle.dump(segmentador, out)
out.close()

