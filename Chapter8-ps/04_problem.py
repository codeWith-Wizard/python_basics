#pattern printing using function recursion

'''
*
**
***
****
*****
'''
def p_print(n):
    if(n==1):
        print("*"*n)
        return
    p_print(n-1)
    print("*"*n)
    return
n = int(input("enter the value of n: "))
p_print(n)
