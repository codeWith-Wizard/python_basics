#len function returns the length of the function
a = "tanishq";
print(len(a));

#enswith function => used to check if the string ends with the given string or not
print(a.endswith("q"));
print(a.endswith("h"));
print(a.endswith("hq"));

#startswith function => similar to ends with
print(a.startswith("t"));
print(a.startswith("T")); #case sensitive


#capitalize function => used to capitalize the first letter of the string
print(a.capitalize());

#lower function => makes every letter smalll
print(a.lower());

#upper function => make every letter capital
print(a.upper());

'''orignal string remains same'''

print(a);

#title function => first character of each word is captilalized along with making other letters small
b = "hi my name is tANishq";
print(b);
print(b.title());

#count function => counts the toatal no. of occurences of that given character 
print(a.count("t"));
print(b.count("i"));
print(b.count("z"));
print(b.count(" ")); #blank space


#find function => used yto find teh index of the given character from the string
print(a.find("i"));
print(b.find("i")); #if multiple then gives the address of the first occurence

#replace function => replace the given word with given word
newWord = "hello hello world world   ";
print(newWord.replace("hello","hi")); 
# does not update the string
print(newWord);
'''very helpfull if used to remove extra spaces'''
print(newWord.replace(" ","*" ));