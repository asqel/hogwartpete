import pygame as py
from obj import *
class World:
    def __init__(self,name,backgroung:py.surface,objs:list[Obj]=list()):
        self.name=name
        self.bg=backgroung
        self.objects=objs