import pygame as py
import os
path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

folders = list(os.listdir(f"{path}/src"))
py.mixer.init()

def play_sound(name:str):
    while 1:
        py.mixer.music.load(f"{path}/src/sound/{name}")
        py.mixer.music.play()
        while py.mixer.music.get_busy():
            py.time.Clock().tick(10)
