import pygame
from entities import *
from events import *


def wand_events(players, pygame_events : pygame.event.Event):
    if not players[0].inventaire[players[0].inventaire_idx].id == "Wand":
        return 0
    for i in pygame_events:
        if i.type == pygame.KEYDOWN:
            if i .key == pygame.K_SPACE:
                if players[0].dir == "u":
                    shield = Npcs["Protego"](players[0].pos + (-10, -50))
                    shield.dir = players[0].dir
                    shield.hitbox = Hitbox(HITBOX_RECT_t, NULL_VEC, 0, 70, 50)
                    players[0].world.add_entity(shield)

                elif players[0].dir == "r":
                    shield = Npcs["Protego"](players[0].pos + (50, -10))
                    shield.dir = players[0].dir
                    shield.hitbox = Hitbox(HITBOX_RECT_t, NULL_VEC, 0, 50, 70)
                    players[0].world.add_entity(shield)

                elif players[0].dir == "d":
                    shield = Npcs["Protego"](players[0].pos + (-10, 50))
                    shield.dir = players[0].dir
                    shield.hitbox = Hitbox(HITBOX_RECT_t, NULL_VEC, 0, 70, 50)
                    players[0].world.add_entity(shield)

                elif players[0].dir == "l":
                    shield = Npcs["Protego"](players[0].pos + (-50, -10))
                    shield.dir = players[0].dir
                    shield.hitbox = Hitbox(HITBOX_RECT_t, NULL_VEC, 0, 50, 70)
                    players[0].world.add_entity(shield)



registerEvent(Event(Event_after_tick_t, wand_events))