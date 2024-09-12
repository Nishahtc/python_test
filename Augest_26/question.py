import numpy as np
list=[]
user=input().split()
#print(user)

for i in user:
    y=int(i)
    list.append(y)
print(list)
newarr=np.array(list)
print(newarr)
newarr+=10
print(newarr)
newarr.sort()
print(newarr)


