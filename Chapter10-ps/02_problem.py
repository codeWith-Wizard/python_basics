class calculator:
    
    def __init__(self,n):
        self.n = n
        print(f"Calculator for {self.n} called !")
    
    def square(self):
        print(f"square of {self.n} is {self.n*self.n}")

    def cube(self):
        print(f"cube of {self.n} is {self.n*self.n*self.n}")
        
    def squareRoot(self):
        print(f"square root of {self.n} is {self.n**(1/2)}")
    
    
calc4 = calculator(4)
calc4.square()
calc4.cube()
calc4.squareRoot()