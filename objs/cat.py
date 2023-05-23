from uti import *
from objs import *
import world as w
import jsonizer as js

class Cat(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["cat_1"],HITBOX_50X50)
        self.frame=0
        self.maxframe=3
        self.frames=[Textures["Obj"]["cat_1"],Textures["Obj"]["cat_2"],Textures["Obj"]["cat_3"],Textures["Obj"]["cat_4"]]
        self.count=0
        self.maxcount=75

    def on_draw(self, world, has_been_drawn):
        if self.count>self.maxcount:
            self.count=0
        if self.count==self.maxcount:
            if self.frame>self.maxframe:
                self.frame=0
            else:
                self.texture = self.frames[self.frame]
                self.frame+=1
        self.count+=1

registerObj(Cat)