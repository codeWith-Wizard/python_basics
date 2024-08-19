#defining operators


class number():
    def __init__(self,n):
        self.n = n
        
    def __add__(self,num):
        return self.n + num.n
        
        
n1 = number(1)
n2 = number(2)

print(n1 +n2)
