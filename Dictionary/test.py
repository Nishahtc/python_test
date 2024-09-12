dic={
    '1':"2000",
    '2':"4000",
    '3':"10000",
    '4':"4000",
    
}
v=dic.get('2')
print(v)

print(dic['4'])
for i,x in dic.items():
    print(f"key-{i}value-{x}")

for y in dic.keys():
    print(y)
for s in dic.values():
    print(s)    
