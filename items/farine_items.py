import pygame as py
from items import *
from uti import *

class Couscous(Item):
    def __init__(self, quantity) -> None:
        super().__init__(self.__class__.__name__, 2, Textures["item"]["couscous"], quantity, "Couscous")
    def on_use(self, world, user):
        if user.pv < 100:
            self.quantity -= 1
            user.pv = min(user.pv + 15, 100)


class Sausage(Item):
    def __init__(self, quantity) -> None:
        super().__init__(self.__class__.__name__, 5, Textures["item"]["saucisses"], quantity ,"Sausage")

    def on_use(self, world, user):
        if user.pv < 100:
            self.quantity -= 1
            user.pv = min(user.pv + 5, 100)

class Taboule(Item):
    def __init__(self, quantity) -> None:
        super().__init__(self.__class__.__name__, 3, Textures["item"]["taboule"], quantity, "taboule")
    def on_use(self, world, user):
        if user.pv < 100:
            self.quantity -= 1
            user.pv = min(user.pv + 10, 100)

class Spatula(Item):
    def __init__(self, quantity) -> None:
        super().__init__(self.__class__.__name__, 1, Textures["item"]["spatula"], quantity, "spatula")


registerItem(Couscous)
registerItem(Taboule)
registerItem(Sausage)
registerItem(Spatula)