import itertools
import pygame
from objs import *
from entities import *
from objs import *
from math import ceil

#in pixel (its a square)
CHUNK_SIZE=1000
show_hitbox=True

class Chunk:
    def __init__(self,chunk_pos:'Vec',world:'World') -> None:
        self.pos:Vec=chunk_pos#pos x,y in World:chuncks
        self.top_left_pos:Vec=chunk_pos*CHUNK_SIZE
        self.world=world
        self.entities:list[Npc]=[]
        self.objects:list[Obj]=[]
        self.dyn_objects:list[Dynamic_Obj]=[]
        self.tiles=[[None]*10 for i in range(10)]
        self.background_obj:list[Obj]=[]
        self.hitboxes:list[Hitbox]=[]

    def get_borders(self)->list[Vec]:
        """
        return corners of the chunk
        (Top-left, Top-right, bottom-left, bottom-right)
        each corner are in the chunk
        if chunk is at 0:
            return ( (0,0), (999,0), (0,999), (999,999) )
        """
        x=self.top_left_pos.x
        y=self.top_left_pos.y
        return (Vec(x, y), Vec(x + 999, y), Vec(x, y + 999), Vec(x + 999, y + 999))

class World:
    """
    difference between function called ...at and ...from_pos:
        ...at : pos in the chunks dictionary of ther world
        ...from_pos : pos of an entity or player or an object
    
    """
    def __init__(self,name,background_col:list[int])->None:
        self.name=name
        self.bg=background_col
        self.chuncks:dict[int,dict[int,Chunk]]={}# chuncks[x][y]
        self.id=uuid.uuid4()
        
    def add_entity(self,n:Npc)->None:
        """
        add an entity to the world
        if the entity is in a chunk that doesn't exists the chunk will be generated 
        """
        self.get_Chunk_from_pos(n.pos).entities.append(n)
        
    def add_Obj(self,n:Obj)->None:
        """
        add an Obj to the world
        if the Obj is in a chunk that doesn't exists the chunk will be generated 
        """
        self.get_Chunk_from_pos(n.pos).objects.append(n)

    def add_Dyn_Obj(self,n:Dynamic_Obj)->None:
        """
        add an Dyn_Obj to the world
        if the Dyn_Obj is in a chunk that doesn't exists the chunk will be generated 
        """
        self.get_Chunk_from_pos(n.pos).dyn_objects.append(n)
        
    def gen_Chunk_at(self,pos:Vec):
        """
        generate a new chunk a {pos}
        if chunk already exist it will be erased
        """
        if pos.x not in self.chuncks.keys():
            self.chuncks[pos.x]={}
        self.chuncks[pos.x][pos.y]=newChunk(pos,self)
        
    def gen_Chunk_from_pos(self,pos:Vec):
        """
        generate a new chunk a {pos}
        if chunk already exist it will be erased
        """
        self.gen_Chunk_at(pos//CHUNK_SIZE)
        
    def get_Chunk_at(self, pos:Vec)->Chunk:
        if not self.chunk_exists_at(pos):
            self.gen_Chunk_at(pos)
        return self.chuncks[pos.x][pos.y]

    def get_Chunk_from_pos(self,pos:Vec)->Chunk:
        return self.get_Chunk_at(pos//CHUNK_SIZE)
        
    def chunk_exists_at(self,pos:Vec) -> bool:
        if pos.x not in self.chuncks.keys():
            return False
        return pos.y in self.chuncks[pos.x].keys()

    def chunk_exists_from_pos(self,pos:Vec) -> bool:
        return self.chunk_exists_at(pos//CHUNK_SIZE)
    
    def get_entities_in_Chunk_at(self,pos:Vec)->list[Npc]:
        return self.get_Chunk_at(pos).entities
    
    def get_entities_in_Chunk_from_pos(self,pos:Vec)->list[Npc]:
        return self.get_Chunk_from_pos(pos).entities
    
    def show(self,screen:pygame.Surface, zoom_out: int) -> None:
        __bg_obj:list[Obj]=[]
        __objects:list[Obj]=[]
        __dyn_obj:list[Dynamic_Obj]=[]
        __players:list[Character]=[players[i] for i in range(1,len(players))]
        __entities:list[Npc]=[]
        __chunks:list[Chunk]=[]
        x = (players[0].pos//CHUNK_SIZE).x

        scr_w = screen.get_width() * zoom_out
        scr_h = screen.get_height() * zoom_out

        screen.fill(self.bg)
        y = (players[0].pos // CHUNK_SIZE).y

        for i in range(-players[0].render_distance // 2 + 1, players[0].render_distance // 2 + 1):
            __chunks.extend(self.get_Chunk_at(Vec(x + i, y + k)) for k in range(-players[0].render_distance // 2 + 1, players[0].render_distance // 2 + 1))

        for e in __chunks:
            __objects.extend(e.objects)
            __dyn_obj.extend(e.dyn_objects)
            __entities.extend(e.entities)
            __bg_obj.extend(e.background_obj)

        if zoom_out != 1:

            # scale all the textures
            scaled_textures = {}
            for e in __objects:
                if e.id not in scaled_textures.keys():
                    scaled_textures[e.id] = pygame.transform.scale(e.texture, (ceil(e.texture.get_width() / zoom_out), ceil(e.texture.get_height() / zoom_out)))
                e.texture = scaled_textures[e.id]

            __offset = Vec(scr_w // 2, scr_h // 2) - players[0].pos + Vec(players[0].current_texture.get_width() * zoom_out // 2,players[0].current_texture.get_height() * zoom_out // 2)

            for i in __objects:
                if not i.toplayer:
                    p = (i.pos + __offset) // zoom_out
                    if -50 < p.x < scr_w and -50 < p.y < scr_h:
                        screen.blit(i.texture, (int(p.x), int(p.y)))

            if players[0].isvisible:
                p=(players[0].pos+__offset) // zoom_out
                screen.blit(pygame.transform.scale(players[0].current_texture,(players[0].current_texture.get_width()//zoom_out,players[0].current_texture.get_height()//zoom_out)),(int(p.x),int(p.y)))

            for i in __players:
                p = i.pos + __offset
                if -50<=p.x<scr_w and -50<=p.y<scr_h and i.isvisible:
                    screen.blit(i.current_texture,(int(p.x),int(p.y)))

            for i in __entities:
                p = i.pos + __offset
                if -50<=p.x<scr_w and -50<=p.y<scr_h and i.isvisible:
                    screen.blit(i.texture,(int(p.x),int(p.y)))

            for i in __objects:
                if i.toplayer:
                    p=i.pos+__offset
                    if -50<=p.x<scr_w and -50<=p.y<scr_h:
                        screen.blit(i.texture,tuple(p))

            if players[0].chunk_border:
                for i in __chunks:
                    corn=i.get_borders()

                    py.draw.line(screen,(255,0,0),tuple((corn[0]+__offset) // zoom_out),tuple((corn[1]+__offset) // zoom_out))
                    py.draw.line(screen,(255,0,0),tuple((corn[2]+__offset) // zoom_out),tuple((corn[3]+__offset) // zoom_out))
                    py.draw.line(screen,(255,0,0),tuple((corn[0]+__offset) // zoom_out),tuple((corn[2]+__offset) // zoom_out))
                    py.draw.line(screen,(255,0,0),tuple((corn[1]+__offset) // zoom_out),tuple((corn[3]+__offset) // zoom_out))
        else:
            __offset=Vec(scr_w//2,scr_h//2)-players[0].pos+Vec(players[0].current_texture.get_width()//2,players[0].current_texture.get_height()//2)
            for i in __bg_obj:
                p= i.pos+__offset
                if -50<p.x<scr_w and -50<p.y<scr_h:
                    screen.blit(i.texture,tuple(p))
            for i in __objects:
                if (not i.toplayer):
                    p= i.pos+__offset
                    if -50<p.x<scr_w and -50<p.y<scr_h:
                        screen.blit(i.texture,tuple(p))

            if players[0].isvisible:
                p= players[0].pos+__offset
                screen.blit(players[0].current_texture,tuple(p))

            for i in __players:
                p=i.pos+__offset
                if -50<=p.x<scr_w and -50<=p.y<scr_h and i.isvisible:
                    screen.blit(i.current_texture,tuple(p))

            for i in __entities:
                p=i.pos+__offset
                if -50<=p.x<scr_w and -50<=p.y<scr_h and i.isvisible:
                    screen.blit(i.current_texture,tuple(p+i.texture_pos))

            for i in __objects:
                if i.toplayer:
                    p=i.pos+__offset
                    if -50<=p.x<scr_w and -50<=p.y<scr_h:
                        screen.blit(i.texture,tuple(p))
            if show_hitbox:
                for i in __chunks:
                    for k in i.hitboxes:
                        s=py.Surface((k.width,k.height))
                        s.fill((0,255,0))
                        s.set_alpha(50)
                        screen.blit(s,tuple(k.pos+__offset))
                        
            if players[0].chunk_border:
                for i in __chunks:
                    corn=i.get_borders()

                    py.draw.line(screen,(255,0,0),tuple(corn[0]+__offset),tuple(corn[1]+__offset))
                    py.draw.line(screen,(255,0,0),tuple(corn[2]+__offset),tuple(corn[3]+__offset))
                    py.draw.line(screen,(255,0,0),tuple(corn[0]+__offset),tuple(corn[2]+__offset))
                    py.draw.line(screen,(255,0,0),tuple(corn[1]+__offset),tuple(corn[3]+__offset))

    def resolve_collision(self):
        x=(players[0].pos//CHUNK_SIZE).x
        y=(players[0].pos//CHUNK_SIZE).y
        __chunks:list[Chunk]=[]
        __objects:list[Obj]=[]
        __entities:list[Npc]=[]
        __hitboxes:list[Hitbox]=[]
        for i in range(- players[0].render_distance // 2 + 1, players[0].render_distance // 2 + 1):
            __chunks.extend(self.get_Chunk_at(Vec(x+i,y+k)) for k in range(- players[0].render_distance // 2 + 1, players[0].render_distance // 2 + 1))
        for i in __chunks:
            __objects.extend(i.objects)
            __entities.extend(i.entities)
            __hitboxes.extend(i.hitboxes)
        for i in __entities:
            if i.hitbox :
                if players[0].hitbox:
                    hit1=i.hitbox.copy()
                    hit1.pos+=i.pos
                    hit2=players[0].hitbox.copy()
                    hit2.pos+=players[0].pos
                    if hit1.iscolliding(hit2):
                        v=( i.pos-players[0].pos )
                        v=v/v.len()  
                        players[0].pos-=v*2*players[0].speed
                        initial_pos=i.pos
                        i.pos+=v*2*players[0].speed
                        for k in __hitboxes:
                            hit1=i.hitbox.copy()
                            hit1.pos+=i.pos
                            if hit1.iscolliding(k):
                                i.pos=initial_pos

            
    def update(self)->int:
        self.resolve_collision()
        ...
        #TODO : entity with pv<=0 have to die npc.die() 
        #TODO : return a certain value when the players[0] die
worlds:list[World]=[]


from random import randint

def newChunk(pos:Vec,world:World) -> Chunk:
    c=Chunk(pos,world)
    #TODO temporary
    #for i, k in itertools.product(range(20), range(20)):
    #    c.objects.append(Objs["Grass"](i*50+c.top_left_pos.x,k*50+c.top_left_pos.y))
    #c.objects.append(Objs["Pebble"](randint(0,999)+c.top_left_pos.x,randint(0,999)+c.top_left_pos.y))
    #c.objects.append(Objs["Stone"](randint(0,999)+c.top_left_pos.x,randint(0,999)+c.top_left_pos.y))
    return c

def newWorld(name:str,background_color:list[int]=(0,0,0)):
    return World(name,background_color)


def new_bed_room():
    w=newWorld("bed room")
    w.get_Chunk_at(Vec(0,0)).hitboxes.extend([
        Hitbox(HITBOX_RECT_t,Vec(0,0),0,10,8*50),
        Hitbox(HITBOX_RECT_t,Vec(0,0),0,10*50,10),
        Hitbox(HITBOX_RECT_t,Vec(10*50,0),0,10,8*50),
        Hitbox(HITBOX_RECT_t,Vec(0,8*50),0,10*50,10),
        ]
    )
    chun=w.get_Chunk_at(Vec(0,0))
    for x,y in itertools.product(range(10),range(8)):
        chun.background_obj.append(Objs["Wood"](x*50,y*50))
    chun.objects.append(Objs["Bed_head"](8*50,5*50))
    chun.objects.append(Objs["Bed_feet"](8*50,6*50))
    chun.objects.append(Objs["Commode"](6*50,-0.45*50))
    chun.objects.append(Objs["Grogu"](0*50,0*50))
    chun.objects.append(Objs["Stairs"](0,7*50))
    chun=w.get_Chunk_at(Vec(0,-1))
    for i in range(10):
        chun.background_obj.append(Objs["Wall"](i*50+chun.top_left_pos.x,CHUNK_SIZE-50+chun.top_left_pos.y))
    chun.background_obj.append(Objs["Mandalorian_poster"](2*50+chun.top_left_pos.x+5,CHUNK_SIZE-50+chun.top_left_pos.y+2))
    w.add_entity(new_farine())
    return w

def toggle_hitbox():
    global show_hitbox
    show_hitbox = not show_hitbox