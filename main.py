#Hogwarts Legacy en version pétée by Léa et Asqel
import pygame as py
from pygame.locals import *

import uti.textures as tx
from entities import *
from time import time ,sleep
from world import *
from spells.unforgivable_curses import *
from spells import *
print(__package__)
py.font.init()
screen=py.display.set_mode((500,500))

a=py.font.SysFont("Arial",25,False,False)

worlds[0].addPlayer(Character("Jean","Magie","pouffsoufle",None,None,None,None,[tx.Textures["player"]["mc_back.png"], tx.Textures["player"]["mc_right_0_poufsouffle.png"],tx.Textures["player"]["mc_front_poufsouffle.png"],tx.Textures["player"]["mc_left_0_poufsouffle.png"]],None,0,0))
worlds[0].addEntity(Npc("choixpeau","",tx.Textures["npc"]["choixpeau.png"],None,20,20))

def main():
    TPS=0
    
    py.joystick.init()
    joystick_count=py.joystick.get_count()
    if joystick_count:
        joysticks = []
        for i in range(joystick_count):
            joystick = py.joystick.Joystick(i)
            joystick.init()
            joysticks.append(joystick)

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
                for i in range(num_axes):
                    axis = joysticks[0].get_axis(i)
                    if i == 0:  # axe X
                        joystick_vec.x=axis
                    elif i == 1:  # axe Y
                        joystick_vec.y=axis
        if joystick_count:
            players[0].pos+=joystick_vec*2
            players[0].update_texture(joystick_vec)
        keys=py.key.get_pressed()
        if keys[py.K_q]:
            players[0].left()
        if keys[py.K_d]:
            players[0].right()
        if keys[py.K_z]:
            players[0].up()
        if keys[py.K_s]:
            players[0].down()
        if keys[py.K_SPACE]:
            Avada_kedavra(players[0].uuid).shoot(worlds[0],Vec(py.mouse.get_pos()))
        
        worlds[0].show(screen)
        worlds[0].update()
        screen.blit(a.render(str(int(TPS)),False,(255,0,0)),(0,0))
        
        py.display.update()
        t=time()-t0
        
        if t<1/60:
            sleep(1/60-t)
        TPS=1/(time()-t0)
        

main()
