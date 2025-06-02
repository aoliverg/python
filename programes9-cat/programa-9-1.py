import sys
import chardet
fitxer_entrada=sys.argv[1]
raw_data=open(fitxer_entrada,"rb").read()
codificacio=chardet.detect(raw_data)
print("Fitxer:",fitxer_entrada,"Codificació:",codificacio)
print(codificacio["encoding"])
