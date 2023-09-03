import pygame as py
from uti import *
import os
import importlib as imp

py.font.init()

main_font=py.font.SysFont("Consolas, 'Courier New', monospace",23)

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
    
def getGui(name : str, user):
    return guis[name](user)


def draw_4_line(screen, text : tuple[str, str, str, str], colors : tuple[tuple[int, int, int], tuple[int, int, int] ,tuple[int, int, int]]):
    x = (screen.get_width() - Textures["other"]["text_box"].get_width())/2
    y = screen.get_height() -Textures["other"]["text_box"].get_height() - 20 
    screen.blit(Textures["other"]["text_box"],(x,y))
    screen.blit(main_font.render(text[0], 0, colors[0]), (x+20,y+30-15))
    screen.blit(main_font.render(text[1], 0, colors[1]), (x+20,y+60-15))
    screen.blit(main_font.render(text[2], 0, colors[2]), (x+20,y+90-15))      
    screen.blit(main_font.render(text[3], 0, colors[3]), (x+20,y+90-15+30))                               

    
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