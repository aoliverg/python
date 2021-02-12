import nltk
import pickle
import codecs

#cargamos el etiquetador
entrada=open('etiquetador-spa.pkl','rb')
etiquetador=pickle.load(entrada)
entrada.close()

#cargamos las oraciones del corpus de test

entrada=codecs.open("fragmento-wikicorpus-tagged-spa.txt","r",encoding="utf-8")

tagged_words=[]
test_tagged_sents=[]
for linia in entrada:
    linia=linia.rstrip()
    if linia.startswith("<") or len(linia)==0:
        #nova linia
        if len(tagged_words)>0:
            test_tagged_sents.append(tagged_words)
            tagged_words=[]
    else:
        camps=linia.split(" ")
        forma=camps[0]
        lema=camps[1]
        etiqueta=camps[2]
        tupla=(forma,etiqueta)
        tagged_words.append(tupla)

precisio=etiquetador.evaluate(test_tagged_sents)
print("PRECISION: ",precisio)
