#sometimes thgere is no need to send whole object into the method 
#this is the case when static methods are use
class employee:
    lang ="python"
    salary = 1200000

    def getInfo(self):
        print(f"the language is {self.lang} and the salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("good morning !!") 
        #dont need to poss whole object by using self

jaggu = employee()
jaggu.greet()