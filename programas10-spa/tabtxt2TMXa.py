import sys
import codecs
from xml.sax.saxutils import escape

fentrada=sys.argv[1]
fsalida=sys.argv[2]
l1=sys.argv[3]
l2=sys.argv[4]

entrada=codecs.open(fentrada,"r",encoding="utf-8")
salida=codecs.open(fsalida,"w",encoding="utf-8")

cadena='<?xml version="1.0" encoding="UTF-8" ?>'
salida.write(cadena+"\n")
cadena='<tmx version="1.4">'
salida.write(cadena+"\n")
cadena='<header/>'
salida.write(cadena+"\n")
cadena='  <body>'
salida.write(cadena+"\n")

for linia in entrada:
    linia=linia.rstrip()
    camps=linia.split("\t")
    segment1=camps[0]
    segment2=camps[1]
    cadena='   <tu>'
    salida.write(cadena+"\n")
    cadena='      <tuv xml:lang="'+l1+'"><seg>'+escape(segment1)+'</seg></tuv>'
    salida.write(cadena+"\n")
    cadena='      <tuv xml:lang="'+l2+'"><seg>'+escape(segment2)+'</seg></tuv>'
    salida.write(cadena+"\n")
    cadena='    </tu>'
    salida.write(cadena+"\n")
    
cadena='  </body>'
salida.write(cadena+"\n")
cadena='</tmx>'
salida.write(cadena+"\n")
