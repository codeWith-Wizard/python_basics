#different methods in list

'''methods of list updates the list'''

fruits = ['apple' , 'banana', 10 , True , 49.1 , 'h'];

#append method => adds given value at the last of the list
print(fruits.append("library"));  #*****returns none
print(fruits);

#insert method => used to isert given value at given index
fruits.insert(1, 'lol');
print(len(fruits));
print(fruits);

#sort method => used to sort a numbered list 
#fruits.sort();
arr = [1,4,0,6,43,3,2,2,3,4,25,7,8];
print(arr.sort());
print(arr);

#reverse method => used to reverse a list\
fruits.reverse();
print(fruits);

