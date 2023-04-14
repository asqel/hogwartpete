from uti.vector import *
from uti.hitbox import *
import pygame as py
import os 
import importlib as imp

class Obj:
    def __init__(self,id:str,x:float,y:float,istop:bool,texture:py.Surface,hitbox:Hitbox=None,data:dict=None) -> None:
        self.id=id
        self.texture=texture
        self.toplayer=istop# object is under or above player and entities
        self.pos=Vec(x,y)
        self.hitbox=hitbox
        self.data=( {} if data is None or not isinstance(data,dict) else data )
    
    def on_rClick(self):
        ...
    def on_lClick(self):
        ...    
        
class Dynamic_Obj:#Object that can be updated on each tick
    def __init__(self,id:str,x:float,y:float,istop:bool,texture:py.Surface)->None:
        self.id=id
        self.texture=texture
        self.toplayer=istop# object is under or above player and entities
        self.pos=Vec(x,y)
        
    def on_tick(self):
        ...
    def on_rClick(self):
        ...
    def on_lClick(self):
        ...   

Objs={}
Dynamic_Objs={}


def registerObj(obj:type,name:str):
    Objs[name]=obj
    
def registerDynamic_Obj(dyn_obj:type,name:str):
    Dynamic_Objs[name]=dyn_obj


#import every spells
module_names=os.listdir(os.path.dirname(os.path.abspath(__file__)))

for i in range(len(module_names)):
    if module_names[i]=="__init__.py":
        module_names.pop(i)
        break
for i in range(len(module_names)):
    if module_names[i].endswith(".py"):
        module_names[i]=module_names[i][:-3]
        
for i in module_names:
    imp.import_module("."+i,__package__)
