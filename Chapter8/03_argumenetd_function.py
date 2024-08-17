def greet(name,ending = "by - by"):
    print("good day, "+ name)
    print(ending)
    return "ok"

greet("jaggu" ,"thanks" )
greet("rohan")

a = greet(name="kannu", ending="tata")
print(a, type(greet))
