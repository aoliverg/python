from nltk.tokenize import TreebankWordTokenizer as tokenitzador

oracio="We need to conduct an assessment to learn whether a student's dificulties are because he or she can't or won't complete assignments."
tokens=tokenitzador().tokenize(oracio)
print(tokens)
