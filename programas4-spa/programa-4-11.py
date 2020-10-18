from nltk.tokenize import PunktSentenceTokenizer

parrafo1="Hoy hace un día muy bonito. Mañana Albert irá a comer en casa."

parrafo2="El Sr. Martínez llegará mañana de Alicante con la R.E.N.F.E. a las 22.30 h. y se alojará en el hotel de la estación. El día siguiente visitará al Dr. Rovira en la Avda. Tibidabo. La vuelta la hará en avión en el vuelo AF.352."

segmentador=PunktSentenceTokenizer()
segmentos1=segmentador.tokenize(parrafo1)
print(segmentos1)
segmentos2=segmentador.tokenize(parrafo2)
print(segmentos2)
