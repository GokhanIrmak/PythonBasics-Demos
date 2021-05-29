import os

print(__file__)
path = os.path.dirname(__file__)

with open(path+"/file.txt","r")as file:
    for line in file:
        print(line)