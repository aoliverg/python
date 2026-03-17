import spacy

nlp = spacy.load('ca_core_news_md')
doc = nlp("L'estudiant llegeix un llibre molt antic.")

print(f"{'Token':<12} | {'Relació':<10} | {'Cap (Pare)':<12}")
print("-" * 40)
for token in doc:
    print(f"{token.text:<12} | {token.dep_:<10} | {token.head.text:<12}")
