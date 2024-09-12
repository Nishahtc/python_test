def string(words,separtor=""):
    return separtor.join (words)
list=["hello","world","this","is","python" ]
space=string(list)
print(space)
comma=string(list,",")
print(comma)