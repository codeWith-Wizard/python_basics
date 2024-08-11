a = (1,2,0,2,2,2,2,9,4,5,5,5,3,3,1,32,21);
seen = [];
for i in range(len(a)):
    if a.count(a[i]) >1 and a[i] not in seen:
        print(a[i]);
        seen.append(a[i]);