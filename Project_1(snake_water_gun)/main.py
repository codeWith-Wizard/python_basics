import random as rnd

#defining choice and dictionary
game_dict = { "s" : -1 , "w" : 1 , "g" : 0}
rv_game_dict = { -1 : "s" , 1 : "w" , 0 : "g"}
choose =[-1,1,0]
run = "r"

def chk_value(c, u, dictionary = { -1 : "snake" , 1 : "water" , 0 : "gun"} ):
    print(f"{dictionary.get(c)} :VS: {dictionary.get(u)} ")
    return



def game(game_dict, choose, chk_value):   #high order function => functionm accepting another function
    computer = rnd.choice(choose)
    user = input("Enter your choice (s for snake, w for water, g for gun): ").lower()
    user_num = game_dict.get(user)

    chk_value(c=computer, u = user_num)

    if(computer == user_num):
        print("draw !!")
    elif((computer == 1 and user_num == -1 ) or (computer == 0 and user_num == 1 ) or (computer == -1 and user_num == 0 )):
         print("you win !!")
    else:
        print("you lose !!")
    
    


while(run == "r"):
    game(game_dict, choose, chk_value)
    run = input("to run again => press 'r' : ")


