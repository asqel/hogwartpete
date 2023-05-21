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
from random import randint  
class Grass(Obj):
    def __init__(self, x: float, y: float) -> None:
        texture = [Textures["Obj"]["grass_empty"],
                   Textures["Obj"]["grass_flowers"],
                   Textures["Obj"]["grass_roses"]
                   ]
        r = randint(0,100)
        if 10 <= r <= 100:
            texture = texture[0]
        elif 5 <= r < 10:
            texture = texture[1]
        else:
            texture = texture[2]
        texture = py.transform.rotate(texture, [0, 90, 180, 270][randint(0,3)])
        super().__init__(self.__class__.__name__, x, y,False,texture,HITBOX_50X50)
        
        
class Tree(Obj):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(self.__class__.__name__, x, y,False,Textures["Obj"]["tree"])
        self.hitbox=Hitbox(HITBOX_RECT_t,Vec(0,0),width=100,height=100)

registerObj(Stone)
registerObj(Pebble)
registerObj(Grass)
registerObj(Tree)
registerObj(Air)
registerDynamic_Obj(Air)