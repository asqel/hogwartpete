import uuid 
from world import *
from vector import *


class Spell:
    def __init__(self,name_of_spell,sender:uuid.UUID) -> None:
        self.sender=sender
        self.name=name_of_spell
    
    def getname(self):
        return self.name
    
    def shoot(self,w:World,mouse_pos:Vec):
        ...#ya rien ici c'est chaque sort qui doit le changer lui meme
        
        
AVADA_KEDAVRA="avada kedavra"
class Avada_kedavra(Spell):
    def __init__(self, sender: uuid.UUID) -> None:
        super().__init__(AVADA_KEDAVRA, sender)
    
    def shoot(self,w:World,mouse_pos:Vec):
        pass
        
        
            
