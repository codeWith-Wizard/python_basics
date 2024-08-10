#slicing of strngs
#indexing starts from satrt index to end index excluding end index

name = "tanishq";
nameshort = name[0:3]; #imp point==> last index is not printed or considered 
revNameShort = name[-5:-1]; #negative indexing
print(nameshort);
print(revNameShort); 
print(name[:4]);
print(name[1:]);

#conecpt of skip value during slincing
arr = "0123456789";
print(arr[0:9:2]); # the number on which index jumps is also printed 
print(arr[0:9:1]); #by default the jump is 1
print(arr[0:9:3]);

#space in string slicing
newarr = "hi i m tanishq";
print(newarr[:5]);
'''so ya!! spaces are also taken as string and will be indexed'''


#reversing the string using slicing
print(name[::-1]);
 
