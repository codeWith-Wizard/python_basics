#pattern printing using function recursion


'''
*****
****
***
**
*
'''
def p_print(n):
    if(n==1):
        print("*")
        return
    print("*"*n)
    p_print(n-1)
    return
n = int(input("enter the value of n: "))
p_print(n)
