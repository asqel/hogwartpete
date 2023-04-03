import uuid 
from uti.vector import *


class Spell:
    def __init__(self,name_of_spell,sender:uuid.UUID) -> None:
        self.sender=sender
        self.name=name_of_spell
    
    def getname(self):
        return self.name
    
    def shoot(self,world,mouse_pos:Vec):
        ...
        
        
Spells={}

"""
register classes of spells
"""
def registerSpell(spell:type,name:str):
    Spells[name]=spell
            


