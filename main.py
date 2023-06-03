#Prettystick en version pétée by Léa et Asqel
import pygame as py
from pygame.locals import *

from uti.textures import *
from uti.sound import play_sound
from entities import *
from time import time, sleep
from interface import *
from world import *
from events import *

from _thread import start_new_thread
import jsonizer as js

from random import *

py.joystick.init()
py.font.init()

FPS_MAX = 60
TPS_MAX = 150

g_tps = 0

running_dict = {
    "global": True,
    "server": True
}

pygame_events=[]
    

def server_thread():
    global running_dict, g_tps, pygame_events, show_hitbox

    loop_start = time()
    loop_count = 0

    joystick_count = py.joystick.get_count()
    if joystick_count:
        joysticks = []
        for i in range(joystick_count):
            joystick = py.joystick.Joystick(i)
            joystick.init()
            joysticks.append(joystick)

    while running_dict["global"]:
        iter_start = time()
        loop_count += 1

        for i in events[Event_before_tick_t]:
            i.function(players, pygame_events)
        
        if players[0].gui is not None:
            players[0].gui.tick(pygame_events)
            pygame_events = []
        for i in pygame_events:
            if i.type == py.QUIT:
                running_dict["global"] = False
        
            elif i.type == py.KEYDOWN:
                if i.key == K_F3:
                    players[0].chunk_border=not players[0].chunk_border

                elif i.key == K_ASTERISK:
                    toggle_hitbox()

                elif i.key == K_LCTRL:
                    players[0].speed = 0.85
                elif i.key == K_1:
                    players[0].inventaire_idx = 0
                elif i.key == K_2:
                    players[0].inventaire_idx = 1
                elif i.key == K_3:
                    players[0].inventaire_idx = 2
                elif i.key == K_4:
                    players[0].inventaire_idx = 3
                elif i.key == K_5:
                    players[0].inventaire_idx = 4
                elif i.key == K_6:
                    players[0].inventaire_idx = 5
                elif i.key == K_7:
                    players[0].inventaire_idx = 6
                elif i.key == K_8:
                    players[0].inventaire_idx = 7
                elif i.key == K_9:
                    players[0].inventaire_idx = 8
                elif i.key == K_0:
                    players[0].inventaire_idx = 9

                elif i.key == K_t:
                    players[0].remove_item_current_slot()
                elif i.key == K_r:
                    players[0].inventaire[players[0].inventaire_idx].on_use(players[0].world, players[0])
                elif i.key == K_ESCAPE:
                    players[0].gui = guis["Escape_gui"](players[0])

                elif i.key ==K_e:
                    if not players[0].gui:
                        if players[0].dir == 'u':
                            players[0].world.get_Obj(players[0].pos+(25,-10)).on_interact(players[0].world,players[0])

                        if players[0].dir == 'r':
                            players[0].world.get_Obj(players[0].pos+(10+50, 25)).on_interact(players[0].world,players[0])

                        if players[0].dir == 'd':
                            players[0].world.get_Obj(players[0].pos+(25,50+10)).on_interact(players[0].world,players[0])
                           
                        if players[0].dir == 'l':
                            players[0].world.get_Obj(players[0].pos+(-10,25)).on_interact(players[0].world,players[0])
                elif i.key ==K_a and players[0].has_item("Wand"):
                    if not players[0].gui:
                        if players[0].dir == 'u':
                            bullet = Npcs["Bullet"](players[0].pos + (13,-25))
                            bullet.direction = players[0].dir
                            bullet.sender = players[0]
                            players[0].world.get_Chunk_from_pos(players[0].pos).entities.append(bullet)
                            

                        if players[0].dir == 'r':
                            bullet = Npcs["Bullet"](players[0].pos + (10+50, 13))
                            bullet.direction = players[0].dir
                            bullet.sender = players[0]
                            players[0].world.get_Chunk_from_pos(players[0].pos).entities.append(bullet)

                        if players[0].dir == 'd':
                            bullet = Npcs["Bullet"](players[0].pos + (13,50+10))
                            bullet.sender = players[0]
                            bullet.direction = players[0].dir
                            players[0].world.get_Chunk_from_pos(players[0].pos).entities.append(bullet)
                            
                        if players[0].dir == 'l':
                            bullet = Npcs["Bullet"](players[0].pos + (-10,13))
                            bullet.sender = players[0]
                            bullet.direction = players[0].dir
                            players[0].world.get_Chunk_from_pos(players[0].pos).entities.append(bullet)
            
            elif i.type == py.KEYUP:
                if i.key == py.K_LCTRL:
                    players[0].speed = 0.5  
       
        

        pushed_keys=py.key.get_pressed()
        if not players[0].gui:
            if pushed_keys[py.K_q] and pushed_keys[py.K_s]:
                players[0].downleft()
                players[0].world.activate_collision()
            
            elif pushed_keys[py.K_q] and pushed_keys[py.K_z]:
                players[0].upleft()
                players[0].world.activate_collision()
            
            elif pushed_keys[py.K_d] and pushed_keys[py.K_z]:
                players[0].upright()
                players[0].world.activate_collision()
    
            elif pushed_keys[py.K_d] and pushed_keys[py.K_s]:
                players[0].downright()
                players[0].world.activate_collision()
    
            elif pushed_keys[py.K_q]:
                players[0].left()
                players[0].world.activate_collision()

            elif pushed_keys[py.K_d]:
                players[0].right()
                players[0].world.activate_collision()

            elif pushed_keys[py.K_z]:
                players[0].up()
                players[0].world.activate_collision()

            elif pushed_keys[py.K_s]:
                players[0].down()
                players[0].world.activate_collision()

        if not players[0].gui:
            players[0].world.update()
            
        for i in events[Event_after_tick_t]:
            i.function(players, pygame_events)
                
        pygame_events = []


        # tps moyenizer
        moy_fps = 1 / (time() - loop_start) * loop_count if loop_count > 10 else TPS_MAX
        to_sleep = (1 / TPS_MAX - (time() - iter_start)) - (1 - (moy_fps / TPS_MAX))
        if to_sleep > 0: sleep(to_sleep)

        g_tps = 1 / (time() - loop_start) * loop_count

    running_dict["server"] = False

def draw_inventory():
    x, y = screen.get_width()/2 - Textures["other"]["slot_x_10"].get_width()/2, 10
    screen.blit(Textures["other"]["slot_x_10"], (x,y))
    for i in range(10):
        screen.blit(players[0].inventaire[i].texture, (x+46*(i+1)-40, y+6))
        if players[0].inventaire[i].quantity > 1:
            screen.blit(mc_font.render(str(players[0].inventaire[i].quantity),False,(0,0,0)), (x+46*(i+1)-25, y+27))
        if players[0].inventaire_idx == i:
            py.draw.rect(screen, (255,0,0), py.Rect(x+46*(i+1)-46, y+45,40,5))




def main():

    global pygame_events
    #start_new_thread(play_sound, ("nymphe-echo-demo1.flac",))
    
    starting_world = js.load_world("bed room")
    players.append(Character("Jean", "Magie", "pouffsoufle", None, None, POUFSOUFFLE_TEXTURES_0, None, 100, 0, starting_world))
    players[0].gui = guis["Choose_name"](players[0])

    players[0].zoom_out = 1
    players[0].render_distance = 3

    start_new_thread(server_thread, ())

    arial = py.font.SysFont("Arial", 25, False, False)
    fps = 0
    while running_dict["global"] and running_dict["server"]:
        start_time = time()
        pygame_events = py.event.get()
        for i in pygame_events:
            if i.type == py.QUIT:
                running_dict["global"] = False
        
                
        players[0].world : World = players[0].world
        players[0].world.show(screen, players[0].zoom_out)

        screen.blit(arial.render(f"fps: {int(fps)}", False, (255, 0, 0)), (0, 0))
        screen.blit(arial.render(f"mid tps: {int(g_tps)}", False, (255, 0, 0)), (0, 30))
        screen.blit(arial.render(str(players[0].pos.floor()), False, (255, 0, 0)), (0, 60))
        screen.blit(arial.render(str(players[0].world.get_Chunk_from_pos(players[0].pos).pos), False, (255, 0, 0)), (0, 90))
        screen.blit(arial.render(str(players[0].money)+" €", False, (255, 0, 0)), (0, 120))
        screen.blit(arial.render(str(players[0].pv) + " Pv", False, (255, 0, 0)), (0, 150))
        draw_inventory()
        if players[0].gui:
            players[0].gui.draw(screen)

        for i in events[Event_on_draw_t]:
            i.function(players, screen)
        
        py.display.update()
        t = time()
        if  t - start_time < 1 / 60:
            sleep(1 / 60 - t + start_time)
        fps = 1 / (time() - start_time)

main()