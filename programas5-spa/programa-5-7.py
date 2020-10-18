import nltk
from nltk.corpus import cess_esp
from nltk.tokenize import word_tokenize
tagged_sents=cess_esp.tagged_sents()
unigram_tagger=nltk.UnigramTagger(tagged_sents)
oracio="Mañana por la mañana lloverá."
tokens=word_tokenize(oracio)
analisis=unigram_tagger.tag(tokens)
print(analisis)
