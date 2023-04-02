import pygame as py
from objs import *
from entities import *

class World:
    def __init__(self,name,background_col:list[int,int,int],objs:list[Obj]=list()):
        self.name=name
        self.bg=background_col
        self.objects=objs
        self.entities=[]
        self.players=players
        
    def addEntity(self,n:Npc)->None:
        self.entities.append(n)
        
    def addPlayer(self,p:Character)->None:
        self.players.append(p)
        
    def show(self,screen:py.Surface):  
        screen.fill(self.bg)
        for i in self.objects:
            if(not i.toplayer):
                screen.blit(i.texture,(i.pos.x,i.pos.y))
        for i in self.players:
            screen.blit(i.texture,(i.pos.x,i.pos.y))
        for i in self.entities:
            screen.blit(i.texture,(i.pos.x,i.pos.y))
            
    def update(self):
        p=0
        while p<len(self.entities):
            if self.entities[p].pv<=0:
                self.entities.pop(p)
                continue
            p+=1
worlds:list[World]=[World("a",(0,255,255),[])]
        
        
def root(x):
    if 0<=x<10:
        return x
    if 10<=x<20:
        return x-10+1
    return root(sum([int(i) for i in str(x)]))

def root2(x):
    return (x - 1) % 9 + 1 if x else 0
print(root(3997))
print(root2(0))