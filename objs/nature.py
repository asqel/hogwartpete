from objs import *
from uti import *

class Pebble(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__("Pebble", x, y, False, Textures["Obj"]["pebble.png"],Hitbox(HITBOX_RECT_t,Vec(0,0),0,50,50))


registerObj(Pebble,"Pebble")