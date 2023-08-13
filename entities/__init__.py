from uti.vector import *
from uti.hitbox import *
from uti.textures import *
from interface import *
from items import *
import pygame as py
from  spells import *
import uuid

class Character:
    def __init__(self,name:str,surname:str,maison:str,spells:dict[int, Spell],genre:str,texture:list[py.Surface],clothes,x:float,y:float,world):
        self.name=name
        self.surname=surname
        self.house=maison
        self.spells=spells
        self.inventaire : list[Item]=[items["Air"](1) for i in range(10)]
        self.inventaire_idx = 0 
        self.pv=100
        self.pvmax=100
        self.effects=[]
        self.genre=genre
        self.hitbox=Hitbox(HITBOX_RECT_t,Vec(0,0),width=50,height=50)
        self.texture=texture#[UP,RIGHT,DOWN,LEFT]
        self.current_texture=texture[2]
        self.clothes=clothes
        self.pos=Vec(x,y)
        self.protection=0
        self.dir:str="d" #d -> down  |  u -> up  |  r -> right  |  l -> left  |
        self.level=0
        self.puissance=0
        self.speed=0.5
        self.isvisible=True
        self.render_distance=3
        self.world =world
        self.chunk_border=False
        self.uuid=uuid.uuid4()
        self.zoom_out=1
        self.transparent=False # si on peut passer a travers != de invisble
        self.gui :Gui = None
        self.money = 0
        self.is_world_editor = False
        self.day_count = 0
        self.tick_count = 0

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
        if self.dir!="":
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

    def add_item(self, item : Item):
        """
        try to add the item to first finded slot 
        return 0 if the item was not able to be added or not the entire item was added
        return 1 if the item was able to be added 
        """
        for i in range(len(self.inventaire)):
            if self.inventaire[i].id == "Air":
                self.inventaire[i] = item
                return 1
            if self.inventaire[i].id == item.id:
                if self.inventaire[i].quantity + item.quantity <= item.max_stack:
                    self.inventaire[i].quantity += item.quantity
                    return 1
                else:
                    item.quantity -= item.max_stack - self.inventaire[i].quantity
                    self.inventaire[i].quantity = self.inventaire[i].max_stack


        return 0

    def remove_item_current_slot(self):
        self.inventaire[self.inventaire_idx].quantity -= 1
        if self.inventaire[self.inventaire_idx].quantity <= 0:
            self.inventaire[self.inventaire_idx] = items["Air"](1)

    def drop_item(self):
        if self.inventaire[self.inventaire_idx].id != "Air":
            item = self.inventaire[self.inventaire_idx].copy()
            item.quantity = 1
            self.world.spawn_item(item, self.pos)
            self.remove_item_current_slot()
            
    
    def has_item(self, id: str):
        for i in self.inventaire:
            if i.id == id:
                return 1
        return 0
    
    def open_gui(self, gui_name : str):
        self.gui = guis[gui_name](self)
        
    def close_gui(self):
        self.gui = None
        

class Npc:
    def __init__(self,name:str,surname:str,texture:py.Surface,spells:list[Spell],pos:Vec,texture_pos:Vec=NULL_VEC,hitbox:Hitbox=HITBOX_50X50,action=None,tick=None) -> None:
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
        self.transparent=False # si on peut passer a travers != de invisble
        self.collide_player = True
    
    def on_draw(self,world,has_been_drawn):
        ...
    def die(self, world):
        return 1
    def tick(self,world):
        ...
    def on_interact(self,world,user):
        ...
players:list[Character]=[]

Npcs : dict[str,type] = {}

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


