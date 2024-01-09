from entities import *



def save_player(player : Character) -> None:
	res = {}
	res["special_data"] = {}
	res["special_data"]["speed"] = player.speed
	res["data"] = player.data