import pygame
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

    def getBorders(self)->list[Vec]:
        """
        return corners of the chunk
        (Top-left, Top-right, bottom-left, bottom-right)
        each corner are in the chunk
        if chunk is at 0:
            return ( (0,0), (999,0), (0,999), (999,999) )
        """
        x=self.top_left_pos.x
        y=self.top_left_pos.y
        return (Vec(x,y),Vec(x+999,y),Vec(x,y+999),Vec(x+999,y+999))
        
class World:
    def __init__(self,name,background_col:list[int])->None:
        self.name=name
        self.bg=background_col
        self.chuncks:dict[int,dict[int,Chunk]]={}# chuncks[x][y]
        self.id=uuid.uuid4()
        
    def addEntity(self,n:Npc)->None:
        self.getChunkfromPos(n.pos).entities.append(n)
        
    def addObj(self,n:Obj)->None:
        self.getChunkfromPos(n.pos).objects.append(n)
    def addDyn_Obj(self,n:Obj)->None:
        self.getChunkfromPos(n.pos).dyn_objects.append(n)
        
    def genChunkat(self,pos:Vec):
        """
        generate a new chunk a {pos}
        if chunk already exist it will be erased
        """
        if pos.x not in self.chuncks.keys():
            self.chuncks[pos.x]={}
        self.chuncks[pos.x][pos.y]=newChunk(pos,self)
        
    def genChunkatfromPos(self,pos:Vec):
        """
        generate a new chunk a {pos}
        if chunk already exist it will be erased
        """
        self.genChunkat(pos//CHUNK_SIZE)
        
    def getChunk(self, pos:Vec)->Chunk:
        if not self.chunkExists(pos):
            self.genChunkat(pos)
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
    
    def show(self,screen:pygame.Surface)->None:  
        screen.fill(self.bg)
        __objects:list[Obj]=[]
        __dyn_obj:list[Dynamic_Obj]=[]
        __players:list[Character]=[players[i] for i in range(1,len(players))]
        __entities:list[Npc]=[]
        __chunks:list[Chunk]=[]
        x=(players[0].pos//CHUNK_SIZE).x
        y=(players[0].pos//CHUNK_SIZE).y
        for i in range(-1,2):
            for k in range(-1,2):
                __chunks.append(self.getChunk(Vec(x+i,y+k)))
        for i in __chunks:
            __objects.extend(i.objects)
            __dyn_obj.extend(i.dyn_objects)
            __entities.extend(i.entities)
        
        __offset=Vec(500/2,500/2)-players[0].pos-Vec(players[0].current_texture.get_width()//2,players[0].current_texture.get_height()//2)
        
        for i in __objects:
            if (not i.toplayer):
                p=i.pos+__offset
                screen.blit(i.texture,(int(p.x),int(p.y)))
                
        p=players[0].pos+__offset
        screen.blit(players[0].current_texture,(int(p.x),int(p.y)))
        
        for i in players:
            p=i.pos+__offset
            screen.blit(i.current_texture,(int(p.x),int(p.y)))
        for i in __entities:
            p=i.pos+__offset
            screen.blit(i.current_texture,(int(p.x),int(p.y)))
            
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



