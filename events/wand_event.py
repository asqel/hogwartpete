import pygame
from pygame.event import Event
from uti.hitbox import *
import entities
import events
import key_map
import interface

def wand_events(players, pygame_events : pygame.event.Event):
    for i in pygame_events:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if (1,i.button) == key_map.key_map["protego"]:
                shoot_protego(players)
            if (1,i.button) == key_map.key_map["shoot wand"]:
                shoot_wand(players[0])
        if i.type == pygame.KEYDOWN:
            if i.key == key_map.key_map["protego"]:
                shoot_protego(players)
            if i.key == key_map.key_map["shoot wand"]:
                shoot_wand(players[0])


def shoot_protego(players):
    if players[0].dir == "u":
        shield = entities.Npcs["Protego"](players[0].pos + (-10, -50))
        shield.dir = players[0].dir
        shield.sender = players[0]
        shield.hitbox = Hitbox(HITBOX_RECT_t, NULL_VEC, 0, 70, 50)
        players[0].world.add_entity(shield)

    elif players[0].dir == "r":
        shield = entities.Npcs["Protego"](players[0].pos + (50, -10))
        shield.dir = players[0].dir
        shield.sender = players[0]
        shield.hitbox = Hitbox(HITBOX_RECT_t, NULL_VEC, 0, 50, 70)
        players[0].world.add_entity(shield)

    elif players[0].dir == "d":
        shield = entities.Npcs["Protego"](players[0].pos + (-10, 50))
        shield.dir = players[0].dir
        shield.sender = players[0]
        shield.hitbox = Hitbox(HITBOX_RECT_t, NULL_VEC, 0, 70, 50)
        players[0].world.add_entity(shield)

    elif players[0].dir == "l":
        shield = entities.Npcs["Protego"](players[0].pos + (-50, -10))
        shield.dir = players[0].dir
        shield.sender = players[0]
        shield.hitbox = Hitbox(HITBOX_RECT_t, NULL_VEC, 0, 50, 70)
        players[0].world.add_entity(shield)

def shoot_wand(user):
    if not user.guis:
        if user.dir == 'u':
            bullet = entities.Npcs["Bullet"](user.pos + (13,-25))
            bullet.direction = user.dir
            bullet.sender = user
            user.world.get_Chunk_from_pos(user.pos).entities.append(bullet)
            

        if user.dir == 'r':
            bullet = entities.Npcs["Bullet"](user.pos + (10+50, 13))
            bullet.direction = user.dir
            bullet.sender = user
            user.world.get_Chunk_from_pos(user.pos).entities.append(bullet)

        if user.dir == 'd':
            bullet = entities.Npcs["Bullet"](user.pos + (13,50+10))
            bullet.sender = user
            bullet.direction = user.dir
            user.world.get_Chunk_from_pos(user.pos).entities.append(bullet)
            
        if user.dir == 'l':
            bullet = entities.Npcs["Bullet"](user.pos + (-10,13))
            bullet.sender = user
            bullet.direction = user.dir
            user.world.get_Chunk_from_pos(user.pos).entities.append(bullet)


events.registerEvent(events.Event(events.Event_after_tick_t, wand_events))