import pygame as py
from interface import *
from uti import *

class Game_over(Gui):
    def __init__(self, player) -> None:

        super().__init__("Game_over", {}, player)
        
        
    def tick(self, events: list[py.event.Event]):
        
        for i in events:
            if i.type == py.KEYDOWN:
                if i.key == py.K_e:
                    exit(1)
                    
            
    def draw(self, screen):
        screen.fill((0,0,0))
        screen.blit(mc_font.render("Vous avez perdu", False, (255,255,255)), (screen.get_width()//2, screen.get_height()//2))
        
    
registerGui(Game_over)
