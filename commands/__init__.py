from typing import TypedDict

Arg_type = int
Cmd_None = 0
Cmd_int = 1
Cmd_str = 2
Cmd_float = 3
Cmd_bool = 4
Cmd_identifier = 5

def types_to_str(_type : int):
    if _type == Cmd_None:
        return "None"
    if _type == Cmd_int:
        return "int"
    if _type == Cmd_bool:
        return "bool"
    if _type == Cmd_float:
        return "float"
    if _type == Cmd_str:
        return "str"
    if _type == Cmd_identifier:
        return "id"

function = type(print)

Cmd_args = tuple[Arg_type, ...]


"""
Cmd_int : base10 int / hex int (0x notation)  
            3 / 0x16
cmd_None : None
cmd_float : base10 float 
            3.14
cmd_str : a string surrounded by single or double quote 
            'hi' / "hello"
cmd_bool : a boolean written as (0b / 1b) / (False / True) / (false / true)
cmd_identifier : anything that is not surrounded by quotes or doubleee quotes
                    and which correspond to no other type, restrictions :
                                                cannot start with a number
                                                cannot contains quotes / double quotes
                                                cannot contain spaces

special identifier:
    @self : user
    @all : every player
    @entities : every entities

"""
class Token_arg:
    def __init__(self, _type : Arg_type, value) -> None:
        self.type = _type
        self.value = value
    def __str__(self) -> str:
        return f"T_{types_to_str(self.type)}['{str(self.value)}']"
    def __repr__(self) -> str:
        return self.__str__()

class Command(TypedDict):
    is_free :  bool
    accept_free : bool
    cmd_func : function | None # func(args : list[Token_arg], user)
    args_func : dict[Cmd_args, function] | None

commands : dict[str, Command] = {}


def new_free_command(func : function):
    com : Command = {
        'is_free' : True,
        'accept_free' : True,
        'cmd_func' : func,
        'args_func' : None
        }
    return com


def new_struct_command(accept_free : bool = False, func = None):
    if accept_free and func is None:
        raise Exception("ERROR cannot make struct command accept_free = True with func =  None")
    com : Command = {
        'is_free' : False,
        'accept_free' : accept_free,
        'cmd_func' : func
    }
    com['args_func'] : dict[Cmd_args, function] = {}
    return com

def add_arg(com : Command, args : Cmd_args, func : function):
    com['args_func'][args] = func

def register_command(name : str, com : Command):
    commands[name] = com


def lexe_command(text : str):
    tokens :list[Token_arg] = []
    p = 0
    l = len(text)
    while p < l:
        while text[p].isspace():
            p += 1
        if text[p] in "01" and p + 1 < l and text[p + 1] in "Bb":
            tokens.append(Token_arg(Cmd_bool, text[p] == '1'))
            p += 2
            continue

        if text[p] == "0" and p + 1 < l and text[p + 1] in "xX" and p + 2 < l:
            if text[p + 2] not in "1234567890ABCDEFabcdef":
                raise Exception("ERROR command parsing expected a hex diigit after '0x'")
            start = p + 2
            end = start
            while end < l and text[end] in "1234567890ABCDEFabcdef":
                end += 1
            num = text[start:end]
            num = int(num,base = 16)
            tokens.append(Token_arg(Cmd_int, num))
            p = end
            continue
        if text[p] in "1234567890.-":
            start = p
            end = p
            while end < l and text[end] in "1234567890.-+":
                end += 1
            num = text[start:end]
            if num.count("+") + num.count("-") > 1:
                raise Exception("ERROR command parsing on number expected only one '+' or one '-'")
            dot_count = num.count(".")
            if dot_count > 1:
                raise Exception("ERROR command parsing one number expected only one '.'")
            if dot_count == 0:
                tokens.append(Token_arg(Cmd_int, int(num)))
            else:
                tokens.append(Token_arg(Cmd_float, float(num)))
            p = end
            continue
        start = p
        end = start
        while end < l and not text[end].isspace():
            end +=1
        identifier = text[start:end]
        if identifier == "True":
            tokens.append(Token_arg(Cmd_bool, True))
            p = end
            continue
        elif identifier == "False":
            tokens.append(Token_arg(Cmd_bool, False))
            p = end
            continue
        elif identifier == "true":
            tokens.append(Token_arg(Cmd_bool, True))
            p = end
            continue
        elif identifier == "false":
            tokens.append(Token_arg(Cmd_bool, False))
            p = end
            continue
        elif identifier == "None":
            tokens.append(Token_arg(Cmd_None, None))
            p = end
            continue
        elif identifier[0] not in "1234567890-.":
            tokens.append(Token_arg(Cmd_identifier, identifier))
            p = end
            continue
        else:
            tok1 = ''
            tok2 = text[p]
            tok3 = ''
            if p - 1 >= 0:
                tok1 = text[p - 1]
            if p + 1 < l:
                tok1 = text[p + 1]
            raise Exception(f"ERROR parsing command unexcepted token : {tok1}{tok2}{tok3}")
    return tokens


import os
import importlib as imp
module_names=os.listdir(os.path.dirname(os.path.abspath(__file__)))

for i in range(len(module_names)):
    if module_names[i]=="__init__.py":
        module_names.pop(i)
        break
for i in range(len(module_names)):
    if module_names[i].endswith(".py"):
        module_names[i]=module_names[i][:-3]

for i in module_names:
    imp.import_module(f".{i}", __package__)