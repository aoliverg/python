import sys
import codecs
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.etree import ElementTree
from xml.dom import minidom


def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")


fentrada=sys.argv[1]
fsalida=sys.argv[2]
l1=sys.argv[3]
l2=sys.argv[4]

entrada=codecs.open(fentrada,"r",encoding="utf-8")
salida=codecs.open(fsalida,"w",encoding="utf-8")


# Configure one attribute with set()
root = Element('tmx')
root.set('version', '1.4')

header = SubElement(root, 'header')

body = SubElement(root, 'body')


for linia in entrada:
    linia=linia.rstrip()
    camps=linia.split("\t")
    segment1=camps[0]
    segment2=camps[1]
    tu=SubElement(body, 'tu')
    
    tuv = SubElement(tu,'tuv')
    tuv.set('xml:lang',l1)
    seg= SubElement(tuv,'seg')
    seg.text=segment1
    
    tuv = SubElement(tu,'tuv')
    tuv.set('xml:lang',l2)
    seg= SubElement(tuv,'seg')
    seg.text=segment2
salida.write((prettify(root)))
