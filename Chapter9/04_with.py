#to automatically close the file 
with open("Chapter9/file.txt") as f:
    data = f.read()
    print(data)


#dont need to explicitly close the file 