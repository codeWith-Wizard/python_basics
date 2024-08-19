#demo of multiple inheritance

class Characters:
    type = "human"
    
class goodCharacters:
    quality = "kind"

class superHero(goodCharacters , Characters):
    power = "flying"

Superman = superHero()
print(Superman.type)
print(Superman.quality)
print(Superman.power)
