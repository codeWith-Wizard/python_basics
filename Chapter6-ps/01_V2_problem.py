#find the greatest of 4 no.s entered by the user

num_list = [];

#taking input
for i in range(4):
    temp = int(input(f"enter no{i+1} : "))
    num_list.append(temp)

grt_num = num_list[0];

for num in num_list:
    if(num > grt_num):
        grt_num = num

print(grt_num);