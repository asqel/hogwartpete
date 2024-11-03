import objs
from uti.textures import *
from uti.vector import *
from uti.hitbox import *
import interface
import entities
import world

class Farine_camping_car(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["farine:camping_car"],Hitbox(HITBOX_RECT_t, NULL_VEC, 0, 300, 100))

    def on_interact(self, world, user):
        if -550 - 25 <= user.pos.x <= -550 + 25:
            w_ = user.world
            user.world = world.World("farine_camping_car",(0,0,0))
            user.world.old_world = w_

class Farine(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, Textures["player"]["farine:farine_right"],Hitbox(HITBOX_RECT_t, NULL_VEC, 0, 50, 75))

    def on_interact(self, world, user):
        if user.pos.x >= self.pos.x + 50:
            user.close_gui()
            user.open_gui("Farine_shop")

objs.registerObj(Farine)
objs.registerObj(Farine_camping_car)



class Farine_wall_left_up(objs.Obj):
    def __init__(self, x:float, y:float):
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["farine:wall_left_up"], Hitbox(HITBOX_RECT_t, Vec(0, 0), 0, 3, 16))
class Farine_wall_left(objs.Obj):
    def __init__(self, x:float, y:float):
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["farine:wall_left"], Hitbox(HITBOX_RECT_t, Vec(0, 0), 0, 3, 16))
class Farine_wall_right_up(objs.Obj):
    def __init__(self, x:float, y:float):
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["farine:wall_right_up"], Hitbox(HITBOX_RECT_t, Vec(13, 0), 0, 3, 16))
class Farine_wall_right(objs.Obj):
    def __init__(self, x:float, y:float):
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["farine:wall_right"], Hitbox(HITBOX_RECT_t, Vec(13, 0), 0, 3, 16))
class Farine_wall_left_down(objs.Obj):
    def __init__(self, x:float, y:float):
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["farine:wall_left_down"], Hitbox(HITBOX_RECT_t, Vec(0, 0), 0, 3, 16))
class Farine_wall_right_down(objs.Obj):
    def __init__(self, x:float, y:float):
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["farine:wall_right_down"], Hitbox(HITBOX_RECT_t, Vec(13, 0), 0, 3, 16))

class Farine_wall(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["farine:wall"],HITBOX_50X50)

class Farine_floor(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["farine:floor"],HITBOX_50X50)


objs.registerObj(Farine_wall_left)
objs.registerObj(Farine_wall_left_down)
objs.registerObj(Farine_wall_left_up)
objs.registerObj(Farine_wall_right)
objs.registerObj(Farine_wall_right_down)
objs.registerObj(Farine_wall_right_up)
objs.registerObj(Farine_floor)
objs.registerObj(Farine_wall)