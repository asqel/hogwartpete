from uti import *
from objs import *
import world as w
import jsonizer as js

class Wood(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["wood"],HITBOX_0x0)

class Wall(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, 1, Textures["Obj"]["wall"],HITBOX_50X50)

class Bed_head(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["bed_0"],HITBOX_50X50)
        
class Bed_feet(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["bed_1"],HITBOX_50X50)

class Mandalorian_poster(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["mandalorian_poster"],HITBOX_50X50)

class Commode(Obj):
    def __init__(self, x: float, y: float):
        super().__init__(self.__class__.__name__,x,y,False,Textures["Obj"]["commode"],Hitbox(HITBOX_RECT_t,Vec(0,0),0,100,50))

class Frigo(Obj):
    def __init__(self, x: float, y: float):
        super().__init__(self.__class__.__name__,x,y,False,Textures["Obj"]["frigo"],Hitbox(HITBOX_RECT_t,Vec(0,0),0,50,100))

class Grogu(Obj):
    def __init__(self, x: float, y: float):
        super().__init__(self.__class__.__name__,x,y,False,Textures["Obj"]["grogu"],Hitbox(HITBOX_RECT_t,Vec(0,0),0,25,25))

class Stairs(Obj):
    def __init__(self, x:float, y:float):
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["stairs"],HITBOX_50X50)

    def on_interact(self, world, user):
        if world.name=="bed room":
            user.world=js.load_world("rdc")
            user.pos=Vec(100,100)
        else:
            user.world=js.load_world("bed room")
            user.pos=Vec(100,100)

import random

class Tv(Obj):
    def __init__(self, x:float, y:float):
        self.max_count = 20
        self.count = 0
        self.frame_idx=0
        self.frames=[[Textures["Obj"]["tv"],Textures["Obj"]["tv_2"]][random.randint(0,1)] for i in range(random.randint(3,20))]
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["tv"],HITBOX_50X50)

    def on_draw(self, world,has_been_drawn):
        self.count += 1
        if self.count >= self.max_count:
            self.count=0
            self.frame_idx +=1
            if self.frame_idx >= len(self.frames):
                self.frame_idx=0
            self.texture = self.frames[self.frame_idx]






class Empty_commode(Obj):
    def __init__(self, x:float, y:float):
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["empty_commode"],HITBOX_50X50)


class Wall_left_up(Obj):
    def __init__(self, x:float, y:float):
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["wall_left_up"], Hitbox(HITBOX_RECT_t, Vec(0, 0), 0, 3, 16))
class Wall_left(Obj):
    def __init__(self, x:float, y:float):
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["wall_left"], Hitbox(HITBOX_RECT_t, Vec(0, 0), 0, 3, 16))
class Wall_right_up(Obj):
    def __init__(self, x:float, y:float):
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["wall_right_up"], Hitbox(HITBOX_RECT_t, Vec(13, 0), 0, 3, 16))
class Wall_right(Obj):
    def __init__(self, x:float, y:float):
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["wall_right"], Hitbox(HITBOX_RECT_t, Vec(13, 0), 0, 3, 16))
class Wall_left_down(Obj):
    def __init__(self, x:float, y:float):
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["wall_left_down"], Hitbox(HITBOX_RECT_t, Vec(0, 0), 0, 3, 16))
class Wall_right_down(Obj):
    def __init__(self, x:float, y:float):
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["wall_right_down"], Hitbox(HITBOX_RECT_t, Vec(13, 0), 0, 3, 16))



registerObj(Wood)
registerObj(Wall)
registerObj(Bed_head)
registerObj(Bed_feet)
registerObj(Mandalorian_poster)
registerObj(Grogu)
registerObj(Commode)
registerObj(Stairs)
registerObj(Tv)
registerObj(Empty_commode)
registerObj(Wall_left_up)
registerObj(Wall_left)
registerObj(Wall_right_up)
registerObj(Wall_right)
registerObj(Wall_left_down)
registerObj(Wall_right_down)
registerObj(Frigo)