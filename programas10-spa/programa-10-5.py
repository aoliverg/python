import xml.etree.ElementTree as etree
import codecs
artist=""
title=""
year=""
salida=codecs.open("catalog.txt","w",encoding="utf-8")
for event, elem in etree.iterparse("catalog.xml",events=("start", "end")):
    if event=="end" and elem.tag=="cd":
        cadena=artist+"\t"+title+"\t"+year
        print(cadena)
        salida.write(cadena+"\n")
        artist=""
        title=""
        year=""
    if event=="end" and elem.tag=="title":
        title="".join(elem.itertext()).lstrip().rstrip()
    if event=="end" and elem.tag=="artist":
        artist="".join(elem.itertext()).lstrip().rstrip()
    if event=="end" and elem.tag=="year":
        year="".join(elem.itertext()).lstrip().rstrip()
