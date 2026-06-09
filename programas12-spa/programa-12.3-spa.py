import spacy

# 1. Cargamos el model en español
nlp = spacy.load('es_core_news_md')

# 2. Definimos un texto con varias frases y posibles trampas
text = """El Instituto de Estudios Catalanes (IEC) fue fundado en 1907. ¡El Dr. Pompeu Fabra fue una figura clave en la normativización de la lengua! Hoy en día, casi 10.5 millones de personas lo hablan (aproximadamente). ¿Te gustaría aprender más?"""

# 3. Procesamos el texto
doc = nlp(text)

llista_frases = list(doc.sents)
# Ahora sí que podemos contarlas
nombre_frases = len(llista_frases)
print(f"El texto tiene un total de {nombre_frases} frases.")

# Y acceder a una posición concreta (recuerda que empiezan por 0)
print(f"La segunda frase es: {llista_frases[1].text}")
