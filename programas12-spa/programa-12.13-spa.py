import spacy

nlp = spacy.load('es_core_news_md')
doc = nlp("El estudiante de la universidad lee un libro muy antiguo.")

print("--- Sintagmas Nominales detectados ---")
for chunk in doc.noun_chunks:
    # Mostramos el texto del sintagma, su núcleo y su función
    print(f"Sintagma: {chunk.text:<30} | Núcleo: {chunk.root.text}")
