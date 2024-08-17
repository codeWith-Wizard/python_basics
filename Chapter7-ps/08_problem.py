a = "*"
b = " "
n = int(input("enter the value of n: "))

for i in range(1,n+1):
    if (i==1 or i==n):
        print(a*n)
    else:
        print(a, end = "" )
        print(b*(n-2), end = "")
        print(a)