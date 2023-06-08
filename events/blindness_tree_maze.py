from events import *
from uti.vector import *
from uti.textures import *
import pygame

texture = Textures["other"]["blindness"].convert_alpha()
w = texture.get_width()
h = texture.get_height()

def draw(players, screen : pygame.Surface):
    x = players[0].pos.x
    y = players[0].pos.y
    obj = players[0].world.get_Obj(Vec(-1600, -1450))
    if obj.id == "Resurrection_stone_pedestal":
        if not obj.data["used"]:
            if -2700 < x < -100 and -2600 < y < -400:
                global h, w, texture
                new_w = screen.get_width() 
                new_h = screen.get_height()
                if new_h != h or new_w != w:
                    texture = pygame.transform.scale(texture, (new_w, new_h)).convert_alpha()
                    w = new_w
                    h = new_h
                screen.blit(texture, (0,0))
                screen.blit(texture, (0,0))


#apply blindness to the player
registerEvent(Event(Event_on_draw_t, draw))


