#demo of multilevel inheritance

class Characters:
    type = "human"
    
class goodCharacters(Characters):
    quality = "kind"

class superHero(goodCharacters):
    power = "flying"

Superman = superHero()
print(Superman.type)
print(Superman.quality)
print(Superman.power)
