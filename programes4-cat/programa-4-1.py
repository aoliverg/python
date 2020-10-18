import nltk

print("TEXT EN BRUT")
a=input()

text_en_brut=nltk.corpus.gutenberg.raw("melville-moby_dick.txt")
print(text_en_brut[0:100000])

print("PARAGRAFS")
a=input()

paragrafs=nltk.corpus.gutenberg.paras("melville-moby_dick.txt")
for para in paragrafs:
    print(para)

print("ORACIONS")
a=input()

oracions=nltk.corpus.gutenberg.sents("melville-moby_dick.txt")
for oracio in oracions:
    print(oracio)

print("PARAULES")
a=input()

paraules=nltk.corpus.gutenberg.words("melville-moby_dick.txt")
for paraula in paraules:
    print(paraula)
