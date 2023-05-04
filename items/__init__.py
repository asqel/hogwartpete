import pygame as py
from world import *
from entities import *

class Item:
    def __init__(self,max_stack:int,id:str,texture:py.Surface,quantity:int) -> None:
        self.max_stack=max_stack
        self.id=id
        self.texture=texture
        self.quantity=quantity
    
    def on_use(self,world:World,user:Npc|Character):
        ...
        
    def on_inventory_tick(self,world:World,user:Npc|Character|Obj):
        ...
        