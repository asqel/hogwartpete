from uti import *
from entities import *
from world import *

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