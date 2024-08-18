
class animal:
    limbs = 4
    tail = True
    type = ""

    def __init__(cr,name):   #using something else than self like ==> cr
        cr.name = name
        print(f"object named {cr.name} created!!")

    def getInfo(self):
        print(f"name : {self.name}")
        print(f"type : {self.type}")
        print(f"limbs : {self.limbs}")
        print(f"tail : {self.tail}")
    


poppy = animal("poppy")
poppy.type = "dog" 
poppy.getInfo()