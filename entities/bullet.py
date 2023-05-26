from entities import *
from uti import *
import random
from world import *

class Bullet(Npc):
    def __init__(self,pos:Vec) -> None:
        super().__init__(
                        "bullet",
                        "bullet",
                        [Textures["Spells"]["spell_0"] for i in range(4)],
                        None,
                        pos,
                        NULL_VEC,
                        Hitbox(HITBOX_RECT_t, Vec(0,0), 0, 25, 25)
                        )
        self.direction = "u"
        self.duration = 0
        self.max_duration = 150*3
        self.speed *= 3.5
        
    def tick(self, world :World ):
        self.duration += 1
        if self.duration >= self.max_duration:
            self.pv = 0
        if self.direction == "u":
            self.pos += Vec(0,-1)*self.speed
        elif self.direction == "d":
            self.pos += Vec(0,1)*self.speed
        elif self.direction == "r":
            self.pos += Vec(1,0)*self.speed
        elif self.direction == "l":
            self.pos += Vec(-1,0)*self.speed   
            
        if world.get_Obj(self.pos).id != "Air":
            self.pv = 0
        entities : list[Npc] = []
        for i in range(-1, 2):
            for k in range(-1, 2):
                entities.extend(world.get_Chunk_at(self.pos // CHUNK_SIZE + (i, k)).entities)
        
        hit1 = self.hitbox.copy()
        hit1.pos += self.pos
        for i in entities:
            if i.hitbox and i != self:
                hit2 = i.hitbox.copy()
                hit2.pos += i.pos
                if (hit1.iscolliding(hit2)):
                    i.pv = 0
                    self.pv = 0
                    break
            
                
            


registerNpc(Bullet)