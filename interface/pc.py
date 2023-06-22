import pygame as py
from interface import *
from uti import *



class Pc(Gui):
    def __init__(self, player) -> None:
        super().__init__("Pc", {}, player)
        
        
    def tick(self, events: list[py.event.Event]):
        
        for i in events:
            if i.type == py.KEYDOWN:
                if i.key == py.K_e:
                    self.player.gui = None
                    
            
    def draw(self, screen):
        x = (screen.get_width() - Textures["other"]["text_box"].get_width())/2
        y = screen.get_height() -Textures["other"]["text_box"].get_height() - 20 
        screen.blit(Textures["other"]["text_box"],(x,y))
        

        screen.blit(mc_font.render("Vous ne reconnaissez pas",0,(0,0,0)), (x+30-6,y+30-10-10))
        screen.blit(mc_font.render("l'OS quelqu'un a du le",0,(0,0,0)), (x+30-6,y+60-10-10))
        screen.blit(mc_font.render("changer mais vous le",0,(0,0,0)), (x+30-6,y+90-10-10))
        screen.blit(mc_font.render("trouvez pas mal.",0,(0,0,0)), (x+30-6,y+120-10-10))
        
    
registerGui(Pc)
