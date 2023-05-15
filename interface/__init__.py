import pygame as py
from uti.vector import *
import os
py.font.init()

mc_font=py.font.Font(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/fonts/Minecraft.otf",10)

class Gui:
    def __init__(self, name, tick_func, on_interact_func, draw_func, data) -> None:
        self.name = name
        self.tick = tick_func
        self.on_interact = on_interact_func
        self.draw = draw_func
        self.data = data