class employee:
    lang = "python" #class attribute
    salary = 1200000
    
    #its very important to give self paarmeter while defining function
    def getInfo(self): #self similar to this as in c++
        print(f"the language is {self.lang} and the salary is {self.salary}")

harry = employee()
harry.name = "harrry"
print(harry.name , harry.lang , harry.salary)

harry.getInfo()
#similar call
#employee.getInfo(harry) ==> 1 attribute passed