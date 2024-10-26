import pygame as py
from uti.textures import *
import items

class Wand(items.Item):
    def __init__(self, quantity) -> None:
        super().__init__(self.__class__.__name__, 1, Textures["item"]["wand"], quantity, "wand")


items.registerItem(Wand)