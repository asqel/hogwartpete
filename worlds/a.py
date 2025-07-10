import json as j
import os

d = {}
name = "rdc"
with open(f"./{name}.json","r") as f:
    d = j.load(f)

for i in d["chunks"].keys():
    for k in d["chunks"][i].keys():
        path = f"./{name}/c_{i}_{k}.json"
        with open(path,"w+") as f:
            j.dump(d["chunks"][i][k],f)