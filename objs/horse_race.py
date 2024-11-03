import pygame as py
from uti.vector import *
from uti.hitbox import *
from uti.textures import *

import objs
import interface
import world
import key_map
import entities
import quests

class Horse_track_left(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["horse_track_left"],HITBOX_50X50)

class Horse_track_middle(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["horse_track_middle"],HITBOX_50X50)

class Horse_track_right(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["horse_track_right"],HITBOX_50X50)

class Horse_race_sign(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["horse_race_sign"],HITBOX_100X100)

class Cowboy_horse_race(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["cowboy_horse_race_down"],Hitbox(HITBOX_RECT_t, NULL_VEC, 0, 50, 59))

    def on_interact(self, world, user : 'entities.Character'):
        if user.pos.y >= self.pos.y + 50:
            user.open_gui("Cowboy_horse_race_gui")
            if not user.has_quest("horse_race_won"):
                user.add_quest("horse_race_won", quests.Quest("Beat the record at the horse race"))
class Cowboy_horse_race_gui(interface.Gui):
    def __init__(self, player : 'entities.Character') -> None:
        super().__init__(self.__class__.__name__, {}, player)
        self.user = player
        self.idx = 0

    def tick(self, events: list[py.event.Event]):
        for i in events:
            if i.type == py.KEYDOWN:
                if i.key == py.K_UP :
                    self.idx -= 1
                    if self.idx < 0: 
                        self.idx = 1
                        
                if i.key == py.K_DOWN :
                    self.idx += 1
                    if self.idx > 1: 
                        self.idx = 0
                if i.key == key_map.key_map[key_map.t_use_object]:
                    if self.idx == 0:
                        self.user.pos = Vec(900, -3295)
                        self.user.riding = entities.Npcs["Horse"](self.user.pos)
                        self.user.riding.rider = self.user
                        self.user.riding.world = self.user.world
                        self.user.close_gui()
                        self.user.data["horse_race_tick"] = 0
                    if self.idx == 1:
                        self.user.close_gui()
    def draw(self, screen):
        _ = ["abcdefghijklmnopqrstuvwxyz*"]
        l = ["Salut ma boy bats mon temps",
             "et tu gagneras une spatule.",
             "       pourquoi pas","        au revoir"]
        c = [(0,) * 3] * 4
        c[2] = (255,0,0)
        c[3] = (255,0,0)
        if self.idx == 0:
            c[2] = (0,255,0)
            l[2] = "     > pourquoi pas"
        elif self.idx == 1:
            c[3] = (0,255,0)
            l[3] = "      > au revoir"
        interface.draw_4_line(screen, l, c, "Texas Mccain")
       


class Public_horse_race(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["public_horse_race"],Hitbox(HITBOX_RECT_t, NULL_VEC, 0, 175, 144))

objs.registerObj(Horse_track_left)
objs.registerObj(Horse_track_middle)
objs.registerObj(Horse_track_right)
objs.registerObj(Horse_race_sign)
objs.registerObj(Cowboy_horse_race)
interface.registerGui(Cowboy_horse_race_gui)
objs.registerObj(Public_horse_race)