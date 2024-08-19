 
class complex:
    
    def __init__(self,r,i):
        self.i = i
        self.r = r
    
    def __add__(self, new_c):
        return complex(i= self.i + new_c.i , r= self.r + new_c.r)

    
    def __str__(self):
        return f"{self.r} + {self.i}i"
    

c1 = complex(r = 4 , i = 5)
c2 = complex(r = 3 , i = 5)
print(c1+c2)