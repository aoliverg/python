import nltk
import pickle
import nltk
entrada=open('pcfg-cat.pkl','rb')
grammar=pickle.load(entrada)
entrada.close()
viterbi_parser = nltk.ViterbiParser(grammar)
frase="el noi mira la noia amb ulleres"
tokens = frase.split()
for analisi in viterbi_parser.parse(tokens):
    print(analisi)
    analisi.draw()