class Programmer:
    age = ""
    salary = 1500000
    lang = "python"
    yrs_of_exp = 3

    def __init__(self,name,age,salary,lang = "Python ",yrs_of_exp=3):
        self.name = name
        self.age = age
        self.salary = salary
        self.yrs_of_exp = yrs_of_exp
        self.lang = lang
        print(f"{self.name} : logged into system !")

    def getInfo(self):
        print(f"name : {self.name}")
        print(f"age : {self.age}")
        print(f"language : {self.lang}")
        print(f"salary : {self.salary}")
        print(f"years of experience : {self.yrs_of_exp}")


Rohan = Programmer(name="Rohan" ,age= 26,salary = 1800000)
Jaggu = Programmer(name="Jaggu" ,age= 27,salary = 1500000,lang = "javascript")
Raju = Programmer(name="Raju" ,age= 25,salary = 1300000,lang = "c++")


programmers = [ Rohan, Jaggu, Raju]

for i in programmers:
    i.getInfo()
    print("")
    print("*"*10)
    print("")

