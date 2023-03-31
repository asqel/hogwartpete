from textures import *

class Stone(Obj):
    def __init__(self, x: float, y: float) -> None:
        self.texture=Textures["Obj"]["stone"]
        self.hitbox=None
        super().__init__("Stone", x, y)
        

class Diorite(Obj):
    def __init__(self, x: float, y: float) -> None:
        self.texture=Textures["Obj"]["stone"]
        self.hitbox=None
        super().__init__("Diorite", x, y)