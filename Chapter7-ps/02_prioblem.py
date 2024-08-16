#greeting all the names with s

names = ["Harry" , "Soham" , "Sachin" , "Rahul" ];

check_str = "s";

for nm in names:
    if check_str in nm.lower():
        print("good morning !! " + nm)