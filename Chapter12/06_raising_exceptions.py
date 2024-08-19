a = int(input("enter a no1 : "))
b = int(input("enter a no2 : "))

if (b==0):
    raise ZeroDivisionError("cant divide by zero !!")
else:
    print(f"{a} / {b} = {a/b}")