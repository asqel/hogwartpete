import pygame as py
from uti.vector import *
import os
import importlib as imp

py.font.init()

mc_font=py.font.Font(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/fonts/Monocraft.otf",20)

class Gui:
    def __init__(self, name, data, player) -> None:
        self.name = name
        self.data = data
        self.player = player
        
    def tick(self, events : list[py.event.Event]):
        ...
    def draw(self,screen):
        ...
        
        
guis :dict[str,Gui] = {}


def registerGui(gui : type):
    guis[gui.__name__] = gui
    
    
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
