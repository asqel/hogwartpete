import pygame as py
from objs import *
from entities import *

class World:
    def __init__(self,name,backgroung:py.surface,objs:list[Obj]=list()):
        self.name=name
        self.bg=backgroung
        self.objects=objs
        self.entities=[]
        self.players=players
        
    def registerEntity(self,n:Npc)->None:
        self.entities.append(n)
        
    def registerPlayer(self,p:Character)->None:
        self.players.append(p)
        
    def show(self,screen:py.Surface):  
        screen.blit(self.bg,(0,0)) if self.bg is not None  else None
        for i in self.players:
            screen.blit(i.texture,(i.position.x,i.position.y))
        for i in self.entities:
            screen.blit(i.texture,(i.position.x,i.position.y))
            
    def update(self):
        p=0
        while p<len(self.entities):
            if self.entities[p].pv<=0:
                self.entities.pop(p)
                continue
            p+=1
worlds:list[World]=[World("a",None,None)]
        