
#function to write a table of n
def table(n,t = [],i = 10, ):
    if(i==0):#function return statement
        return
    
    table(n,t,i-1)#recursion

    temp = f"{n} x {i} = {n*i}\n"  #formatted string for table
    t.append(temp)
    
    return t  #returning the table list


#empty folder list
tables = []
#filling the folder list
for i in range(2,21):
    temp = f"Chapter9-ps/Tables/0{i}_table.txt"
    tables.append(temp)
    
n=2
for i in tables:
    with open(i,"w+") as f:
        temp = table(n)
        n+=1
        f.writelines(temp)
        temp.clear() #will write the lines given as list on to the file


