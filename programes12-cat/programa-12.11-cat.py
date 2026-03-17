import spacy

# 1. Carreguem el model en català
print("--- Inicialitzant spaCy...")
try:
    nlp = spacy.load('ca_core_news_md')
except OSError:
    from spacy.cli import download
    download('ca_core_news_md')
    nlp = spacy.load('ca_core_news_md')

# 2. La nostra oració amb la paraula polisèmica "sobre"
oracio = "L'estudiant va deixar el sobre groc sobre la taula, oi?"

# 3. Processem l'oració (es fa la desambiguació i la lematització)
doc = nlp(oracio)

print(f"\nOració analitzada: {oracio}\n")
print(f"{'Token':<12} | {'Lema':<12} | {'POS':<6} | {'Morfologia (Trets)'}")
print("-" * 80)

# 4. Iterem sobre cada token per extreure'n tota la informació
for token in doc:
    # token.text   : La paraula original
    # token.lemma_ : La forma base (lema)
    # token.pos_   : La categoria gramatical desambiguada
    # token.morph  : Els trets morfològics
    
    morfologia = str(token.morph) if str(token.morph) else "-"
    
    print(f"{token.text:<12} | {token.lemma_:<12} | {token.pos_:<6} | {morfologia}")
