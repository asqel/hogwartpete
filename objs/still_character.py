from objs import *
from uti import *
from interface import *
import pygame as py

def close_gui(gui : Gui):
    gui.player.gui = None
    
def draw_gui(gui : Gui, screen : py.Surface):
    x = (screen.get_width() - Textures["other"]["text_box"].get_width())/2
    y = screen.get_height() -Textures["other"]["text_box"].get_height() - 20 
    screen.blit(Textures["other"]["text_box"],(x,y))
    screen.blit(mc_font.render("tiens prends ta baguette,",0,(0,0,0)), (x+30,y+30))
    screen.blit(mc_font.render("fait attention dehors",0,(0,0,0)), (x+30,y+60))
    screen.blit(mc_font.render("il y a des mange-morts ",0,(0,0,0)), (x+30,y+90))
    

class Snape(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, False, Textures["player"]["rogue_down"],HITBOX_50X50)

    def on_interact(self, world, user):
        user.gui = Gui("mother text",None, close_gui, draw_gui,dict(), user)

class Madre(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["madre"],HITBOX_50X50)

    def on_interact(self, world, user):
        user.gui = Gui("mother text",None, close_gui, draw_gui,dict(), user)

registerObj(Snape)
registerObj(Madre)