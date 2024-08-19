#similar to switch cas in c

def network(ping):
    match ping:
        case 30:
            return "very good" 
        case 50:
            return "good"
        case 100:
            return "fluctuating"
        case 200:
            return "bad"
        case _:
            return "very bad"
        
print(network(200))
print(network(30))