#import pygame as py
#import interface
#from uti.textures import *
#
#class Game_over(interface.Gui):
#    def __init__(self, player) -> None:
#
#        super().__init__("Game_over", {}, player)
#        
#        
#    def tick(self, events: list[py.event.Event]):
#        for i in events:
#            if i.type == py.KEYDOWN:
#                if i.key == py.K_ESCAPE:
#                    return "end_game"
#                    
#            
#    def draw(self, screen):
#        screen.fill((0,0,0))
#        screen.blit(interface.main_font.render("Vous avez perdu", False, (255,255,255)), (screen.get_width()//2, screen.get_height()//2))
#        
#    
#interface.registerGui(Game_over)
