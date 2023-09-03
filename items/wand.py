import pygame as py
from items import *
from uti import *
import entities as en

class Wand(Item):
    def __init__(self, quantity) -> None:
        super().__init__(self.__class__.__name__, 1, Textures["item"]["wand"], quantity, "wand")


registerItem(Wand)