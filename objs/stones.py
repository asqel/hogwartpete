from uti.textures import *
from objs import *

class Stone(Obj):
    def __init__(self, x: float, y: float) -> None:
        self.hitbox=None
        super().__init__("Stone", x, y,False,Textures["Obj"]["stone"])
        

class Diorite(Obj):
    def __init__(self, x: float, y: float) -> None:
        self.hitbox=None
        super().__init__("Diorite", x, y,False,Textures["Obj"]["stone"])
        
        
registerObj(Stone,"Stone")
registerObj(Diorite,"Diorite")