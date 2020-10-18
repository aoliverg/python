freglas=open("reglas.txt","r")

reglas=[]

while True:
	linea=freglas.readline().rstrip()
	if not linea:break
	reglas.append(linea)
freglas.close()

fdiccionario=open("diccionario.txt","r")

while True:
	linea=fdiccionario.readline().rstrip()
	if not linea:break
	(lema,tipo)=linea.split(":")
	for regla in reglas:
		(tf,tl,etiqueta,tipo2)=regla.split(":")
		if ((tipo2 == tipo)&(lema.endswith(tl))):
			print(lema[0:(len(lema)-len(tl))]+tf,lema,etiqueta)

fdiccionario.close()
