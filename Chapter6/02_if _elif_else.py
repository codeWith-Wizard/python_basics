#checking age consent

age = int(input("enter the age: "));


if (age >= 18):
    print("Congrats !! you are above the age of consent!")

elif(age<0):
    print("invalid age !!")

elif(age==0):
    print("age can't be zero !!")

else:
    print("Sorry !! you are below the age of consent!")

