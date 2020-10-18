import nltk
from nltk.corpus import cess_cat
from nltk.tokenize import word_tokenize
tagged_sents=cess_cat.tagged_sents()
unigram_tagger=nltk.UnigramTagger(tagged_sents)
oracio="avui fa sol però demà plourà"
tokens=word_tokenize(oracio)
analisi=unigram_tagger.tag(tokens)
print(analisi)
