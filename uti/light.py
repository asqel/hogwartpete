from uti.vector import *
import pygame as py


class Light:
	def __init__(self, texture : py.Surface, pos : Vec) -> None:
		self.texture = texture
		self.pos = pos