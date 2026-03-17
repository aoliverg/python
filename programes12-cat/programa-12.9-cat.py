import spacy
import os

def carregar_diccionari_morfologic(ruta_fitxer):
    """
    Llegeix el diccionari de FreeLing i en retorna un de Python.
    """
    diccionari = {}
    if not os.path.exists(ruta_fitxer):
        print(f"Error: No s'ha trobat el fitxer '{ruta_fitxer}'.")
        return diccionari

    print(f"Carregant el diccionari '{ruta_fitxer}' a la memòria...")
    with open(ruta_fitxer, 'r', encoding='utf-8') as fitxer:
        for linia in fitxer:
            parts = linia.strip().split()
            if len(parts) >= 3:
                forma, lema, etiqueta = parts[0], parts[1], parts[2]
                interpretacio = f"[{lema} - {etiqueta}]"
                
                if forma not in diccionari:
                    diccionari[forma] = []
                diccionari[forma].append(interpretacio)
                
    print(f"Diccionari carregat! Conté {len(diccionari)} formes úniques.\n")
    return diccionari


# 1. Carreguem el model de spaCy en català (només per tokenitzar)
print("--- Inicialitzant spaCy...")
try:
    nlp = spacy.load('ca_core_news_md')
except OSError:
    print("Descarregant el model ca_core_news_md...")
    from spacy.cli import download
    download('ca_core_news_md')
    nlp = spacy.load('ca_core_news_md')

# 2. Carreguem el diccionari extern
fitxer_diccionari = 'freeling-cat.txt'
analitzador_morfologic = carregar_diccionari_morfologic(fitxer_diccionari)

# 3. Només executem l'anàlisi si el diccionari s'ha carregat correctament
if analitzador_morfologic:
    
    # Definim l'oració d'entrada
    oracio = "L'estudiant va deixar el sobre groc sobre la taula, oi?"
    
    # Tokenitzem l'oració amb spaCy
    doc = nlp(oracio)
    
    print(f"Oració a analitzar: {oracio}\n")
    print(f"{'Token':<12} | {'Interpretacions Possibles'}")
    print("-" * 80)
    
    # 4. Iterem sobre els tokens que ha separat spaCy
    for token in doc:
        # Convertim a minúscules per buscar-ho al diccionari
        paraula_cerca = token.text.lower()
        
        # Cas A: La paraula és al diccionari de FreeLing
        if paraula_cerca in analitzador_morfologic:
            opcions = ", ".join(analitzador_morfologic[paraula_cerca])
            print(f"{token.text:<12} | {opcions}")
            
        # Cas B: És un signe de puntuació (ho sabem gràcies a spaCy)
        elif token.is_punct:
            print(f"{token.text:<12} | [{token.text} - PUNCT]")
            
        # Cas C: Són espais en blanc (els ignorem)
        elif token.is_space:
            continue
            
        # Cas D: La paraula no és al diccionari (neologisme, error, etc.)
        else:
            print(f"{token.text:<12} | ESCONEGUDA (No és al diccionari)")
