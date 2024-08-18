#sometimes thgere is no need to send whole object into the method 
#this is the case when static methods are use
class employee:
    lang ="python"
    salary = 1200000

    def __init__(self): #constructor / dunder method which is automatically called at the time of creation
        print("object created !")

    def getInfo(self):
        print(f"the language is {self.lang} and the salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("good morning !!") 
        #dont need to poss whole object by using self

jaggu = employee()
jaggu.name = "jaggu"
print(jaggu.name)
jaggu.greet()

'''double underscore methods in python are called DUNDER METHODS'''