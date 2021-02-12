import os

for root, dirs, files in os.walk("./directorio-recursivo"):
    for file in files:
        print(os.path.join(root, file))
