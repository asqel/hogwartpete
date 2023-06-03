import pygame as py
from items import *
from uti import *

class Couscous(Item):
    def __init__(self, quantity) -> None:
        super().__init__(self.__class__.__name__, 2, Textures["item"]["couscous"], quantity)
    def on_use(self, world, user):
        self.quantity -= 1
        user.pv += 10


class Sausage(Item):
    def __init__(self, quantity) -> None:
        super().__init__(self.__class__.__name__, 5, Textures["item"]["saucisses"], quantity)

    def on_use(self, world, user):
        self.quantity -= 1
        user.pv += 10

class Taboule(Item):
    def __init__(self, quantity) -> None:
        super().__init__(self.__class__.__name__, 3, Textures["item"]["taboule"], quantity)
    def on_use(self, world, user):
        self.quantity -= 1
        user.pv += 10

registerItem(Couscous)
registerItem(Taboule)
registerItem(Sausage)