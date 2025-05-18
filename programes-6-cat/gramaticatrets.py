import nltk
import sys
import os.path
from nltk.parse import load_parser

if len(sys.argv)<3:
    print("Es necessiten dos argument: gramatica i frase a analitzar")
    sys.exit()
gramatica=sys.argv[1]
if not os.path.exists(gramatica):
    print("El fitxer de gramatica no esta en la ruta especificada")
    sys.exit()
try:
    gramatica2=load_parser('file:%s' % gramatica)
except:
    print("Error en la gramatica:")
    print(sys.exc_info()[1])
    sys.exit()
oracio=sys.argv[2]
try:
    oracio2=oracio.split()
    arbres = gramatica2.parse(oracio2)
    for arbre in arbres:
        print(arbre)
        arbre.draw()
except:
    print("Error en l'analisi:")
    print(sys.exc_info()[1])
    sys.exit()
oracio=sys.argv[2]
