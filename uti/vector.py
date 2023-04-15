
import math
"""
can be converted to tuple, dict and str  but not list
can acces values with Vec(3,7)["x"] or Vec(3,7)["y"] or Vec(3,7)[0] or Vec(3,7)[1] or Vec(3,7).x or Vec(3,7).y

operation:
    Vec+Vec
    -Vec
    +Vec
    ~Vec
    Vec-Vec
    Vec*(int|float)
    (int|float)*Vec
    Vec/(int|float)  
    Vec//(int|float) 
"""
class Vec:
    
    def __init__(self,x=None,y=None):
        """
        if x and y are set to None then the vector will be (0,0)

        if y is None and x is a tuple or a list and if its len is equal to 2 the vector will be (x[0],x[1])
        """
        if ((x is not None ) and (y is not None)):
            self.x=x
            self.y=y
        elif((x is None ) and (y is None)):
            self.x=0
            self.y=0
        elif y is None:
            if isinstance(x,(tuple,list)):
                if len(x) != 2:
                    raise Exception(f"len of x is {'greater' if len(x)>2 else 'less'} than 2")
                self.x=x[0]
                self.y=x[1]
            elif isinstance(x,Vec):
                self.x=x.x
                self.y=x.y
            elif isinstance(x,complex):
                self.x=x.real
                self.y=x.imag
            else:
                raise Exception("x not a tuple nor a list nor a Vec in Vec")
        else:
            raise Exception("missing value for x in Vec")
        
    def __add__(self,other):
        if isinstance(other,(Vec,tuple,list)):
            other=Vec(other)
            return(Vec(self.x+other.x,self.y+other.y))
        return NotImplemented
        
    def __sub__(self,other):
        if isinstance(other,(Vec,tuple,list)):
            other=Vec(other)
            return(Vec(self.x-other.x,self.y-other.y))
        return NotImplemented
    
    def __neg__(self): 
        return(Vec(-self.x,-self.y,))
    
    def __pos__(self):
        return(self)
    
    def __invert__(self):
        return(Vec(~self.x,~self.y))
    
    def __mul__(self,other):
        if isinstance(other, (int, float)):
            return(Vec(self.x*other,self.y*other))
        return NotImplemented
    
    def __truediv__(self,other):
        if isinstance(other, (int, float)):
            return(Vec(self.x/other,self.y/other))
        return NotImplemented
    
    def __floordiv__(self,other):
        if isinstance(other, (int, float)):
            return(Vec(self.x//other,self.y//other))
        return NotImplemented
    
    def __radd__(self,other):
        if isinstance(other,(Vec,tuple,list)):
            other=Vec(other)
            return(Vec(self.x+other.x,self.y+other.y))
        return NotImplemented
        
    def __rsub__(self,other):
        if isinstance(other,(Vec,tuple,list)):
            other=Vec(other)
            return(Vec(self.x-other.x,self.y-other.y))
        return NotImplemented
    
    def __rmul__(self,other):
        if isinstance(other, (int, float)):
            return(Vec(self.x*other,self.y*other))
        return NotImplemented
    
    def __rtruediv__(self,other):
        if isinstance(other, (int, float)):
            return(Vec(self.x/other,self.y/other))
        return NotImplemented
    
    def __rfloordiv__(self,other):
        if isinstance(other, (int, float)):
            return(Vec(self.x//other,self.y//other))
        return NotImplemented
    
    def __str__(self):
        return str((self.x,self.y))
    
    def len(self)->float:
        """
        return the length of the Vector
        """
        return(math.sqrt(self.x**2 + self.y**2))
    def squareLength(self)->float:
        """
        return the squared length of the Vector
        """
        return self.x**2 +self.y**2
    def invertedLen(self)->float:
        """
        return 1/len
        """
        return (self.x**2 + self.y**2)**-0.5
    
    def __getitem__(self, index):
        if index in [0,"x"]:
            return self.x
        return self.y if index in [1,"y"] else NotImplemented

    def __setitem__(self, index, value):
        if not isinstance(value,(int,float)):
            return NotImplemented
        if index == 0:
            self.x=value
        elif index == 1:
            self.y=value
        return NotImplemented

    def __iter__(self):
        yield self.x
        yield self.y

    def floor(self):
        return Vec(int(self.x),int(self.y))

    def normalize(self):
        return self/self.len

    def copy(self):
        return Vec(self.x,self.y)