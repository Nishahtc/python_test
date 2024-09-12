studentdata={1:4000,2:4000,3:15000,4:30000,5:10000,6:4000}
list=[]
#Get the maximum and Minum Salary with student id
#maxnum=max(studentdata.values())
#mini=min(studentdata.values())
#print(maxnum,mini)
for i in studentdata.values():
    list.append(i)
list.sort() 
for x,y in studentdata.items() :
    if y==list[2]:
        print(f"mini value {x} :{y}")
    if y==list[-1] :
        print(f"max value {x} :{y}")   



    


        


    
    






