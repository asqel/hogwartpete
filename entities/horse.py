import entities
from uti.vector import *
from uti.textures import *
from uti.hitbox import *
from math import *
from random import *

class Horse(entities.Npc):
    def __init__(self,pos:Vec) -> None:
        super().__init__(
                        "Horse",
                        "Horse",
                        [
                            Textures["other"]["horse1"],
                            Textures["other"]["horse2"],
                            Textures["other"]["horse3"],
                            Textures["other"]["horse4"],
                        ],
                        None,
                        pos,
                        NULL_VEC,
                        HITBOX_50X50
                        )
        self.dir="d"
        self.data = {"next" : "l"}
        self.current_texture = self.texture[0]
        self.rider_offset = Vec(0,40)

    def mov(self, world, rider, dir: str):
        if dir == "l":
            if self.data["next"] == "l":
                self.data["next"] = "r"
                self.next_texture()
                self.pos += Vec(15,0)
        elif dir == "r":
            if self.data["next"] == "r":
                self.data["next"] = "l"
                self.next_texture()
                self.pos += Vec(15,0)
    def tick(self, world):
        self.rider.data["horse_race_tick"] += 1
        if self.rider:
            self.rider.dir = "r"
            self.rider.update_texture_from_pos()

        if -3250 - 50 < self.pos.y < -3250 + 50 and self.pos.x > 2100:
            self.rider.riding = None
            if self.rider.has_quest_incompleted("horse_race_won"):
                #i = items["Spatula"](1)
                #if not self.rider.add_item(i):
                #    self.world.spawn_item(i, self.pos)
                self.rider.get_quest("horse_race_won").pourcentage = 100
                self.rider.complete_quest("horse_race_won")

    def next_texture(self):
        if self.current_texture == self.texture[0]:
            self.current_texture = self.texture[1]
        elif self.current_texture == self.texture[1]:
            self.current_texture = self.texture[2]
        elif self.current_texture == self.texture[2]:
            self.current_texture = self.texture[3]
        elif self.current_texture == self.texture[3]:
            self.current_texture = self.texture[0]

    
entities.registerNpc(Horse)