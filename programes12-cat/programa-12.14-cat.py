import spacy
from spacy import displacy
from pathlib import Path

nlp = spacy.load('ca_core_news_md')
doc = nlp("L'estudiant de la universitat llegeix un llibre molt antic.")

# Generem el codi SVG de l'arbre
svg = displacy.render(doc, style="dep", jupyter=False)

# El guardem en un fitxer HTML per obrir-lo amb el navegador
Path("arbre_sintactic.html").write_text(svg, encoding="utf-8")
print("\n✅ Obre el fitxer 'arbre_sintactic.html' per veure l'anàlisi gràfica.")
