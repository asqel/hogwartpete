import commands as cmd
import entities

tp_cmd = cmd.new_struct_command()

def func_tp_to(args : list[cmd.Token_arg], user : 'entities.Character'):
    user.pos.x = args[1].value
    user.pos.y = args[2].value
def func_tp_who_to(args : list[cmd.Token_arg], user : 'entities.Character'):
    if args[1].value == "@self":
        user.pos.x = args[2].value
        user.pos.y = args[3].value
    else:
        for i in entities.players:
            if i.pseudo  == args[1].value:
                i.pos.x = args[2].value
                i.pos.y = args[3].value
                break
        raise Exception("ERROR command /tp player not found")


cmd.add_arg(tp_cmd, (cmd.Cmd_identifier, cmd.Cmd_int, cmd.Cmd_int), func_tp_to)
cmd.add_arg(tp_cmd, (cmd.Cmd_identifier, cmd.Cmd_identifier, cmd.Cmd_int, cmd.Cmd_int), func_tp_who_to)
cmd.register_command("/tp", tp_cmd)