a=input("Introduce un número ")
b=input("Introduce otro número ")
try:
    c=float(a)/float(b)
    print("La división és ",c)
except:
    print("Las cifras que has introducido no son correctas")
