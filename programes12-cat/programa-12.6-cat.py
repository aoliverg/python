import spacy
from spacy.language import Language

nlp = spacy.load('ca_core_news_md')

# 1. Definim el nostre component de regles
@Language.component("regles_segmentacio_custom")
def segmentacio_custom(doc):
    # Iterem per tots els tokens menys l'últim
    for token in doc[:-1]: 
        # Si trobem un punt i coma o un salt de línia...
        if token.text in [";", "\n"]:
            # Marquem el següent token com l'inici d'una nova frase
            doc[token.i + 1].is_sent_start = True
    return doc

# 2. Afegim el component al pipeline, abans del parser
nlp.add_pipe("regles_segmentacio_custom", before="parser")

# 3. Provem-ho
text = "Primera frase normal. Segona frase amb punt i coma; tercera frase forçada per la regla.\nI quarta frase després del salt de línia."
doc = nlp(text)

print("--- SEGMENTACIÓ AMB REGLES CUSTOM ---")
for frase in doc.sents:
    # Utilitzem .strip() per netejar espais o salts de línia al principi/final
    print(f"- {frase.text.strip()}")
