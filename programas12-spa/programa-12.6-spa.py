import spacy
from spacy.language import Language

nlp = spacy.load('es_core_news_md')

# 1. Definimos nuestro componente de reglas
@Language.component("reglas_segmentacion_custom")
def segmentacio_custom(doc):
    # Iteramos por todos los tokens menos el último
    for token in doc[:-1]: 
        # Si encontramos un punto y coma o un salto de línea...
        if token.text in [";", "\n"]:
            # Marcamos el siguiente token como el inicio de una nueva frase
            doc[token.i + 1].is_sent_start = True
    return doc

# 2. Añadimos el componente al pipeline, antes del parser
nlp.add_pipe("reglas_segmentacion_custom", before="parser")

# 3. Lo probamos
text = "Primera frase normal. Segunda frase con punto y coma; tercera frase forzada por la regla.\nY cuarta frase después del salto de línea."
doc = nlp(text)

print("--- SEGMENTACIÓN CON REGLAS CUSTOM ---")
for frase in doc.sents:
    # Utilizamos .strip() para limpiar espacios o saltos de línea al principio/final
    print(f"- {frase.text.strip()}")
