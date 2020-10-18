import codecs
entrada=codecs.open("archivo.txt","r",encoding="utf-8")
lineas=entrada.readlines()
print(lineas)
print(type(lineas))
