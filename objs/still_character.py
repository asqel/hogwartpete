from objs import *
from uti import *
from interface import *
import pygame as py


class Madre_gui(Gui):
    def __init__(self, player) -> None:
        super().__init__("madre gui", {}, player)
    def draw(self, screen):
        x = (screen.get_width() - Textures["other"]["text_box"].get_width())/2
        y = screen.get_height() -Textures["other"]["text_box"].get_height() - 20 
        screen.blit(Textures["other"]["text_box"],(x,y))
        screen.blit(mc_font.render("tiens prends ta baguette,",0,(0,0,0)), (x+30,y+30-10-5))
        screen.blit(mc_font.render("fait attention dehors",0,(0,0,0)), (x+30,y+60-10-5))
        screen.blit(mc_font.render("il y a des mange-morts ",0,(0,0,0)), (x+30,y+90-10-5))
        screen.blit(mc_font.render("il y a des mange-morts ",0,(0,0,0)), (x+30,y+90-10+30-5))                    
        
    def tick(self, events:[py.event.Event]):
        for i in events:
            if i.type == py.KEYDOWN:
                if i.key == py.K_e:
                    self.player.gui = None

class Snape(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, False, Textures["player"]["rogue_down"],HITBOX_50X50)

class Madre(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["madre"],HITBOX_50X50)

    def on_interact(self, world, user):
        print(guis)
        user.gui = guis["Madre_gui"](user)


    
        
registerObj(Snape)
registerObj(Madre)
registerGui(Madre_gui)