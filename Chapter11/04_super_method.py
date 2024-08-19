#demo of multilevel inheritance

class Characters:
    type = "human"
    def __init__(self):
        print("constructor of Characters called !!")
    
class goodCharacters(Characters):
    quality = "kind"
    def __init__(self):
        super().__init__()
        print("constructor of goodCharacters called !!")

class superHero(goodCharacters):
    power = "flying"
    def __init__(self):
        super().__init__() #super constructor ==> calling parent constructor
        print("constructor of superHero called !!")

Superman = superHero()
print(Superman.type)
print(Superman.quality)
print(Superman.power)
