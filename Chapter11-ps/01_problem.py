#creating vectors

class twoDVector():
    def __init__(self,i,j):
        self.i = i
        self.j = j
    
    def show(self):
        print(f"{self.i}i + {self.j}j")

class threeDVector(twoDVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k
    
    def show(self):
        print(f"{self.i}i + {self.j}j + {self.k}k")
       
    
bVector = threeDVector(i=7 , j =5 , k=6) 
bVector.show()
    
        
