import pygame as py
from interface import *
from uti import *
from items import *



class Farine_shop(Gui):
    def __init__(self, player) -> None:
        self.idx = 0
        self.max_idx = 3
        super().__init__("Farine_shop", {}, player)
        
        
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
                        
                if self.idx == 3:
                    if i.key == py.K_e:
                        self.player.gui = None
                if self.idx == 0:
                    if i.key == py.K_e:
                        if self.player.money >= 5:
                            if not self.player.add_item(items["Taboule"](1)):
                                self.player.gui = guis["Le_bord"](self.player)
                            else:
                                self.player.money -= 5
                if self.idx == 1:
                    if i.key == py.K_e:
                        if self.player.money >= 5:
                            if not self.player.add_item(items["Couscous"](1)):
                                self.player.gui = guis["Le_bord"](self.player)
                            else:
                                self.player.money -= 5
                if self.idx == 2:
                    if i.key == py.K_e:
                        if self.player.money >= 5:
                            if not self.player.add_item(items["Sausage"](1)):
                                self.player.gui = guis["Le_bord"](self.player)
                            else:
                                self.player.money -= 5

                    
            
    def draw(self, screen):
        x = (screen.get_width() - Textures["other"]["text_box"].get_width())/2
        y = screen.get_height() -Textures["other"]["text_box"].get_height() - 20 
        screen.blit(Textures["other"]["text_box"],(x,y))
        screen.blit(mc_font.render("    taboulé           5 €",0,(0,255,0)if self.idx == 0 and self.player.money >=5 else((255,0,0)if self.idx == 0 else (0,0,0))), (x+30,y+30-15))
        screen.blit(mc_font.render("    couscous          5 $",0,(0,255,0)if self.idx == 1 and self.player.money >=5 else((255,0,0)if self.idx == 1 else (0,0,0))), (x+30,y+60-15))
        screen.blit(mc_font.render("    saucisses         5 £",0,(0,255,0)if self.idx == 2 and self.player.money >=5 else((255,0,0)if self.idx == 2 else (0,0,0))), (x+30,y+90-15))                    
        screen.blit(mc_font.render("            exit",0,(0,255,0)if self.idx == 3 else (0,0,0)), (x+30,y+90-15+30))                    

        screen.blit(Textures["item"]["taboule"], (x+30,y+30-15))
        screen.blit(Textures["item"]["couscous"], (x+30,y+60-15))
        screen.blit(Textures["item"]["saucisses"], (x+30,y+90-15))


class Le_bord(Gui):
    def __init__(self, player) -> None:
        super().__init__("Le_bord", {}, player)
        
        
    def tick(self, events: list[py.event.Event]):
        
        for i in events:
            if i.type == py.KEYDOWN:
                if i.key == py.K_e:
                    self.player.gui = guis["Farine_shop"](self.player)

                    
            
    def draw(self, screen):
        x = (screen.get_width() - Textures["other"]["text_box"].get_width())/2
        y = screen.get_height() -Textures["other"]["text_box"].get_height() - 20 
        screen.blit(Textures["other"]["text_box"],(x,y))
        screen.blit(mc_font.render("hop hop hop",0,(0,0,0)), (x+30,y+60-15))
        screen.blit(mc_font.render("pas plus haut qu'le bord !",0,(0,0,0)), (x+30,y+90-15))                    




registerGui(Farine_shop)
registerGui(Le_bord)