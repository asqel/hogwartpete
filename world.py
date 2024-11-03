import itertools
import pygame as py
import objs
import events
import entities
import json
import jsonizer

import os

from uti.textures import *
from uti.hitbox import *
from uti.vector import *

#in pixel (its a square)
CHUNK_SIZE = 1000
show_hitbox = False

import entities as en

class Chunk:
    def __init__(self, chunk_pos : 'Vec', world : 'World') -> None:
        self.pos : Vec = chunk_pos # pos x,y in World:chuncks
        self.top_left_pos : Vec = chunk_pos * CHUNK_SIZE
        self.world : World = world
        self.entities : list[entities.Npc]=[]
        self.objects : list[list[objs.Obj]]=[[None for i in range(20)] for k in range(20)]
        self.dyn_objects : list[list[objs.Obj]]=[[None for i in range(20)] for k in range(20)]
        self.background_obj : list[list[objs.Obj]]=[[None for i in range(20)] for k in range(20)]
        self.hitboxes : list[Hitbox] = []

    def get_borders(self)->list['Vec']:
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
        """
        check if entities or objects are outside the chunk but still registered in chunk
        if so then they will be moved to the right chunk
        """
        p = 0
        while p < len(self.entities):
            new_pos = self.entities[p].pos// CHUNK_SIZE
            if new_pos != self.pos:
                self.world.get_Chunk_at(new_pos).entities.append(self.entities.pop(p))
                continue
            p += 1
        
        #new_chunk_pos = Vec(0,0)
        #while p < len(self.objects):
        #    if self.objects[p].pos.x < corners[0].x:
        #        new_chunk_pos += (-1, 0)
        #    elif self.objects[p].pos.x > corners[3].x:
        #        new_chunk_pos += (1, 0)
#
        #    if self.objects[p].pos.y < corners[0].y:
        #        new_chunk_pos += (0, -1)
        #    elif self.objects[p].pos.y > corners[3].y:
        #        new_chunk_pos += (0, 1)
#
        #    if new_chunk_pos != (0,0):
        #        self.world.add_entity(self.objects.pop(p))
        #        p -= 1
        #    p += 1
        #
        #new_chunk_pos = Vec(0,0)
        #while p < len(self.background_obj):
        #    if self.background_obj[p].pos.x < corners[0].x:
        #        new_chunk_pos += (-1, 0)
        #    elif self.background_obj[p].pos.x > corners[3].x:
        #        new_chunk_pos += (1, 0)
#
        #    if self.background_obj[p].pos.y < corners[0].y:
        #        new_chunk_pos += (0, -1)
        #    elif self.background_obj[p].pos.y > corners[3].y:
        #        new_chunk_pos += (0, 1)
#
        #    if new_chunk_pos != (0,0):
        #        self.world.add_entity(self.background_obj.pop(p))
        #        p -= 1
        #    p += 1
#
        #new_chunk_pos = Vec(0,0)
        #while p < len(self.dyn_objects):
        #    if self.dyn_objects[p].pos.x < corners[0].x:
        #        new_chunk_pos += (-1, 0)
        #    elif self.dyn_objects[p].pos.x > corners[3].x:
        #        new_chunk_pos += (1, 0)
#
        #    if self.dyn_objects[p].pos.y < corners[0].y:
        #        new_chunk_pos += (0, -1)
        #    elif self.dyn_objects[p].pos.y > corners[3].y:
        #        new_chunk_pos += (0, 1)
#
        #    if new_chunk_pos != (0,0):
        #        self.world.add_entity(self.dyn_objects.pop(p))
        #        p -= 1
        #    p += 1
        
            


class World:
    """
    difference between function called ...at and ...from_pos:
        ...at : pos in the chunks dictionary of the world like chunk.pos
        ...from_pos : pos of an entity or player or an object
    
    """
    def __init__(self, name, background_col : list[int], mod = "", is_outside = False) -> None:
        self.name = name
        self.bg = background_col
        self.mod = mod
        self.loaded_chunks : dict[tuple[int,int],Chunk]= {} #(x,y) : chunk
        self.has_to_collide = False # this check if collisions have to be computed when player moves it is set to True
                                  # will call chunk.tick if true 
        self.is_outside = is_outside

    def activate_collision(self):
        """
        set has_to_collide to true 
        when the world tick and has_to_cliide is true then the collision will be called
        """
        self.has_to_collide = True

    def add_entity(self, n: 'entities.Npc') -> None:
        self.get_Chunk_from_pos(n.pos).entities.append(n)
    
    def add_hitbox(self, n: Hitbox):
        self.get_Chunk_from_pos(n.pos).hitboxes.append(n)
        
    def add_background_Obj(self, n: objs.Obj) -> None:
        c = self.get_Chunk_from_pos(n.pos)
        c.background_obj[int((n.pos.y - c.top_left_pos.y) // 50)][int((n.pos.x - c.top_left_pos.x) // 50)] = n
    
    def add_Obj(self, n: objs.Obj) -> None:
        c = self.get_Chunk_from_pos(n.pos)
        c.objects[int((n.pos.y - c.top_left_pos.y) // 50)][int((n.pos.x - c.top_left_pos.x) // 50)] = n

    def add_Dyn_Obj(self, n: objs.Obj) -> None:
        c = self.get_Chunk_from_pos(n.pos)
        c.dyn_objects[int((n.pos.y - c.top_left_pos.y) // 50)][int((n.pos.x - c.top_left_pos.x) // 50)] = n
        
    def gen_Chunk_at(self, pos:Vec) -> None:
        """
        generate a new chunk at {pos} (pos of chunk)
        if chunk already exist it will be erased
        """
        if tuple(pos) not in self.loaded_chunks.keys():
            self.loaded_chunks[tuple(pos)] = newChunk(pos,self)
        for i in events.events[events.Event_on_chunk_generate]:
            i.function(entities.players, self.loaded_chunks[pos.x][pos.y])
        
    def gen_Chunk_from_pos(self, pos:Vec) -> None:
        """
        generate a new chunk at {pos} (pos of obj/entity)
        if chunk already exist it will be erased
        """
        return self.gen_Chunk_at(pos//1000)
        
    def get_Chunk_at(self, pos: Vec) -> Chunk:
        """
        return the chunk at {pos} (pos of chunk)
        """
        pos = pos.floor()
        pos_as_tuple = tuple(pos)
        if pos_as_tuple not in self.loaded_chunks:
            if self.mod == "":
                if os.path.exists(f"./worlds/{self.name}/c_{pos.x}_{pos.y}.json"):
                    with open(f"./worlds/{self.name}/c_{pos.x}_{pos.y}.json","r") as f:
                        self.loaded_chunks[pos_as_tuple] = jsonizer.load_chunk(json.load(f), self)
                else:
                    self.gen_Chunk_at(pos)
            else:
                if os.path.exists(f"./mods/{self.mod}/worlds/{self.name}/c_{pos.x}_{pos.y}.json"):
                    with open(f"./mods/{self.mod}/worlds/{self.name}/c_{pos.x}_{pos.y}.json","r") as f:
                        self.loaded_chunks[pos_as_tuple] = jsonizer.load_chunk(json.load(f), self)
                else:
                    self.gen_Chunk_at(pos)
        return self.loaded_chunks[pos_as_tuple]

    def get_Chunk_from_pos(self, pos: Vec) -> Chunk:
        """
        return the chunk at {pos} (pos of obj/entity)
        """
        return self.get_Chunk_at(pos//1000)
        
    def chunk_exists_at(self, pos: Vec) -> bool:
        """
        return if the chunk at {pos} exists (pos of chunk)
        """
        if tuple(pos) in self.loaded_chunks.keys():
            return True
        if self.mod == "":
            return os.path.exists(f"./worlds/{self.name}/c_{pos.x}_{pos.y}.json")
        else:
            return os.path.exists(f"./mods/{self.mod}/worlds/{self.name}/c_{pos.x}_{pos.y}.json")
        return False 

    def chunk_exists_from_pos(self, pos: Vec) -> bool:
        """
        return if the chunk at {pos} exists (pos of obj/entity)
        """
        return self.chunk_exists_at(pos // CHUNK_SIZE)
    
    def get_Obj(self, pos: Vec) -> 'objs.Obj':
        c = self.get_Chunk_from_pos(pos)
        obj = c.objects[int((pos.y - c.top_left_pos.y) // 50)][int((pos.x - c.top_left_pos.x) // 50)]
        if obj is not None:
            return obj
        return objs.Objs["Air"](pos.x, pos.y)
    
    def get_background_Obj(self, pos:Vec) -> objs.Obj:
        c = self.get_Chunk_from_pos(pos)
        obj = c.background_obj[int((pos.y - c.top_left_pos.y) // 50)][int((pos.x - c.top_left_pos.x) // 50)]
        if obj is not None:
            return obj
        return objs.Objs["Air"](pos.x, pos.y)

    def remove_entity(self, entity : 'entities.Npc'):
        chunk = self.get_Chunk_from_pos(entity.pos)
        if entity in chunk.entities:
            chunk.entities.remove(entity)

    def remove_background_obj_at(self, pos: Vec):
        c = self.get_Chunk_from_pos(pos)
        c.background_obj[int((pos.y - c.top_left_pos.y) // 50)][int((pos.x - c.top_left_pos.x) // 50)] = None
    
    def remove_obj_at(self, pos: Vec):
        c = self.get_Chunk_from_pos(pos)
        c.objects[int((pos.y - c.top_left_pos.y) // 50)][int((pos.x - c.top_left_pos.x) // 50)] = None
  
    def remove_dyn_obj_at(self, pos: Vec):
        c = self.get_Chunk_from_pos(pos)
        c.dyn_objects[int((pos.y - c.top_left_pos.y) // 50)][int((pos.x - c.top_left_pos.x) // 50)] = None

    def get_dyn_Obj(self, pos:Vec) -> 'objs.Dynamic_Obj':
        c = self.get_Chunk_from_pos(pos)
        obj = c.dyn_objects[int((pos.y - c.top_left_pos.y) // 50)][int((pos.x - c.top_left_pos.x) // 50)]
        if obj is not None:
            return obj
        return objs.Objs["Air"](pos.x, pos.y)
    
    def on_load(self):
        for i in events.events[events.Event_on_world_load]:
            i.function(entities.players, self)

    def show(self, screen : py.Surface, zoom_out: int) -> None:
        """
        display everything that has to be rendered on the screen
        """
        __bg_obj : list[objs.Obj] = []
        __objects : list[objs.Obj] = []
        __dyn_obj : list[objs.Obj] = []
        __players : list[entities.Character] = [entities.players[i] for i in range(1,len(entities.players))]#get players except user
        __entities : list[entities.Npc] = []
        __chunks : list[Chunk] = []
        x = (entities.players[0].pos // CHUNK_SIZE).x
        y = (entities.players[0].pos // CHUNK_SIZE).y
        
        scr_w = screen.get_width() * zoom_out
        scr_h = screen.get_height() * zoom_out
        new_texture = get_time_layout(entities.players[0].tick_count, self.is_outside)

        screen.fill(self.bg)

        #get chunks in render distance
        for i in range(-entities.players[0].render_distance // 2 + 1, entities.players[0].render_distance // 2 + 1):
            __chunks.extend(self.get_Chunk_at(Vec(x + i, y + k)) for k in range(-entities.players[0].render_distance // 2 + 1, entities.players[0].render_distance // 2 + 1))

        #get everythings form the chunks
        for i in __chunks:
            __entities.extend(i.entities)
            for k in range(20):
                __objects.extend(i.objects[k])
                __dyn_obj.extend(i.dyn_objects[k])
                __bg_obj.extend(i.background_obj[k])


        __offset = Vec(scr_w // 2, scr_h // 2) - entities.players[0].pos - Vec(entities.players[0].current_texture.get_width() // 2, entities.players[0].current_texture.get_height() // 2)

        #draw background objects
        for i in __bg_obj:
            if i is None:
                continue
            p = i.pos + __offset
            if -i.texture.get_width() <= p.x < scr_w and -i.texture.get_height() <= p.y < scr_h:
                screen.blit(i.texture,tuple(p))
                i.on_draw(self,True)
            else:
                i.on_draw(self,False)
        
        #draw objects that are not toplayer
        for i in __objects:
            if i is None:
                continue
            p = i.pos + __offset
            if -i.texture.get_width() <= p.x < scr_w and -i.texture.get_height() <= p.y < scr_h:
                screen.blit(i.texture,tuple(p))
                i.on_draw(self,True)
            else:
                i.on_draw(self,False)
            if i.light:
                p = i.light.pos + __offset + i.pos
                if -i.light.texture.get_width() <= p.x < scr_w and -i.light.texture.get_height() <= p.y < scr_h:
                    new_texture.blit(i.light.texture,tuple(p))

        #draw user
        if entities.players[0].isvisible:
            if not entities.players[0].riding:
                p = entities.players[0].pos + __offset
                screen.blit(entities.players[0].current_texture, tuple(p))
                entities.players[0].on_draw(self, True)
            else:
                p = entities.players[0].pos + __offset

                screen.blit(entities.players[0].riding.current_texture, tuple(p))
                screen.blit(entities.players[0].current_texture, tuple(p + entities.players[0].riding.rider_offset + (entities.players[0].riding.current_texture.get_width()//2 - entities.players[0].current_texture.get_width()//2 ,-entities.players[0].current_texture.get_height())))

        #draw other players
        for i in __players:
            p = i.pos + __offset
            if -i.current_texture.get_width() <= p.x < scr_w and -i.current_texture.get_height() <= p.y < scr_h:
                screen.blit(i.current_texture, tuple(p))
                i.on_draw(self, True)
            else:
                i.on_draw(self, False)

        #draw entities
        for i in __entities:
            p = i.pos + __offset
            if -i.current_texture.get_width() <= p.x < scr_w and -i.current_texture.get_height() <= p.y < scr_h:
                screen.blit(i.current_texture, tuple(p + i.texture_pos))
                i.on_draw(self, True)
            else:
                i.on_draw(self, False)

        for i in __dyn_obj:
            if i is None:
                continue
            p = i.pos + __offset
            if -i.texture.get_width() <= p.x < scr_w and -i.texture.get_height() <= p.y < scr_h:
                screen.blit(i.texture,tuple(p))
                i.on_draw(self,True)
            else:
                i.on_draw(self,False)
            if i.light:
                p = i.light.pos + __offset + i.pos
                if -i.light.texture.get_width() <= p.x < scr_w and -i.light.texture.get_height() <= p.y < scr_h:
                    new_texture.blit(i.light.texture,tuple(p))
        
        screen.blit(new_texture, (0,0))

        #draw hitboxes if theyre are visible
        if show_hitbox:
            for i in __chunks:
                for k in i.hitboxes:
                    s = py.Surface((k.width, k.height))
                    s.fill((0, 255, 0))
                    s.set_alpha(50)
                    screen.blit(s, tuple(k.pos + __offset))
        
        #draw chunk borders if the player can see them
        if entities.players[0].chunk_border:
            for i in __chunks:
                corn=i.get_borders()

                py.draw.line(screen, (255, 0, 0), tuple(corn[0] + __offset), tuple(corn[1] + __offset))
                py.draw.line(screen, (255, 0, 0), tuple(corn[2] + __offset), tuple(corn[3] + __offset))
                py.draw.line(screen, (255, 0, 0), tuple(corn[0] + __offset), tuple(corn[2] + __offset))
                py.draw.line(screen, (255, 0, 0), tuple(corn[1] + __offset), tuple(corn[3] + __offset))
    def update(self) -> int :
        """
        called each game tick so ~150 times a second
        if world.has_to_collide is set to true the collision will be computed
        and has_to_collide will be set to false
        
        if the player is dead(pv <=0) the function will return 1
        """
        

        chunks : list[Chunk] = []
        distance = entities.players[0].render_distance // 2 + 1
        chunk_pos = entities.players[0].pos // CHUNK_SIZE
        for i in range(-distance + 1, distance):
            for k in range(-distance + 1, distance):
                chunks.append(self.get_Chunk_at((i, k) + chunk_pos))
        

        for i in chunks:
            i.tick()
            
        __dyn_objs : list[objs.Obj] = []
        __entities : list[entities.Npc] = []

        for i in chunks:
            __entities.extend(i.entities)
            for k in range(20):
                __dyn_objs.extend(i.dyn_objects[k])


        p = 0
        while p < len(__entities):
            if __entities[p].pv <= 0:
                if __entities[p].die(self):
                    self.remove_entity(__entities[p])
                    __entities.pop(p)
                    continue
            p += 1
    
        for i in __entities:
            if i.tick:
                i.tick(self)
        if entities.players[0].riding:
            entities.players[0].riding.tick(self)

        for i in __dyn_objs:
            if i is not None and i.does_tick:
                i.tick(self)


        self.has_to_collide=False
        if entities.players[0].riding:
            entities.players[0].pos = entities.players[0].riding.pos
            entities.players[0].riding.world = entities.players[0].world
        if entities.players[0].pv <= 0:
            ...
        return 0


def newChunk(pos:Vec,world:World) -> Chunk:
    return Chunk(pos,world)

def newWorld(name:str,background_color:list[int]=(0,0,0)):
    return World(name,background_color)

def toggle_hitbox():
    global show_hitbox
    show_hitbox = not show_hitbox
    
def get_time_layout(tick : int, outside : bool):
    if not outside or tick <= 54000 or tick >= 108000:
        return NOTHING_TEXTURE_1024_576.copy()
    if tick > 54000 and tick < 64000:
        new_texture = Textures["other"]["night_layout"].copy()
        new_texture.set_alpha(int(25.5 * tick / 1000 - 1377))
    elif tick >= 64000 and tick <= 98000:
        new_texture = Textures["other"]["night_layout"].copy()
    elif tick > 98000:
        new_texture = Textures["other"]["night_layout"].copy()
        new_texture.set_alpha(int(-25.5 * tick / 1000 + 2754))
    else:
        new_texture = NOTHING_TEXTURE_1024_576.copy()
    return new_texture