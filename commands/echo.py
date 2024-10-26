import commands as cmd

echo_cmd = cmd.new_struct_command()

def echo_func(args, user):
    raise Exception(args[1].value)


cmd.add_arg(echo_cmd, (cmd.Cmd_identifier, cmd.Cmd_identifier), echo_func)
cmd.add_arg(echo_cmd, (cmd.Cmd_identifier, cmd.Cmd_str), echo_func)
cmd.register_command("/echo", echo_cmd)