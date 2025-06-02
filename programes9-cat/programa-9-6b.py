import os

for root, dirs, files in os.walk("./directori-recursiu"):
    for file in files:
        if file.endswith(".txt"):
            print(os.path.join(root, file))
