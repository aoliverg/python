import spacy

# 1. Carreguem el model en català
nlp = spacy.load('ca_core_news_md')

# 2. Definim un text amb diverses frases i possibles trampes
text = """L'Institut d'Estudis Catalans (IEC) va ser fundat el 1907. El Dr. Pompeu Fabra va ser una figura clau en la normativització de la llengua! Avui en dia, gairebé 10.5 milions de persones el parlen (aproximadament). T'agradaria aprendre'n més?"""

# 3. Processem el text
doc = nlp(text)

# 4. Iterem sobre les frases i les imprimim
print("--- FRASES DETECTADES ---")
for i, frase in enumerate(doc.sents, 1):
    print(f"Frase {i}: {frase.text}")
