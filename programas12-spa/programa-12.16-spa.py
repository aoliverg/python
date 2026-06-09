import spacy
from spacy import displacy
from pathlib import Path

# 1. Cargamos el modelo normal
nlp = spacy.load('es_core_news_md')

# 2. Creamos el componente EntityRuler y lo añadimos ANTES del NER estadístico
# Esto hace que nuestras reglas tengan prioridad
ruler = nlp.add_pipe("entity_ruler", before="ner")

# 3. Definimos nuestros patrones personalizados
patterns = [
    {"label": "PLATO", "pattern": "pan con tomate"},
    {"label": "PLATO", "pattern": "escudella y carne de olla"},
    {"label": "PLATO", "pattern": [{"LOWER": "crema"}, {"LOWER": "catalana"}]},
    {"label": "ORG", "pattern": "Universitat Oberta de Catalunya"} # Añadimos a una categoría existente
]

ruler.add_patterns(patterns)

# 4. Probamos el sistema personalizado
text = "En la Universitat Oberta de Catalunya hemos comido escudella y carne de olla y de postre crema catalana."
doc = nlp(text)

print(f"Análisis personalizado:\n")
for ent in doc.ents:
    print(f"Entidad: {ent.text:<30} | Categoría: {ent.label_}")
    
# 5. Visualización gráfica (Genera un HTML con colores para cada entidad)
html = displacy.render(doc, style="ent", jupyter=False)
Path("ner_visualizacion2.html").write_text(html, encoding="utf-8")

print("\nSe ha generado 'ner_visualizacion2.html'. ¡Ábrelo para ver las entidades en colores!")
