import json
from world import *
from objs import *
from uti import *
from events import *
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

def save_Obj(o:Obj):
    return {
        "pos":save_vec(o.pos),
        "data":o.data,
        "hitbox":save_hitbox(o.hitbox),
        "id":o.id,
        "toplayer":o.toplayer,
    }
    
def save_dyn_Obj(o : Dynamic_Obj):
    return {
        "pos":save_vec(o.pos),
        "data":o.data,
        "hitbox":save_hitbox(o.hitbox),
        "id":o.id,
        "toplayer":o.toplayer,
    }
    
def save_chunk(c:"Chunk"):
    return {
        "background_obj":[save_Obj(i) for i in c.background_obj] ,   
        "Dyn_Obj":[save_dyn_Obj(i) for i in c.dyn_objects],
        "entities":[],
        "hitboxes":[save_hitbox(i) for i in c.hitboxes],
        "objects":[save_Obj(i) for i in c.objects],
        "pos":save_vec(c.pos),
        "top-left":save_vec(c.top_left_pos)
    }


def save_world(w:"World"):
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
        
           
def load_obj(d):
    if d["id"] not in Objs.keys():
        return None
    x=Objs[d["id"]](d["pos"][0],d["pos"][1])
    x.toplayer=d["toplayer"]
    x.data=d["data"]
    x.hitbox=load_hitbox(d["hitbox"])
    return x
         
def load_Dyn_obj(d):
    if d["id"] not in Dynamic_Objs.keys():
        return None
    x=Dynamic_Objs[d["id"]](d["pos"][0],d["pos"][1])
    x.toplayer=d["toplayer"]
    x.data=d["data"]
    x.hitbox=load_hitbox(d["hitbox"])
    return x

def load_chunk(d,w):
    import world as wo
    c=wo.Chunk(load_vec(d["pos"]),w)    
    for i in d["background_obj"]:
        o = load_obj(i)
        if o:
            c.background_obj.append(o)
    c.hitboxes=[load_hitbox(i) for i in d["hitboxes"]] 
    for i in d["objects"]:
        o = load_obj(i)
        if o:
            c.objects.append(o)
    for i in d["Dyn_Obj"]:
        o = load_Dyn_obj(i)
        if o:
            c.dyn_objects.append(o)
    c.top_left_pos=load_vec(d["top-left"])
    return c

def load_world(name:str, mod = ""):
    import world as wo
    d={}
    if mod != "":
        with open(f"{dir_path}/mods/{mod}/worlds/{name}.json") as f:
            d=json.load(f)
    else : 
        with open(f"{path}/{name}.json") as f:
            d=json.load(f)
    w=wo.World(name,d["background"])
    w.chuncks={}
    for i in d["chunks"].keys():
        for k in d['chunks'][i].keys():
            x=int(i)
            y=int(k)
            w.get_Chunk_at(Vec(x,y))
            w.chuncks[x][y]=load_chunk(d["chunks"][i][k],w)#here i,k because str in json
    for i in events[Event_on_world_chunk]:
        i.function(players, w)
    return w
