import numpy as np
list=[]
newlist=[]
user=input().split()
for i in user:
    y=int(i)
    list.append(y)
print(list)
for k in list:
    if k not in newlist:
        newlist.append(k)
newarry=np.array(newlist)
print(newarry)
for x in newarry:
    print(x,end=" ")

    





