from objs import *
from uti import *
from interface import *
import pygame as py
from items import *


class Madre_gui(Gui):
    def __init__(self, player) -> None:
        super().__init__("madre gui", {}, player)
    def draw(self, screen):
        x = (screen.get_width() - Textures["other"]["text_box"].get_width())/2
        y = screen.get_height() -Textures["other"]["text_box"].get_height() - 20 
        screen.blit(Textures["other"]["text_box"],(x,y))
        screen.blit(mc_font.render("Madre", 0, (0,0,0)), (x,y+30-15-30-5))
        screen.blit(mc_font.render("tiens prends ta baguette,",0,(0,0,0)), (x+30,y+30-10-5))
        screen.blit(mc_font.render("fait attention dehors",0,(0,0,0)), (x+30,y+60-10-5))
        screen.blit(mc_font.render("il y a des mange-morts ",0,(0,0,0)), (x+30,y+90-10-5))
        
    def tick(self, events:list[py.event.Event]):
        for i in events:
            if i.type == py.KEYDOWN:
                if i.key == py.K_e:
                    self.player.gui = None
                    if not self.player.has_item("Wand"):
                        self.player.add_item(items["Wand"](1))
                        self.player.money += 25

class Snape(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, False, Textures["player"]["rogue_down"],HITBOX_50X50)

class Madre(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["madre"],HITBOX_50X50)

    def on_interact(self, world, user):
        user.gui = guis["Madre_gui"](user)

class Paolo(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["paolo"],HITBOX_50X50)

    def on_interact(self, world, user):
        print(guis)
        user.gui = guis["Paolo_gui"](user)

class Paolo_gui(Gui):
    def __init__(self, player) -> None:
        super().__init__("paolo", {}, player)
    def draw(self, screen):
        x = (screen.get_width() - Textures["other"]["text_box"].get_width())/2
        y = screen.get_height() -Textures["other"]["text_box"].get_height() - 20 
        screen.blit(Textures["other"]["text_box"],(x,y))
        screen.blit(mc_font.render("Connais-tu ProfanOS?",0,(0,0,0)), (x+30,y+30-10-5))
        screen.blit(mc_font.render("Reste pas sur Windaube",0,(0,0,0)), (x+30,y+60-10-5))
        screen.blit(mc_font.render("Switch to Linux, ou ProfanOS",0,(0,0,0)), (x+30,y+90-10-5))
        screen.blit(mc_font.render("https://github.com/elydre/profanOS",0,(0,0,0)), (x+30,y+90-10+30-5))                    
        
    def tick(self, events:list[py.event.Event]):
        for i in events:
            if i.type == py.KEYDOWN:
                if i.key == py.K_e:
                    self.player.gui = None
class Farine(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, False, Textures["player"]["farine_right"],Hitbox(HITBOX_RECT_t, NULL_VEC, 0, 50, 75))

    def on_interact(self, world, user):
        if user.pos.x >= self.pos.x + 50:
            user.gui = guis["Farine_shop"](user)

registerObj(Snape)
registerObj(Madre)
registerObj(Farine)
registerGui(Madre_gui)
registerObj(Paolo)
registerGui(Paolo_gui)
