
import interface
from random import randint
from math import cos, sin
import key_map as key
import saves
import pygame as py
import entities

from uti.textures import *
import saves 

class Create_save(interface.Gui):
	def __init__(self, player: 'entities.Character') -> None:
		super().__init__("Choose_save", {}, player)
		self.particles = []
		for i in range(100):
			self.particles.append({
				"x" : randint(0, 1023),
				"y" : randint(0, 575),
			})
			angle = randint(0, 359)
			self.particles[i]["vx"] = cos(angle)
			self.particles[i]["vy"] = sin(angle)
			self.particles[i]["col"] = (randint(0, 255), randint(0, 255), randint(0, 255))
			self.player = player
		
		
	def tick(self, events: list[py.event.Event]):
		...
			
	def draw(self, screen):
		screen.fill((0,0,0))
		p = 0
		for i in self.particles:
			if 1024 > i["x"] >= 0 and 885 > i["y"] >= 0:
				py.draw.circle(screen, i["col"], (int(i["x"]), int(i["y"])), 3)
				i["x"] += i["vx"] * randint(1, 3)
				i["y"] += i["vy"] * randint(1, 3)
			else:
				self.particles[p]["vx"] *= -1;
				self.particles[p]["vy"] *= -1;
				self.particles[p]["col"] = (randint(0, 255), randint(0, 255), randint(0, 255))
				self.particles[p]["x"] += i["vx"] * 2
				self.particles[p]["y"] += i["vy"] * 2
				angle = randint(0, 359)
				self.particles[p]["vx"] = cos(angle)
				self.particles[p]["vy"] = sin(angle)
			p += 1
		screen.blit(Textures["other"]["create_save"], (0, 0))
		text = interface.main_font_40.render("create your save", 0, (116, 44, 156))
		screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, 30))

	


interface.registerGui(Create_save)