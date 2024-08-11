#list concepts
#can store any type of datatype

fruits = ['apple' , 'banana', 10 , True , 49.1 , 'h'];
empty_list = [] # creates a empty list

#indexing of list
print(fruits[1]);
print(fruits[3]);
print(fruits[-1]);


#slicing of list
print(fruits[2:5]);
print(fruits[::1]);

#reversed list
print(fruits[::-1]);

#item assignment =>  shows that lists are mutable
fruits[1] = "grapes";
print(fruits);

#operations on list
a = [1,2,3];
b = [4,5,6];
print(a+b); #concatinate the lsit
print(a*2); #repetition of strings

#list comprehension =. used to create list in single line
square = [i**2 for i in range(10)];
print("squares from 1 to 9 are : ", square);