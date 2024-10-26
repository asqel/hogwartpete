import events
import pygame as py

from uti.hitbox import HITBOX_50X50 

def arrow_key_move(players, pygame_events : py.event.Event):
    pushed_keys = py.key.get_pressed()
    if not players[0].guis:
            if pushed_keys[py.K_LEFT] and pushed_keys[py.K_DOWN]:
                players[0].downleft()
                players[0].world.activate_collision()
            
            elif pushed_keys[py.K_LEFT] and pushed_keys[py.K_UP]:
                players[0].upleft()
                players[0].world.activate_collision()
            
            elif pushed_keys[py.K_RIGHT] and pushed_keys[py.K_UP]:
                players[0].upright()
                players[0].world.activate_collision()
    
            elif pushed_keys[py.K_RIGHT] and pushed_keys[py.K_DOWN]:
                players[0].downright()
                players[0].world.activate_collision()
    
            elif pushed_keys[py.K_LEFT]:
                players[0].left()
                players[0].world.activate_collision()
    
            elif pushed_keys[py.K_RIGHT]:
                players[0].right()
                players[0].world.activate_collision()
    
            elif pushed_keys[py.K_UP]:
                players[0].up()
                players[0].world.activate_collision()
    
            elif pushed_keys[py.K_DOWN]:
                players[0].down()
                players[0].world.activate_collision()               
                
        


events.registerEvent(events.Event(events.Event_after_tick_t,arrow_key_move))

