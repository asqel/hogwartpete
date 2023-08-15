from uti import *
from objs import *
from interface import *
import world as w
import jsonizer as js
from entities import *
import world as w

class Wood(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["wood"],HITBOX_0x0)

class Wall(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, 1, Textures["Obj"]["wall"],HITBOX_50X50)

class Bed_head(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["bed_0"],HITBOX_50X50)
        
class Bed_feet(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["bed_1"],HITBOX_50X50)

class Mandalorian_poster(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["mandalorian_poster"],HITBOX_50X50)

class Commode(Obj):
    def __init__(self, x: float, y: float):
        super().__init__(self.__class__.__name__,x,y,False,Textures["Obj"]["commode"],Hitbox(HITBOX_RECT_t,Vec(0,0),0,100,50))

class Frigo_up(Obj):
    def __init__(self, x: float, y: float):
        super().__init__(self.__class__.__name__,x,y,False,Textures["Obj"]["frigo_up"],HITBOX_50X50)

class Frigo_down(Obj):
    def __init__(self, x: float, y: float):
        super().__init__(self.__class__.__name__,x,y,False,Textures["Obj"]["frigo_down"],HITBOX_50X50)

class Grogu(Obj):
    def __init__(self, x: float, y: float):
        super().__init__(self.__class__.__name__,x,y,False,Textures["Obj"]["grogu"],Hitbox(HITBOX_RECT_t,Vec(0,0),0,25,25))

class Stairs(Obj):
    def __init__(self, x:float, y:float):
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["stairs"],HITBOX_50X50)

    def on_interact(self, world, user):
        if world.name=="bed room":
            user.world=w.World("rdc",(125, 125, 125))
            user.pos=Vec(50,400)
            user.dir = "r"
            user.update_texture_from_pos()
        else:
            user.world=w.World("bed room",(125, 125, 125))
            user.pos=Vec(50,200)
            user.dir = "r"
            user.update_texture_from_pos()

import random

class Tv(Obj):
    def __init__(self, x:float, y:float):
        self.max_count = 20
        self.count = 0
        self.frame_idx=0
        self.frames=[[Textures["Obj"]["tv"],Textures["Obj"]["tv_2"]][random.randint(0,1)] for i in range(random.randint(3,20))]
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["tv"],HITBOX_50X50)

    def on_draw(self, world,has_been_drawn):
        self.count += 1
        if self.count >= self.max_count:
            self.count=0
            self.frame_idx +=1
            if self.frame_idx >= len(self.frames):
                self.frame_idx=0
            self.texture = self.frames[self.frame_idx]






class Empty_commode(Obj):
    def __init__(self, x:float, y:float):
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["empty_commode"],HITBOX_50X50)


class Wall_left_up(Obj):
    def __init__(self, x:float, y:float):
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["wall_left_up"], Hitbox(HITBOX_RECT_t, Vec(0, 0), 0, 3, 16))
class Wall_left(Obj):
    def __init__(self, x:float, y:float):
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["wall_left"], Hitbox(HITBOX_RECT_t, Vec(0, 0), 0, 3, 16))
class Wall_right_up(Obj):
    def __init__(self, x:float, y:float):
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["wall_right_up"], Hitbox(HITBOX_RECT_t, Vec(13, 0), 0, 3, 16))
class Wall_right(Obj):
    def __init__(self, x:float, y:float):
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["wall_right"], Hitbox(HITBOX_RECT_t, Vec(13, 0), 0, 3, 16))
class Wall_left_down(Obj):
    def __init__(self, x:float, y:float):
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["wall_left_down"], Hitbox(HITBOX_RECT_t, Vec(0, 0), 0, 3, 16))
class Wall_right_down(Obj):
    def __init__(self, x:float, y:float):
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["wall_right_down"], Hitbox(HITBOX_RECT_t, Vec(13, 0), 0, 3, 16))

class House(Obj):
    def __init__(self, x:float, y:float):
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["house"], Hitbox(HITBOX_RECT_t, NULL_VEC, 0, 150, 150))

    def on_interact(self, world, user):
        if user.pos.y >= 150 + self.pos.y:
            user.world = w.World("rdc",(125, 125, 125))
            user.pos = Vec(200, 400)



class Door_frame(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, 1, Textures["Obj"]["door_frame"],HITBOX_50X50)

    def on_interact(self, world, user):
        user.world = w.World("exterior",(0,0,0))
        user.pos = Vec(400, 400)


class plank_void(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, 1, Textures["Obj"]["plank_void"],HITBOX_50X50)


class Pc(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, 0, Textures["Obj"]["pc"],HITBOX_50X50)
    def on_interact(self, world, user):
        if user.pos.y >= self.pos.y + 50:
            user.open_gui("Pc")


class Sign(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, 1, Textures["Obj"]["sign"],HITBOX_50X50, {"gui": ""})

    def on_interact(self, world, user):
        if user.pos.y >= self.pos.y + 50:
            if self.data["gui"] != "":
                user.open_gui(self.data["gui"])




class Clay_statue(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, 0, Textures["Obj"]["clay_statue"],Hitbox(HITBOX_RECT_t, NULL_VEC, 0, 50, 100))

    def on_interact(self, world, user):
        if user.has_item("Resurrection_stone") and user.has_item("Elder_wand") and user.has_item("Cloak_of_invisibility"):
            user.open_gui("game_ended")
        else:
            user.open_gui("Death_statue")
class Bridge_middle(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, 0, Textures["Obj"]["bridge_middle"],HITBOX_50X50)

class Bridge_end(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, 0, Textures["Obj"]["bridge_end"],HITBOX_50X50)

class Bridge_start(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, 0, Textures["Obj"]["bridge_start"],HITBOX_50X50)

class Resurrection_stone_pedestal(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, 0, Textures["Obj"]["resurrection_stone_pedestal"],Hitbox(HITBOX_RECT_t, NULL_VEC, 0, 50, 100), {"used" : False})

    def on_interact(self, world, user):
        if not self.data["used"]:
            if user.add_item(items["Resurrection_stone"](1)):
                self.data["used"] = True
                self.texture = Textures["Obj"]["death_pedestal_50x100"]


class Kitchen_work_station_left_top(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, 1, Textures["Obj"]["kitchen_work_station_top"],HITBOX_50X50)

class Kitchen_work_station_middle_top(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, 1, Textures["Obj"]["kitchen_work_station_top"],HITBOX_50X50)

class Kitchen_work_station_right_top(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, 1, Textures["Obj"]["kitchen_work_station_top"],HITBOX_50X50)

class Kitchen_work_station_left_down(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, 0, Textures["Obj"]["kitchen_work_station_left_down"],HITBOX_0x0)

class Kitchen_work_station_middle_down(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, 0, Textures["Obj"]["kitchen_work_station_middle_down"],HITBOX_0x0)

class Kitchen_work_station_right_down(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, 0, Textures["Obj"]["kitchen_work_station_right_down"],HITBOX_0x0)

class Cavern_floor(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, 1, Textures["Obj"]["cavern_floor"],HITBOX_50X50)


class Cavern_entrance(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, 1, Textures["Obj"]["cavern_entrance"],Hitbox(HITBOX_RECT_t, Vec(0,0), 0, 150, 100))

    def on_interact(self, world, user):
        if user.pos.y >= self.pos.y + 100 and self.pos.x + 75 < user.pos.x < self.pos.x + 125:
            w_ = user.world
            user.world = w.World("cavern",(0,0,0))
            user.world.old_world = w_
            user.pos = Vec(50,50)
            user.world.add_entity(Npcs["Death"](Vec(616,616)))

class Cavern_wall(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, 1, Textures["Obj"]["cavern_wall"],HITBOX_50X50)

registerObj(Wood)
registerObj(Wall)
registerObj(Bed_head)
registerObj(Bed_feet)
registerObj(Mandalorian_poster)
registerObj(Grogu)
registerObj(Commode)
registerObj(Stairs)
registerObj(Tv)
registerObj(Empty_commode)
registerObj(Wall_left_up)
registerObj(Wall_left)
registerObj(Wall_right_up)
registerObj(Wall_right)
registerObj(Wall_left_down)
registerObj(Wall_right_down)
registerObj(Frigo_up)
registerObj(Frigo_down)
registerObj(Door_frame)
registerObj(plank_void)
registerObj(House)
registerObj(Sign)
registerObj(Clay_statue)
registerObj(Bridge_middle)
registerObj(Bridge_start)
registerObj(Bridge_end)
registerObj(Resurrection_stone_pedestal)
registerObj(Pc)
registerObj(Kitchen_work_station_left_top)
registerObj(Kitchen_work_station_middle_top)
registerObj(Kitchen_work_station_right_top)
registerObj(Kitchen_work_station_left_down)
registerObj(Kitchen_work_station_middle_down)
registerObj(Kitchen_work_station_right_down)
registerObj(Cavern_floor)
registerObj(Cavern_entrance)
registerObj(Cavern_wall)


class Cochon_spawner(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, False, Textures["other"]["couchon"],Hitbox(HITBOX_RECT_t,NULL_VEC,0, 100, 100))

    def on_draw(self, world, has_been_drawn):
        if not players[0].is_world_editor:
            world.get_Chunk_from_pos(self.pos).objects.remove(self)
            world.add_entity(Npcs["Couchon"](self.pos))

    
registerObj(Cochon_spawner)
