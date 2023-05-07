from objs import *
from uti import *

class Air(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, False, NOTHING_TEXTURE,Hitbox(HITBOX_RECT_t,Vec(0,0),0,50,50))

class Pebble(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["pebble"],Hitbox(HITBOX_RECT_t,Vec(0,0),0,50,50))

class Stone(Obj):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(self.__class__.__name__, x, y,False,Textures["Obj"]["stone"])
        self.hitbox=Hitbox(HITBOX_RECT_t,Vec(0,0),width=50,height=50)


registerObj(Stone)
registerObj(Pebble)
registerObj(Air)
registerDynamic_Obj(Air)