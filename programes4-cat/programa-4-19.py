import nltk
from nltk.corpus import cess_cat
import pylab
paraules=cess_cat.words()
paraules1=paraules[:1000]
freqdist=nltk.FreqDist(paraules1)
freqdist.plot()
