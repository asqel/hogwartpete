import events
import objs
from uti.vector import *

pumkin_pos = [
	(-550, -1600),
	(300, 400)
]

def place_pumkin(players , world):
	if world.name != "exterior":
		return
	for i in pumkin_pos:
		if world.get_Obj(Vec(*i)).id != "Air":
			continue
		world.add_Obj(objs.Objs["Pumpkin"](*i))

#registerEvent(Event(Event_on_world_load, place_pumkin))