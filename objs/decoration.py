from uti.vector import *
from uti.hitbox import *
from uti.textures import *
import objs
import interface
import entities
import world
import jsonizer

class Wood(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["wood"],HITBOX_0x0)

class Wall(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["wall"],HITBOX_50X50)

class Bed_head(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["bed_0"],HITBOX_50X50)
        
class Bed_feet(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["bed_1"],HITBOX_50X50)

class Mandalorian_poster(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["mandalorian_poster"],HITBOX_50X50)

class Commode(objs.Obj):
    def __init__(self, x: float, y: float):
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["commode"],Hitbox(HITBOX_RECT_t,Vec(0,0),0,100,50))

class Frigo_up(objs.Obj):
    def __init__(self, x: float, y: float):
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["frigo_up"],HITBOX_50X50)

class Frigo_down(objs.Obj):
    def __init__(self, x: float, y: float):
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["frigo_down"],HITBOX_50X50)

class Grogu(objs.Obj):
    def __init__(self, x: float, y: float):
        super().__init__(self.__class__.__name__,x,y,Textures["Obj"]["grogu"],Hitbox(HITBOX_RECT_t,Vec(0,0),0,25,25))

class Stairs(objs.Obj):
    def __init__(self, x:float, y:float):
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["stairs"],HITBOX_50X50)

    def on_interact(self, _world, user):
        if world.name=="bed room":
            user.world = world.World("rdc",(125, 125, 125))
            user.pos = Vec(50,400)
            user.dir = "r"
            user.update_texture_from_pos()
        else:
            user.world = world.World("bed room",(125, 125, 125))
            user.pos=Vec(50,200)
            user.dir = "r"
            user.update_texture_from_pos()

import random

class Tv(objs.Obj):
    def __init__(self, x:float, y:float):
        self.max_count = 20
        self.count = 0
        self.frame_idx=0
        self.frames=[[Textures["Obj"]["tv"],Textures["Obj"]["tv_2"]][random.randint(0,1)] for i in range(random.randint(3,20))]
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["tv"],HITBOX_50X50)

    def on_draw(self, world,has_been_drawn):
        self.count += 1
        if self.count >= self.max_count:
            self.count=0
            self.frame_idx +=1
            if self.frame_idx >= len(self.frames):
                self.frame_idx=0
            self.texture = self.frames[self.frame_idx]






class Empty_commode(objs.Obj):
    def __init__(self, x:float, y:float):
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["empty_commode"],HITBOX_50X50)


class Wall_left_up(objs.Obj):
    def __init__(self, x:float, y:float):
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["wall_left_up"], Hitbox(HITBOX_RECT_t, Vec(0, 0), 0, 3, 16))
class Wall_left(objs.Obj):
    def __init__(self, x:float, y:float):
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["wall_left"], Hitbox(HITBOX_RECT_t, Vec(0, 0), 0, 3, 16))
class Wall_right_up(objs.Obj):
    def __init__(self, x:float, y:float):
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["wall_right_up"], Hitbox(HITBOX_RECT_t, Vec(13, 0), 0, 3, 16))
class Wall_right(objs.Obj):
    def __init__(self, x:float, y:float):
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["wall_right"], Hitbox(HITBOX_RECT_t, Vec(13, 0), 0, 3, 16))
class Wall_left_down(objs.Obj):
    def __init__(self, x:float, y:float):
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["wall_left_down"], Hitbox(HITBOX_RECT_t, Vec(0, 0), 0, 3, 16))
class Wall_right_down(objs.Obj):
    def __init__(self, x:float, y:float):
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["wall_right_down"], Hitbox(HITBOX_RECT_t, Vec(13, 0), 0, 3, 16))

class House(objs.Obj):
    def __init__(self, x:float, y:float):
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["house"], Hitbox(HITBOX_RECT_t, NULL_VEC, 0, 150, 150))

    def on_interact(self, _world, user):
        if user.pos.y >= 150 + self.pos.y:
            user.world = world.World("rdc",(125, 125, 125))
            user.pos = Vec(200, 400)



class Door_frame(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["door_frame"],HITBOX_50X50)

    def on_interact(self, _world, user):
        user.world = world.World("exterior",(0,0,0),is_outside = True)
        user.world.on_load()
        user.pos = Vec(400, 400)


class plank_void(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["plank_void"],HITBOX_50X50)


class Pc(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["pc"],HITBOX_50X50)
    def on_interact(self, world, user):
        if user.pos.y >= self.pos.y + 50:
            user.open_gui("Pc")


class Sign(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["sign"],HITBOX_50X50, {"gui": ""})

    def on_interact(self, world, user):
        if user.pos.y >= self.pos.y + 50:
            if self.data["gui"] != "":
                user.open_gui(self.data["gui"])




class Clay_statue(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["clay_statue"],Hitbox(HITBOX_RECT_t, NULL_VEC, 0, 50, 100))

    def on_interact(self, world, user):
        user.open_gui("Death_statue")
class Bridge_middle(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["bridge_middle"],HITBOX_50X50)

class Bridge_end(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["bridge_end"],HITBOX_50X50)

class Bridge_start(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["bridge_start"],HITBOX_50X50)

#class Resurrection_stone_pedestal(objs.Obj):
#    def __init__(self, x:float, y:float) -> None:
#        super().__init__(self.__class__.__name__, x, y, 0, Textures["Obj"]["resurrection_stone_pedestal"],Hitbox(HITBOX_RECT_t, NULL_VEC, 0, 50, 100), {"used" : False})
#
#    def on_interact(self, world, user):
#        if not self.data["used"]:
#            if user.add_item(items["Resurrection_stone"](1)):
#                self.data["used"] = True
#                self.texture = Textures["Obj"]["death_pedestal_50x100"]


class Kitchen_work_station_left_top(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["kitchen_work_station_top"],HITBOX_50X50)

class Kitchen_work_station_middle_top(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["kitchen_work_station_top"],HITBOX_50X50)

class Kitchen_work_station_right_top(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["kitchen_work_station_top"],HITBOX_50X50)

class Kitchen_work_station_left_down(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["kitchen_work_station_left_down"],HITBOX_0x0)

class Kitchen_work_station_middle_down(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["kitchen_work_station_middle_down"],HITBOX_0x0)

class Kitchen_work_station_right_down(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["kitchen_work_station_right_down"],HITBOX_0x0)

class Cavern_floor(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["cavern_floor"],HITBOX_50X50)


class Cavern_entrance(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["cavern_entrance"],Hitbox(HITBOX_RECT_t, Vec(0,0), 0, 150, 100))

    def on_interact(self, _world, user):
        if user.pos.y >= self.pos.y + 90 and self.pos.x + 25 < user.pos.x < self.pos.x + 75:
            w_ = user.world
            user.world = world.World("cavern",(0,0,0))
            user.world.old_world = w_
            user.pos = Vec(50,50)
            user.world.add_entity(entities.Npcs["Death"](Vec(616,616)))

class Cavern_wall(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["cavern_wall"], HITBOX_50X50)

objs.registerObj(Wood)
objs.registerObj(Wall)
objs.registerObj(Bed_head)
objs.registerObj(Bed_feet)
objs.registerObj(Mandalorian_poster)
objs.registerObj(Grogu)
objs.registerObj(Commode)
objs.registerObj(Stairs)
objs.registerObj(Tv)
objs.registerObj(Empty_commode)
objs.registerObj(Wall_left_up)
objs.registerObj(Wall_left)
objs.registerObj(Wall_right_up)
objs.registerObj(Wall_right)
objs.registerObj(Wall_left_down)
objs.registerObj(Wall_right_down)
objs.registerObj(Frigo_up)
objs.registerObj(Frigo_down)
objs.registerObj(Door_frame)
objs.registerObj(plank_void)
objs.registerObj(House)
objs.registerObj(Sign)
objs.registerObj(Clay_statue)
objs.registerObj(Bridge_middle)
objs.registerObj(Bridge_start)
objs.registerObj(Bridge_end)
#registerobjs.Obj(Resurrection_stone_pedestal)
objs.registerObj(Pc)
objs.registerObj(Kitchen_work_station_left_top)
objs.registerObj(Kitchen_work_station_middle_top)
objs.registerObj(Kitchen_work_station_right_top)
objs.registerObj(Kitchen_work_station_left_down)
objs.registerObj(Kitchen_work_station_middle_down)
objs.registerObj(Kitchen_work_station_right_down)
objs.registerObj(Cavern_floor)
objs.registerObj(Cavern_entrance)
objs.registerObj(Cavern_wall)


#class Cochon_spawner(objs.Obj):
#    def __init__(self, x:float, y:float) -> None:
#        super().__init__(self.__class__.__name__, x, y, False, Textures["other"]["couchon"],Hitbox(HITBOX_RECT_t,NULL_VEC,0, 100, 100))
#
#    def on_draw(self, world, has_been_drawn):
#        if not players[0].is_world_editor:
#            world.get_Chunk_from_pos(self.pos).objects.remove(self)
#            world.add_entity(Npcs["Couchon"](self.pos))
#
#    
#registerobjs.Obj(Cochon_spawner)
