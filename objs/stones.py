from uti.textures import *
from objs import *

class Stone(Obj):
    def __init__(self, x: float, y: float) -> None:
        self.hitbox=None
        super().__init__("Stone", x, y,False,Textures["Obj"]["stone.png"])
        

class Diorite(Obj):
    def __init__(self, x: float, y: float) -> None:
        self.hitbox=None
        super().__init__("Diorite", x, y,False,Textures["Obj"]["stone.png"])
        
#TODO this is temporary , its just for testing
from random import randint
grass_rotate=[py.transform.rotate(Textures["Obj"]["grass.png"],[0,90,180,270][i])for i in range((4))]

class Grass(Obj):
    def __init__(self, x: float, y: float) -> None:
        self.hitbox=None
        super().__init__("Grass", x, y,False,grass_rotate[randint(0,3)])

registerObj(Stone,"Stone")
registerObj(Diorite,"Diorite")
registerObj(Grass,"Grass")