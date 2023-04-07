import uuid 
from uti.vector import *
import importlib as imp
import os 


class Spell:
    def __init__(self,name_of_spell,sender:uuid.UUID) -> None:
        self.sender=sender
        self.name=name_of_spell
    
    def getname(self):
        return self.name
    
    def shoot(self,world,mouse_pos:Vec):
        ...
        
        
Spells:dict[str,Spell]={}

"""
register classes of spells
"""
def registerSpell(spell:type,name:str):
    Spells[name]=spell
    
    
#import every spells
module_names=os.listdir(os.path.dirname(os.path.abspath(__file__)))

for i in range(len(module_names)): #pour tous les fichiers dans modules_names
    if module_names[i]=="__init__.py": #si le nom du fichier est lui même
        module_names.pop(i) #il se supprime de la liste
        break
for i in range(len(module_names)): #pour tous les fichiers dans modules_names
    if module_names[i].endswith(".py"): #si le fichier finit par py
        module_names[i]=module_names[i][:-3] #on enlève l'extension ".py"
        
for i in module_names: 
    imp.import_module("."+i,__package__) #import les choses dans le init