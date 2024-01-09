from objs import *
from uti import *
from interface import *
from entities import *
import world as w

class Farine_camping_car(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["farine:camping_car"],Hitbox(HITBOX_RECT_t, NULL_VEC, 0, 300, 100))

    def on_interact(self, world, user):
        if -550 - 25 <= user.pos.x <= -550 + 25:
            w_ = user.world
            user.world = w.World("farine_camping_car",(0,0,0))
            user.world.old_world = w_

class Farine(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, False, Textures["player"]["farine:farine_right"],Hitbox(HITBOX_RECT_t, NULL_VEC, 0, 50, 75))

    def on_interact(self, world, user):
        if user.pos.x >= self.pos.x + 50:
            user.gui = guis["Farine_shop"](user)

registerObj(Farine)
registerObj(Farine_camping_car)



class Farine_wall_left_up(Obj):
    def __init__(self, x:float, y:float):
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["farine:wall_left_up"], Hitbox(HITBOX_RECT_t, Vec(0, 0), 0, 3, 16))
class Farine_wall_left(Obj):
    def __init__(self, x:float, y:float):
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["farine:wall_left"], Hitbox(HITBOX_RECT_t, Vec(0, 0), 0, 3, 16))
class Farine_wall_right_up(Obj):
    def __init__(self, x:float, y:float):
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["farine:wall_right_up"], Hitbox(HITBOX_RECT_t, Vec(13, 0), 0, 3, 16))
class Farine_wall_right(Obj):
    def __init__(self, x:float, y:float):
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["farine:wall_right"], Hitbox(HITBOX_RECT_t, Vec(13, 0), 0, 3, 16))
class Farine_wall_left_down(Obj):
    def __init__(self, x:float, y:float):
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["farine:wall_left_down"], Hitbox(HITBOX_RECT_t, Vec(0, 0), 0, 3, 16))
class Farine_wall_right_down(Obj):
    def __init__(self, x:float, y:float):
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["farine:wall_right_down"], Hitbox(HITBOX_RECT_t, Vec(13, 0), 0, 3, 16))

class Farine_wall(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, 1, Textures["Obj"]["farine:wall"],HITBOX_50X50)

class Farine_floor(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, 1, Textures["Obj"]["farine:floor"],HITBOX_50X50)


registerObj(Farine_wall_left)
registerObj(Farine_wall_left_down)
registerObj(Farine_wall_left_up)
registerObj(Farine_wall_right)
registerObj(Farine_wall_right_down)
registerObj(Farine_wall_right_up)
registerObj(Farine_floor)
registerObj(Farine_wall)