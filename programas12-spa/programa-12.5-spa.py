import spacy
from spacy.symbols import ORTH

nlp = spacy.load('es_core_news_md')

text = "El Excmo. Sr. Pérez está de viaje. Volverá pronto."
doc = nlp(text)

print("--- SEGMENTACIÓN POR DEFECTO ---")
for frase in doc.sents:
    print(frase.text)

excepcion = [{ORTH: "Excmo."}]
nlp.tokenizer.add_special_case("Excmo.", excepcion)

doc = nlp(text)

print("--- SEGMENTACIÓN AÑADIENDO ABREVIATURA ---")
for frase in doc.sents:
    print(frase.text)
