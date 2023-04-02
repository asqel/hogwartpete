from spells import *

AVADA_KEDAVRA="avada kedavra"
class Avada_kedavra(Spell):
    def __init__(self, sender: uuid.UUID) -> None:
        super().__init__(AVADA_KEDAVRA, sender)
    
    def shoot(self,world,mouse_pos:Vec):
        for i in world.entities:
            if((mouse_pos-i.pos).squareLength()<=2*16**2):
                i.pv=0
                
IMPERO="impero"
class Impero(Spell):
    def __init__(self, sender: uuid.UUID) -> None:
        super().__init__(IMPERO, sender)
    
    def shoot(self,world,mouse_pos:Vec):
        pass#TODO : implement Impero:shoot
                

CRUCIO="curcio"
class Crucio(Spell):
    def __init__(self, sender: uuid.UUID) -> None:
        super().__init__(CRUCIO, sender)
    
    def shoot(self,world,mouse_pos:Vec):
        pass#TODO : implement Crucio:shoot
                

                

registerSpell(Avada_kedavra,AVADA_KEDAVRA)
registerSpell(Impero,IMPERO)
registerSpell(Crucio,CRUCIO)
        
        