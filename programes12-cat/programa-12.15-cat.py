import spacy
from spacy import displacy
from pathlib import Path

# 1. Carreguem el model en català
nlp = spacy.load('ca_core_news_md')

# 2. Una frase amb entitats variades
text = """
El president de la Generalitat de Catalunya, Salvador Illa, es va reunir a Barcelona 
amb representants de la Unió Europea el passat 15 de març.
"""

doc = nlp(text)

print(f"Anàlisi NER de: {text.strip()}\n")
print(f"{'Entitat':<30} | {'Categoria':<10} | {'Explicació'}")
print("-" * 70)

# 3. Iterem per les entitats detectades
for ent in doc.ents:
    # spacy.explain ens dóna una descripció de l'etiqueta (en anglès)
    explicacio = spacy.explain(ent.label_)
    print(f"{ent.text:<30} | {ent.label_:<10} | {explicacio}")

# 4. Visualització gràfica (Genera un HTML amb colors per a cada entitat)
html = displacy.render(doc, style="ent", jupyter=False)
Path("ner_visualitzacio.html").write_text(html, encoding="utf-8")

print("\nS'ha generat 'ner_visualitzacio.html'. Obre'l per veure les entitats amb colors!")
