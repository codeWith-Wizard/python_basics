class employee:
    lang = "python" #class attribute
    salary = 1200000

harry = employee()
harry.name = "harrry"
print(harry.name , harry.lang , harry.salary)


rohan = employee()
rohan.name = "rohan"
rohan.lang = "java script"  #instance attribute
print(rohan.name , rohan.lang , rohan.salary)

'''instance attribute take advantage over class attribute'''