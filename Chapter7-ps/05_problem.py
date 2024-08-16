#sum of first n natural no.s using while loop

n = int(input("enetr the no. : "))
i = 1
sum_n = 0

while(i<=n):
    sum_n +=i
    i+=1

print("the sum upto ", n , " is ",sum_n) 
