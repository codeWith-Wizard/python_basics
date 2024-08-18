class employee:
    language = "py" #class attribute
    salary = "120000" #class attribute

harry = employee() #instantiation of class through harrry(object)
harry.name = "harry" #instance attribute
print(harry.name , harry.language)

rohan = employee()
rohan.name = "Rohan Singh" #name is an object attribute and salary,language are class attributes
print(rohan.name , rohan.salary , harry.language)

