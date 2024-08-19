 
class Employee:
    name = ""
    salary = 1100000
    age = 27

    @staticmethod
    def greet():
        print("good morning !!")
    
    def getInfo(self):
        print(f"hi {self.name} \nsalary : {self.salary}")



class Programmer(Employee):  #basic inheritance from single parent
    
    #dunder method ==> constructor
    def __init__(self,name,age,company,lang = "Python"):
        self.name = name
        self.lang = lang
        self.age = age
        self.company = company
    
    def profStats(self):
        print("\n")
        print(f"lang : {self.lang}")
        print(f"age : {self.age}")
        print(f"company : {self.company}")
        print("\n")
    

    
Rohan = Programmer(name = "Rohan" , company="ITC" , age= 26 )
Rohan.getInfo()
Rohan.profStats()