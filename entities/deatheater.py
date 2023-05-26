from entities import *
from uti import *

class Death(Npc):
    def __init__(self,pos:Vec) -> None:
        super().__init__(
                        "Death",
                        "Eater",
                        SNAPE_TEXTURE,
                        None,
                        pos,
                        NULL_VEC,
                        HITBOX_50X50
                        )
        
    def go_to_player(self,Player:Character, world):
        v=Player.pos-self.pos
        if v.squareLength()<=10000**2 and v.squareLength()>=150**2:
            if world.get_Obj(self.pos+v*self.speed/150).id=="Air":
                self.pos+=v*self.speed/150
            else:
                self.pos-=v*self.speed/150
    
    def tick(self, world):
        self.go_to_player(players[0], world)
        world.activate_collision()


registerNpc(Death)