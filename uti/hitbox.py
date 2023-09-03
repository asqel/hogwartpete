from uti.vector import *

HITBOX_RECT_t=0
HITBOX_CIRCLE_t=1




class Hitbox:
    """
    RECT:
        pos: position of tthe top left corner
        width: the width of the hitbox 
        height: the height of the hitbox
         
    CIRCLE:
        pos: position of the centre of the cirlce
        radius: radius of the circle
    """
    def __init__(self,type:int,pos:Vec,radius=0,width=0,height=0) -> None:
        self.type=type
        self.pos=pos
        self.width=width
        self.height=height
        self.radius=radius
            
    def iscolliding(self,other) -> bool:
        if not isinstance(other,Hitbox):
            print(f"ERROR: cant detect collision betwenn hitbox and {type(other).__name__}")
            exit(1)
        if self == HITBOX_0x0 or other == HITBOX_0x0:
            return 0
        if self.type==HITBOX_RECT_t:
            if other.type==HITBOX_RECT_t:
                if self.height == self.width == 0 or other.height == other.width == 0  :
                    return False
                return (
                    self.pos.x + self.width > other.pos.x
                    and self.pos.x < other.pos.x + other.width
                    and self.pos.y + self.height > other.pos.y
                    and self.pos.y < other.pos.y + other.height
                )
            print("ERROR collision between rect and other not implemented yet")
            exit(1)
        if self.type==HITBOX_CIRCLE_t:
            if other.type==HITBOX_CIRCLE_t:
                return (self.pos-other.pos).squareLength() <= (self.radius+other.radius)**2
            print("ERROR collision between circle and other not implemented yet")
            exit(1)
            
    def copy(self):
        return Hitbox(self.type,self.pos.copy(),self.radius,self.width,self.height)
    
    def __str__(self) -> str:
        if self.type == HITBOX_RECT_t:
            return f"[w:{str(self.width)}, h:{str(self.height)}, pos:{str(self.pos)}]"

def collide_rect_dot(rect:Hitbox,dot:Vec):
    if rect.pos.x <= dot.x <= rect.pos.x+rect.width:
        if rect.pos.y <= dot.y <= rect.pos.y+rect.height:
            return True
    return False

HITBOX_50X50=Hitbox(HITBOX_RECT_t,NULL_VEC,0,50,50)
HITBOX_100X100=Hitbox(HITBOX_RECT_t,NULL_VEC,0,100,100)
HITBOX_0x0 = Hitbox(HITBOX_RECT_t, Vec(0, 0), 0, 0, 0)