import nltk
gramatica_senzilla=nltk.CFG.fromstring("""
    O -> SN SV
    SN -> Det N
    SV -> V
    Det -> 'el'
    N -> 'nen'
    V -> 'canta'
    """)
frase=['el', 'nen', 'canta']
parser = nltk.ChartParser(gramatica_senzilla)
arbres = parser.parse(frase)
for arbre in arbres:
    print(arbre)
    arbre.draw()