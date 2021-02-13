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

for termEntry in root.iter('termEntry'):
    termL1=""
    termL2=""
    ident=termEntry.attrib['id']
    subjects=""
    reliability=0
    for group in termEntry.iter('descripGrp'):
        
        for descrip in group.iter('descrip'):
            if descrip.attrib['type']=='subjectField':
                subjects=descrip.text
    for langset in termEntry.iter('langSet'):
        lang=langset.attrib['{http://www.w3.org/XML/1998/namespace}lang']
        for tig in langset.iter('tig'):
            for term in tig.iter('term'):
                termino=term.text
                if lang==l1:
                    termL1=termino
                elif lang==l2:
                    termL2=termino
            for descrip in tig.iter('descrip'):
                if descrip.attrib['type']=='reliabilityCode':
                    reliability=int(descrip.text)

        
        
        if not termL1=="" and not termL2=="" and reliability>=3:
            cadena=ident+"\t"+subjects+"\t"+termL1+"\t"+termL2
            print(cadena)
            salida.write(cadena+"\n")
        
