from commands import *
import entities as ent
import items as it

echo_cmd = new_struct_command()

def echo_func(args, user):
    raise Exception(args[1].value)


add_arg(echo_cmd, (Cmd_identifier, Cmd_identifier), echo_func)
add_arg(echo_cmd, (Cmd_identifier, Cmd_str), echo_func)
register_command("/echo", echo_cmd)