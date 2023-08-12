import pygame as py
from uti import *
from objs import *
import world as w
import jsonizer as js
from interface import *
from items import *

class Cat(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["cat_1"],Hitbox(HITBOX_RECT_t,NULL_VEC,0, 100, 100))
        self.frame=0
        self.maxframe=3
        self.frames=[Textures["Obj"]["cat_1"],Textures["Obj"]["cat_2"],Textures["Obj"]["cat_3"],Textures["Obj"]["cat_4"]]
        self.count=0
        self.maxcount=75

    def on_draw(self, world, has_been_drawn):
        if self.count>self.maxcount:
            self.count=0
        if self.count==self.maxcount:
            if self.frame>self.maxframe:
                self.frame=0
            else:
                self.texture = self.frames[self.frame]
                self.frame+=1
        self.count+=1

    def on_interact(self, world, user):
        user.gui=Cat_gui(user)
    
class Cat_gui(Gui):
    def __init__(self, player) -> None:
        super().__init__("Michel", {}, player)

    def draw(self, screen):
        x = (screen.get_width() - Textures["other"]["text_box"].get_width())/2
        y = screen.get_height() -Textures["other"]["text_box"].get_height() - 20 
        screen.blit(Textures["other"]["text_box"],(x,y))
        screen.blit(main_font.render("Miaou Miaou Miaou Miaou Miaou,",0,(0,0,0)), (x+30,y+30-10-5))
        screen.blit(main_font.render("Miaou Miaou Miaou Miaou Miaou",0,(0,0,0)), (x+30,y+60-10-5))
        screen.blit(main_font.render("Miaou Miaou Miaou Miaou Miaou",0,(0,0,0)), (x+30,y+90-10-5))
        screen.blit(main_font.render("Miaou Miaou Miaou Miaou Miaou",0,(0,0,0)), (x+30,y+90-10+30-5))
    
    def tick(self, events: list[py.event.Event]):
        for i in events:
            if i.type == py.KEYDOWN:
                if i.key == py.K_e:
                    self.player.gui = None
                    if not self.player.has_item("goggles_of_truth"):
                        self.player.add_item(items["goggles_of_truth"](1))

registerObj(Cat)
registerGui(Cat_gui)