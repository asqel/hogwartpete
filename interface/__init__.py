import pygame as py
from uti.vector import *

class Text:
    def __init__(self,txt:str,pos:Vec,color:list[int,int,int]) -> None:
        self.txt
        self.pos=pos
        self.color=color

class Text:
    def __init__(self,txt:str,txt_col:list[int,int,int],pos:Vec,texture:py.Surface) -> None:
        self.txt
        self.pos=pos
        self.txt_col=txt_col
        self.texture=texture
        
        
class Image:
    def __init__(self,texture:py.Surface,pos:Vec) -> None:
        self.texture=texture
        self.pos=pos


class Interface:
    def __init__(self,texts,buttons,images) -> None:
        self.texts=texts
        self.buttons=buttons
        self.images=images