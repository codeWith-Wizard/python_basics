#inches to cm
'''cm = 2.54 x inches'''

def inc_cm(a):
    temp = a*2.54
    return temp

temp = int(input("enter measure in inches: "))
print(f"{inc_cm(temp)} cm")
