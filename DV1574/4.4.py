import os

paths = os.listdir("C:/Games")
for item in paths:
    print(item)

directory = "C:/Games"
items = os.listdir(directory) 
for item in items:
    path = directory + "/" + item
    print(path, ", ", os.path.isdir(path))