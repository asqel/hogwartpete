import pygame as py
import os
path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
folders=[i for i in os.listdir(path+"/src")]

Textures={i:{} for i in folders}
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

for i in folders:
    if os.path.isdir(path+"/src/"+i):
        for k in os.listdir(path+"/src/"+i):
            Textures[i][k]=py.image.load(path+"/src/"+i+"/"+k)
    else:
        Textures[i]=py.image.load(path+"/src/"+i)
    

    