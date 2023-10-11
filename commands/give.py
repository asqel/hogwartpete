from commands import *
import entities as ent
import items as it

tp_cmd = new_struct_command()

def func_give(args : list[Token_arg], user : 'ent.Character'):
    if args[1].value < 0:
        raise Exception("ERROR command give cannot give negative number of item")
    if args[1].value == 0:
        return
    if not user.add_item(it.items[args[2].value](args[1].value)):
        user.world.spawn_item(it.items[args[2].value](args[1].value), user.pos)

def func_give_who(args : list[Token_arg], user : 'ent.Character'):
    if args[2].value < 0:
        raise Exception("ERROR command give cannot give negative number of item")
    if args[2].value == 0:
        return
    if args[1].value == "@self":
        if not user.add_item(it.items[args[3].value](args[2].value)):
            user.world.spawn_item(it.items[args[3].value](args[2].value), user.pos)
    else:
        for i in ent.players:
            if i.pseudo == args[1].value:
                if not i.add_item(it.items[args[3].value](args[2].value)):
                    i.world.spawn_item(it.items[args[3].value](args[2].value), user.pos)
                break

add_arg(tp_cmd, (Cmd_identifier, Cmd_int, Cmd_identifier), func_give)
add_arg(tp_cmd, (Cmd_identifier, Cmd_identifier, Cmd_int, Cmd_identifier), func_give_who)
register_command("/give", tp_cmd)