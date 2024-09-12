dic={1:"40000",2:"60000",3:"70000",4:"40000",5:"20000"}
list=[]
for i in dic.values():
    list.append(i)
list.sort()  
for x,y in dic.items() :
    if y==list[-1]:
        print(f"mini={x} :{y}") 
    if y==list[3] :
        print(f"max={x} :{y}")  


