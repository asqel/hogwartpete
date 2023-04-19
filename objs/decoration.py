from uti import *
from objs import *

class Wood(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__("Pebble", x, y, False, Textures["Obj"]["wood"],None)

class Wall(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__("Pebble", x, y, False, Textures["Obj"]["wall"],HITBOX_50X50)

class Bed_head(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__("Bed_head", x, y, False, Textures["Obj"]["bed_0"],HITBOX_50X50)
        
class Bed_feet(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__("Bed_feet", x, y, False, Textures["Obj"]["bed_1"],HITBOX_50X50)

class Mandalorian_poster(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__("Mandalorian_poster", x, y, False, Textures["Obj"]["mandalorian_poster"],HITBOX_50X50)

class Commode(Obj):
    def __init__(self, x: float, y: float):
        super().__init__("Commode",x,y,False,Textures["Obj"]["commode"],Hitbox(HITBOX_RECT_t,Vec(0,0),0,100,50))

class Grogu(Obj):
    def __init__(self, x: float, y: float):
        super().__init__("Grogu",x,y,False,Textures["Obj"]["grogu"],Hitbox(HITBOX_RECT_t,Vec(0,0),0,25,25))

class Stairs(Obj):
    def __init__(self, x:float, y:float):
        super().__init__("Stairs", x, y, False, Textures["Obj"]["stairs"],None)

registerObj(Wood,"Wood")
registerObj(Wall,"Wall")
registerObj(Bed_head,"Bed_head")
registerObj(Bed_feet,"Bed_feet")
registerObj(Mandalorian_poster,"Mandalorian_poster")
registerObj(Grogu,"Grogu")
registerObj(Commode,"Commode")
registerObj(Stairs,"Stairs")