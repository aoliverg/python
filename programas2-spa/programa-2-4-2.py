a=input("Introduce un número ")
b=input("Introduce otro número ")
if a.isnumeric() and b.isnumeric() and not b=="0":
    c=float(a)/float(b)
    print("La división és ",c)
else:
    print("Las cifras que has introducido no son correctas")
