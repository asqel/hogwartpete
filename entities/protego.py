import entities
from uti.vector import *
from uti.hitbox import *
from uti.textures import *
import random
import world

class Protego(entities.Npc):
    def __init__(self, pos:Vec) -> None:
        super().__init__(
                        "protego",
                        "protego",
                        [Textures["Spells"][f"protego_{i}"] for i in "urdl"],
                        None,
                        pos,
                        NULL_VEC,
                        Hitbox(HITBOX_RECT_t, Vec(0,0), 0, 25, 25)
                        )
        self.x = self.pos.x
        self.y = self.pos.y
        self.duration = 0
        self.pv = 1
        self.max_duration = 150/2
        self.sender = None
        self.collide_player = False
        
    def tick(self, world : world.World ):
        self.pos = Vec(self.x, self.y)
        if self.dir == "u":
            self.current_texture = self.texture[0]
        elif self.dir == "r":
            self.current_texture = self.texture[1]
        elif self.dir == "d":
            self.current_texture = self.texture[2]
        elif self.dir == "l":
            self.current_texture = self.texture[3]
            
        self.duration += 1

        if self.duration >= self.max_duration:
            self.pv = 0
            return 0
        
        
        
                
            


entities.registerNpc(Protego)