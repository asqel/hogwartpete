import pygame as py
from objs import *
from entities import *
from objs import *

#in pixel (its a square)
CHUNK_SIZE=1000

class Chunk:
    def __init__(self,chunk_pos:'Vec',world:'World') -> None:
        self.pos:Vec=chunk_pos#pos x,y in World:chuncks
        self.top_left_pos:Vec=chunk_pos*CHUNK_SIZE
        self.world=world
        self.entities:list[Npc]=[]
        self.objects:list[Obj]=[]
        self.dyn_objects:list[Dynamic_Obj]=[]

class World:
    def __init__(self,name,background_col:list[int])->None:
        self.name=name
        self.bg=background_col
        self.chuncks:dict[int,dict[int,Chunk]]={}# chuncks[x][y]
        self.id=uuid.uuid4()
        
    def addEntity(self,n:Npc)->None:
        x=n.pos.x
        y=n.pos.y
        
    def getChunk(self, pos:Vec)->Chunk:
        return self.chuncks[pos.x][pos.y]
    
    def getChunkfromPos(self,pos:Vec)->Chunk:
        return self.getChunk(pos//CHUNK_SIZE)
        
    def chunkExists(self,pos:Vec)->bool:
        if pos.x not in self.chuncks.keys():
            return False
        if pos.y not in self.chuncks[pos.x].keys():
            return False
        return True

    def chunkExistsfromPos(self,pos:Vec)->bool:
        pos=pos//CHUNK_SIZE
        if pos.x not in self.chuncks.keys():
            return False
        if pos.y not in self.chuncks[pos.x].keys():
            return False
        return True
    
    def getEntitiesInChunk(self,pos:Vec)->list[Npc]:
        return self.getChunk(pos).entities
    
    def getEntitiesInChunkfromPos(self,pos:Vec)->list[Npc]:
        return self.getChunkfromPos(pos).entities
    
    def show(self,screen:py.Surface)->None:  
        screen.fill(self.bg)
        
        #for i in self.objects:
        #    if(not i.toplayer):
        #        screen.blit(i.texture,(i.pos.x,i.pos.y))
        for i in players:
            screen.blit(i.current_texture,(i.pos.x,i.pos.y))
        for i in self.entities:
            screen.blit(i.texture,(i.pos.x,i.pos.y))
            
    def update(self)->None:
        ...
        #TODO : entity with pv<=0 have to die npc.die() 
        #TODO : return a certain value when the players[0] die
worlds:list[World]=[]


def newChunk(pos:Vec,world:World)->Chunk:
    c=Chunk(pos,world)
    return c

from random import randint
def newWorld(name:str,background_color:list[int]=(0,0,0)):
    w=World(name,background_color)
    w.chuncks[-1]={}
    w.chuncks[0]={}
    w.chuncks[1]={}
    for i in range(-1,2):
        for k in range(-1,2):
            w.chuncks[i][k]=newChunk(Vec(i,k),w)
            a:Chunk=w.getChunk(Vec(i,k))
            a.objects.append(Objs["Stone"](randint(0,999)+a.top_left_pos.x,randint(0,999)+a.top_left_pos.y))

    return w



