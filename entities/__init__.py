import Clothes as c
from uti.vector import *
import pygame as py
from  spells import *
import uuid

class Character:
    def __init__(self,name:str,surname:str,maison:str,sorts,potions,inventaire,genre:str,texture:list[py.Surface],clothes,x:float,y:float,world):
        self.name=name
        self.surname=surname
        self.house=maison
        self.sorts=sorts
        self.potions=potions
        self.inventaire=inventaire
        self.pv=100
        self.pvmax=100
        self.effects=[]
        self.genre=genre
        self.texture=texture#[UP,RIGHT,DOWN,LEFT]
        self.current_texture=texture[2]
        self.clothes=clothes
        self.pos=Vec(x,y)
        self.protection=0
        self.dir:str="d" #d -> down  |  u -> up  |  r -> right  |  l -> left  |
        self.level=0
        self.puissance=0
        self.speed=1
        self.isvisible=True
        self.render_distance=3
        self.world=world
        self.chunk_border=False
        self.uuid=uuid.uuid4()
        self.zoom_out=1

    def left(self):
        if self.dir!="l":
            self.dir="l"
            self.current_texture=self.texture[3]
        self.pos-=Vec(2,0)*self.speed

    def right(self):
        if self.dir!="r":
            self.dir="r"
            self.current_texture=self.texture[1]
        self.pos+=Vec(2,0)*self.speed


    def up(self):
        if self.dir!="u":
            self.dir="u"
            self.current_texture=self.texture[0]
        self.pos-=Vec(0,2)*self.speed

    def down(self):
        if self.dir!="d":
            self.dir="d"
            self.current_texture=self.texture[2]
        self.pos+=Vec(0,2)*self.speed
    
    def update_texture(self,vec):
        corner=math.sqrt(2)/2
        if -corner<=vec.x<=corner and corner<=vec.y<=1:
            self.current_texture=self.texture[2]
            
        elif -corner<=vec.x<=corner and -corner>=vec.y>=-1:
            self.current_texture=self.texture[0]
            
        elif vec.x<0:
            self.current_texture=self.texture[3]
        else:
            self.current_texture=self.texture[1]
class Npc:
    def __init__(self,name:str,surname:str,texture:py.Surface,spells:list[Spell],x,y) -> None:
        self.name=name
        self.surname=surname
        self.texture=texture
        self.spells=spells
        self.pv=100
        self.pos=Vec(x,y)
        

players:list[Character]=[]
entitys:list[Npc]=[]#npcs / animals /moving things 






