import pygame as py
from interface import * 
from items import *
class Fisherman_shop(Gui):
    def __init__(self, player) -> None:
        super().__init__("Escape_gui", {}, player)
        self.idx = 0
        self.max_idx = 1

    def tick(self, events: list[py.event.Event]):
         for i in events:
            if i.type == py.KEYDOWN:
                if i.key == py.K_UP :
                    self.idx -= 1
                    if self.idx < 0: 
                        self.idx = self.max_idx
                        
                if i.key == py.K_DOWN :
                    self.idx += 1
                    if self.idx > self.max_idx: 
                        self.idx = 0
                
                if i.key == py.K_e:
                    if self.idx == 0:
                        if self.player.money >= 1:
                            if self.player.add_item(items["Super_moule"](1)):
                                self.player.money -= 1
                    elif self.idx == 1:
                        self.player.close_gui()
    
    def draw(self, screen):
        x = (screen.get_width() - Textures["other"]["text_box"].get_width())/2
        y = screen.get_height() -Textures["other"]["text_box"].get_height() - 20 
        screen.blit(Textures["other"]["text_box"],(x,y))
        screen.blit(main_font.render("Edward Findus", 0, (0,0,0)), (x,y+30-15-30-5))
        screen.blit(main_font.render("Hey matelot ! La pêche ?", 0, (0,0,0)), (x+30,y+30-15))
        screen.blit(main_font.render("Tu viens pour mes moules ?",0,(0,0,0)), (x+30,y+60-15))
        screen.blit(main_font.render("    Super moule        1€",0,(0,255,0)if self.idx == 0 and self.player.money >=1 else((255,0,0)if self.idx == 0 else (0,0,0))), (x+30,y+90-15))                    
        screen.blit(main_font.render("            exit",0,(0,255,0)if self.idx == 1 else (0,0,0)), (x+30,y+90-15+30))                    

        screen.blit(Textures["other"]["moule"], (x+30,y+90-15))

registerGui(Fisherman_shop)