import pygame as py
from uti.vector import *
import os
py.font.init()

mc_font=py.font.Font(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/fonts/Minecraft.otf",10)

class Text:
    def __init__(self,txt:str,pos:Vec,color:list[int,int,int],action,width:int,height:int) -> None:
        self.txt
        self.pos=pos
        self.color=color
        self.action=action
        self.width=width
        self.height=height

class Button:
    def __init__(self,txt:str,txt_col:list[int,int,int],pos:Vec,texture:py.Surface,action,width:int,height:int) -> None:
        self.txt=txt
        self.pos=pos
        self.txt_col=txt_col
        self.texture=texture
        self.action=action
        self.width=width
        self.height=height
        
        
class Image:
    def __init__(self,texture:py.Surface,pos:Vec,action,width:int,height:int) -> None:
        self.texture=texture
        self.pos=pos
        self.action=action
        self.width=width
        self.height=height

class Interface:
    def __init__(self,texts:list[Text],buttons:list[Button],images:list[Image],action,background:py.Surface,pos:Vec,width:int,height:int) -> None:
        self.texts=texts
        self.buttons=buttons
        self.images=images
        self.bag=background
        self.action=action#will be called every tick and has to take 3 parameter (World,Character,Vec)->(current_world,interface_user,mouse_pos)
        self.pos=pos
        self.width=width
        self.height=height
    
    def on_tick(self,world,user):
        ...
        
        
    def draw(self,screen:py.Surface):
        ...