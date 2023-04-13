#Hogwarts Legacy en version pétée by Léa et Asqel
import pygame as py
from pygame.locals import *

from uti.textures import *
from uti.sound import play_sound
from entities import *
from time import time ,sleep
from world import *

from _thread import start_new_thread

py.joystick.init()
py.font.init()

def main():
    start_new_thread(play_sound, ("nymphe-echo-demo1.flac",))
    TPS=0
    py.display.init()

    arial=py.font.SysFont("Arial",25,False,False)
    
    starting_world=newWorld("first_world",(194, 154, 128))
    players.append(Character("Jean","Magie","pouffsoufle",None,None,None,[Textures["player"]["mc_back.png"], Textures["player"]["mc_right_0_poufsouffle.png"], Textures["player"]["mc_front_poufsouffle.png"], Textures["player"]["mc_left_0_poufsouffle.png"]],None,0,0,starting_world))
    
    players[0].speed=1
    players[0].zoom_out = 1
    players[0].render_distance=3

    joystick_count=py.joystick.get_count()
    if joystick_count:
        joysticks = []
        for i in range(joystick_count):
            joystick = py.joystick.Joystick(i)
            joystick.init()
            joysticks.append(joystick)
            
    fps_cooldown=1
    FPS_MAX=1/60
    
    while 1:
        screen.fill((0,255,255))
        t0=time()
        e=py.event.get()
        joystick_vec=Vec(0,0)
        for i in e:
            if i.type == py.QUIT:
                exit(0)
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
                elif i.key == K_p:
                    players[0].zoom_out+=1
                elif i.key == K_m:
                    players[0].zoom_out = max(1, players[0].zoom_out-1)
                elif i.key == K_o:
                    players[0].render_distance+=2
                elif i.key == K_l:
                    players[0].render_distance = max(1, players[0].render_distance-2)
                

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

        players[0].world:World=players[0].world
        players[0].world.show(screen, players[0].zoom_out)
        players[0].world.update()
        
        
        screen.blit(arial.render(str(int(TPS)),False,(255,0,0)),(0,0))
        screen.blit(arial.render(str(players[0].pos.floor()),False,(255,0,0)),(0,30))
        screen.blit(arial.render(str(players[0].world.getChunkfromPos(players[0].pos).pos),False,(255,0,0)),(0,60))
        
        py.display.update()
        t=time()-t0
        
        if t<FPS_MAX:
            sleep(FPS_MAX-t)
        
        fps_cooldown-=1
        if not fps_cooldown:
            TPS=1/(time()-t0)
            fps_cooldown=5
        
        

main()