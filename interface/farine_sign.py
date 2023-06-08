import pygame as py
from interface import *
from uti import *



class Farine_sign(Gui):
    def __init__(self, player) -> None:
        super().__init__("Farine_sign", {}, player)
        
        
    def tick(self, events: list[py.event.Event]):
        
        for i in events:
            if i.type == py.KEYDOWN:
                if i.key == py.K_e:
                    self.player.gui = None
                    
            
    def draw(self, screen):
        x = (screen.get_width() - Textures["other"]["text_box"].get_width())/2
        y = screen.get_height() -Textures["other"]["text_box"].get_height() - 20 
        screen.blit(Textures["other"]["text_box"],(x,y))
        
        screen.blit(mc_font.render("un panneau", 0, (0,0,0)), (x,y+30-15-30-5))

        screen.blit(mc_font.render("Le chef Farine s'est exilé.",0,(0,0,0)), (x+30-6,y+30-10-10))
        screen.blit(mc_font.render("La légende raconte qu'il",0,(0,0,0)), (x+30-6,y+60-10-10))
        screen.blit(mc_font.render("vit maintenant dans la",0,(0,0,0)), (x+30-6,y+90-10-10))
        screen.blit(mc_font.render("forêt...",0,(0,0,0)), (x+30-6,y+120-10-10))
        
    
registerGui(Farine_sign)
