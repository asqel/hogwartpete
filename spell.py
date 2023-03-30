import uuid 
from world import *

AVADA_KEDAVRA="avada kedavra"

class Spell:
    def __init__(self,name,sender:uuid.UUID) -> None:
        self.sender=sender
        self.name=name
        
    def shoot(self,world:World):
        if self.name==AVADA_KEDAVRA:
            print("vous avez lancer avada kedavra")
            
