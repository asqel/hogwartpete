from spells import *

LUMOS="lumos"
class Lumos(Spell):

    def __init__(self, sender: uuid.UUID) -> None:
        super().__init__(LUMOS, sender)

    def shoot(self, world, mouse_pos: Vec):
        ...
