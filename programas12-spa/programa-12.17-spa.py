import spacy
from transformers import pipeline

# 1. Cargamos el modelo de spaCy (para la parte lingüística)
nlp = spacy.load('es_core_news_md')

# 2. Creamos un "pipeline" de análisis de sentimiento (modelo multilingüe de Hugging Face)
# Este modelo ha sido entrenado con millones de reseñas en varios idiomas
sentiment_analysis = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

# 3. Analizamos algunas frases
frases = [
    "¡Este restaurante es fantástico, la comida está buenísima!",
    "No me ha gustado nada el servicio, ha sido muy lento.",
    "El libro está bien, pero el final es un poco aburrido.",
    "La película es realmente aburrida, hubiera salido del cine a los 10 minutos.",
    "He ido a la escuela a las ocho."
]

print(f"{'Frase':<55} | {'Estrellas':<10}")
print("-" * 75)

for text in frases:
    # Pasamos el texto por el modelo de sentimiento
    resultado = sentiment_analysis(text)[0]
    
    # El modelo 'nlptown' nos devuelve puntuaciones de 1 a 5 estrellas
    label = resultado['label']
    score = resultado['score']
    
    print(f"{text[:53]:<55} | {label:<10} (confianza: {score:.2f})")
