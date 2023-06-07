import pygame as py
from entities import *
from uti import *
import random
from world import *
import entities as en

class Couchon(Npc):
    def __init__(self,pos:Vec) -> None:
        super().__init__(
                        "couchon",
                        "couchon",
                        [Textures["other"]["couchon"] for i in range(4)],
                        None,
                        pos,
                        NULL_VEC,
                        Hitbox(HITBOX_RECT_t, Vec(0,0), 0, 200, 100)
                        )
            


registerNpc(Couchon)


class Cochon_spawner(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, False, Textures["other"]["couchon"],Hitbox(HITBOX_RECT_t,NULL_VEC,0, 100, 100))

    def on_draw(self, world, has_been_drawn):
        if not players[0].is_world_editor:
            world.get_Chunk_from_pos(self.pos).objects.remove(self)
            world.add_entity(Couchon(self.pos))

    
registerObj(Cochon_spawner)

class Super_moule(Item):
    def __init__(self, quantity) -> None:
        super().__init__(self.__class__.__name__, 1, Textures["other"]["moule"], quantity)
        self.entity = None

    def on_use(self, world, user):
        if not user.gui:
            if user.dir == 'u':
                bullet = en.Npcs["Super_moule_entity"](user.pos + (13,-25))
                bullet.direction = user.dir
                bullet.item = user.inventaire[user.inventaire_idx]
                bullet.sender = user
                user.world.get_Chunk_from_pos(user.pos).entities.append(bullet)
                

            if user.dir == 'r':
                bullet = en.Npcs["Super_moule_entity"](user.pos + (10+50, 13))
                bullet.direction = user.dir
                bullet.item = user.inventaire[user.inventaire_idx]
                bullet.sender = user
                user.world.get_Chunk_from_pos(user.pos).entities.append(bullet)

            if user.dir == 'd':
                bullet = en.Npcs["Super_moule_entity"](user.pos + (13,50+10))
                bullet.sender = user
                bullet.direction = user.dir
                bullet.item = user.inventaire[user.inventaire_idx]
                user.world.get_Chunk_from_pos(user.pos).entities.append(bullet)
                
            if user.dir == 'l':
                bullet = en.Npcs["Super_moule_entity"](user.pos + (-10,13))
                bullet.sender = user
                bullet.direction = user.dir
                bullet.item = user.inventaire[user.inventaire_idx]
                user.world.get_Chunk_from_pos(user.pos).entities.append(bullet)



registerItem(Super_moule)

class Super_moule_entity(Npc):
    def __init__(self,pos:Vec) -> None:
        super().__init__(
                        "bullet",
                        "bullet",
                        [Textures["other"]["moule"] for i in range(4)],
                        None,
                        pos,
                        NULL_VEC,
                        Hitbox(HITBOX_RECT_t, Vec(0,0), 0, 25, 25)
                        )
        self.direction = "u"
        self.duration = 0
        self.max_duration = 150*3
        self.speed *= 4
        self.sender = None
        self.item = None
        
    def tick(self, world :World ):
        self.duration += 1

        if self.duration >= self.max_duration:
            world.remove_entity(self)
            self.item.quantity = 0
            return 0

        if self.direction == "u":
            self.pos += Vec(0,-1)*self.speed
        elif self.direction == "d":
            self.pos += Vec(0,1)*self.speed
        elif self.direction == "r":
            self.pos += Vec(1,0)*self.speed
        elif self.direction == "l":
            self.pos += Vec(-1,0)*self.speed   
            
        if world.get_Obj(self.pos).id != "Air":
            if self.item.entity:
                self.item.entity.pos = self.pos
                self.item.entity.pv =100
                world.add_entity(self.item.entity)
                self.item.entity = None
                world.remove_entity(self)
            else:
                world.remove_entity(self)
                self.item.quantity = 0
            return 0

        entities : list[Npc] = []
        for i in range(-1, 2):
            for k in range(-1, 2):
                entities.extend(world.get_Chunk_at((self.pos // CHUNK_SIZE) + (i, k)).entities)
        
        if self.duration >= 150:
            if self.item.entity:
                self.item.entity.pos = self.pos
                self.item.entity.pv = 100

                world.add_entity(self.item.entity)
                self.item.entity = None
                world.remove_entity(self)
                return 




        if self.item.entity is None:
            hit1 = self.hitbox.copy()
            hit1.pos += self.pos
            for i in entities:
                if i.hitbox and i != self and i != self.sender:
                    hit2 = i.hitbox.copy()
                    hit2.pos += i.pos
                    if hit1.iscolliding(hit2):
                        self.item.entity = i
                        world.remove_entity(i)
                        world.remove_entity(self)
                        return 


registerNpc(Super_moule_entity)


class Fisherman(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, False, Textures["other"]["fisherman"],Hitbox(HITBOX_RECT_t,NULL_VEC,0, 100, 100))

    def on_interact(self, world, user):
        user.open_gui("Fisherman_shop")

registerObj(Fisherman)


class Fisherman_shop(Gui):
    def __init__(self, player) -> None:
        super().__init__("Escape_gui", {}, player)
        self.idx = 0
        self.max_idx = 1

    def tick(self, events: list[Event]):
         for i in events:
            if i.type == py.KEYDOWN:
                if i.key == py.K_UP :
                    self.idx -= 1
                    if self.idx < 0: 
                        self.idx = self.max_idx
                        
                if i.key == py.K_DOWN :
                    self.idx += 1
                    if self.idx > self.max_idx: 
                        self.idx = 0
                
                if i.key == py.K_e:
                    if self.idx == 0:
                        if self.player.money >= 1:
                            if self.player.add_item(items["Super_moule"](1)):
                                self.player.money -= 1
                    elif self.idx == 1:
                        self.player.close_gui()
    
    def draw(self, screen):
        x = (screen.get_width() - Textures["other"]["text_box"].get_width())/2
        y = screen.get_height() -Textures["other"]["text_box"].get_height() - 20 
        screen.blit(Textures["other"]["text_box"],(x,y))
        screen.blit(mc_font.render("Edward Findus", 0, (0,0,0)), (x,y+30-15-30-5))
        screen.blit(mc_font.render("Hey matelot ! La pêche ?", 0, (0,0,0)), (x+30,y+30-15))
        screen.blit(mc_font.render("Tu viens pour mes moules ?",0,(0,0,0)), (x+30,y+60-15))
        screen.blit(mc_font.render("    Super moule        1€",0,(0,255,0)if self.idx == 0 and self.player.money >=1 else((255,0,0)if self.idx == 0 else (0,0,0))), (x+30,y+90-15))                    
        screen.blit(mc_font.render("            exit",0,(0,255,0)if self.idx == 1 else (0,0,0)), (x+30,y+90-15+30))                    

        screen.blit(Textures["other"]["moule"], (x+30,y+90-15))

registerGui(Fisherman_shop)