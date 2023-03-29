import uuid 

class Spell:
    def __init__(self,name,sender:uuid.UUID) -> None:
        self.sender=sender
        self.name=name