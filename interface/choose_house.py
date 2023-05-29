import pygame as py
from interface import *
from uti import *



class Choose_house(Gui):
    def __init__(self, player) -> None:
        self.houses = ["p","g","sd","sp"]
        self.house_idx = 0
        super().__init__("Choose_house", {}, player)
        
        
    def tick(self, events: list[py.event.Event]):
        for i in events:
            if i.type == py.KEYDOWN:
                if i.key == py.K_UP or i.key == py.K_z:
                    self.house_idx -= 1
                    if self.house_idx < 0: 
                        self.house_idx = len(self.houses) -1
                        
                if i.key == py.K_DOWN or i.key == py.K_s:
                    self.house_idx += 1
                    if self.house_idx >= len(self.houses): 
                        self.house_idx = 0
                        
                if i.key == py.K_e:
                    if self.house_idx == 0:
                        self.player.house = "pouffsoufle"
                        self.player.texture= POUFSOUFFLE_TEXTURES_0
                        self.player.current_texture = self.player.texture[2]
                        
                    elif self.house_idx == 1:
                        self.player.house = "griffondor"
                        self.player.texture= GRIFFONDOR_TEXTURES_0
                        self.player.current_texture = self.player.texture[2]
                        
                    elif self.house_idx == 2:
                        self.player.house = "serdaigle"
                        self.player.texture= SERDAIGLE_TEXTURES_0
                        self.player.current_texture = self.player.texture[2]
                        
                    elif self.house_idx == 3:
                        self.player.house = "serpentard"
                        self.player.texture= SERPENTARD_TEXTURES_0
                        self.player.current_texture = self.player.texture[2]
                    self.player.gui = None
                    

    def draw(self, screen):
        x = (screen.get_width() - Textures["other"]["text_box"].get_width())/2
        y = screen.get_height() -Textures["other"]["text_box"].get_height() - 20 
        screen.blit(Textures["other"]["text_box"],(x,y))
        screen.blit(mc_font.render("pouffsoufle",0,(0,255,0)if self.house_idx == 0 else (0,0,0)), (x+30,y+30-15))
        screen.blit(mc_font.render("griffondor",0,(0,255,0)if self.house_idx == 1 else (0,0,0)), (x+30,y+60-15))
        screen.blit(mc_font.render("serdaigle",0,(0,255,0)if self.house_idx == 2 else (0,0,0)), (x+30,y+90-15))                    
        screen.blit(mc_font.render("serpentard",0,(0,255,0)if self.house_idx == 3 else (0,0,0)), (x+30,y+90-15+30))                    
        
    
    
registerGui(Choose_house)