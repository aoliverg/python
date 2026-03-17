import spacy
from transformers import pipeline

# 1. Carreguem el model de spaCy (per a la part lingüística)
nlp = spacy.load('ca_core_news_md')

# 2. Creem un "pipeline" d'anàlisi de sentiment (model multilingüe de Hugging Face)
# Aquest model ha estat entrenat amb milions de ressenyes en diversos idiomes
sentiment_analysis = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

# 3. Analitzem algunes frases
frases = [
    "Aquest restaurant és fantàstic, el menjar és boníssim!",
    "No m'ha agradat gens el servei, ha estat molt lent.",
    "El llibre està bé, però el final és una mica avorrit.",
    "La pel·lícula és realment avorrida, hagués sortit del cinema als 10 minuts.",
    "He anat a l'escola a les vuit."
]

print(f"{'Frase':<55} | {'Estrelles':<10}")
print("-" * 70)

for text in frases:
    # Passem el text pel model de sentiment
    resultat = sentiment_analysis(text)[0]
    
    # El model 'nlptown' ens torna puntuacions d'1 a 5 estrelles
    label = resultat['label']
    score = resultat['score']
    
    print(f"{text[:53]:<55} | {label:<10} (confiança: {score:.2f})")
