import pygame as py
import interface
import commands as cmd
from uti.textures import *


class Exec_command(interface.Gui):
    def __init__(self, player) -> None:
        self.command = ""
        self.world = player.world
        self.player = player
        self.error = ""
        self.error_tick = 0
        self.error_max_tick = 180
        super().__init__(self.__class__.__name__, {}, player)
        
        
    def tick(self, events: list[py.event.Event]):
        if self.error:
            self.error_tick += 1
            if self.error_max_tick <= self.error_tick:
                self.error = ""
        
        for i in events:
            if i.type == py.KEYDOWN:
                if self.error:
                    self.error = ""
                    break
                if i.key == py.K_ESCAPE:
                    self.player.close_gui()
                elif i.key != py.K_BACKSPACE and i.key != py.K_RETURN:
                    self.command += i.unicode
                if i.key == py.K_BACKSPACE:
                    self.command = self.command[:-1]
                if i.key == py.K_RETURN:
                    try:
                        res = exec_command(self.command, self.world, self.player)
                        if res is not None:
                            self.error = res
                            self.error_tick = 0
                    except Exception as E:
                        self.error = str(E)
                        self.error_tick = 0



                    
            
    def draw(self, screen):
        x = (screen.get_width() - Textures["other"]["text_box"].get_width())/2
        y = screen.get_height() -Textures["other"]["text_box"].get_height() - 20 
        screen.blit(Textures["other"]["text_box"],(x,y))
        if self.error:
            screen.blit(interface.main_font.render(self.error,0,(0,255,0)), (x+30,y+30))
        else:
            screen.blit(interface.main_font.render(f"command : {self.command}",0,(0,255,0)), (x+30,y+30))
    
interface.registerGui(Exec_command)


def exec_command(command : str, world, player):
    toks = cmd.lexe_command(command)
    toks_len = len(toks)
    print(toks)
    if toks_len < 1:
        return
    if toks[0].type != cmd.Cmd_identifier:
        return
    com = toks[0].value
    if com not in cmd.commands.keys():
        return
    c = cmd.commands[com]
    if c["is_free"]:
        return c["cmd_func"](toks, player)
    else:
        args = []
        for i in toks:
            args.append(i.type)
        args =tuple(args)
        if args in c["args_func"].keys():
            return c["args_func"][args](toks, player)
        elif c["accept_free"]:
            return c["cmd_func"](toks, player)
        else:
            raise Exception(f"ERROR command {toks[0].value} doesnt accept that")
