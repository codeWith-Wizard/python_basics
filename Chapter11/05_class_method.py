

class value:
    a = 1

    @classmethod  #allows to acces the class attributes
    def show(cls):
        print(f"the value of class attribute a is : {cls.a}")  

e  = value()
e.a = 20
e.show()