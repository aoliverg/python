import spacy

nlp = spacy.load('ca_core_news_md')
doc = nlp("L'estudiant de la universitat llegeix un llibre molt antic.")

print("--- Sintagmes Nominals detectats ---")
for chunk in doc.noun_chunks:
    # Mostrem el text del sintagma, el seu nucli i la seva funció
    print(f"Sintagma: {chunk.text:<30} | Nucli: {chunk.root.text}")
