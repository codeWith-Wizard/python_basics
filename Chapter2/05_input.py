#getting input from users
a = input("enter no.1 : ");
b = input("enter no.2 : ");
c = a+b;
print("sum of ", a," and ", b, " is : ", c ," .");
print("string concatenation performed !!");

# the output will be string cause the default input type in python is string;
#=====> string concatenation is going on

a = int(input("enter no.1 : ")); #==> doing explicit type casting
b = int(input("enter no.2 : "));
c = a+b;
print("sum of ", a," and ", b, " is : ", c ," .");