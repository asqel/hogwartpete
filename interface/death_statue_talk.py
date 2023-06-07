import pygame as py
from interface import *
from uti import *
from items import *



class Death_statue(Gui):
    def __init__(self, player) -> None:
        self.text_idx = 0
        self.text = [
            ["Ô toi qui entend ma voix, ", "il y a bien longtemps je   ", "fut scellé dans cette    ", "statue en terre cuite.    "],
            ["Certain me surnome la mort", "d'autre la faucheusse, ici ", "ramène mes 3 reliques.   ", "Tu en sera recompensé.    "],
        ]
        self.text_color = [
            [(0, 0, 0) , (0,0,0), (0,0,0), (0,0,0)],
            [(0, 0, 0) , (0,0,0), (0,0,0), (0,0,0)],
        ]
        self.text_len = len(self.text)
        super().__init__(self.__class__.__name__, {}, player)
        
        
    def tick(self, events: list[py.event.Event]):
        
        for i in events:
            if i.type == py.KEYDOWN:
                if i.key == py.K_e:
                    if self.text_idx < self.text_len - 1:
                        self.text_idx += 1
                    else:
                        self.player.close_gui()
                    
            
    def draw(self, screen):
        draw_4_line(screen , self.text[self.text_idx], self.text_color[self.text_idx])
                    




registerGui(Death_statue)