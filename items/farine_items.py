import pygame as py
from items import *
from uti import *

class Couscous(Item):
    def __init__(self, quantity) -> None:
        super().__init__(self.__class__.__name__, 2, Textures["item"]["couscous"], quantity)


class Sausage(Item):
    def __init__(self, quantity) -> None:
        super().__init__(self.__class__.__name__, 5, Textures["item"]["saucisses"], quantity)

class Taboule(Item):
    def __init__(self, quantity) -> None:
        super().__init__(self.__class__.__name__, 3, Textures["item"]["taboule"], quantity)

registerItem(Couscous)
registerItem(Taboule)
registerItem(Sausage)