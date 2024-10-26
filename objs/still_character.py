
from uti.vector import *
from uti.hitbox import *
from uti.textures import *
import pygame as py
import objs
import interface
import items


class Madre_gui(interface.Gui):
    def __init__(self, player) -> None:
        super().__init__("madre gui", {}, player)
    def draw(self, screen):
        x = (screen.get_width() - Textures["other"]["text_box"].get_width())/2
        y = screen.get_height() -Textures["other"]["text_box"].get_height() - 20 
        screen.blit(Textures["other"]["text_box"],(x,y))
        screen.blit(interface.main_font.render("Madre", 0, (0,0,0)), (x,y+30-15-30-5))
        screen.blit(interface.main_font.render("tiens prends ta baguette,",0,(0,0,0)), (x+30,y+30-10-5))
        screen.blit(interface.main_font.render("fait attention dehors",0,(0,0,0)), (x+30,y+60-10-5))
        screen.blit(interface.main_font.render("il y a des mange-morts ",0,(0,0,0)), (x+30,y+90-10-5))
        
    def tick(self, events:list[py.event.Event]):
        for i in events:
            if i.type == py.KEYDOWN:
                if i.key == py.K_e:
                    self.player.close_gui()

class Snape(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, False, Textures["player"]["rogue_down"],HITBOX_50X50)

class Madre(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["madre"],HITBOX_50X50)

    def on_interact(self, world, user):
        user.open_gui("Madre_gui")

class Paolo(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["paolo"],HITBOX_50X50)

    def on_interact(self, world, user):
        user.open_gui("Paolo_gui")

class Paolo_gui(interface.Gui):
    def __init__(self, player) -> None:
        super().__init__("paolo", {}, player)
    def draw(self, screen):
        x = (screen.get_width() - Textures["other"]["text_box"].get_width())/2
        y = screen.get_height() -Textures["other"]["text_box"].get_height() - 20 
        screen.blit(Textures["other"]["text_box"],(x,y))
        screen.blit(interface.main_font.render("Connais-tu ProfanOS?",0,(0,0,0)), (x+30,y+30-10-5))
        screen.blit(interface.main_font.render("Reste pas sur Windaube",0,(0,0,0)), (x+30,y+60-10-5))
        screen.blit(interface.main_font.render("Switch to Linux, ou ProfanOS",0,(0,0,0)), (x+30,y+90-10-5))
        screen.blit(interface.main_font.render("https://github.com/elydre/profanOS",0,(0,0,0)), (x+30,y+90-10+30-5))                    
        
    def tick(self, events:list[py.event.Event]):
        for i in events:
            if i.type == py.KEYDOWN:
                if i.key == py.K_e:
                    self.player.close_gui()


class Fisherman(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, False, Textures["other"]["fisherman"],Hitbox(HITBOX_RECT_t,NULL_VEC,0, 100, 100))

    def on_interact(self, world, user):
        user.open_gui("Fisherman_shop")


objs.registerObj(Snape)
objs.registerObj(Madre)
interface.registerGui(Madre_gui)
objs.registerObj(Paolo)
interface.registerGui(Paolo_gui)
interface.registerGui(Fisherman)
