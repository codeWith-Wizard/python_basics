#arithmetic operations ===>
#import sys

a=7;
b=4;
c =a+b ;
c2 = a-b;
c3 = a*b;
c4 = a/b;
c5 = a%b;
c6 = a//b;
c7 = a**2; #exponential

print(c);
print(c2);
print(c3);
print(c4);
print(c5);
print(c6);
print(c7);

#assignment operators ===>
a= 4-2;
b += 3; #increment the value of b by 3 and then assign it in b
print(b);
b-=3;#decrement b by 3 and then assign the value to b 
print(b);
b*=4;#multiply the value of b by 4 and then assign it to b
print(b); 
b/=8;#dividing b by 8 and then assigning it to b
print(b);


#comparison operators ===> 
'''these opearators always give boolean values'''
d= 5<4;
print(d);
d= 5 ==4;
print(d);
d= 5!=4;
print(d);


#logical operators ===>

e= 0 and 1;
print(e);
#print(sys.getsizeof(e));
e = 0 or 1;
print(e);
e= not 0;
print(e);

