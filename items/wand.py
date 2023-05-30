import pygame as py
from items import *
from uti import *

class Wand(Item):
    def __init__(self, quantity) -> None:
        super().__init__(self.__class__.__name__, 5, Textures["item"]["wand"], quantity)


registerItem(Wand)