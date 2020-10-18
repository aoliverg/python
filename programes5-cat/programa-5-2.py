fregles=open("regles.txt","r")

regles=[]

while True:
	linia=fregles.readline().rstrip()
	if not linia:break
	regles.append(linia)
fregles.close()

fdiccionari=open("diccionari.txt","r")

while True:
	linia=fdiccionari.readline().rstrip()
	if not linia:break
	(lema,tipus)=linia.split(":")
	for regla in regles:
		(tf,tl,etiqueta,tipus2)=regla.split(":")
		if ((tipus2 == tipus)&(lema.endswith(tl))):
			print(lema[0:(len(lema)-len(tl))]+tf,lema,etiqueta)

fdiccionari.close()
