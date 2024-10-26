from uti.textures import *
import items 

class Resurrection_stone(items.Item):
    def __init__(self, quantity) -> None:
        super().__init__(self.__class__.__name__, 1, Textures["item"]["resurrection_stone"], quantity, "Resurrection stone")

class Elder_wand(items.Item):
    def __init__(self, quantity) -> None:
        super().__init__(self.__class__.__name__, 1, Textures["item"]["elder_wand"], quantity, "Elder wand")

class Cloak_of_invisibility(items.Item):
    def __init__(self, quantity) -> None:
        super().__init__(self.__class__.__name__, 1, Textures["item"]["cloak_of_invisibility"], quantity, "Cloak of invisibility")

class goggles_of_truth(items.Item):
    def __init__(self, quantity) -> None:
        super().__init__(self.__class__.__name__, 1, Textures["item"]["goggles_of_truth"], quantity, "goggles of truth")


items.registerItem(Resurrection_stone)
items.registerItem(Elder_wand)
items.registerItem(Cloak_of_invisibility)
items.registerItem(goggles_of_truth)