import commands as cmd
import entities
import objs
import world

from uti.vector import *


tp_cmd = cmd.new_struct_command()

def func_replace_at(args : list[cmd.Token_arg], user : 'ent.Character'):
    x = args[1].value
    y = args[2].value
    plan = args[3].value
    obj = args[4].value
    if obj not in objs.Objs.keys():
        raise Exception(f"ERROR command replace unknow {obj} Object")
    if plan == "background":
        if user.world.get_background_Obj(Vec(x, y)).id == "Air":
            if obj != "Air":
                user.world.add_background_Obj(objs.Objs[obj](x, y))
        else:
            bg_obj= user.world.get_Chunk_from_pos(Vec(x, y)).background_obj
            for i in range(len(bg_obj)):
                if bg_obj[i].pos.x == x and bg_obj[i].pos.y == y:
                    if obj != "Air":
                        bg_obj[i] == objs.Objs[obj](x, y)
                    else:
                        bg_obj.pop(i)
                        break
    elif plan == "foreground":
        if user.world.get_Obj(Vec(x, y)).id == "Air":
            if obj != "Air":
                user.world.add_Obj(objs.Objs[obj](x, y))
        else:
            user.world.remove_obj_at(Vec(x, y))
            if obj != "Air":
                user.world.add_Obj(objs.Objs[obj](x, y))
    else:
        raise Exception(f"ERROR command replace unknown parameter {plan}")


cmd.add_arg(tp_cmd, (cmd.Cmd_identifier, cmd.Cmd_int, cmd.Cmd_int, cmd.Cmd_identifier, cmd.Cmd_identifier), func_replace_at)
cmd.register_command("/replace", tp_cmd)