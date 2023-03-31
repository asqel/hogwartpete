#Hogwarts Legacy en version pétée by Léa et Asqel
import pygame as py
import uti.textures as tx
from entities import *
from time import time ,sleep
from world import *
from spells.unforgivable_curses import *


screen=py.display.set_mode((500,500))

worlds[0].registerPlayer(Character("Jean","Magie","pouffsoufle",None,None,None,None,tx.Textures["player"]["harry_potter.png"],None,0,0))
worlds[0].registerEntity(Npc("choixpeau","",tx.Textures["npc"]["choixpeau.png"],None,20,20))

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
            players[0].up()
        if keys[py.K_q]:
            players[0].left()
        if keys[py.K_s]:
            players[0].down()
        if keys[py.K_d]:
            players[0].right()
        if keys[py.K_SPACE]:
            Avada_kedavra(players[0].uuid).shoot(worlds[0],Vec(py.mouse.get_pos()))

        worlds[0].show(screen)
        worlds[0].update()
        py.display.update()
        t=time()-t0
        if t<1/60:
            sleep(1/60-t)
        

main()
