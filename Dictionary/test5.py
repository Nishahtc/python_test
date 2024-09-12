one=[1,2,6,6,9]
two=[5,2,3,10,7]
output=[]
for i in one:
    if i not in output:
        output.append(i)
for y in two:
    if y not in output:
        output.append(y) 
print(output)               


        
