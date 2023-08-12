import pygame as py
from items import *
from uti import *
import entities as en

class Wand(Item):
    def __init__(self, quantity) -> None:
        super().__init__(self.__class__.__name__, 1, Textures["item"]["wand"], quantity, "wand")


    def on_use(self, world, user):
        if not user.gui:
            if user.dir == 'u':
                bullet = en.Npcs["Bullet"](user.pos + (13,-25))
                bullet.direction = user.dir
                bullet.sender = user
                user.world.get_Chunk_from_pos(user.pos).entities.append(bullet)
                

            if user.dir == 'r':
                bullet = en.Npcs["Bullet"](user.pos + (10+50, 13))
                bullet.direction = user.dir
                bullet.sender = user
                user.world.get_Chunk_from_pos(user.pos).entities.append(bullet)

            if user.dir == 'd':
                bullet = en.Npcs["Bullet"](user.pos + (13,50+10))
                bullet.sender = user
                bullet.direction = user.dir
                user.world.get_Chunk_from_pos(user.pos).entities.append(bullet)
                
            if user.dir == 'l':
                bullet = en.Npcs["Bullet"](user.pos + (-10,13))
                bullet.sender = user
                bullet.direction = user.dir
                user.world.get_Chunk_from_pos(user.pos).entities.append(bullet)


registerItem(Wand)