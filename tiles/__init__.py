import pygame as py
from uti import *

class Tile:
    def __init__(self,texture:py.Surface,animation:Animation,walk_on:function) -> None:
        self.texture=texture
        self.animation=animation
        self.on_walk_on=walk_on