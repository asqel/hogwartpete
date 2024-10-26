import pygame
import entities
import events


def cavern_events(players, pygame_events : pygame.event.Event):
	...
    ##if players[0].world.name == "cavern":
    ##    if players[0].has_item("Elder_wand"):
    ##        players[0].world = players[0].world.old_world
    ##        players[0].pos = Vec(2550,-3300)+(0,120)



events.registerEvent(events.Event(events.Event_after_tick_t, cavern_events))