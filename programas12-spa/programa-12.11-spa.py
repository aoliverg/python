import spacy

# 1. Cargamos el modelo en castellano
print("--- Inicializando spaCy...")
try:
    nlp = spacy.load('es_core_news_md')
except OSError:
    from spacy.cli import download
    download('es_core_news_md')
    nlp = spacy.load('es_core_news_md')

# 2. Nuestra oración con la palabra polisémica "sobre"
oracio = "¿El estudiante dejó el sobre amarillo sobre la mesa, verdad?"

# 3. Procesamos la oración (se realiza el análisis y la lematización)
doc = nlp(oracio)

print(f"\nOración analizada: {oracio}\n")
print(f"{'Token':<12} | {'Lema':<12} | {'POS':<6} | {'Morfología (Rasgos)'}")
print("-" * 80)

# 4. Iteramos sobre cada token para extraer toda la información
for token in doc:
    # token.text   : La palabra original
    # token.lemma_ : La forma base (lema)
    # token.pos_   : La categoría gramatical
    # token.morph  : Los rasgos morfológicos
    
    morfologia = str(token.morph) if str(token.morph) else "-"
    
    print(f"{token.text:<12} | {token.lemma_:<12} | {token.pos_:<6} | {morfologia}")
