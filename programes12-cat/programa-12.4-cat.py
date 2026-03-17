import spacy

# 1. Carreguem el model en català
nlp = spacy.load('ca_core_news_md')

# 2. Definim un text amb diverses frases i possibles trampes
text = """L'Institut d'Estudis Catalans (IEC) va ser fundat el 1907. El Dr. Pompeu Fabra va ser una figura clau en la normativització de la llengua! Avui en dia, gairebé 10.5 milions de persones el parlen (aproximadament). T'agradaria aprendre'n més?"""

# 3. Processem el text
doc = nlp(text)

llista_frases = list(doc.sents)
# Ara sí que podem comptar-les
nombre_frases = len(llista_frases)
print(f"El text té un total de {nombre_frases} frases.")

# I accedir a una posició concreta (recorda que comencen per 0)
print(f"La segona frase és: {llista_frases[1].text}")
