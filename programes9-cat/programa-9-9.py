import csv
import codecs
entrada=codecs.open("cdlconsulteca.csv","r",encoding="utf-8")
lector=csv.reader(entrada, delimiter=',', quotechar='"')
sortida=codecs.open("cdlconsulteca2.csv","w",encoding="utf-8")
escriptor = csv.writer(sortida, delimiter=';',quotechar='"', quoting=csv.QUOTE_ALL)
for linia in lector:
    escriptor.writerow(linia)
