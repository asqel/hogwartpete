import json
from world import *
from objs import *
from uti import *
import os

path=os.path.dirname(os.path.abspath(__file__))+"/worlds"
dir_path =os.path.dirname(os.path.abspath(__file__))

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
        "transparent":o.transparent
    }
    
    
def save_chunk(c:"Chunk"):
    return {
        "background_obj":[save_Obj(i) for i in c.background_obj] ,   
        "Dyn_Obj":[],
        "entities":[],
        "hitboxes":[save_hitbox(i) for i in c.hitboxes],
        "objects":[save_Obj(i) for i in c.objects],
        "pos":save_vec(c.pos),
        "top-left":save_vec(c.top_left_pos)
    }


def save_world(w:"World"):
    d={
        "background":[w.bg[0],w.bg[1],w.bg[2]],
        "chunks":{}
    }
    for i in w.chuncks.keys():
        d["chunks"][i]={}
        for k in w.chuncks[i].keys():
            d["chunks"][i][k]=save_chunk(w.chuncks[i][k])
    with open(f"{path}/{w.name}.json","w") as f:
        json.dump(d,f)
    
def load_vec(d):
    return Vec(d[0],d[1])

def load_hitbox(d):
    return HITBOX_0x0 if d is None else Hitbox(d["type"],load_vec(d["pos"]),d["r"],d["w"],d["h"]) 
        
           
def load_obj(d):
    x=Objs[d["id"]](d["pos"][0],d["pos"][1])
    x.toplayer=d["toplayer"]
    x.transparent=d["transparent"]
    x.data=d["data"]
    x.hitbox=load_hitbox(d["hitbox"])
    return x
         
def load_chunk(d,w):
    import world as wo
    c=wo.Chunk(load_vec(d["pos"]),w)    
    c.background_obj=[load_obj(i) for i in d["background_obj"]]   
    c.hitboxes=[load_hitbox(i) for i in d["hitboxes"]] 
    c.objects=[load_obj(i) for i in d["objects"]] 
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
    return w
