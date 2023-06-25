from items import *
from uti import *
import entities as en
class Super_moule(Item):
    def __init__(self, quantity) -> None:
        super().__init__(self.__class__.__name__, 1, Textures["other"]["moule"], quantity)
        self.entity = None

    def on_use(self, world, user):
        if not user.gui:
            if user.dir == 'u':
                bullet = en.Npcs["Super_moule_entity"](user.pos + (13,-25))
                bullet.direction = user.dir
                bullet.item = user.inventaire[user.inventaire_idx]
                bullet.sender = user
                user.world.get_Chunk_from_pos(user.pos).entities.append(bullet)
                

            if user.dir == 'r':
                bullet = en.Npcs["Super_moule_entity"](user.pos + (10+50, 13))
                bullet.direction = user.dir
                bullet.item = user.inventaire[user.inventaire_idx]
                bullet.sender = user
                user.world.get_Chunk_from_pos(user.pos).entities.append(bullet)

            if user.dir == 'd':
                bullet = en.Npcs["Super_moule_entity"](user.pos + (13,50+10))
                bullet.sender = user
                bullet.direction = user.dir
                bullet.item = user.inventaire[user.inventaire_idx]
                user.world.get_Chunk_from_pos(user.pos).entities.append(bullet)
                
            if user.dir == 'l':
                bullet = en.Npcs["Super_moule_entity"](user.pos + (-10,13))
                bullet.sender = user
                bullet.direction = user.dir
                bullet.item = user.inventaire[user.inventaire_idx]
                user.world.get_Chunk_from_pos(user.pos).entities.append(bullet)

    def copy(self):
        i = super().copy()
        i.entity = self.entity
        return i

registerItem(Super_moule)