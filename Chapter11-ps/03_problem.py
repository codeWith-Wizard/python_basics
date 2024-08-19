
class employee:
    
    def __init__(self, salary, increment):
        self.salary = salary
        self.increment = increment
        
    @property
    def salaryAfterIncrement(self):
        return (self.salary + (self.salary * self.increment /100))
    
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_salary):
        self.increment = ((new_salary / self.salary)-1)*100 
    

s1 = employee(12000, 20)
s1.salaryAfterIncrement =14400
print(s1.increment)