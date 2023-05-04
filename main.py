#Hogwarts Legacy en version pétée by Léa et Asqel
import pygame as py
from pygame.locals import *

from uti.textures import *
from uti.sound import play_sound
from entities import *
from time import time, sleep
from world import *
from worldlist import*

from _thread import start_new_thread

py.joystick.init()
py.font.init()

FPS_MAX = 60
TPS_MAX = 150

global g_tps, running_dict 
g_tps = 0

running_dict = {
    "global": True,
    "graphic": True,
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

        joystick_vec = Vec(0,0)
        for i in pygame_events:
            if i.type == py.QUIT:
                running_dict["global"] = False
            if i.type == py.JOYBUTTONDOWN:
                print("Bouton appuyé : ", i.button)
            elif i.type == py.JOYBUTTONUP:
                print("Bouton relâché : ", i.button)
            elif i.type == JOYAXISMOTION:
                # Obtenez le nombre d'axes pour le joystick
                num_axes = joysticks[0].get_numaxes()
                
                # Obtenez les vecteurs des axes X et Y pour chaque axe
                for k in range(num_axes):
                    axis = joysticks[0].get_axis(k)
                    if k == 0:  # axe X
                        joystick_vec.x=axis
                    elif k == 1:  # axe Y
                        joystick_vec.y=axis

            elif i.type == py.KEYDOWN:
                if i.key == K_SPACE:
                    players[0].chunk_border=not players[0].chunk_border
                #elif i.key == K_p:
                #    players[0].zoom_out+=1
                #elif i.key == K_m:
                #    players[0].zoom_out = max(1, players[0].zoom_out-1)
                elif i.key == K_o:
                    players[0].render_distance+=2
                elif i.key == K_l:
                    players[0].render_distance = max(1, players[0].render_distance-2)
                elif i.key == K_i:
                    players[0].speed+=2
                elif i.key == K_k:
                    players[0].speed-=2
                elif i.key == K_ASTERISK:
                    toggle_hitbox()
                elif i.key == K_LCTRL:
                    players[0].speed=0.85
                elif i.key == K_BACKSPACE:
                    players[0].texture=next_texture()
                    if players[0].dir=="u":
                        players[0].current_texture=players[0].texture[0]
                    if players[0].dir=="r":
                        players[0].current_texture=players[0].texture[1]
                    if players[0].dir=="d":
                        players[0].current_texture=players[0].texture[2]
                    if players[0].dir=="l":
                        players[0].current_texture=players[0].texture[3]
                elif i.key ==K_e:
                    if players[0].dir=="u":
                        players[0].world.get_Obj(players[0].pos+(0,-10)).on_interact(players[0].world,players[0])

                    if players[0].dir=="r":
                        players[0].world.get_Obj(players[0].pos+(10,0)).on_interact(players[0].world,players[0])

                    if players[0].dir=="d":
                        players[0].world.get_Obj(players[0].pos+(0,10)).on_interact(players[0].world,players[0])

                    if players[0].dir=="l":
                        players[0].world.get_Obj(players[0].pos+(-10,0)).on_interact(players[0].world,players[0])
                
            elif i.type ==py.KEYUP:
                if i.key == py.K_LCTRL:
                    players[0].speed=0.5  
                
        pygame_events=[]
        if joystick_count:
            players[0].pos+=joystick_vec*2*players[0].speed
            players[0].update_texture(joystick_vec)

        pushed_keys=py.key.get_pressed()
        if pushed_keys[py.K_q]:
            players[0].left()
        if pushed_keys[py.K_d]:
            players[0].right()
        if pushed_keys[py.K_z]:
            players[0].up()
        if pushed_keys[py.K_s]:
            players[0].down()


        players[0].world.update()

        # tps moyenizer
        moy_fps = 1 / (time() - loop_start) * loop_count if loop_count > 10 else TPS_MAX
        to_sleep = (1 / TPS_MAX - (time() - iter_start)) - (1 - (moy_fps / TPS_MAX))
        if to_sleep > 0: sleep(to_sleep)

        g_tps = 1 / (time() - loop_start) * loop_count

    running_dict["server"] = False

def main():
    global pygame_events
    start_new_thread(play_sound, ("nymphe-echo-demo1.flac",))
    init_worlds()
    starting_world=Worlds["bed_room"]
    players.append(Character("Jean","Magie","pouffsoufle",None,None,None,POUFSOUFFLE_TEXTURES_0,None,50,50,starting_world))

    players[0].zoom_out = 1
    players[0].render_distance=3

    start_new_thread(server_thread, ())

    arial=py.font.SysFont("Arial",25,False,False)
    fps = 0
    
    while running_dict["global"] and running_dict["graphic"] and running_dict["server"]:
        start_time = time()
        pygame_events=py.event.get()
        for i in pygame_events:
            if i.type == py.QUIT:
                running_dict["global"]=False
        
                
        players[0].world: World = players[0].world
        players[0].world.show(screen, players[0].zoom_out)
 
        screen.blit(arial.render(f"fps: {int(fps)}", False, (255, 0, 0)), (0, 0))
        screen.blit(arial.render(f"mid tps: {int(g_tps)}", False, (255, 0, 0)), (0, 30))
        screen.blit(arial.render(str(players[0].pos.floor()), False, (255, 0, 0)), (0, 60))
        screen.blit(arial.render(str(players[0].world.get_Chunk_from_pos(players[0].pos).pos), False, (255, 0, 0)), (0, 90))

        py.display.update()
        t=time()
        if  t - start_time <1/60:
            sleep(1/60 -t+start_time)
        fps = 1/(time()-start_time)


main()