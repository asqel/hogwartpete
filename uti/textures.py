import pygame as py
import os
path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
folders=[i for i in os.listdir(path+"/src")]

Textures:dict[str,dict[str,py.Surface]]={i:{} for i in folders}
"""
{
    folder_name:{
        file_name,
        file2
    },
    folder2:{
        file3
    }
}
"""
py.display.init()
screen=py.display.set_mode((1080,720),py.RESIZABLE)

for i in folders:
    if os.path.isdir(path+"/src/"+i):
        for k in os.listdir(path+"/src/"+i):
            Textures[i][k]=py.transform.scale(py.image.load(path+"/src/"+i+"/"+k),(50,50)).convert_alpha()
    else:
        Textures[i]=py.image.load(path+"/src/"+i)
    

    