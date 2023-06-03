import pygame as py
from interface import *
from uti import *
from items import *



class Escape_gui(Gui):
    def __init__(self, player) -> None:
        super().__init__("Escape_gui", {}, player)
        
        
    def tick(self, events: list[py.event.Event]):
        
        for i in events:
            if i.type == py.KEYDOWN:
                if i.key == py.K_e:
                    self.player.close_gui()
                if i.key == py.K_ESCAPE:
                    self.player.close_gui()

                    
            
    def draw(self, screen):
        x = (screen.get_width() - Textures["other"]["text_box_x2"].get_width())/2
        y = screen.get_height() -Textures["other"]["text_box_x2"].get_height() - 20 
        screen.blit(Textures["other"]["text_box_x2"],(x,y))
        screen.blit(mc_font.render("zqsd to move", 0, (0,0,0)), (x+30,y+30-15))
        screen.blit(mc_font.render("a to shoot only if you have wand", 0, (0,0,0)), (x+30,y+60-15))
        screen.blit(mc_font.render("e to interact", 0, (0,0,0)), (x+30,y+90-15))                  
        screen.blit(mc_font.render("t to delete item", 0, (0,0,0)), (x+30,y+90-15+30))                  
        screen.blit(mc_font.render("1 to 0 to change slot", 0, (0,0,0)), (x+30,y+90-15+30+30))                  
        screen.blit(mc_font.render("r to use item of slot", 0, (0,0,0)), (x+30,y+90-15+30+60))                  
registerGui(Escape_gui)