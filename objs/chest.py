from objs import *
from uti import *
from entities import *



class Chest(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, False, Textures["Obj"]["chest_0"],HITBOX_50X50)
        self.data["opened"] = 0

    def on_interact(self, world, user):
        if self.data["opened"] == 0:
            if user.add_item(items["Cloak_of_invisibility"](1)):
                self.data["opened"] = 1

    def on_draw(self, world, has_been_drawn):
        if players[0].has_item("goggles_of_truth"):
            if self.data["opened"]:
                self.texture = Textures["Obj"]["chest_1"]
            else:
                self.texture = Textures["Obj"]["chest_0"]
        else:
            self.texture = NOTHING_TEXTURE
        return super().on_draw(world, has_been_drawn)



registerObj(Chest)