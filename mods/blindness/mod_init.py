from events import *
import pygame
import os

texture = pygame.image.load(os.path.dirname(os.path.abspath(__file__))+"/blindness.png").convert_alpha()
w = texture.get_width()
h = texture.get_height()

def draw(players, screen : pygame.Surface):
    global h, w, texture
    new_w = screen.get_width() 
    new_h = screen.get_height()
    if new_h != h or new_w != w:
        texture = pygame.transform.scale(texture, (new_w, new_h)).convert_alpha()
        w = new_w
        h = new_h
    screen.blit(texture, (0,0))


#apply blindness to the player
#registerEvent(Event(Event_on_draw_t, draw))