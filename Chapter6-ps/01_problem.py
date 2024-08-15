#find the greatest of 4 no.s entered by the user

num_list = [];
grt_num = 0;

#taking input
for i in range(4):
    temp = int(input(f"enter no{i+1} : "))
    num_list.append(temp)


check = False;
        
for i in range(4):
    for j in range(4):
        if(i == j):
            continue
        if(num_list[i]>num_list[j]):
            check  = True
        else:
            check = False
    if (check==True):
        grt_num = num_list[i]
        break

print(grt_num);