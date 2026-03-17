import spacy

# 1. Carreguem el model en català
nlp = spacy.load('ca_core_news_md')

# 2. Text amb apòstrofs, pronoms febles i puntuació
text = "L'estudiant va decidir apuntar-se al curs de l'IEC, oi?"

# 3. Processem el text
doc = nlp(text)

# 4. Imprimim una capçalera per veure-ho clar
print(f"{'Índex':<6} | {'Token':<12} | {'És lletra?':<12} | {'És puntuació?'}")
print("-" * 50)

# 5. Iterem sobre cada token de l'objecte 'doc'
for token in doc:
    # token.i : l'índex (posició) del token dins la frase
    # token.text : el text original del token
    # token.is_alpha : retorna True si només conté lletres
    # token.is_punct : retorna True si és un signe de puntuació
    
    print(f"{token.i:<6} | {token.text:<12} | {str(token.is_alpha):<12} | {str(token.is_punct)}")
