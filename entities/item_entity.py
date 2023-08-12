from entities import *
from uti import *
import random
from world import *
from items import *

class Item_entity(Npc):
    def __init__(self,pos:Vec) -> None:
        super().__init__(
                        "Item_entity",
                        "Item_entity",
                        [NOTHING_TEXTURE for i in range(4)],
                        None,
                        pos,
                        NULL_VEC,
                        Hitbox(HITBOX_RECT_t, Vec(0,0), 0, 30, 30)
                        )
        self.item = items["Air"](1)
        self.pv = float("inf")
        self.moving = "u"
        self.collide_player = False
        self.pick_up = 150
        
    def tick(self, world :World ):
        if world.get_Obj(self.pos + (15, 15)).id != "Air":
            self.pos += (players[0].pos - self.pos).normalize()*50
        if self.pick_up > 0:
            self.pick_up -= 1
            
        if self.texture_pos.y >= 10:
            self.moving = "u"
        if self.texture_pos.y <= -10:
            self.moving = "d"
            
        if self.moving == "u":
            self.texture_pos -= (0,0.1)
        elif self.moving == "d":
            self.texture_pos += (0,0.1)
        if not self.pick_up:
            hit1 = self.hitbox.copy()
            hit1.pos += self.pos
            for i in players:
                hit2 = i.hitbox.copy()
                hit2.pos += i.pos
                if hit1.iscolliding(hit2):
                    if i.add_item(self.item):
                        self.pv = 0
                        i.world.remove_entity(self)
                        return 0
        
        
        
                
            


registerNpc(Item_entity)