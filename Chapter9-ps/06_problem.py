
find = input("enter the word to found : ")

with open("Chapter9-ps/log.txt") as f :
    data = f.readlines()
    count = 0
    for i in data:
        if find in i:
            print(f"{find} found at line {count + 1}")
            
        count +=1
