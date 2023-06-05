from objs import *
from uti import *


class Water_ul(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, 0, Textures["Obj"]["water_ul"],HITBOX_50X50)

class Water_u(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, 0, Textures["Obj"]["water_u"],HITBOX_50X50)

class Water_ur(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, 0, Textures["Obj"]["water_ur"],HITBOX_50X50)


class Water_l(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, 0, Textures["Obj"]["water_l"],HITBOX_50X50)

class Water(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, 0, Textures["Obj"]["water"],HITBOX_50X50)

class Water_r(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, 0, Textures["Obj"]["water_r"],HITBOX_50X50)



class Water_dl(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, 0, Textures["Obj"]["water_dl"],HITBOX_50X50)

class Water_d(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, 0, Textures["Obj"]["water_d"],HITBOX_50X50)

class Water_dr(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, 0, Textures["Obj"]["water_dr"],HITBOX_50X50)



class Water_ext_1(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, 0, Textures["Obj"]["water_ext_1"],HITBOX_50X50)

class Water_ext_2(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, 0, Textures["Obj"]["water_ext_2"],HITBOX_50X50)

class Water_ext_3(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, 0, Textures["Obj"]["water_ext_3"],HITBOX_50X50)

class Water_ext_4(Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, 0, Textures["Obj"]["water_ext_4"],HITBOX_50X50)


registerObj(Water_ul)
registerObj(Water_u)
registerObj(Water_ur)

registerObj(Water_l)
registerObj(Water)
registerObj(Water_r)


registerObj(Water_dl)
registerObj(Water_d)
registerObj(Water_dr)

registerObj(Water_ext_1)
registerObj(Water_ext_2)
registerObj(Water_ext_3)
registerObj(Water_ext_4)
