import sys
a=input("Entra un número ")
b=input("Entra un altre numero ")
try:
    c=float(a)/float(b)
    print("La divisió és ",c)
except:
    print("Les xifres que has entrat no són correctes",sys.exc_info()[0])
