

from entities import *
from uti import *
import random

class Cat(Npc):
    def __init__(self,pos:Vec) -> None:
        super().__init__(
                        "cat",
                        "cat",
                        FARINE_TEXTURE,
                        None,
                        pos,
                        NULL_VEC,
                        HITBOX_50X50
                        )
        self.ticks_in_same_direction = 0
        self.max_ticks_same_direction = random.randint(0, 2 * 150)
        self.tick_direction = Vec(random.randint(-1,1), random.randint(-1,1))
        self.speed = 0.2
        if self.tick_direction == NULL_VEC:
            self.tick_direction = Vec(1,-1)
        
    def tick(self, world):
        if self.max_ticks_same_direction <= self.ticks_in_same_direction:
            self.ticks_in_same_direction = 0
            self.max_ticks_same_direction = random.randint(0, 4 * 150)
            self.tick_direction = Vec(random.randint(-1,1), random.randint(-1,1))
            if self.tick_direction == NULL_VEC:
                self.tick_direction = Vec(1,-1)
        self.ticks_in_same_direction +=1
        if world.get_Obj(self.pos + self.tick_direction * self.speed).id != "Air":
            self.ticks_in_same_direction +=1
        else:
            self.pos += self.tick_direction * self.speed
                
            


registerNpc(Cat)