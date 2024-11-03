import entities
import os
import json
import world
from uti.vector import *
import quests
from uti.textures import *

save_dir=os.path.abspath(".")+"/saves"

if not os.path.exists(save_dir):
	os.mkdir(save_dir)

def save_player(player : 'entities.Character') -> None:
	res = {}
	res["data"] = player.data
	res["world_name"] = player.world.name
	res["world_is_outside"] = player.world.is_outside
	res["world_mod"] = player.world.mod
	res["world_bg"] = player.world.bg
	res["quest"] = {}
	res["quest_completed"] = {}
	res["pos"] = [player.pos.x, player.pos.y];
	for i in player.quests.keys():
		res["quest"][i] = player.quests[i].json()
	for i in player.quests_completed.keys():
		res["quest_completed"][i] = player.quests_completed[i].json()
	with open(save_dir+f"/{player.save_name}.json", "w+") as f:
        	json.dump(res, f)
	
def load_save(player: 'entities.Character', save_name: str):
	player.save_name = save_name
	with open(save_dir+f"/{player.save_name}.json", "r") as f:
		d : dict = json.load(f)
		player.data = d["data"]
		player.pos = Vec(d["pos"][0], d["pos"][1])
		player.world = world.World(d["world_name"], d["world_bg"], d["world_mod"], d["world_is_outside"])
		player.quests = d["quest"]
		player.quests_completed = d["quest_completed"]
		for i in player.quests.keys():
			player.quests[i] = quests.Quest(None, None, None, None, None).from_json(player.quests[i])
		for i in player.quests.keys():
			player.quests_completed[i] = quests.Quest(None, None, None, None, None).from_json(player.quests_completed[i])



def get_saves_names() -> list[str]:
    l = []
    for i in os.listdir(os.path.join(path, "saves")):
        l.append(i.removesuffix(".json"))
    return l

def create_character(save_name: str) -> 'entities.Character':
	res : entities.Character = entities.Character(POUFSOUFFLE_TEXTURES_0, 100, 0, world.World("starting", (0, 0, 0)) , save_name)
	return res
