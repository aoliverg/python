import spacy

# 1. Cargamos el modelo en castellano
nlp = spacy.load('es_core_news_md')

# 2. Texto con pronombres enclíticos, contracciones y puntuación
text = "¿El estudiante decidió apuntarse al curso de la RAE, verdad?"

# 3. Procesamos el texto
doc = nlp(text)

# 4. Imprimimos una cabecera para verlo claro
print(f"{'Índice':<6} | {'Token':<12} | {'¿Es letra?':<12} | {'¿Es puntuación?'}")
print("-" * 55)

# 5. Iteramos sobre cada token del objeto 'doc'
for token in doc:
    # token.i : el índice (posición) del token dentro de la frase
    # token.text : el texto original del token
    # token.is_alpha : devuelve True si solo contiene letras
    # token.is_punct : devuelve True si es un signo de puntuación
    
    print(f"{token.i:<6} | {token.text:<12} | {str(token.is_alpha):<12} | {str(token.is_punct)}")
