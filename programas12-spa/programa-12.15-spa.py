import spacy
from spacy import displacy
from pathlib import Path

# 1. Cargamos el modelo en castellano
nlp = spacy.load('es_core_news_md')

# 2. Una frase con entidades variadas
text = """
El presidente del Gobierno se reunió en Madrid con representantes de la Unión Europea el pasado 15 de marzo.
"""

doc = nlp(text)

print(f"Análisis NER de: {text.strip()}\n")
print(f"{'Entidad':<30} | {'Categoría':<10} | {'Explicación'}")
print("-" * 70)

# 3. Iteramos por las entidades detectadas
for ent in doc.ents:
    # spacy.explain nos da una descripción de la etiqueta (en inglés)
    explicacio = spacy.explain(ent.label_)
    print(f"{ent.text:<30} | {ent.label_:<10} | {explicacio}")

# 4. Visualización gráfica (Genera un HTML con colores para cada entidad)
html = displacy.render(doc, style="ent", jupyter=False)
Path("ner_visualizacion.html").write_text(html, encoding="utf-8")

print("\nSe ha generado 'ner_visualizacion.html'. ¡Ábrelo para ver las entidades en colores!")
