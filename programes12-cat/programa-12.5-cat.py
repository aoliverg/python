import spacy
from spacy.symbols import ORTH

nlp = spacy.load('ca_core_news_md')


text = "El Excm. Sr. Planell està de viatge. Tornarà aviat."
doc = nlp(text)

print("--- SEGMENTACIÓ PER DEFECTE ---")
for frase in doc.sents:
    print(frase.text)

excepcio = [{ORTH: "Excm."}]
nlp.tokenizer.add_special_case("Excm.", excepcio)

doc = nlp(text)

print("--- SEGMENTACIÓ AFEGINT ABREVIATURA ---")
for frase in doc.sents:
    print(frase.text)


