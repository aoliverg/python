import spacy
import os

def cargar_diccionario_morfologico(ruta_fichero):
    """
    Lee el diccionario de FreeLing y devuelve uno de Python.
    """
    diccionario = {}
    if not os.path.exists(ruta_fichero):
        print(f"Error: No se ha encontrado el fichero '{ruta_fichero}'.")
        return diccionario

    print(f"Cargando el diccionario '{ruta_fichero}' en la memoria...")
    with open(ruta_fichero, 'r', encoding='utf-8') as fichero:
        for linea in fichero:
            parts = linea.strip().split()
            if len(parts) >= 3:
                forma, lema, etiqueta = parts[0], parts[1], parts[2]
                interpretacion = f"[{lema} - {etiqueta}]"
                
                if forma not in diccionario:
                    diccionario[forma] = []
                diccionario[forma].append(interpretacion)
                
    print(f"¡Diccionario cargado! Contiene {len(diccionario)} formas únicas.\n")
    return diccionario


# 1. Cargamos el modelo de spaCy en castellano (solo para tokenizar)
print("--- Inicializando spaCy...")
try:
    nlp = spacy.load('es_core_news_md')
except OSError:
    print("Descargando el modelo es_core_news_md...")
    from spacy.cli import download
    download('es_core_news_md')
    nlp = spacy.load('es_core_news_md')

# 2. Cargamos el diccionario externo
fichero_diccionario = 'freeling-spa.txt'
analizador_morfologico = cargar_diccionario_morfologico(fichero_diccionario)

# 3. Solo ejecutamos el análisis si el diccionario se ha cargado correctamente
if analizador_morfologico:
    
    # Definimos la oración de entrada con la palabra polisémica "sobre"
    oracion = "¿El estudiante dejó el sobre amarillo sobre la mesa, verdad?"
    
    # Tokenizamos la oración con spaCy
    doc = nlp(oracion)
    
    print(f"Oración a analizar: {oracion}\n")
    print(f"{'Token':<12} | {'Interpretaciones Posibles'}")
    print("-" * 80)
    
    # 4. Iteramos sobre los tokens que ha separado spaCy
    for token in doc:
        # Convertimos a minúsculas para buscarlo en el diccionario
        palabra_busqueda = token.text.lower()
        
        # Caso A: La palabra está en el diccionario de FreeLing
        if palabra_busqueda in analizador_morfologico:
            opciones = ", ".join(analizador_morfologico[palabra_busqueda])
            print(f"{token.text:<12} | {opciones}")
            
        # Caso B: Es un signo de puntuación (lo sabemos gracias a spaCy)
        elif token.is_punct:
            print(f"{token.text:<12} | [{token.text} - PUNCT]")
            
        # Caso C: Son espacios en blanco (los ignoramos)
        elif token.is_space:
            continue
            
        # Caso D: La palabra no está en el diccionario (neologismo, error, etc.)
        else:
            print(f"{token.text:<12} | DESCONOCIDA (No está en el diccionario)")
