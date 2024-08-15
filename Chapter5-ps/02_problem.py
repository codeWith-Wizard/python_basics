#input no.s from the user and displaying unique no.s

num_list = [];

#taking input from the user
for i in range(9):
    temp = input(f"enter no{i+1} : ") #*****imp statement used
    num_list.append(temp);

#converting input to set122
num_set = set(num_list)
print(num_set);