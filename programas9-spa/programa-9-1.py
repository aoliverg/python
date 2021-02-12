import sys
import chardet
archivo_entrada=sys.argv[1]
raw_data=open(archivo_entrada,"rb").read()
codificacion=chardet.detect(raw_data)
print("Archivo:",archivo_entrada,"Codificación:",codificacion)
print(codificacion["encoding"])
