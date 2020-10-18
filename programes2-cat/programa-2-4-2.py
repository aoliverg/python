a=input("Entra un número ")
b=input("Entra un altre numero ")
if a.isnumeric() and b.isnumeric() and not b=="0":
    c=float(a)/float(b)
    print("La divisió és ",c)
else:
    print("Les xifres que has entrat no són correctes")
