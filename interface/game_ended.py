import pygame as py
from interface import *
from uti import *


class game_ended(Gui):
    def __init__(self, player) -> None:
        self.idx = 0
        self.max_idx = 2
        self.player_name = ""
        self.player_surname = ""
        super().__init__("game_ended", {}, player)
        
        
    def tick(self, events: list[py.event.Event]):
        ...
    def draw(self, screen):
        screen.fill((0,0,0))
        screen.blit(mc_font.render("Vous avez fini le jeu  bravo", False, (255,255,255)), (screen.get_width()//2, screen.get_height()//2))
    
    
registerGui(game_ended)