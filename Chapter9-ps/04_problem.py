

with open("Chapter9-ps/story.txt", "r+") as f:
    data = f.readlines()
    new_data = []
    count  = 0
    for i in data:
        i = i.lower()
        i = i.replace("donkey" ,"####")
        new_data.append(i)
        count +=1

    f.seek(0)
    f.writelines(new_data)



