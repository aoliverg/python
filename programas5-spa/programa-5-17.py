import nltk
from nltk.corpus import brown
brown_tagged_sents=brown.tagged_sents()
print("TOTAL ORACIONES:", len(brown_tagged_sents))
train_sents=brown_tagged_sents[:10000]
test_sents=brown_tagged_sents[56001:]
default_tagger=nltk.DefaultTagger("NN")
affix_tagger=nltk.AffixTagger(train_sents, affix_length=-3, min_stem_length=2)
unigram_tagger=nltk.UnigramTagger(train_sents, backoff=affix_tagger)
bigram_tagger=nltk.BigramTagger(train_sents, backoff=unigram_tagger)
trigram_tagger=nltk.TrigramTagger(train_sents, backoff=bigram_tagger)
precisio=trigram_tagger.evaluate(test_sents)
print("PRECISION: ",precisio)
