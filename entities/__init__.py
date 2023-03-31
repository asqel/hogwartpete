import clothes as c
from uti.vector import *
import pygame as py
from  spells import *
import uuid

class Character:
    def __init__(self,name:str,surname:str,maison:str,sorts,potions,inventaire,genre:str,texture:py.surface,clothes,x:float,y:float):
        self.name=name
        self.surname=surname
        self.maison=maison
        self.sorts=sorts
        self.potions=potions
        self.inventaire=inventaire
        self.pv=100
        self.pvmax=100
        self.effects=[]
        self.genre=genre
        self.texture=texture
        self.clothes=clothes
        self.position=Vec(x,y)
        self.protection=0
        self.dir:bool=0 #0 c'est droite et 1 c'est gauche
        self.level=0
        self.puissance=0
        self.uuid=uuid.uuid4()

    def left(self):
        if self.dir==0:
            self.flip()
            self.dir=1
        self.position-=(2,0)

    def right(self):
        if self.dir==1:
            self.flip()
            self.dir=0
        self.position+=(2,0)


    def up(self):
        self.position-=(0,2)

    def down(self):
        self.position+=(0,2)

    def flip(self):
        self.texture=py.transform.flip(self.texture,1,0)


class Npc:
    def __init__(self,name:str,surname:str,texture:py.Surface,spells:list[Spell],x,y) -> None:
        self.name=name
        self.surname=surname
        self.texture=texture
        self.spells=spells
        self.pv=100
        self.position=Vec(x,y)
        

players:list[Character]=[]
entitys:list[Npc]=[]#npcs / animals /moving things 





