l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
l3 = []

len1 = len(l1)
len2 = len(l2)




if len1 != len2:
    if len1 > len2:
        for i in range((len2-1),(len1-1)):
            l2.append(0)
    else:
        for i in range((len1-1),(len2-1)):
            l1.append(0)

b = 0 #setting the carry variable

for i in range(len(l1)):
    x1 = l1[i]
    x2 = l2[i]
    x3 = x1 + x2
    if x3 > 9 or b == 1 :
        x3 = x3%10 + b
        if(x3 == 10):
            x3 = 0
        temp = x3
        
        b = 1
        
    else:
        x3 = x3 + b
        temp = x3
        b = 0

    l3.append(x3)
    if( b == 1 and i == (len(l1)-1)):
       l3.append(b)
       

print(l3)
    
