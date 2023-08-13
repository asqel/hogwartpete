import pygame as py
from interface import *
from uti import *


class Exec_command(Gui):
    def __init__(self, player) -> None:
        self.command = ""
        self.world = player.world
        self.player = player
        super().__init__(self.__class__.__name__, {}, player)
        
        
    def tick(self, events: list[py.event.Event]):
        
        for i in events:
            if i.type == py.KEYDOWN:
                if i.key == py.K_ESCAPE:
                    self.player.gui = None
                elif i.key != py.K_BACKSPACE and i.key != py.K_RETURN:
                    self.command += i.unicode
                if i.key == py.K_BACKSPACE:
                    self.command = self.command[:-1]
                if i.key == py.K_RETURN:
                    exec_command(self.command, self.world, self.player)
                    
            
    def draw(self, screen):
        x = (screen.get_width() - Textures["other"]["text_box"].get_width())/2
        y = screen.get_height() -Textures["other"]["text_box"].get_height() - 20 
        screen.blit(Textures["other"]["text_box"],(x,y))
        screen.blit(main_font.render(f"command : {self.command}",0,(0,255,0)), (x+30,y+30))
    
registerGui(Exec_command)


def exec_command(command : str, world, player):
    args = command.split(" ")
    #data set x y key value
    if len(args) == 6:
        if args[0] == "data":
            if args[1] == "set":
                x_negatif = False
                if args[2].startswith("-"):
                    x_negatif = True
                    args[2] = args[2][1:]
                if args[2].isdigit():
                    x = int(args[2])
                elif args[2] == '*':
                    x = player.pos.x
                    y_negatif = False
                    if args[3].startswith("-"):
                        y_negatif = True
                        args[3] = args[3][1:]
                    if args[3].isdigit():
                        y = int(args[3])
                    elif args[3] == '*':
                        y = player.pos.y
                        key = args[4]
                        value = args[5]
                        if y_negatif: y = -y
                        if x_negatif: x = -x
                        obj = world.get_Obj(Vec(x,y))
                        print(x,y)
                        if obj.id != "Air":
                            if value.isdecimal():
                                value = float(value)
                            elif value.isdigit():
                                value = int(value)
                            elif value == "True":
                                value = True
                            elif value == "False":
                                value = False
                            obj.data[key] = value
                            

