
import math

class Vec:
    def __init__(self,x=0.0,y=0.0):
        self.x=x
        self.y=y
    
    def __add__(self,other):
        if isinstance(self,Vec) and isinstance(other,Vec):
            return(Vec(self.x+other.x,self.y+other.y))
    def __sub__(self,other):
        return(self+(-other))
    def __neg__(self): 
        return(Vec(-self.x,-self.y,))
    def __pos__(self):
        return(self)
    def __invert__(self):
        return(Vec(~self.x,~self.y))
    def __mul__(self,other):
        if (isinstance(other,int) or isinstance(other,float)) and isinstance(self,Vec):
            return(Vec(self.x*other,self.y*other,))
        if (isinstance(self,int) or isinstance(self,float)) and isinstance(other,Vec):
            return(Vec(other.x*self,other.y*self))
        raise NotImplementedError()
    def __truediv__(self,other):
        if isinstance(other,int)or isinstance(other,float):
            return self*(1/other)
    def __truediv__(self,other):
        if isinstance(other,int)or isinstance(other,float):
            return self*(1/other)
    
    def __radd__(self,other):
        if isinstance(self,Vec) and isinstance(other,Vec):
            return(Vec(self.x+other.x,self.y+other.y))
    def __rsub__(self,other):
        return(self+(-other))
    def __rmul__(self,other):
        if (isinstance(other,int) or isinstance(other,float)) and isinstance(self,Vec):
            return(Vec(self.x*other,self.y*other,))
        if (isinstance(self,int) or isinstance(self,float)) and isinstance(other,Vec):
            return(Vec(other.x*self,other.y*self))
        raise NotImplementedError()
    def __rtruediv__(self,other):
        if isinstance(other,int)or isinstance(other,float):
            return self*(1/other)    
    def __str__(self):
        return str((self.x,self.y))

    def length(self)->float:
        """
        return the length of the Vector
        """
        return(math.sqrt(self.squareLength()))
    def squareLength(self)->float:
        """
        return the squared length of the Vector
        """
        return(self.x*self.x+self.y*self.y)
