import nltk

print("TEXTO EN BRUTO")
a=input()

texto_en_bruto=nltk.corpus.gutenberg.raw("melville-moby_dick.txt")
print(texto_en_bruto[0:100000])

print("PÁRRAFOS")
a=input()

parrafos=nltk.corpus.gutenberg.paras("melville-moby_dick.txt")
for para in parrafos:
    print(para)

print("ORACIONES")
a=input()

oraciones=nltk.corpus.gutenberg.sents("melville-moby_dick.txt")
for oracion in oraciones:
    print(oracion)

print("PALABRAS")
a=input()

palabras=nltk.corpus.gutenberg.words("melville-moby_dick.txt")
for palabra in palabras:
    print(palabra)
