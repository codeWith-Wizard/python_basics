#celcius to fahrenheit and kelvin

def clc_frn(a):
    temp = (a*(9/5))+32
    return temp

def clc_kelvin(a):
    temp = a+273.5
    return temp

temp = int(input("enter the temp in celcius : "))
print(" 1=> to kelvin ")
print(" 2=> to fahrenheit ")
choice = int(input("enter your choice:"))

if(choice == 1):
    k = clc_kelvin(temp)
    print(f"{k} kelvin")
elif(choice == 2):
    f = clc_frn(temp)
    print(f"{f} fahrenheit")
else:
    print("invalid choice!!")
