import pygame as py
import os
path=os.path.dirname(os.path.abspath(__file__))



#check if foldes exists from src
folder_to_check=["player"]
missing=[]
for i in folder_to_check:
    if not os.path.exists(path+"/src/"+i):
        missing.append(i)
        
#print errors
if missing:
    print(f"ERROR missing folder{'s' if len(missing)>1 else ''} :")
    for i in missing:
        print(f"  src/{i}")
    exit(1)


Textures={}
for i in folder_to_check:
    if os.path.isdir(path+"/src/"+i):
        for k in os.listdir(path+"/src/"+i):
            Textures["src/"+i+"/"+k]=py.image.load(path+"/src/"+i+"/"+k)
    else:
        print(f"ERROR src/{i} is not a folder")
        exit(1)
    
print(Textures)