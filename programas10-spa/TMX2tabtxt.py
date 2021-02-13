import xml.etree.ElementTree as ET
import sys
import codecs

fentrada=sys.argv[1]
fsalida=sys.argv[2]
l1=sys.argv[3]
l2=sys.argv[4]

minrel=3
nmax=5
salida=codecs.open(fsalida,"w",encoding="utf-8")

tree = ET.parse(fentrada)
root = tree.getroot()

for tu in root.iter('tu'):
    sl_text=""
    tl_text=""
    for tuv in tu.iter('tuv'):
        lang=tuv.attrib['{http://www.w3.org/XML/1998/namespace}lang']
        for seg in tuv.iter('seg'):
            text=seg.text
            if lang==l1: sl_text=text
            elif lang==l2: tl_text=text
    
        
    if not sl_text=="" and not tl_text=="":
        cadena=sl_text+"\t"+tl_text
        print(cadena)
        salida.write(cadena+"\n")
