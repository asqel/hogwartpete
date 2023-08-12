import pygame as py
from interface import *
from uti import *


class game_ended(Gui):
    def __init__(self, player) -> None:
        self.idx = 0
        self.max_idx = 2
        self.player_name = ""
        self.player_surname = ""
        self.tick_count = player.tick_count
        self.day_count = player.day_count
        super().__init__("game_ended", {}, player)
        
        
    def tick(self, events: list[py.event.Event]):
        for i in events:
            if i.type == py.KEYDOWN:
                if i.key == py.K_ESCAPE:
                    return "end_game"
    def draw(self, screen):
        screen.fill((0,0,0))
        text1 = main_font.render("Vous avez fini le jeu  bravo", False, (255,255,255))
        text2 = main_font.render(str(self.day_count)+" days and "+str(self.tick_count)+" ticks", False, (255,255,255))
        screen.blit(text1, (screen.get_width()//2 - text1.get_width()//2,(screen.get_height() - 2*text1.get_height())//2))
        screen.blit(text2, (screen.get_width()//2 - text2.get_width()//2,text1.get_height() + (screen.get_height() - 2*text1.get_height())//2))

    
registerGui(game_ended)