import csv
import codecs
entrada=codecs.open("cdlconsulteca.csv","r",encoding="utf-8")
lector=csv.reader(entrada, delimiter=',', quotechar='"')
for campos in lector:
    print(campos)
