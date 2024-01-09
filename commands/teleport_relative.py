from commands import *
import entities as ent

tp_cmd = new_struct_command()

def func_tp_to(args : list[Token_arg], user : 'ent.Character'):
    user.pos.x += args[1].value
    user.pos.y += args[2].value
def func_tp_who_to(args : list[Token_arg], user : 'ent.Character'):
    if args[1].value == "@self":
        user.pos.x += args[2].value
        user.pos.y += args[3].value
    else:
        for i in ent.players:
            if i.pseudo  == args[1].value:
                i.pos.x += args[2].value
                i.pos.y += args[3].value
                break
        raise Exception("ERROR command /tpr player not found")


add_arg(tp_cmd, (Cmd_identifier, Cmd_int, Cmd_int), func_tp_to)
add_arg(tp_cmd, (Cmd_identifier, Cmd_identifier, Cmd_int, Cmd_int), func_tp_who_to)
register_command("/tpr", tp_cmd)