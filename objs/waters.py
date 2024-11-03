import objs
from uti.textures import *
from uti.hitbox import *
from uti.vector import *


class Water_ul(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["water_ul"],HITBOX_50X50)

class Water_u(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["water_u"],HITBOX_50X50)

class Water_ur(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["water_ur"],HITBOX_50X50)


class Water_l(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["water_l"],HITBOX_50X50)

class Water(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["water"],HITBOX_50X50)

class Water_r(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["water_r"],HITBOX_50X50)



class Water_dl(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["water_dl"],HITBOX_50X50)

class Water_d(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["water_d"],HITBOX_50X50)

class Water_dr(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["water_dr"],HITBOX_50X50)



class Water_ext_1(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["water_ext_1"],HITBOX_50X50)

class Water_ext_2(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["water_ext_2"],HITBOX_50X50)

class Water_ext_3(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["water_ext_3"],HITBOX_50X50)

class Water_ext_4(objs.Obj):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(self.__class__.__name__, x, y, Textures["Obj"]["water_ext_4"],HITBOX_50X50)


objs.registerObj(Water_ul)
objs.registerObj(Water_u)
objs.registerObj(Water_ur)

objs.registerObj(Water_l)
objs.registerObj(Water)
objs.registerObj(Water_r)


objs.registerObj(Water_dl)
objs.registerObj(Water_d)
objs.registerObj(Water_dr)

objs.registerObj(Water_ext_1)
objs.registerObj(Water_ext_2)
objs.registerObj(Water_ext_3)
objs.registerObj(Water_ext_4)
