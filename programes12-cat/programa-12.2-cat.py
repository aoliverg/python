import spacy

# Inicialitzem el pipeline en català (assegura't d'haver fet el python -m spacy download previament)
nlp = spacy.load('ca_core_news_md')

# El text que volem analitzar
text = "L'spaCy és una eina fantàstica per analitzar el català."

# Processem el text
doc = nlp(text)

# Comprovem que funciona imprimint el text processat
print(doc.text)

# Mostrem per pantalla les diferents anàlisis obtingudes
print(f"{'Text':<12} | {'Lema':<12} | {'Categoria (POS)':<15} | {'Sintaxi (Dep)'}")
print("-" * 60)

for token in doc:
    # token.text: La paraula original
    # token.lemma_: El lema (forma base de la paraula)
    # token.pos_: La categoria gramatical (nom, verb, adjectiu...)
    # token.dep_: La funció sintàctica dins la frase
    print(f"{token.text:<12} | {token.lemma_:<12} | {token.pos_:<15} | {token.dep_}")
