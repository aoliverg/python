import nltk
from nltk.corpus import cess_esp
import pylab
palabras=cess_esp.words()
palabras1=palabras[:1000]
freqdist=nltk.FreqDist(palabras1)
freqdist.plot()
