import spacy
from spacy.cli import download  # Importamos la herramiena de descarga al principio

def carregar_nlp(nom_model='es_core_news_md'):
    try:
        print(f"--- Inicializando el modelo  ({nom_model})...")
        # exclude=['ner'] evita cargar el reconocedor de entidades si no lo necesitamos
        return spacy.load(nom_model, exclude=['ner'])
    except OSError:
        print(f"--- El modelo '{nom_model}' no se ha encontrado.")
        print("Descargándolo automáticamente. Esto puede tardar un poco...")
        
        # Descargamos el model directamente
        download(nom_model)
        
        # Volvemos a intentar cargarlo una vez descargado
        print(f"--- Carga completada. Inicializando ({nom_model})...")
        return spacy.load(nom_model, exclude=['ner'])

# Uso del programa
nlp = carregar_nlp('es_core_news_md')
doc = nlp("Esto es una prueba de carga automática.")

print(f"Texto procesado con éxito: {doc.text}")
