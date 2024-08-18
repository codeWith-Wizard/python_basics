

#defining the finding function 
def finding(data, find):
    length = len(data)
    temp = 0
    for i in range(length):
        temp_data = data[i].lower()
        if i == 0:
            temp = temp_data.count(find)
        else:
            temp = temp + temp_data.count(find)
    return temp


#opening the file and storing the lines in data
with open("Chapter9-ps/ps_file.txt") as f :
    data = f.readlines()

#taking input from the user 
find = input("enter the word to found :").lower()

#function call
temp = finding(data, find)

#evaluating 
if(temp > 0):
    if (temp > 1 ):
        print(f"yes , the {find} words are present.")
        print(f" {find} word repeated {temp} times.")
        
    else:
        print(f" yes , the {find} word is present.")
        print(f"{find} word repeated {temp} time.")
        

else:
    print(f"{find} word not present .")



