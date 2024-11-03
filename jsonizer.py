import json
import world
import objs
import events
from uti.vector import *
from uti.hitbox import *
import entities
import os

path=os.path.abspath(".")+"/worlds"
dir_path =os.path.abspath(".")

def save_vec(pos:Vec):
    return (pos.x,pos.y)

def save_hitbox(hit:Hitbox):
    return {
        "type":hit.type,
        "h":hit.height,
        "w":hit.width,
        "r":hit.radius,
        "pos":save_vec(hit.pos) 
    } if hit else None

def save_Obj(o : objs.Obj):
    if o is None:
        return 0
    if o.id == "Air":
        return 0
    return {
        "data":o.data,
        "hitbox":save_hitbox(o.hitbox),
        "id":o.id,
    }
    
def save_chunk(c:"world.Chunk"):
    d = {
        "background_obj":[[0 for i in range(20)] for k in range(20)],   
        "Dyn_Obj":[[0 for i in range(20)] for k in range(20)],
        "entities":[],
        "hitboxes":[save_hitbox(i) for i in c.hitboxes],
        "objects":[[0 for i in range(20)] for k in range(20)],
        "pos":save_vec(c.pos),
        "top-left":save_vec(c.top_left_pos)
    }
    for i in range(20):
        for k in range(20):
            d["background_obj"][i][k] = save_Obj(c.background_obj[i][k])
            d["objects"][i][k] = save_Obj(c.objects[i][k])
            d["Dyn_Obj"][i][k] = save_Obj(c.dyn_objects[i][k])
    return d


def save_world(w:"world.World"):
    if not os.path.exists(f"./worlds/{w.name}"):
        os.makedirs(f"./worlds/{w.name}")
    if not os.path.isdir(f"./worlds/{w.name}"):
        os.makedirs(f"./worlds/{w.name}")
    for i in w.loaded_chunks.keys():
        x ,y = i
        with open(f"./worlds/{w.name}/c_{x}_{y}.json", "w+") as f:
            json.dump(save_chunk(w.loaded_chunks[i]), f)
    
def load_vec(d):
    return Vec(d[0],d[1])

def load_hitbox(d):
    return HITBOX_0x0 if d is None else Hitbox(d["type"],load_vec(d["pos"]),d["r"],d["w"],d["h"]) 
        
           
def load_obj(d, x, y):
    if d is None or d == 0:
        return None
    if d["id"] not in objs.Objs.keys():
        return None
    x = objs.Objs[d["id"]](x, y)
    x.data=d["data"]
    x.hitbox=load_hitbox(d["hitbox"])
    return x

def load_chunk(d, w):
    c = world.Chunk(load_vec(d["pos"]), w)
    for i in range(20):
        for k in range(20):
            d["background_obj"][i][k] = load_obj(d["background_obj"][i][k], c.top_left_pos.y + k * 50, c.top_left_pos.y + i * 50)
            d["objects"][i][k] = load_obj(d["objects"][i][k], c.top_left_pos.y + k * 50, c.top_left_pos.y + i * 50)
            d["Dyn_Obj"][i][k] = load_obj(d["Dyn_Obj"][i][k], c.top_left_pos.y + k * 50, c.top_left_pos.y + i * 50)
    c.objects = d["objects"]
    c.dyn_objects = d["Dyn_Obj"]
    c.background_obj = d["background_obj"]
    c.hitboxes = [load_hitbox(i) for i in d["hitboxes"]] 
    c.top_left_pos = load_vec(d["top-left"])
    return c