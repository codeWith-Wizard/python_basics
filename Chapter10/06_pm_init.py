
class animal:
    limbs = 4
    tail = True
    type = ""

    def __init__(self,name):
        self.name = name
        print(f"object named {self.name} created!!")

    def getInfo(self):
        print(f"name : {self.name}")
        print(f"type : {self.type}")
        print(f"limbs : {self.limbs}")
        print(f"tail : {self.tail}")
    


poppy = animal("poppy")
poppy.type = "dog" 
poppy.getInfo()