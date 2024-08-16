#greeting all the names with s

names = ["Harry" , "Soham" , "Sachin" , "Rahul" ];

check_str = "s";

i = 0;

while(i<len(names)):
    if check_str in names[i].lower():
        print("good morning !! " + names[i])
    i+=1