#filtering spam comments

filter_words =  ("Make a lot of money", "buy this" , "subscribe this" , "click this");

comment = input("enter expected comment : ");
status = True
for phrase in filter_words:
    if(phrase in comment):
        print("susupecetd spam!!")
        status = False
        break
if (status==True):
    print("ok no problem !")

