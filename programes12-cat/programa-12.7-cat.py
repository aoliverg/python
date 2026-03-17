import spacy
# Importem la classe i la funció de la teva llibreria srx_segmenter
from srx_segmenter import SrxSegmenter, parse

def carregar_nlp(nom_model='ca_core_news_md'):
    """Funció de càrrega segura de spaCy."""
    try:
        return spacy.load(nom_model)
    except OSError:
        print(f"Descarregant el model {nom_model}...")
        from spacy.cli import download
        download(nom_model)
        return spacy.load(nom_model)

# 1. Carreguem el model de spaCy en català
print("--- Inicialitzant spaCy...")
nlp = carregar_nlp('ca_core_news_md')

# 2. Llegim les regles del fitxer SRX
fitxer_regles = 'segment.srx' 
nom_regla_idioma = 'Catalan' # Aquest nom HA DE COINCIDIR amb el 'languagerulename' del teu fitxer XML

print(f"--- Llegint les regles SRX del fitxer '{fitxer_regles}'...")
try:
    # 'parse' retorna un diccionari amb totes les regles del fitxer
    totes_les_regles = parse(fitxer_regles)
    
    # Extraiem només les regles de l'idioma que ens interessa
    regles_catala = totes_les_regles[nom_regla_idioma]
except KeyError:
    print(f"Error: No s'ha trobat la regla '{nom_regla_idioma}' dins del fitxer SRX.")
    exit()
except Exception as e:
    print(f"Error llegint el fitxer SRX: {e}")
    exit()

# 3. Text de prova amb possibles paranys
text_original = "El Sr. Garcia (del dpt. de vendes) vindrà demà a les 10.30 hores. T'ho ha dit? Jo crec que sí."

# 4. PAS A: Segmentem el text PRIMER amb l'eina SRX
print("--- Segmentant el text amb SRX...")
# Inicialitzem l'objecte passant-li les regles i el text
segmentador = SrxSegmenter(rule=regles_catala, source_text=text_original)

# El mètode extract() retorna dues llistes: els segments purs i els espais en blanc.
# Nosaltres ens quedem amb la primera (les frases)
frases_srx, _ = segmentador.extract()

print("\n=== RESULTATS DE L'ANÀLISI ===")

# 5. PAS B: Processem cada frase individualment amb spaCy
for i, text_frase in enumerate(frases_srx, 1):
    # Passem la frase ja tallada pel SRX a l'spaCy
    doc = nlp(text_frase)
    
    print(f"\n[Frase {i} segmentada per SRX]: {doc.text}")
    print(f"{'Text':<12} | {'Lema':<12} | {'POS':<6} | {'Sintaxi'}")
    print("-" * 45)
    
    # Extraiem l'anàlisi de spaCy
    for token in doc:
        print(f"{token.text:<12} | {token.lemma_:<12} | {token.pos_:<6} | {token.dep_}")
