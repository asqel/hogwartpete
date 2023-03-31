from textures import *

class Obj:
    def __init__(self,id:str,x:float,y:float) -> None:
        self.id=id
        self.x=x
        self.y=y
        

class Stone(Obj):
    def __init__(self, x: float, y: float) -> None:
        self.texture=Textures["Obj"]["stone"]
        self.hitbox=None
        super().__init__("Stone", x, y)