import pygame
from entities import *
from events import *
from key_map import *


def wand_events(players, pygame_events : pygame.event.Event):
    if not players[0].inventaire[players[0].inventaire_idx].id == "Wand":
        return 0
    for i in pygame_events:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if (1,i.button) == key_map["protego"]:
                shoot_protego(players)
            if (1,i.button) == key_map["shoot wand"]:
                shoot_wand(players[0])
        if i.type == pygame.KEYDOWN:
            if i.key == key_map["protego"]:
                shoot_protego(players)
            if i.key == key_map["shoot wand"]:
                shoot_wand(players[0])


def shoot_protego(players):
    if players[0].dir == "u":
        shield = Npcs["Protego"](players[0].pos + (-10, -50))
        shield.dir = players[0].dir
        shield.sender = players[0]
        shield.hitbox = Hitbox(HITBOX_RECT_t, NULL_VEC, 0, 70, 50)
        players[0].world.add_entity(shield)

    elif players[0].dir == "r":
        shield = Npcs["Protego"](players[0].pos + (50, -10))
        shield.dir = players[0].dir
        shield.sender = players[0]
        shield.hitbox = Hitbox(HITBOX_RECT_t, NULL_VEC, 0, 50, 70)
        players[0].world.add_entity(shield)

    elif players[0].dir == "d":
        shield = Npcs["Protego"](players[0].pos + (-10, 50))
        shield.dir = players[0].dir
        shield.sender = players[0]
        shield.hitbox = Hitbox(HITBOX_RECT_t, NULL_VEC, 0, 70, 50)
        players[0].world.add_entity(shield)

    elif players[0].dir == "l":
        shield = Npcs["Protego"](players[0].pos + (-50, -10))
        shield.dir = players[0].dir
        shield.sender = players[0]
        shield.hitbox = Hitbox(HITBOX_RECT_t, NULL_VEC, 0, 50, 70)
        players[0].world.add_entity(shield)

def shoot_wand(user):
    if not user.gui:
        if user.dir == 'u':
            bullet = Npcs["Bullet"](user.pos + (13,-25))
            bullet.direction = user.dir
            bullet.sender = user
            user.world.get_Chunk_from_pos(user.pos).entities.append(bullet)
            

        if user.dir == 'r':
            bullet = Npcs["Bullet"](user.pos + (10+50, 13))
            bullet.direction = user.dir
            bullet.sender = user
            user.world.get_Chunk_from_pos(user.pos).entities.append(bullet)

        if user.dir == 'd':
            bullet = Npcs["Bullet"](user.pos + (13,50+10))
            bullet.sender = user
            bullet.direction = user.dir
            user.world.get_Chunk_from_pos(user.pos).entities.append(bullet)
            
        if user.dir == 'l':
            bullet = Npcs["Bullet"](user.pos + (-10,13))
            bullet.sender = user
            bullet.direction = user.dir
            user.world.get_Chunk_from_pos(user.pos).entities.append(bullet)

registerEvent(Event(Event_after_tick_t, wand_events))