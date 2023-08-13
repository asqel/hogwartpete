import itertools
import pygame
from objs import *
from entities import *
from objs import *
from events import *
import json
import jsonizer as js

#in pixel (its a square)
CHUNK_SIZE = 1000
show_hitbox = False

class Chunk:
    def __init__(self, chunk_pos : 'Vec', world : 'World') -> None:
        self.pos : Vec = chunk_pos # pos x,y in World:chuncks
        self.top_left_pos : Vec = chunk_pos * CHUNK_SIZE
        self.world :World = world
        self.entities : list[Npc]=[]
        self.objects : list[Obj]=[]
        self.dyn_objects : list[Dynamic_Obj]=[]
        self.background_obj : list[Obj] = []
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
    def __init__(self, name, background_col : list[int]) -> None:
        self.name = name
        self.bg = background_col
        self.loaded_chunks : dict[tuple[int,int],Chunk]= {} #(x,y) : chunk
        self.has_to_collide = False # this check if collisions have to be computed when player moves it is set to True
                                  # will call chunk.tick if true 

   
    def activate_collision(self):
        """
        set has_to_collide to true 
        when the world tick and has_to_cliide is true then the collision will be called
        """
        self.has_to_collide = True
        
    def add_entity(self, n:Npc)->None:
        """
        add an entity to the world
        if the entity is in a chunk that doesn't exists the chunk will be generated 
        """
        self.get_Chunk_from_pos(n.pos).entities.append(n)
    
    def add_hitbox(self, n:Hitbox):
        self.get_Chunk_from_pos(n.pos).hitboxes.append(n)
        
    def add_background_Obj(self, n:Obj):
        self.get_Chunk_from_pos(n.pos).background_obj.append(n) 
    
    def add_Obj(self, n:Obj)->None:
        """
        add an Obj to the world
        if the Obj is in a chunk that doesn't exists the chunk will be generated 
        """
        self.get_Chunk_from_pos(n.pos).objects.append(n)

    def add_Dyn_Obj(self, n:Dynamic_Obj)->None:
        """
        add an Dyn_Obj to the world
        if the Dyn_Obj is in a chunk that doesn't exists the chunk will be generated 
        """
        self.get_Chunk_from_pos(n.pos).dyn_objects.append(n)
        
    def gen_Chunk_at(self, pos:Vec):
        """
        generate a new chunk at {pos} (pos of chunk)
        if chunk already exist it will be erased
        """
        if tuple(pos) not in self.loaded_chunks.keys():
            self.loaded_chunks[tuple(pos)] = newChunk(pos,self)
        for i in events[Event_on_chunk_generate]:
            i.function(players, self.loaded_chunks[pos.x][pos.y])
        
    def gen_Chunk_from_pos(self, pos:Vec):
        """
        generate a new chunk at {pos} (pos of obj/entity)
        if chunk already exist it will be erased
        """
        return self.gen_Chunk_at(pos//1000)
        
    def get_Chunk_at(self, pos:Vec)->Chunk:
        """
        return the chunk at {pos} (pos of chunk)
        """
        pos = pos.floor()
        if tuple(pos) not in self.loaded_chunks:
            if os.path.exists(f"./worlds/{self.name}/c_{pos.x}_{pos.y}.json"):
                with open(f"./worlds/{self.name}/c_{pos.x}_{pos.y}.json","r") as f:
                    self.loaded_chunks[tuple(pos)] = js.load_chunk(json.load(f), self)
            else:
                self.gen_Chunk_at(pos)
        return self.loaded_chunks[tuple(pos)]

    def get_Chunk_from_pos(self, pos:Vec)->Chunk:
        """
        return the chunk at {pos} (pos of obj/entity)
        """
        return self.get_Chunk_at(pos//1000)
        
    def chunk_exists_at(self, pos:Vec) -> bool:
        """
        return if the chunk at {pos} exists (pos of chunk)
        """
        if tuple(pos) in self.loaded_chunks.keys():
            return True
        if os.path.exists(f"./worlds/{self.name}/c_{pos.x}_{pos.y}.json"):
            return True
        return False 

    def chunk_exists_from_pos(self, pos:Vec) -> bool:
        """
        return if the chunk at {pos} exists (pos of obj/entity)
        """
        return self.chunk_exists_at(pos // CHUNK_SIZE)
    
    def get_Obj(self, pos:Vec) ->Obj:
        """
        return the object at pos or an object that collide with
        a dot at pos 
        if there is not object then object of type air is returned
        """
        x = pos.x // CHUNK_SIZE
        y = pos.y // CHUNK_SIZE
        chunks = [
            self.get_Chunk_at(Vec(x, y)),
            self.get_Chunk_at(Vec(x - 1, y)),
            self.get_Chunk_at(Vec(x + 1, y)),
            self.get_Chunk_at(Vec(x, y - 1)),
            self.get_Chunk_at(Vec(x, y + 1)),
            self.get_Chunk_at(Vec(x - 1, y - 1)),
            self.get_Chunk_at(Vec(x - 1, y - 1)),
            self.get_Chunk_at(Vec(x - 1, y + 1)),
            self.get_Chunk_at(Vec(x + 1, y - 1))
        ]
        # check for pos
        for i in chunks:
            for k in i.objects:
                if k.pos == pos:
                    return k
        
        for i in chunks:
            for k in i.objects:
                new_hitbox = k.hitbox.copy()
                new_hitbox.pos += k.pos
                if collide_rect_dot(new_hitbox, pos):
                    return k
        return Objs["Air"](pos.x, pos.y)

    def remove_entity(self, entity : Npc):
        chunk = self.get_Chunk_from_pos(entity.pos)
        if entity in chunk.entities:
            chunk.entities.remove(entity)
    
    def get_dyn_Obj(self, pos:Vec) ->Dynamic_Obj:
        """
        return the dyn_object at pos or an object that collide with
        a dot at pos 
        if there is not dyn_object then object of type air is returned
        """
        x = pos.x // CHUNK_SIZE
        y = pos.y // CHUNK_SIZE
        chunks = [
            self.get_Chunk_at(Vec(x, y)),
            self.get_Chunk_at(Vec(x - 1, y)),
            self.get_Chunk_at(Vec(x + 1, y)),
            self.get_Chunk_at(Vec(x, y - 1)),
            self.get_Chunk_at(Vec(x, y + 1)),
            self.get_Chunk_at(Vec(x - 1, y - 1)),
            self.get_Chunk_at(Vec(x - 1, y - 1)),
            self.get_Chunk_at(Vec(x - 1, y + 1)),
            self.get_Chunk_at(Vec(x + 1, y - 1))
        ]
        # check for pos
        for i in chunks:
            for k in i.dyn_objects:
                if k.pos == pos:
                    return k
                
        for i in chunks:
            for k in i.dyn_objects:
                new_hitbox = k.hitbox.copy()
                new_hitbox.pos += k.pos
                if collide_rect_dot(new_hitbox, pos):
                    return k
        return Dynamic_Objs["Air"](pos.x, pos.y)
    
    def spawn_item(self, item : Item, pos : Vec):
        i = Npcs["Item_entity"](pos)
        i.item = item
        i.current_texture = item.texture
        self.add_entity(i)

    def show(self, screen:pygame.Surface, zoom_out: int) -> None:
        """
        display everything that has to be rendered on the screen
        """
        __bg_obj : list[Obj] = []
        __objects : list[Obj] = []
        __dyn_obj : list[Dynamic_Obj] = []
        __players : list[Character] = [players[i] for i in range(1,len(players))]#get players except user
        __entities : list[Npc] = []
        __chunks : list[Chunk] = []
        x = (players[0].pos // CHUNK_SIZE).x
        y = (players[0].pos // CHUNK_SIZE).y
        
        scr_w = screen.get_width() * zoom_out
        scr_h = screen.get_height() * zoom_out

        screen.fill(self.bg)

        #get chunks in render distance
        for i in range(-players[0].render_distance // 2 + 1, players[0].render_distance // 2 + 1):
            __chunks.extend(self.get_Chunk_at(Vec(x + i, y + k)) for k in range(-players[0].render_distance // 2 + 1, players[0].render_distance // 2 + 1))

        #get everythings form the chunks
        for i in __chunks:
            __objects.extend(i.objects)
            __dyn_obj.extend(i.dyn_objects)
            __entities.extend(i.entities)
            __bg_obj.extend(i.background_obj)


        __offset = Vec(scr_w // 2, scr_h // 2) - players[0].pos - Vec(players[0].current_texture.get_width() // 2, players[0].current_texture.get_height() // 2)

        #draw background objects
        for i in __bg_obj:
            p = i.pos + __offset
            if -i.texture.get_width() <= p.x < scr_w and -i.texture.get_height() <= p.y < scr_h:
                screen.blit(i.texture,tuple(p))
                i.on_draw(self,True)
            else:
                i.on_draw(self,False)
        
        #draw objects that are not toplayer
        for i in __objects:
            if not i.toplayer:
                p = i.pos + __offset
                if -i.texture.get_width() <= p.x < scr_w and -i.texture.get_height() <= p.y < scr_h:
                    screen.blit(i.texture,tuple(p))
                    i.on_draw(self,True)
                else:
                    i.on_draw(self,False)

        #draw dynamic objects that are not toplayer
        for i in __dyn_obj:
            if not i.toplayer:
                p = i.pos+__offset
                if -i.texture.get_width() <= p.x < scr_w and -i.texture.get_height() <= p.y < scr_h:
                    screen.blit(i.texture,tuple(p))
                    i.on_draw(self,True)
                else:
                    i.on_draw(self,False)

        #draw user
        if players[0].isvisible:
            p = players[0].pos + __offset
            screen.blit(players[0].current_texture, tuple(p))
            players[0].on_draw(self, True)

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

        #draw objects that are toplayer
        for i in __objects:
            if i.toplayer:
                p = i.pos + __offset
                if -i.texture.get_width() <= p.x < scr_w and -i.texture.get_height() <= p.y < scr_h:
                    screen.blit(i.texture,tuple(p))
                    i.on_draw(self,True)
                else:
                    i.on_draw(self,False)

        #draw dynamic objects that are toplayer
        for i in __dyn_obj:
            if i.toplayer:
                p = i.pos + __offset
                if -i.texture.get_width() <= p.x < scr_w and -i.texture.get_height() <= p.y < scr_h:
                    screen.blit(i.texture, tuple(p))
                    i.on_draw(self, True)
                else:
                    i.on_draw(self, False)

        #draw hitboxes if theyre are visible
        if show_hitbox:
            for i in __chunks:
                for k in i.hitboxes:
                    s=py.Surface((k.width, k.height))
                    s.fill((0, 255, 0))
                    s.set_alpha(50)
                    screen.blit(s, tuple(k.pos + __offset))
        
        #draw chunk borders if the player can see them
        if players[0].chunk_border:
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
        for i in range(-players[0].render_distance // 2 + 1, players[0].render_distance // 2 + 1):
            for k in range(-players[0].render_distance // 2 + 1, players[0].render_distance // 2 + 1):
                chunks.append(self.get_Chunk_at((i, k) + players[0].pos // CHUNK_SIZE))
        

        for i in chunks:
            i.tick()
            
        __objs : list[Obj] = []
        __dyn_objs : list[Dynamic_Obj] = []
        __entities : list[Npc] = []

        for i in chunks:
            __objs.extend(i.objects)
            __entities.extend(i.entities)
            __dyn_objs.extend(i.dyn_objects)


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

        for i in __dyn_objs:
            i.tick(self)


        self.has_to_collide=False

        if players[0].pv<=0:
            players[0].gui=guis["Game_over"](players[0])
        for i in players[0].inventaire:
            i.on_inventory_tick(self,players[0])
        for i in range(10):
            if players[0].inventaire[i].quantity <= 0:
                players[0].inventaire[i] = items["Air"](1)
        return 0


def newChunk(pos:Vec,world:World) -> Chunk:
    return Chunk(pos,world)

def newWorld(name:str,background_color:list[int]=(0,0,0)):
    return World(name,background_color)

def toggle_hitbox():
    global show_hitbox
    show_hitbox = not show_hitbox
    

    

    