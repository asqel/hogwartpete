from uti.textures import *
from uti.vector import *
from uti.hitbox import *
import objs
from random import randint , choice 



class Air(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, NOTHING_TEXTURE,Hitbox(HITBOX_RECT_t,Vec(0,0),0,50,50))

class Pebble(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["pebble"],HITBOX_50X50)


class Grass(objs.Obj):
    def __init__(self, x: float, y: float) -> None:
        textures = [Textures["Obj"]["grass_flowers"],
                   Textures["Obj"]["grass_roses"]
                   ]
        r = randint(0,100)
        if 0 <= r <= 10:
            texture = choice(textures)
        else:
            texture = Textures["Obj"]["grass_empty"]
        texture = py.transform.rotate(texture, [0, 90, 180, 270][randint(0,3)])
        super().__init__(self.__class__.__name__, x, y,texture,HITBOX_50X50)
        
        
class Tree(objs.Obj):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(self.__class__.__name__, x, y,Textures["Obj"]["tree"])
        self.hitbox = Hitbox(HITBOX_RECT_t, Vec(0,0), width = 100, height = 100)
        
class Pumpkin(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["pumpkin"],Hitbox(HITBOX_RECT_t, Vec(6, 6), 0, 41, 44))

objs.registerObj(Pebble)
objs.registerObj(Grass)
objs.registerObj(Tree)
objs.registerObj(Air)
objs.registerObj(Pumpkin)