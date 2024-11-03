import interface
from random import randint
from math import cos, sin
import key_map as key
import saves
import pygame as py
import entities

from uti.textures import *
import saves 

class Choose_save(interface.Gui):
	def __init__(self, player: 'entities.Character') -> None:
		super().__init__("Choose_save", {}, player)
		self.saves : list[str] = saves.get_saves_names()
		self.saves.append(None)
		self.save_idx = 0
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
		for i in events:
			if key.is_event_key_pressed(i, key.t_mov_down):
				if self.save_idx < len(self.saves) - 1:
					self.save_idx += 1
			elif key.is_event_key_pressed(i, key.t_mov_up):
				if self.save_idx > 0:
					self.save_idx -= 1
			elif key.is_event_key_pressed(i, key.t_use_object):
				if self.save_idx < len(self.saves) - 1:
					saves.load_save(self.player, self.saves[self.save_idx])
					self.player.close_gui()
				else:
					self.player.close_gui()
					self.player.open_gui("Create_save")
			
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
		screen.blit(Textures["other"]["choose_save"], (0, 0))
		text = interface.main_font_40.render("choose your save", 0, (116, 44, 156))
		screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, 30))

		#render save names
		idx =  self.save_idx
		while idx + 6 >= len(self.saves):
			if idx == 0:
				break;
			idx -= 1
		for i in range(idx, min(idx + 7, len(self.saves))):
			x = 350
			y = 81 + 63 * (i - idx) + 10
			if self.saves[i] != None and i < idx + 6:
				if self.save_idx == i:
					text = interface.main_font_40.render(self.saves[i], 0, (80, 140, 93))
				else:
					text = interface.main_font_40.render(self.saves[i], 0, (255, 255, 255))
			else:
				if self.save_idx == i:
					text = interface.main_font_40.render("... +", 0, (80, 140, 93))
				else:
					text = interface.main_font_40.render("...", 0, (255, 255, 255))
			screen.blit(text, (x, y))
	


interface.registerGui(Choose_save)