
import math

class Vec:
    
    def __init__(self,x=None,y=None):
        """
        if x and y are set to None then the vector will be (0,0)
        if y is None and x is a tuple or a list and if its len is equal to 2 the vector will be (x[0],x[1])
        """
        if(x is None and y is None):
            self.x=0
            self.y=0
        elif y is None :
            if isinstance(x,(tuple,list)):
                if len(x)==2:
                    self.x=x[0]
                    self.y=x[1]
                else:
                    raise Exception(f"len of x is {'greater' if len(x)>2 else 'less'} than 2")
            else:
                raise Exception("x not a tuple nor a list in Vec")
        else:
            raise Exception("missing value for x in Vec")
        
    def __add__(self,other):
        if isinstance(other,(Vec,tuple,list)):
            other=Vec(other)
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
