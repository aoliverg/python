import nltk.tokenize.punkt
import pickle
import codecs
segmentador = nltk.tokenize.punkt.PunktSentenceTokenizer()
text = codecs.open("DOGC-2015-cat.txt","r","utf8").read()
segmentador.train(text)
out = open("catalan.pickle","wb")
pickle.dump(segmentador, out)
out.close()

