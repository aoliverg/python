import nltk
grammar = nltk.PCFG.fromstring("""
S  -> SN SV  [1.0]
SN -> PrP  [0.3]
SN -> Det N      [0.5]
SN -> SN SP  [0.2]
SP -> Prep SN    [1.0]
SV -> V    [0.2]
SV -> V SN  [0.4]
SV -> V SN SP  [0.4]
PrP -> 'jo'      [1.0]
Det -> 'la'      [0.5]
Det -> 'el'      [0.5]
        N -> 'noia'      [0.5]
        N -> 'telescopi' [0.5]
        Prep -> 'amb'    [1.0]
        V -> 'miro'      [1.0]
    """)
viterbi_parser = nltk.ViterbiParser(grammar)
frase="jo miro la noia amb el telescopi"
tokens = frase.split()
for analisi in viterbi_parser.parse(tokens):
    print(analisi)
    analisi.draw()