import pygame as py
import os
path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

folders = list(os.listdir(f"{path}/src"))

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
    if os.path.isdir(f"{path}/src/{i}"):
        for k in os.listdir(f"{path}/src/{i}"):
            if k.endswith(".png"):
                Textures[i][k] = py.transform.scale(
                    py.image.load(f"{path}/src/{i}/{k}"), (50, 50)
                ).convert_alpha()
    elif i.endswith(".png"):
        Textures[i] = py.image.load(f"{path}/src/{i}")
