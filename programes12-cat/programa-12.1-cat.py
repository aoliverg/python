import spacy
from spacy.cli import download  # Importem l'eina de descàrrega a l'inici

def carregar_nlp(nom_model='ca_core_news_md'):
    try:
        print(f"--- Inicialitzant el model ({nom_model})...")
        # exclude=['ner'] evita carregar el reconeixedor d'entitats si no el necessitem
        return spacy.load(nom_model, exclude=['ner'])
    except OSError:
        print(f"--- El model '{nom_model}' no s'ha trobat.")
        print("Descarregant-lo automàticament. Això pot trigar una mica...")
        
        # Descarreguem el model directament
        download(nom_model)
        
        # Tornem a intentar carregar-lo un cop descarregat
        print(f"--- Càrrega completada. Inicialitzant ({nom_model})...")
        return spacy.load(nom_model, exclude=['ner'])

# Ús del programa
nlp = carregar_nlp('ca_core_news_md')
doc = nlp("Això és una prova de càrrega automàtica.")

print(f"Text processat amb èxit: {doc.text}")
