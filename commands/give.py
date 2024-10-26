import commands as cmd
import entities

tp_cmd = cmd.new_struct_command()

def func_give(args : list[cmd.Token_arg], user : 'entities.Character'):
    if args[1].value < 0:
        raise Exception("ERROR command give cannot give negative number of item")
    if args[1].value == 0:
        return
    #if not user.add_item(it.items[args[2].value](args[1].value)):
    #    user.world.spawn_item(it.items[args[2].value](args[1].value), user.pos)

def func_give_who(args : list[cmd.Token_arg], user : 'entities.Character'):
    if args[2].value < 0:
        raise Exception("ERROR command give cannot give negative number of item")
    if args[2].value == 0:
        return
    if args[1].value == "@self":
        ...
        #if not user.add_item(it.items[args[3].value](args[2].value)):
        #    user.world.spawn_item(it.items[args[3].value](args[2].value), user.pos)
    else:
        for i in entities.players:
            if i.pseudo == args[1].value:
                ...
                #if not i.add_item(it.items[args[3].value](args[2].value)):
                #    i.world.spawn_item(it.items[args[3].value](args[2].value), user.pos)
                break

cmd.add_arg(tp_cmd, (cmd.Cmd_identifier, cmd.Cmd_int, cmd.Cmd_identifier), func_give)
cmd.add_arg(tp_cmd, (cmd.Cmd_identifier, cmd.Cmd_identifier, cmd.Cmd_int, cmd.Cmd_identifier), func_give_who)
cmd.register_command("/give", tp_cmd)