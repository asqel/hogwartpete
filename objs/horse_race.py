import pygame as py
from uti import *
from objs import *
from interface import *
from uti import py
import world as w
import jsonizer as js
from key_map import *
from entities import *
import world as w

class Horse_track_left(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["horse_track_left"],HITBOX_50X50)

class Horse_track_middle(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["horse_track_middle"],HITBOX_50X50)

class Horse_track_right(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["horse_track_right"],HITBOX_50X50)

class Horse_race_sign(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["horse_race_sign"],HITBOX_100X100)

class Cowboy_horse_race(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["cowboy_horse_race_down"],Hitbox(HITBOX_RECT_t, NULL_VEC, 0, 50, 59))

    def on_interact(self, world, user : Character):
        user.open_gui("Cowboy_horse_race_gui")

class Cowboy_horse_race_gui(Gui):
    def __init__(self, player : Character) -> None:
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
                if i.key == key_map[t_use_object]:
                    if self.idx == 0:
                        self.user.pos = Vec(900, -3250)
                        self.user.riding = Npcs["Horse"](self.user.pos)
                        self.user.riding.rider = self.user
                        self.user.riding.world = self.user.world
                        self.user.close_gui()
                    if self.idx == 1:
                        self.user.close_gui()
    def draw(self, screen):
        x = ["abcdefghijklmnopqrstuvwxyz*"]
        l = ["salut ma boy bats mon temps",
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
        draw_4_line(screen, l, c)


class Public_horse_race(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["public_horse_race"],Hitbox(HITBOX_RECT_t, NULL_VEC, 0, 175, 144))

registerObj(Horse_track_left)
registerObj(Horse_track_middle)
registerObj(Horse_track_right)
registerObj(Horse_race_sign)
registerObj(Cowboy_horse_race)
registerGui(Cowboy_horse_race_gui)
registerObj(Public_horse_race)