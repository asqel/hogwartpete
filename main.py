#Hogwarts Legacy en version pétée by Léa et Asqel
import pygame as py
import textures as tx
from character import *
from time import time ,sleep

screen=py.display.set_mode((500,500))

main_player=Character("Jean","magie","pouffsoufle",None,None,None,None,tx.Textures["src/player/p1.png"],None,0,0,None)

def main():
    while 1:
        screen.fill((0,255,255))
        t0=time()
        e=py.event.get()
        for i in e:
            if i.type == py.QUIT:
                exit(0)
        keys=py.key.get_pressed()
        if keys[py.K_z]:
            main_player.up()
        if keys[py.K_q]:
            main_player.left()
        if keys[py.K_s]:
            main_player.down()
        if keys[py.K_d]:
            main_player.right()


        screen.blit(main_player.texture,(main_player.position.x,main_player.position.y))

        py.display.update()
        t=time()-t0
        if t<1/60:
            sleep(1/60-t)
        

main()
