from objs import *
from uti import *
from interface import *

class Farine_camping_car(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["farine:camping_car"],Hitbox(HITBOX_RECT_t, NULL_VEC, 0, 300, 100))


class Farine(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, False, Textures["player"]["farine:farine_right"],Hitbox(HITBOX_RECT_t, NULL_VEC, 0, 50, 75))

    def on_interact(self, world, user):
        if user.pos.x >= self.pos.x + 50:
            user.gui = guis["Farine_shop"](user)

registerObj(Farine)
registerObj(Farine_camping_car)