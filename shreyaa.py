list=[str(x) for x in input().split()]
list1=[]
for i in list:
    for j in range(len(i)):
        if(i[j]=='s'):
            list1.append(i)
print(list1)