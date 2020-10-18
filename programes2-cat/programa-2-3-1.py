import codecs
entrada=codecs.open("arxiu.txt","r",encoding="utf-8")
while 1:
    linia=entrada.readline()
    linia=linia.rstrip()
    if not linia:
        break
    print(linia)
entrada.close()
