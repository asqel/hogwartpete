import pygame as py
import importlib as imp
import os

class Item:
    def __init__(self, id : str, max_stack : int, texture : py.Surface, quantity : int) -> None:
        self.max_stack=max_stack
        self.id=id
        self.texture=texture
        self.quantity=quantity
    
    def on_use(self, world, user):
        ...
        
    def on_inventory_tick(self, world, user):
        ...
        

items :dict[str,Item] = {}


def registerItem(item : type):
    items[item.__name__] = item
    
    
#import every gui
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