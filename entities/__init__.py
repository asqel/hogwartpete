import Clothes as c
from uti.vector import *
from uti.hitbox import *
from uti.textures import *
import pygame as py
from  spells import *
import uuid

class Character:
    def __init__(self,name:str,surname:str,maison:str,spells:list[Spell],inventaire,genre:str,texture:list[py.Surface],clothes,x:float,y:float,world):
        self.name=name
        self.surname=surname
        self.house=maison
        self.spells=spells
        self.inventaire=inventaire
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
        self.world=world
        self.chunk_border=False
        self.uuid=uuid.uuid4()
        self.zoom_out=1
        self.transparent=False # si on peut passer a travers != de invisble

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
            
    def collisions(self,dir:str):
        x=(players[0].pos//1000).x
        y=(players[0].pos//1000).y
        __chunks:list=[]
        __objects:list=[]
        __hitboxes:list[Hitbox]=[]
        for i in range(- players[0].render_distance // 2 + 1, players[0].render_distance // 2 + 1):
            __chunks.extend(self.world.get_Chunk_at(Vec(x+i,y+k)) for k in range(- players[0].render_distance // 2 + 1, players[0].render_distance // 2 + 1))
        for i in __chunks:
            __objects.extend(i.objects)
            __objects.extend(i.background_obj)
            __hitboxes.extend(i.hitboxes)
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
        self.action=action # a function -> action(self, world, user)
        self.tick=tick # tick(self, world)
        

players:list[Character]=[]

def new_farine():
    return Npc("farine","gomez",FARINE_TEXTURE,[],Vec(90,90),Vec(8,0),Hitbox(HITBOX_RECT_t,Vec(0,0),0,50,75))






