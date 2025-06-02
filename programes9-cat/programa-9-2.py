import sys
import magic

fitxer_entrada=sys.argv[1]
m = magic.from_file(fitxer_entrada)
print(m)
