from uti.vector import *
from uti.hitbox import *
import pygame as py
import os 
import importlib as imp
import world
import entities

class Obj:
    def __init__(self, id: str, x: float, y: float, texture: py.Surface, hitbox = HITBOX_50X50, data:dict = None, light = None, does_tick: bool = False) -> None:
        self.id = id
        self.texture = texture
        self.pos = Vec(x, y)
        self.hitbox = hitbox
        self.data = ({} if data is None or not isinstance(data, dict) else data)
        self.light = light
        self.does_tick = does_tick
    
    def on_interact(self, world: 'world.World', user: 'entities.Character'):
        ...
    def on_walk_in(self, world: 'world.World', user: 'entities.Character'):
        ...
    def on_draw(self, world: 'world.World', has_been_drawn: bool):
        ...
    def on_tick(self, world: 'world.World'):
        ...
    def obj_copy(self):
        return Obj(self.id,self.pos.x,self.pos.y,self.toplayer,self.texture,self.hitbox,self.data)

Objs={}


def registerObj(obj:type):
    Objs[obj.__name__]=obj


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
