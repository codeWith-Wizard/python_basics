#using different dictionary methods

marks = {
    "s1" : 90,
    "s2" : 93,
    "s3" : 63,
    "s4" : 76
    }

#1 items method
print(marks.items());

#2 keys method
print(marks.keys());

#3 values method
print(marks.values());

#4 update method ==> use d to update the dictionary
marks.update({"s1" : 78});
print(marks);

#can uopdate method add new key value pair 
marks.update({"s5" : 67});
print(marks); 
#ans is yes

#5 get method ==> use to return the value of the key
print(marks.get("s1"));
print(marks.get("s6")); #getting value of non existing key returns None
#print(marks["s6"]); will give error  

'''removing elements'''

del marks["s1"];
print(marks);

a = marks.pop("s2"); #returns the value of the key
print(marks);
print(a, "got deleted .");


#===> popitem method takes no argument
b = marks.popitem(); #deletes and returns the last element
print(marks);
print( b, " got deleted .");


