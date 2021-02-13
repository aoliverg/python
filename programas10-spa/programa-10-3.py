import xmltodict

xml=open('catalog.xml')
xmldict = xmltodict.parse(xml.read())


for cd in xmldict["catalog"]["cd"]:
    print(cd["artist"],cd["title"],cd["year"])
