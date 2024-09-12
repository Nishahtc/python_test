"""studentdata={1:4000,2:4000,3:15000,4:30000,5:10000,6:4000}
list=[]
for i in studentdata.values():
    list.append(i)
list.sort()
for x,y in studentdata.items():
    if y==list[3]:
        print(f"avarage value{y}")"""


studentdata={1:4000,2:4000,3:15000,4:30000,5:10000,6:4000}
salary=sum(studentdata.values())
length=len(studentdata)  
average=salary/length
print(f"average salary {average}")
   
    
