from transformers import pipeline

# Cargamos un modelo preparado para el análisis de sentimientos
# Este modelo en concreto es multilingüe (funciona en catalán, castellano, inglés...)
classifier = pipeline("sentiment-analysis", model="lxyuan/distilbert-base-multilingual-cased-sentiments-student")

# Textos de prueba
textos = [
    "¡Esta clase de Python es la mejor del mundo!",
    "No me ha gustado nada la comida de este restaurante.",
    "Hoy hace un día normal, ni frío ni calor."
]

print("--- Resultados del análisis ---")

for t in textos:
    resultado = classifier(t)[0]
    label = resultado['label']
    score = resultado['score']

    print(f"Texto: {t}")
    print(f"Sentimiento: {label} (Confianza: {score:.2f})")
    print("-" * 30)
