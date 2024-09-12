"""dic={'1':"one",'2':"two",'3':"three"}
del  dic['2']
print(dic)
a=dic.pop('1')
print(a)"""
dict={1:"nisha",3:"pritam",2:"raj"}
s=sorted(dict)
for key in s:
    value=dict[key]
    print(f"key-{key} values-{value}")
