#Hogwarts Legacy en version pétée by Léa et Asqel
import pygame as py
import textures as tx

screen=py.display.set_mode((500,500))

def main():
    while 1:
        e=py.event.get()
        for i in e:
            pass



        py.display.update()
        
screen.fill((0,255,255))

screen.blit(tx.Textures["src/player/p1.png"],(0,0))
screen.blit(py.transform.flip(tx.Textures["src/player/p1.png"],1,0),(16,16))
py.display.update()
while 1:
    pass
