#prime no or not

num = int(input("enetr the no. : "))
status = True

for i in range(num):
    if (i==0 or i==1):
        continue
    if(num%i==0):
        print("not a prime no. !!")
        status = False
        break

if status == True:
    print("prime no: !!")