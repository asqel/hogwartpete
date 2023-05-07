from uti import *
from objs import *
import world as w
import jsonizer as js

class Wood(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["wood"],None)

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

class Grogu(Obj):
    def __init__(self, x: float, y: float):
        super().__init__(self.__class__.__name__,x,y,False,Textures["Obj"]["grogu"],Hitbox(HITBOX_RECT_t,Vec(0,0),0,25,25))

class Stairs(Obj):
    def __init__(self, x:float, y:float):
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["stairs"],HITBOX_50X50)

    def on_interact(self, world, user):
        user.world=js.load_world("bed room")
        user.pos=Vec(100,100)

import random

class Tv(Obj):
    def __init__(self, x:float, y:float):
        self.max_count = 0
        self.count = 20
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