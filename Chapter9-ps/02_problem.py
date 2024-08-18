import random

#defining the game function
def game(high_score,f):

    #defining variables
    print("game has satrted....")
    score = random.randint(1,100)
    score_str = str(score)
    print(f"your score is : {score}")

    #checks if there is something on the file or not
    if(high_score == ""):
        f.seek(0) # moves the file pointer to start of the file in order to overwrite the file
        f.write(score_str)
        print(f"congo !! new HIGH SCORE : {score}")
        return
    
    #compares the already existing high score with current score 
    if (score > int(high_score)):
        f.seek(0)
        f.write(score_str)
        print(f"congo !! new HIGH SCORE : {score}")
        return
    
    print("you lost !!")
    return


#opening the file using with satement
with open("Chapter9-ps/Hi_score.txt","r+") as f:
    high_score = f.read()
    print(f"high score : {high_score}")
    game(high_score,f)