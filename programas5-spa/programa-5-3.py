import codecs
diccionario={}
archivo_diccipnario=codecs.open("diccionario-freeling-spa.txt","r",encoding="utf-8")

for entrada in archivo_diccipnario:
    entrada=entrada.rstrip()
    campos=entrada.split(":")
    forma=campos[0]
    lema=campos[1]
    etiqueta=campos[2]
    diccionario[forma]=diccionario.get(forma,"")+":"+lema+"\t"+etiqueta
print("DICCIONARIO CARGADO")
while 1:
    palabra=input("Introduce la palabra a analizar: ")
    if palabra==" ":
        break
    if palabra in diccionario:
        print("ANALISIS:",palabra,diccionario[palabra])
    else:
        print("PALABRA DESCONOCIDA")