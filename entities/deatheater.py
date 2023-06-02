from entities import *
from uti import *
from math import *
from random import *

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
        self.dir="d"
        
    def go_to_player(self,Player:Character, world):
        v=Player.pos-self.pos
        if v.squareLength()<=10000**2 and v.squareLength()>=150**2:
            if world.get_Obj(self.pos+v*self.speed/150).id=="Air":
                self.pos+=v*self.speed/150
            else:
                self.pos-=v*self.speed/150
        if v.squareLength()<=150**2:
            if world.get_Obj(self.pos-v*self.speed/150).id=="Air":
                self.pos-=v*self.speed/150
            else:
                self.pos+=v*self.speed/150
        v=v.normalize()
        racine=sqrt(2)/2
        if racine<v.x<=1 and -racine<=v.y<=racine:
            self.dir="r"
            self.current_texture=self.texture[1]
        if -1<=v.x<-racine and -racine<=v.y<=racine:
            self.dir="l"
            self.current_texture=self.texture[3]
        if racine<v.y<=1 and -racine<=v.x<=racine:
            self.dir="d"
            self.current_texture=self.texture[2]
        if -racine<=v.x<=racine and -racine>v.y>=-1:
            self.dir="u"
            self.current_texture=self.texture[0]

    def attack(self, world):
        if self.dir == 'u':
            bullet = Npcs["Bullet"](self.pos + (13,-10))
            bullet.direction = self.dir
            bullet.sender = self
            world.get_Chunk_from_pos(self.pos).entities.append(bullet)
        if self.dir == 'r':
            bullet = Npcs["Bullet"](self.pos + (10 + 50, 13))
            bullet.direction = self.dir
            bullet.sender = self
            world.get_Chunk_from_pos(self.pos).entities.append(bullet)
        if self.dir == 'd':
            bullet = Npcs["Bullet"](self.pos + (13,50 + 10))
            bullet.direction = self.dir
            bullet.sender = self
            world.get_Chunk_from_pos(self.pos).entities.append(bullet)
                            
        if self.dir == 'l':
            bullet = Npcs["Bullet"](self.pos + (-10,13))
            bullet.direction = self.dir
            bullet.sender = self
            world.get_Chunk_from_pos(self.pos).entities.append(bullet)
    
    def tick(self, world):
        self.go_to_player(players[0], world)
        world.activate_collision()
        random=randint(0,300)
        if random==75:
            self.attack(world)


registerNpc(Death)