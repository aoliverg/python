import codecs
diccionari={}
arxiu_diccionari=codecs.open("diccionari-curt-cat.txt","r",encoding="utf-8")

for entrada in arxiu_diccionari:
    entrada=entrada.rstrip()
    camps=entrada.split(" ")
    forma=camps[0]
    lema=camps[1]
    etiqueta=camps[2]
    diccionari[forma]=diccionari.get(forma,"")+":"+lema+"\t"+etiqueta
    
while 1:
    paraula=input()
    if paraula==" ":
        break
    if paraula in diccionari:
        print("ANALISI:",paraula,diccionari[paraula])
    else:
        print("PARAULA DESCONEGUDA")
