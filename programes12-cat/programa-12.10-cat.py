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

# 3. Processem l'oració (aquí és on es fa la màgia de la desambiguació)
doc = nlp(oracio)

print(f"\nOració analitzada: {oracio}\n")
print(f"{'Token':<12} | {'POS (Categoria)':<15} | {'Morfologia (Trets)'}")
print("-" * 75)

# 4. Iterem sobre cada token per extreure'n l'etiqueta correcta
for token in doc:
    # token.text : La paraula original
    # token.pos_ : La categoria gramatical desambiguada (NOUN, VERB, ADP...)
    # token.morph: Els trets morfològics (Gènere, Nombre...)
    
    # Convertim l'objecte morph a text (string) per poder-lo imprimir bé. 
    # Si està buit (ex. preposicions), hi posem un guionet.
    morfologia = str(token.morph) if str(token.morph) else "-"
    
    print(f"{token.text:<12} | {token.pos_:<15} | {morfologia}")
