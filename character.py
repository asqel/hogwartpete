import clothes as c
from vector import *
import pygame as py

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
        self.genre=genre
        self.texture=texture
        self.clothes=clothes
        self.position=Vec(x,y)
        self.protection=0
        self.dir:bool=0 #0 c'est droite et 1 c'est gauche
        self.level=0
        self.puissance=0

    def left(self):
        if not self.dir:
            self.flip()
            self.dir=not self.dir
        Vec(self.position+(2,0))

    def right(self):
        if self.dir:
            self.flip()
            self.dir=not self.dir
        Vec(self.position-(2,0))

    def flip(self):
        self.texture=py.transform.flip(self.texture,1,0)