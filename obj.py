class Obj:
    def __init__(self,id:str,x:float,y:float) -> None:
        self.id=id
        self.x=x
        self.y=y

class Stone(Obj):
    def __init__(self, id: str, x: float, y: float,type) -> None:
        self.type=type
        super().__init__(id, x, y)