import spacy

# Inicializamos el pipeline en castellano (asegúrate de haber hecho el python -m spacy download previamente)
nlp = spacy.load('es_core_news_md')

# El texto que queremos analizar
text = "spaCy es una herramienta fantástica para analizar el castellano."

# Procesamos el texto
doc = nlp(text)

# Comprobamos que funciona imprimiendo el texto procesado
print(doc.text)

# Mostramos por pantalla los diferentes análisis obtenidos
print(f"{'Texto':<12} | {'Lema':<12} | {'Categoría (POS)':<15} | {'Sintaxis (Dep)'}")
print("-" * 60)

for token in doc:
    # token.text: La palabra original
    # token.lemma_: El lema (forma base de la palabra)
    # token.pos_: La categoría gramatical (sustantivo, verbo, adjetivo...)
    # token.dep_: La función sintáctica dentro de la frase
    print(f"{token.text:<12} | {token.lemma_:<12} | {token.pos_:<15} | {token.dep_}")
