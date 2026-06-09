import spacy

nlp = spacy.load('es_core_news_md')
doc = nlp("El estudiante lee un libro muy antiguo.")

print(f"{'Token':<12} | {'Relación':<10} | {'Head':<12}")
print("-" * 42)
for token in doc:
    print(f"{token.text:<12} | {token.dep_:<10} | {token.head.text:<12}")
