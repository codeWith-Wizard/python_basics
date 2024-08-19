
class Animals():
    
    legs = 4
    tail = True
    
    def __init__(self):
        print("kingdom : animnal ")
        

class Pets(Animals):
    
    quality = "friendly"
    manners = "good"
    
    def __init__(self):
        super().__init__()
        print("type : pets")
        

class dog(Pets):
    
    speak = "woof woof !!"
    
    def __init__(self):
        super().__init__()
        print("family : dogs")      
        
    def bark(self):
        print(self.speak)


poppy = dog()
poppy.bark()