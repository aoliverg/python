import spacy
from spacy import displacy
from pathlib import Path

nlp = spacy.load('ca_core_news_md')
doc = nlp("El estudiante de la universidad lee un libro muy antiguo.")

# Generamos el código SVG del árbol
svg = displacy.render(doc, style="dep", jupyter=False)

# Lo guardamos en un archivo HTML para abrirlo con el navegador
Path("arbol_sintactico.html").write_text(svg, encoding="utf-8")
print("\nAbre el archivo 'arbol_sintactico.html' para ver el análisis gráfico.")
