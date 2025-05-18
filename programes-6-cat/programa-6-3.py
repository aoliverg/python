import nltk
import codecs
productions = []
S = nltk.Nonterminal('S')
for tree in nltk.corpus.treebank.parsed_sents():
    productions += tree.productions()
grammar = nltk.induce_pcfg(S, productions)
sortida=codecs.open("gramatica-prob-eng.txt","w",encoding="utf-8")
sortida.write(str(grammar))
viterbi_parser = nltk.ViterbiParser(grammar)
frase="the man saw the girl in the park"
tokens = frase.split()
for analisi in viterbi_parser.parse(tokens):
    print(analisi)
    analisi.draw()