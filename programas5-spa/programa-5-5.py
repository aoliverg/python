import codecs
import nltk
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk.tokenize import RegexpTokenizer

diccionario={}
archivo_diccionario=codecs.open("diccionario-freeling-spa.txt","r",encoding="utf-8")

for entrada in archivo_diccionario:
    entrada=entrada.rstrip()
    camps=entrada.split(":")
    if len(camps)>=3:
        forma=camps[0]
        lema=camps[1]
        etiqueta=camps[2]
        if forma in diccionario:
            diccionario[forma]=diccionario.get(forma,"")+" "+lema+" "+etiqueta
        else:
            diccionario[forma]=lema+" "+etiqueta

#Añadimos los signos de puntuación
diccionario['"']='" Fe'
diccionario["'"]="' Fe"
diccionario['.']='. Fp'
diccionario[',']=', Fc'
diccionario[';']='; Fx'
diccionario[':']=': Fd'
diccionario['(']='( Fpa'
diccionario[')']=') Fpt'
diccionario['[']='[ Fca'
diccionario[']']='] Fct'


segmentador= nltk.data.load("spanish.pickle")
tokenitzador=RegexpTokenizer('\w+|[^\w\s]+')

corpus = PlaintextCorpusReader(".", 'noticia.txt',word_tokenizer=tokenitzador,sent_tokenizer=segmentador)

for forma in corpus.words():
    if forma in diccionario:
        info=diccionario[forma]
    elif forma.lower() in diccionario:
        info=diccionario[forma.lower()]
    else:
        info="DESCONOCIDA"
    print(forma+" "+info)