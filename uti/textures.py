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


"""
animation for animated tiles are store in directories that are in tiles_animation
they are stored in differents png called frame_0 to frame_n where n is ther number of frame +1
and there must be a file called delay containing delay between a frame 

ex :
    tiles_animation/grass_tile/-- frame_0
                               |- frame_1
                               |- frame_2
                               |- delay (contains : 0)
"""
for i in folders:
    if os.path.isdir(f"{path}/src/{i}"):
        if i!="tiles_animation":
            for k in os.listdir(f"{path}/src/{i}"):
                if k.endswith(".png"):
                    Textures[i][k] = py.transform.scale(
                        py.image.load(f"{path}/src/{i}/{k}"), ( (50, 50) if i!="tiles" else (100,100) )
                    ).convert_alpha()
        else:...
            #TODO : implement support for animations
    elif i.endswith(".png"):
        Textures[i] = py.image.load(f"{path}/src/{i}")
