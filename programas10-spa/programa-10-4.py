import xml.etree.ElementTree as etree

for event, elem in etree.iterparse("catalog.xml",events=("start", "end")):
    print(event,elem,elem.tag,elem.attrib)
