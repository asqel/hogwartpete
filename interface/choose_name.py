import pygame as py
from interface import *
from uti import *


class Choose_name(Gui):
    def __init__(self, player) -> None:
        self.idx = 0
        self.max_idx = 2
        self.player_name = ""
        self.player_surname = ""
        super().__init__("Choose_house", {}, player)
        
        
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
                        
                if self.idx == 2:
                    if i.key == py.K_e:
                        self.player.name = self.player_name
                        self.player.surname = self.player_surname
                        self.player.gui = guis["Choose_house"](self.player)
                if self.idx == 1:
                    if i.key != py.K_BACKSPACE:
                        self.player_surname += i.unicode
                    else:
                        self.player_surname = self.player_surname[:-1]
                if self.idx == 0:
                    if i.key != py.K_BACKSPACE:
                        self.player_name += i.unicode
                    else:
                        self.player_name = self.player_name[:-1]
                    
            
    def draw(self, screen):
        x = (screen.get_width() - Textures["other"]["text_box"].get_width())/2
        y = screen.get_height() -Textures["other"]["text_box"].get_height() - 20 
        screen.blit(Textures["other"]["text_box"],(x,y))
        screen.blit(main_font.render(f"nom : {self.player_name}",0,(0,255,0)if self.idx == 0 else (0,0,0)), (x+30,y+30))
        screen.blit(main_font.render(f"prenom : {self.player_surname}",0,(0,255,0)if self.idx == 1 else (0,0,0)), (x+30,y+60))
        screen.blit(main_font.render("            confirm",0,(0,255,0)if self.idx == 2 else (0,0,0)), (x+30,y+90))                    
        
    
    
registerGui(Choose_name)