from uti.vector import *
import pygame as py

class Obj:
    def __init__(self,id:str,x:float,y:float,istop:bool,texture:py.Surface) -> None:
        self.id=id
        self.texture=texture
        self.toplayer=istop# object is under or above player and entities
        self.pos=Vec(x,y)
        
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

