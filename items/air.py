import items
from uti.textures import *


class Air(items.Item):
    def __init__(self, quantity) -> None:
        super().__init__(self.__class__.__name__, 3, NOTHING_TEXTURE, quantity, "Air")



items.registerItem(Air)