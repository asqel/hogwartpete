import pygame as py
import json

key_map = {}

"""
keys.json
{
    trigger: keyname # str: str
}
trigger:
"""
t_mov_up = "mov up"
t_mov_down = "mov down"
t_mov_left = "mov left"
t_mov_right = "mov right"
t_proteo = "protego"
t_use_item = "use item"
t_drop_item = "drop item"
t_use_object = "use object"
t_sprint = "sprint"
t_slot1 = "slot 1"
t_slot2 = "slot 2"
t_slot3 = "slot 3"
t_slot4 = "slot 4"
t_slot5 = "slot 5"
t_slot6 = "slot 6"
t_slot7 = "slot 7"
t_slot8 = "slot 8"
t_slot9 = "slot 9"
t_slot10 = "slot 10"
t_open_chat = "open chat"

key_entries = [
    t_mov_up,
    t_mov_down,
    t_mov_left,
    t_mov_right,
    t_proteo,
    t_use_item,
    t_drop_item,
    t_use_object,
    t_sprint,
    t_slot1,
    t_slot2,
    t_slot3,
    t_slot4,
    t_slot5,
    t_slot6,
    t_slot7,
    t_slot8,
    t_slot9,
    t_slot10,
    t_open_chat
]
"""
key names:
    a-z
    0-9
    lctrl
    rctrl
    lshift
    rshift
    tab
    space
    enter
    M1 (lclick)
    M2 (midclick)
    M3 (rclick)
"""
def str_to_code(key : str):
    key = key.lower()
    if key in "abcdefghijklmnopqrstuvwxyz":
        return py.key.key_code(key)
    if key in "1234567890":
        return py.key.key_code(key)
    if key == "lctrl":
        return py.K_LCTRL
    if key == "rctrl":
        return py.K_RCTRL
    if key == "lshift":
        return py.K_LSHIFT
    if key == "rshift":
        return py.K_RSHIFT
    if key == "tab":
        return py.K_TAB
    if key == "space":
        return py.K_SPACE
    if key == "enter":
        return py.K_RETURN
    if key == "m1":
        return (1, 1)
    if key == "m2":
        return (1, 2)
    if key == "m3":
        return (1, 3)
def load_keys():
    global key_map
    le_json = {}
    with open("./key_map.json","r") as f:
        le_json = json.load(f)
    for i in le_json.keys():
        key_map[i]= le_json[i]
    for i in key_map.keys():
        key_map[i]= str_to_code(key_map[i])
    for i in key_entries:
        if i not in key_map.keys():
            key_map[i] = None
    return key_map

def register_key_entry(key_entry : str):
    key_entries.append(key_entry)

