#greatest of three no.s
def grt3(a,b,c):
    if(a>b and b>c):
        return a
    elif(b>c and b>a):
        return b
    else:
        return c


a = int(input("enetr no1: "))
b = int(input("enetr no2: "))
c = int(input("enetr no3: "))

print(f"Greatest of three no.s is : {grt3(a,b,c)}")