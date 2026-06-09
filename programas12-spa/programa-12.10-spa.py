import spacy

# 1. Cargamos el modelo en castellano
print("--- Inicializando spaCy...")
try:
    nlp = spacy.load('es_dep_news_trf')
except OSError:
    from spacy.cli import download
    download('es_dep_news_trf')
    nlp = spacy.load('es_dep_news_trf')

# 2. Nuestra oración con la palabra polisémica "sobre"
oracio = "¿El estudiante dejó el sobre amarillo sobre la mesa, verdad?"

# 3. Procesamos la oración (aquí es donde se hace la magia de la desambiguación)
doc = nlp(oracio)

print(f"\nOración analizadora: {oracio}\n")
print(f"{'Token':<12} | {'POS (Categoría)':<15} | {'Morfología (Rasgos)'}")
print("-" * 75)

# 4. Iteramos sobre cada token para extraer la etiqueta correcta
for token in doc:
    # token.text : La palabra original
    # token.pos_ : La categoría gramatical desambiguada (NOUN, VERB, ADP...)
    # token.morph: Los rasgos morfológicos (Género, Número...)
    
    # Convertimos el objeto morph a texto (string) para poder imprimirlo bien. 
    # Si está vacío (ej. preposiciones), ponemos un guion.
    morfologia = str(token.morph) if str(token.morph) else "-"
    
    print(f"{token.text:<12} | {token.pos_:<15} | {morfologia}")
