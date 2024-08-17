#function for first n natrural numbers

def sum_natural(n):
    if(n==1):
        return 1
    return n + sum_natural(n-1)

n = int(input("enter the value of n: "))

print(f"the sum is : {sum_natural(n)}")