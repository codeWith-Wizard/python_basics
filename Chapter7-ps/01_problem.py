#printing multiplication table

num = int(input("enter the no. : "))
for i in range(10):
    temp = num * (i+1)
    print(f"{num} x {i+1} = {temp}")