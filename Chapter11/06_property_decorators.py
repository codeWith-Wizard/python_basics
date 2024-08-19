class employee:
    
    def __init__(self,name):
        print("constructor called")
        self.name = name
        
    
    @property  #decorators
    def name(self):
        print("propery name called !!")
        return f"{self.fname} {self.lname}"
    
    @name.setter #decorators
    def name(self,value):
        print("setter called !!")
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
        
jaggu = employee("jaggu bandar")

print("started")
print(jaggu.name) 
print(jaggu.fname) 
print(jaggu.lname) 
    
    