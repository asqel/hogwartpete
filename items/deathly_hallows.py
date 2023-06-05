from uti import *
from items import *
 

class Resurrection_stone(Item):
    def __init__(self, quantity) -> None:
        super().__init__(self.__class__.__name__, 1, Textures["item"]["resurrection_stone"], quantity)

class Elder_wand(Item):
    def __init__(self, quantity) -> None:
        super().__init__(self.__class__.__name__, 1, Textures["item"]["elder_wand"], quantity)

class Cloak_of_invisibility(Item):
    def __init__(self, quantity) -> None:
        super().__init__(self.__class__.__name__, 1, Textures["item"]["cloak_of_invisibility"], quantity)


registerItem(Resurrection_stone)
registerItem(Elder_wand)
registerItem(Cloak_of_invisibility)