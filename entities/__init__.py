from uti.vector import *
from uti.hitbox import *
from uti.textures import *
import quests
import uti
import interface
import items
import pygame as py
import world
import importlib as imp

class Character:
    def __init__(self, texture:list[py.Surface], x : float, y : float, world, save_name : str):
        self.save_name = save_name
        self.pv = 100
        self.pvmax = 100
        self.effects = []
        self.hitbox = Hitbox(HITBOX_RECT_t, Vec(0, 0), width = 50, height = 50)
        self.texture = texture#[UP,RIGHT,DOWN,LEFT]
        self.current_texture = texture[2]
        self.pos = Vec(x, y)
        self.protection = 0
        self.dir : str = "d" #d -> down  |  u -> up  |  r -> right  |  l -> left  |
        self.level = 0
        self.speed=0.5
        self.isvisible=True
        self.render_distance=3
        self.world = world
        self.chunk_border = False
        self.riding : Npc = None # entity wich the player is riding
        self.zoom_out = 1
        self.speed_multiplier : dict[str, int] = {} # name : value
        self.transparent = False # si on peut passer a travers != de invisble
        self.guis : list[interface.Gui] = []
        self.data = {} # str-> str | int | float | list | dict
        self.is_world_editor = False
        self.day_count = 0
        self.tick_count = 0
        self.quests : dict[str, quests.Quest] = {} # incompleted quests
        self.quests_completed : dict[str, quests.Quest] = {}

    def upleft(self):
        if self.dir!="u":
            self.dir="u"
            self.current_texture=self.texture[0]
        self.pos += Vec(0,-2)*self.speed
        self.collisions("u")
        self.pos += Vec(-2,0)*self.speed
        self.collisions("l")

    def upright(self):
        if self.dir!="u":
            self.dir="u"
            self.current_texture=self.texture[0]
        self.pos += Vec(0,-2)*self.speed
        self.collisions("u")
        self.pos += Vec(2,0)*self.speed
        self.collisions("r")

    def downleft(self):
        if self.dir!="d":
            self.dir="d"
            self.current_texture=self.texture[2]
        self.pos += Vec(0,2)*self.speed
        self.collisions("d")
        self.pos += Vec(-2,0)*self.speed
        self.collisions("l")
    
    def downright(self):
        if self.dir!="d":
            self.dir="d"
            self.current_texture=self.texture[2]
        self.pos += Vec(0,2)*self.speed
        self.collisions("d")
        self.pos += Vec(2,0)*self.speed
        self.collisions("r")

    def left(self):
        if self.dir!="l":
            self.dir="l"
            self.current_texture=self.texture[3]
        self.pos-=Vec(2,0)*self.speed
        self.collisions("l")

    def right(self):
        if self.dir!="r":
            self.dir="r"
            self.current_texture=self.texture[1]
        self.pos+=Vec(2,0)*self.speed
        self.collisions("r")


    def up(self):
        if self.dir!="u":
            self.dir="u"
            self.current_texture=self.texture[0]
        self.pos-=Vec(0,2)*self.speed
        self.collisions("u")

    def down(self):
        if self.dir!="d":
            self.dir="d"
            self.current_texture=self.texture[2]
        self.pos+=Vec(0,2)*self.speed
        self.collisions("d")

    def on_draw(self,world,has_been_drawn):
        ...
    
    def update_texture(self,vec):
        corner=math.sqrt(2)/2
        if -corner<=vec.x<=corner and corner<=vec.y<=1:
            self.current_texture=self.texture[2]
            
        elif -corner<=vec.x<=corner and -corner>=vec.y>=-1:
            self.current_texture=self.texture[0]
            
        elif vec.x<0:
            self.current_texture=self.texture[3]
        else:
            self.current_texture=self.texture[1]
    
    def update_texture_from_pos(self):
        if self.dir == "u":
            self.current_texture = self.texture[0]
        if self.dir == "r":
            self.current_texture = self.texture[1]
        if self.dir == "d":
            self.current_texture = self.texture[2]
        if self.dir == "l":
            self.current_texture = self.texture[3]
            
    def collisions(self,dir:str):
        x=(players[0].pos//1000).x
        y=(players[0].pos//1000).y
        __chunks:list=[]
        __objects:list=[]
        __hitboxes:list[Hitbox]=[]
        __enitites:list[Npc] =[]
        for i in range(- players[0].render_distance // 2 + 1, players[0].render_distance // 2 + 1):
            __chunks.extend(self.world.get_Chunk_at(Vec(x+i,y+k)) for k in range(- players[0].render_distance // 2 + 1, players[0].render_distance // 2 + 1))
        for i in __chunks:
            __objects.extend(i.objects)
            __objects.extend(i.dyn_objects)
            __hitboxes.extend(i.hitboxes)
            __enitites.extend(i.entities)
        for i in __objects:
            if i.hitbox and players[0].hitbox:
                hit1=i.hitbox.copy()
                hit1.pos+=i.pos
                hit2=players[0].hitbox.copy()
                hit2.pos+=players[0].pos
                if hit1.iscolliding(hit2):
                    i.on_walk_in(self.world,self)
                    if dir=="d":
                        self.pos-=Vec(0,2)*self.speed
                    if dir=="u":
                        self.pos-=Vec(0,-2)*self.speed
                    if dir=="l":
                        self.pos-=Vec(-2,0)*self.speed
                    if dir=="r":
                        self.pos-=Vec(2,0)*self.speed
                    return 0 
        for i in __hitboxes:
            if i and players[0].hitbox:
                hit2=players[0].hitbox.copy()
                hit2.pos+=players[0].pos
                if i.iscolliding(hit2):
                    if dir=="d":
                        self.pos-=Vec(0,2)*self.speed
                    if dir=="u":
                        self.pos-=Vec(0,-2)*self.speed
                    if dir=="l":
                        self.pos-=Vec(-2,0)*self.speed
                    if dir=="r":
                        self.pos-=Vec(2,0)*self.speed
                    return 0 
        for i in __enitites:
            if i.hitbox and players[0].hitbox and i.name != "Item_entity" and not i.transparent:
                hit2 = players[0].hitbox.copy()
                hit2.pos += players[0].pos
                hit1 = i.hitbox.copy()
                hit1.pos += i.pos
                if hit1.iscolliding(hit2):
                    if dir=="d":
                        v = self.pos-Vec(0,2)*self.speed
                        if self.world.get_Obj(v).id == "Air":
                            self.pos = v
                    if dir=="u":
                        v = self.pos - Vec(0,-2)*self.speed
                        if self.world.get_Obj(v).id == "Air":
                            self.pos = v
                    if dir=="l":
                        v = self.pos - Vec(-2,0)*self.speed
                        if self.world.get_Obj(v).id == "Air":
                            self.pos = v
                    if dir=="r":
                        v = self.pos - Vec(2,0)*self.speed
                        if self.world.get_Obj(v).id == "Air":
                             self.pos = v

    def open_gui(self, gui_name : str):
        self.guis.append(interface.guis[gui_name](self))
        
    def close_gui(self):
        if self.guis:
            self.guis.pop(-1)
    
    def has_quest(self, _id : str):
        return _id in self.quests.keys() or _id in self.quests_completed.keys()
    
    def has_quest_done(self, _id : str):
        return _id in self.quests_completed.keys()

    def has_quest_incompleted(self, _id : str):
        return _id in self.quests.keys()

    def add_quest(self, _id : str, quest : quests.Quest):
        self.quests[_id] = quest

    def add_quest_completed(self, _id : str, quest : quests.Quest):
        self.quests_completed[_id] = quest

    def get_quest(self, _id : str):
        if _id in self.quests.keys():
            return self.quests[_id]
        return None

    def get_quest_completed(self, _id : str):
        if _id in self.quests_completed.keys():
            return self.quests_completed[_id]
        return None

    def complete_quest(self, _id):
        if _id in self.quests.keys():
            self.quests_completed[_id] = self.quests[_id]
            self.quests.pop(_id)

    
class Npc:
    def __init__(self,name:str,surname:str,texture:py.Surface,spells,pos:Vec,texture_pos:Vec=NULL_VEC,hitbox:Hitbox=HITBOX_50X50,action=None,tick=None) -> None:
        self.name=name
        self.surname=surname
        self.texture=texture
        self.current_texture=self.texture[2]
        self.dir="d"
        self.spells=spells
        self.isvisible=True
        self.pv=100
        self.hitbox=hitbox
        self.pos=pos
        self.texture_pos=texture_pos
        self.speed=0.5
        self.speed_multiplier : dict[str:int] = {} # name : value
        self.transparent=False # si on peut passer a travers != de invisble
        self.collide_player = True
        self.world = None
        self.rider : Character = None
        self.data = {}
        self.rider_offset = Vec(0,0)
    
    def on_draw(self,world,has_been_drawn):
        ...
    def die(self, world):
        return 1
    def tick(self,world):
        ...
    def mov(self,world,rider,dir : str): #dir : u/d/r/l/ur/ul/dr/dl
        ...
    def on_interact(self,world,user):
        ...

print("hohohoh")
players:list[Character]=[]

Npcs : dict[str,type] = {}
print("hohohoh")


def new_farine():
    return Npc("farine","gomez",FARINE_TEXTURE,[],Vec(90,90),Vec(8,0),Hitbox(HITBOX_RECT_t,Vec(0,0),0,50,75))

def registerNpc(npc:type):
    Npcs[npc.__name__]=npc
    
module_names=os.listdir(os.path.dirname(os.path.abspath(__file__)))

for i in range(len(module_names)):
    if module_names[i]=="__init__.py":
        module_names.pop(i)
        break
for i in range(len(module_names)):
    if module_names[i].endswith(".py"):
        module_names[i]=module_names[i][:-3]

for i in module_names:
    imp.import_module(f".{i}", __package__)


