
from entities import *
from uti import *

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