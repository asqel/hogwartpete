from events import *
from objs import *

def gen_grass(players, chunk):
    for i in range(20):
        for k in range(20):
            if chunk.world.name == "exterior":
                chunk.background_obj.append(Objs["Grass"](i*50 + chunk.top_left_pos.x, k*50 + chunk.top_left_pos.y))

#registerEvent(Event(Event_on_chunk_generate, gen_grass))