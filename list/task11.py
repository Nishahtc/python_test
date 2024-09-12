def interger(int,sepatpr=" ,"):
    return sepatpr.join(map(str,int))
list=[1,2,3,4,5,6]
v=interger(list," -")
print(v)
