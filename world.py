import itertools
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
        
    def chunkExists(self,pos:Vec) -> bool:
        return self._extracted_from_chunkExistsfromPos_2(pos)

    def chunkExistsfromPos(self,pos:Vec) -> bool:
        pos=pos//CHUNK_SIZE
        return self._extracted_from_chunkExistsfromPos_2(pos)

    # TODO Rename this here and in `chunkExists` and `chunkExistsfromPos`
    def _extracted_from_chunkExistsfromPos_2(self, pos):
        if pos.x not in self.chuncks.keys():
            return False
        return pos.y in self.chuncks[pos.x].keys()
    
    def getEntitiesInChunk(self,pos:Vec)->list[Npc]:
        return self.getChunk(pos).entities
    
    def getEntitiesInChunkfromPos(self,pos:Vec)->list[Npc]:
        return self.getChunkfromPos(pos).entities
    
    def show(self,screen:pygame.Surface, zoom_out: int) -> None:  
        scr_w=screen.get_width() * zoom_out
        scr_h=screen.get_height() * zoom_out
        screen.fill(self.bg)
        __objects:list[Obj]=[]
        __dyn_obj:list[Dynamic_Obj]=[]
        __players:list[Character]=[players[i] for i in range(1,len(players))]
        __entities:list[Npc]=[]
        __chunks:list[Chunk]=[]
        x=(players[0].pos//CHUNK_SIZE).x
        y=(players[0].pos//CHUNK_SIZE).y

        for i in range(- players[0].render_distance // 2 + 1, players[0].render_distance // 2 + 1):
            __chunks.extend(self.getChunk(Vec(x+i,y+k)) for k in range(- players[0].render_distance // 2 + 1, players[0].render_distance // 2 + 1))
        for i in __chunks:
            __objects.extend(i.objects)
            __dyn_obj.extend(i.dyn_objects)
            __entities.extend(i.entities)

        __offset=Vec(scr_w//2,scr_h//2)-players[0].pos+Vec(players[0].current_texture.get_width()*zoom_out//2,players[0].current_texture.get_height()*zoom_out//2)

        for i in __objects:
            if (not i.toplayer):
                p=(i.pos+__offset) // zoom_out
                screen.blit(pygame.transform.scale(i.texture,(i.texture.get_width()//zoom_out,i.texture.get_height()//zoom_out)),(int(p.x),int(p.y)))

        if players[0].isvisible:
            p=(players[0].pos+__offset) // zoom_out
            screen.blit(pygame.transform.scale(players[0].current_texture,(players[0].current_texture.get_width()//zoom_out,players[0].current_texture.get_height()//zoom_out)),(int(p.x),int(p.y)))

        for i in __players:
            p=i.pos+__offset
            if -50<=p.x<scr_w and -50<=p.y<scr_h:
                screen.blit(i.current_texture,(int(p.x),int(p.y)))

        for i in __entities:
            p=i.pos+__offset
            if -50<=p.x<scr_w and -50<=p.y<scr_h:
                screen.blit(i.texture,(int(p.x),int(p.y)))

        if players[0].chunk_border:
            for i in __chunks:
                corn=i.getBorders()

                py.draw.line(screen,(255,0,0),tuple((corn[0]+__offset) // zoom_out),tuple((corn[1]+__offset) // zoom_out))
                py.draw.line(screen,(255,0,0),tuple((corn[2]+__offset) // zoom_out),tuple((corn[3]+__offset) // zoom_out))
                py.draw.line(screen,(255,0,0),tuple((corn[0]+__offset) // zoom_out),tuple((corn[2]+__offset) // zoom_out))
                py.draw.line(screen,(255,0,0),tuple((corn[1]+__offset) // zoom_out),tuple((corn[3]+__offset) // zoom_out))



    def update(self)->int:
        ...
        #TODO : entity with pv<=0 have to die npc.die() 
        #TODO : return a certain value when the players[0] die
worlds:list[World]=[]


from random import randint

def newChunk(pos:Vec,world:World) -> Chunk:
    c=Chunk(pos,world)
    #TODO temporary
    for i, k in itertools.product(range(20), range(20)):
        c.objects.append(Objs["Grass"](i*50+c.top_left_pos.x,k*50+c.top_left_pos.y))
    c.objects.append(Objs["Stone"](randint(0,999)+c.top_left_pos.x,randint(0,999)+c.top_left_pos.y))
    return c

def newWorld(name:str,background_color:list[int]=(0,0,0)):
    return World(name,background_color)
