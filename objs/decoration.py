from uti import *
from objs import *

class Wood(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__("Pebble", x, y, False, Textures["Obj"]["wood.png"],None)


registerObj(Wood,"Wood")