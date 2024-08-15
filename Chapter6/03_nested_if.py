#checking age consent

age = int(input("enter the age: "));


if (age >= 18):
    print("Congrats !! you are above the age of consent!")
    
    if (age >50):
        print("Congrats !! you are in the golden era !")

    elif(age>30):
        print("ok!! you would be working !")

    elif(age>20):
        print("hey there youngster")


elif(age<0):
    print("invalid age !!")

elif(age==0):
    print("age can't be zero !!")

else:
    print("Sorry !! you are below the age of consent!")

