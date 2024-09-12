import os
import datetime
path="D:\nisha-file" 
one=os.path.getmtime(path+r'\first.txt')
two=os.path.getmtime(path+r'\second.txt')
data={}
data["first"]=one
data["second"]=two
print(data)
v=sorted(data.items(),key=lambda x:x[1],reverse=True) 
print("Latest File changed: ", v[0][0])