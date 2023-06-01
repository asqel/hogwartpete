from uti.vector import *
from uti.hitbox import *
import pygame as py
import os 
import importlib as imp

class Obj:
    def __init__(self, id: str, x: float, y: float, istop: bool, texture: py.Surface, hitbox = HITBOX_50X50, data:dict = None) -> None:
        self.id = id
        self.texture = texture
        self.toplayer = istop # object is under or above player and entities
        self.pos = Vec(x, y)
        self.hitbox = hitbox
        self.transparent=False #si on peut passer a travvers ou pas
        self.data = ({} if data is None or not isinstance(data, dict) else data)
    
    def on_interact(self,world,user):
        ...
    def on_walk_in(self,world,user):
        ...
    def on_draw(self,world,has_been_drawn):
        ...
    def obj_copy(self):
        return Obj(self.id,self.pos.x,self.pos.y,self.toplayer,self.texture,self.hitbox,self.data)

class Dynamic_Obj:  #Object that can be updated on each tick
    def __init__(self, id: str, x: float, y: float, istop: bool, texture: py.Surface, hitbox = HITBOX_50X50, data:dict = None) -> None:
        self.id = id
        self.texture = texture
        self.toplayer = istop # object is under or above player and entities
        self.pos = Vec(x, y)
        self.hitbox = hitbox
        self.transparent=False #si on peut passer a travvers ou pas
        self.data = ({} if data is None or not isinstance(data, dict) else data)
    
    def on_interact(self,world,user):
        ...
    def on_walk_in(self,world,user):
        ...
    def tick(self,world):
        ...
    def on_draw(self,world,has_been_drawn):
        ...
    def dyn_obj_copy(self):
        return Obj(self.id,self.pos.x,self.pos.y,self.toplayer,self.texture,self.hitbox,self.data)

Objs={}
Dynamic_Objs={}


def registerObj(obj:type):
    Objs[obj.__name__]=obj
    
def registerDynamic_Obj(obj:type):
    Dynamic_Objs[obj.__name__]=obj


#import every objs
module_names=os.listdir(os.path.dirname(os.path.abspath(__file__)))

for i in range(len(module_names)):
    if module_names[i]=="__init__.py":
        module_names.pop(i)
        break
for i in range(len(module_names)):
    if module_names[i].endswith(".py"):
        module_names[i]=module_names[i][:-3]

for i in module_names:
    imp.import_module(f".{i}", __package__)
