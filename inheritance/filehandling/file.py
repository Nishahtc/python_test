import os
import datetime
path1 = r"D:\nisha-file\first.txt"
path2 = r"D:\nisha-file\second.txt"
path3 = r"D:\nisha-file\final.txt"
with open(path1,'r') as f1:
    data1=f1.read()
with open(path2,'r') as f2:
    data2=f2.read()
combined_data = "=== Data from first.txt ===\n" + data1 + "\n\n" + "=== Data from second.txt ===\n" + data2
with open(path3,'w')as f3:
    f3.write(combined_data)
print("files marged sucessfully")

modified_time = os.path.getmtime(path3)
time_readable = datetime.datetime.fromtimestamp(modified_time)
print(f"marged file{os.path.basename(path1)and {os.path.basename(path2)}}",time_readable)




    import os
import datetime
path=r"D:\Development\Live Class and Student Document\python\Class PDF\Practice" 
one=os.path.getmtime(path+r'\one.txt')
two=os.path.getmtime(path+r'\two.txt')
data={}
data["one"]=one
data["two"]=two
print(data)
v=sorted(data.items(),key=lambda x:x[1],reverse=True) 
print("Latest File changed: ", v[0][0])