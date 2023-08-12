import pygame as py
import os
path=os.path.abspath(".")

folders = list(os.listdir(f"{path}/assests"))
py.mixer.init()

def play_sound(name:str):
    while 1:
        py.mixer.music.load(f"{path}/assests/sound/{name}")
        py.mixer.music.set_volume(0.05) # between 0 and 1
        py.mixer.music.play()
        while py.mixer.music.get_busy():
            py.time.Clock().tick(10)
