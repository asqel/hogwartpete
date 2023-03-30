import pygame as py
import os
path=os.path.dirname(os.path.abspath(__file__))



#check if foldes exists from src
folder_to_check=["player"]
missing=[]
for i in folder_to_check:
    if not os.path.exists(path+"/src/"+i):
        missing.append(i)
        
folder_to_check_1=["Spells"]
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


Texturesplayer={}
Texturesspells={}
for i in folder_to_check:
    if os.path.isdir(path+"/src/"+i):
        for k in os.listdir(path+"/src/"+i):
            Texturesplayer["src/"+i+"/"+k]=py.transform.scale(py.image.load(path+"/src/"+i+"/"+k),(64,64))
    else:
        print(f"ERROR src/{i} is not a folder")
        exit(1)
for i in folder_to_check_1:
    if os.path.isdir(path+"/src/"+i):
        for k in os.listdir(path+"/src/"+i):
            Texturesspells["src/"+i+"/"+k]=py.transform.scale(py.image.load(path+"/src/"+i+"/"+k),(64,64))
    else:
        print(f"ERROR src/{i} is not a folder")
        exit(1)
    
print(Texturesplayer)
print(Texturesspells)