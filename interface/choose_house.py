import pygame as py
from interface import *



class Choose_house(Gui):
    def __init__(self, name, player) -> None:
        super().__init__(name, {}, player)
        self.houses = ["p","g","sd","sp"]
        self.house_idx = 0
        
    def tick(self, events: list[py.event.Event]):
        for i in events:
            if i.type == py.KEYDOWN:
                if i.key == py.K_UP:
                    self.house_idx -= 1
                    if self.house_idx < 0: 
                        self.house_idx = len(self.house) -1
                if i.key == py.K_DOWN:
                    self.house_idx += 1
                    if self.house_idx >= len(self.houses): 
                        self.house_idx = 0
                        
    def draw(self, screen):
        x = (screen.get_width() - Textures["other"]["text_box"].get_width())/2
        y = screen.get_height() -Textures["other"]["text_box"].get_height() - 20 
        screen.blit(Textures["other"]["text_box"],(x,y))
        screen.blit(mc_font.render("tiens prends ta baguette,",0,(0,0,0)), (x+30,y+30-10))
        screen.blit(mc_font.render("fait attention dehors",0,(0,0,0)), (x+30,y+60-10))
        screen.blit(mc_font.render("il y a des mange-morts ",0,(0,0,0)), (x+30,y+90-10))                    
        screen.blit(mc_font.render("il y a des mange-morts ",0,(0,0,0)), (x+30,y+90-10+30))                    
        
    