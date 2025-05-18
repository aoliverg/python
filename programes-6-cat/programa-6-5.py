import nltk
import nltk
import pickle
productions = []
S = nltk.Nonterminal('S')
for tree in nltk.corpus.cess_cat.parsed_sents():
    productions += tree.productions()
grammar = nltk.induce_pcfg(S, productions)
sortida=open('pcfg-cat.pkl', 'wb')
pickle.dump(grammar, sortida, -1)
sortida.close()