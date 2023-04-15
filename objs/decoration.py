from uti import *
from objs import *

class Wood(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__("Pebble", x, y, False, Textures["Obj"]["wood.png"],None)

class Wall(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__("Pebble", x, y, False, Textures["Obj"]["wall.png"],None)

class Bed_head(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__("Pebble", x, y, False, Textures["Obj"]["bed_0.png"],Hitbox(HITBOX_RECT_t,Vec(0,0),0,50,50))
        
class Bed_feet(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__("Pebble", x, y, False, Textures["Obj"]["bed_1.png"],Hitbox(HITBOX_RECT_t,Vec(0,0),0,50,50))


registerObj(Wood,"Wood")
registerObj(Wall,"Wall")
registerObj(Bed_head,"Bed_head")
registerObj(Bed_feet,"Bed_feet")