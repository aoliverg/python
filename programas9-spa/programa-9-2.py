import sys
import magic

archivo_entrada=sys.argv[1]
m = magic.from_file(archivo_entrada)
print(m)
