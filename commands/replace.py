from commands import *
from uti import *
import entities as ent


tp_cmd = new_struct_command()

def func_replace_at(args : list[Token_arg], user : 'ent.Character'):
    import items as it
    import world as wo
    import objs as ob
    x = args[1].value
    y = args[2].value
    plan = args[3].value
    obj = args[4].value
    if obj not in ob.Objs.keys():
        raise Exception(f"ERROR command replace unknow {obj} Object")
    if plan == "background":
        user.world : wo.World = user.world
        if user.world.get_background_Obj(Vec(x, y)).id == "Air":
            if obj != "Air":
                user.world.add_background_Obj(ob.Objs[obj](x, y))
        else:
            bg_obj= user.world.get_Chunk_from_pos(Vec(x, y)).background_obj
            for i in range(len(bg_obj)):
                if bg_obj[i].pos.x == x and bg_obj[i].pos.y == y:
                    if obj != "Air":
                        bg_obj[i] == ob.Objs[obj](x, y)
                    else:
                        bg_obj.pop(i)
                        break
    elif plan == "foreground":
        user.world : wo.World = user.world
        if user.world.get_Obj(Vec(x, y)).id == "Air":
            if obj != "Air":
                user.world.add_Obj(ob.Objs[obj](x, y))
        else:
            user.world.remove_obj_at(Vec(x, y))
            if obj != "Air":
                user.world.add_Obj(ob.Objs[obj](x, y))
    else:
        raise Exception(f"ERROR command replace unknown parameter {plan}")


add_arg(tp_cmd, (Cmd_identifier, Cmd_int, Cmd_int, Cmd_identifier, Cmd_identifier), func_replace_at)
register_command("/replace", tp_cmd)