import csv
import codecs
entrada=codecs.open("cdlconsulteca.csv","r",encoding="utf-8")
lector=csv.reader(entrada, delimiter=',', quotechar='"')
salida=codecs.open("cdlconsulteca2.csv","w",encoding="utf-8")
escriptor = csv.writer(salida, delimiter=';',quotechar='"', quoting=csv.QUOTE_ALL)
for linea in lector:
    escriptor.writerow(linea)
