import os

path1 = r"D:\nisha-file\first.txt"
path2 = r"D:\nisha-file\second.txt"
path3 = r"D:\nisha-file\final.txt"

with open(path1,'r')as f1:
    data1=f1.read()

with open(path2,'r')as f2:
    data2=f2.read()

combined_data=data1+"\n"+data2
with open(path3,'w')as f3:
    f3.write(combined_data)
print("Files merged successfully!")

