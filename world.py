import itertools
import pygame
from objs import *
from entities import *
from objs import *
from math import ceil
from worldlist import*

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

    def tick(self):
        ... # TODO les obj entity ect en dehors du chunk doivent etre deplacer dans le bon chunk
            #  genre si un obj(x,y)  et chunk(x2,y2,w,h)  si not(x2 <= x < x2+w and y2h <=y < y2+h )

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
        self.has_to_collide=False # this check if collisions have to be computed when player moves it is set to True
                                  # will call chunk.tick if true 
    def activate_collision(self):
        self.has_to_collide=True
        
    def add_entity(self,n:Npc)->None:
        """
        add an entity to the world
        if the entity is in a chunk that doesn't exists the chunk will be generated 
        """
        self.get_Chunk_from_pos(n.pos).entities.append(n)
    
    def add_hitbox(self,n:'Hitbox'):
        self.get_Chunk_from_pos(n.pos).hitboxes.append(n)
        
    def add_backgroung_Obj(self,n:'Obj'):
        self.get_Chunk_from_pos(n.pos).background_obj.append(n) 
    
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
    
    def get_Obj(self,pos:Vec) ->Obj:
        x=pos.x//CHUNK_SIZE
        y=pos.y//CHUNK_SIZE
        chunks=[
            self.get_Chunk_at(Vec(x,y)),
            self.get_Chunk_at(Vec(x-1,y)),
            self.get_Chunk_at(Vec(x+1,y)),
            self.get_Chunk_at(Vec(x,y-1)),
            self.get_Chunk_at(Vec(x,y+1)),
            self.get_Chunk_at(Vec(x-1,y-1)),
            self.get_Chunk_at(Vec(x-1,y-1)),
            self.get_Chunk_at(Vec(x-1,y+1)),
            self.get_Chunk_at(Vec(x+1,y-1))
        ]
        # check for pos
        for i in chunks:
            for k in i.objects:
                if k.pos ==pos:
                    return k
        for i in chunks:
            for k in i.objects:
                new_hitbox=k.hitbox.copy()
                new_hitbox.pos+=k.pos
                if collide_rect_dot(new_hitbox,pos):
                    return k
        return Objs["Air"](*tuple(pos))
            
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
        __chunks : list[Chunk] = []
        __objects : list[Obj] = []
        __entities : list[Npc] = []
        __hitboxes : list[Hitbox] = []
        __dyn_obj : list[Dynamic_Obj] = []
        for i in range(- players[0].render_distance // 2 + 1, players[0].render_distance // 2 + 1):
            __chunks.extend(self.get_Chunk_at(Vec(x + i, y + k)) for k in range(- players[0].render_distance // 2 + 1, players[0].render_distance // 2 + 1))
        for i in __chunks:
            __objects.extend(i.objects)
            __entities.extend(i.entities)
            __hitboxes.extend(i.hitboxes)
            __dyn_obj.extend(i.dyn_objects)
        for i in __entities:
            if i.hitbox :
                if players[0].hitbox:
                    hit1 = i.hitbox.copy()
                    hit1.pos += i.pos
                    hit2 = players[0].hitbox.copy()
                    hit2.pos += players[0].pos
                    if hit1.iscolliding(hit2):
                        v = ( i.pos - players[0].pos )
                        v = v / v.len()  
                        players[0].pos -= v * 2 * players[0].speed
                        i.pos += v * 2 * players[0].speed


            
    def update(self) -> int :
        if self.has_to_collide:
            self.resolve_collision()

        chunks : list[Chunk] = []
        for i in range(-players[0].render_distance // 2 + 1, players[0].render_distance // 2 + 1):
            for k in range(-players[0].render_distance // 2 + 1, players[0].render_distance // 2 + 1):
                chunks.append(self.get_Chunk_at(Vec(i, k)))
        
        if self.has_to_collide:
            for i in chunks:
                i.tick()
            
        __objs : list[Obj] = []
        __dyn_objs : list[Dynamic_Obj] = []
        __entities : list[Npc] = []

        p = 0
        while p < len(__entities):
            if __entities[p].pv <= 0:
                if __entities[p].die():
                    __entities.pop(p)
                    continue
            p += 1
        for i in __entities:
            if i.tick:
                i.tick(i, self)
        for i in __dyn_objs:
            i.tick(self)


        self.has_to_collide=False


def newChunk(pos:Vec,world:World) -> Chunk:
    c=Chunk(pos,world)
    return c

def newWorld(name:str,background_color:list[int]=(0,0,0)):
    return World(name,background_color)


def new_bed_room():
    w=newWorld("bed room")
    w.add_hitbox(Hitbox(HITBOX_RECT_t,Vec(0,0),0,10,8*50))
    w.add_hitbox(Hitbox(HITBOX_RECT_t,Vec(0,0),0,10*50,10))
    w.add_hitbox(Hitbox(HITBOX_RECT_t,Vec(10*50,0),0,10,8*50))
    w.add_hitbox(Hitbox(HITBOX_RECT_t,Vec(0,8*50),0,10*50,10))
    
    chun=w.get_Chunk_at(Vec(0,0))
    for x,y in itertools.product(range(10),range(8)):
        w.add_backgroung_Obj(Objs["Wood"](x*50,y*50))
    
    w.add_Obj(Objs["Bed_head"](8*50,5*50))
    w.add_Obj(Objs["Bed_feet"](8*50,6*50))
    w.add_Obj(Objs["Commode"](6*50,0*50))
    w.add_Obj(Objs["Grogu"](0*50,0*50))
    w.add_Obj(Objs["Stairs"](0,7*50))
    chun=w.get_Chunk_at(Vec(0,-1))
    for i in range(10):
        w.add_backgroung_Obj(Objs["Wall"](i*50+chun.top_left_pos.x,CHUNK_SIZE-50+chun.top_left_pos.y))
    w.add_backgroung_Obj(Objs["Mandalorian_poster"](2*50+chun.top_left_pos.x+5,CHUNK_SIZE-50+chun.top_left_pos.y+2))
    return w


def new_house_lvl_0():
    w=newWorld("house_lvl_0")
    

def toggle_hitbox():
    global show_hitbox
    show_hitbox = not show_hitbox
    
def init_worlds():
    Worlds["bed_room"]=new_bed_room()
    

    