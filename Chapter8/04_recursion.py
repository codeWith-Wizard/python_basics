def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)

n=int(input("enter the no: "))
print(f"factorial of {n} is {factorial(n)}")