import spacy
from spacy import displacy
from pathlib import Path

# 1. Carreguem el model normal
nlp = spacy.load('ca_core_news_md')

# 2. Creem el component EntityRuler i l'afegim ABANS del NER estadístic
# Això fa que les nostres regles tinguin prioritat
ruler = nlp.add_pipe("entity_ruler", before="ner")

# 3. Definim els nostres patrons personalitzats
patterns = [
    {"label": "PLAT", "pattern": "pa amb tomàquet"},
    {"label": "PLAT", "pattern": "escudella i carn d'olla"},
    {"label": "PLAT", "pattern": [{"LOWER": "crema"}, {"LOWER": "catalana"}]},
    {"label": "ORG", "pattern": "Universitat Oberta de Catalunya"} # Afegim una a una categoria existent
]

ruler.add_patterns(patterns)

# 4. Provem el sistema personalitzat
text = "A la Universitat Oberta de Catalunya hem dinat escudella i carn d'olla i de postres crema catalana."
doc = nlp(text)

print(f"Anàlisi personalitzada:\n")
for ent in doc.ents:
    print(f"Entitat: {ent.text:<30} | Categoria: {ent.label_}")
    
# 5. Visualització gràfica (Genera un HTML amb colors per a cada entitat)
html = displacy.render(doc, style="ent", jupyter=False)
Path("ner_visualitzacio2.html").write_text(html, encoding="utf-8")

print("\nS'ha generat 'ner_visualitzacio2.html'. Obre'l per veure les entitats amb colors!")
