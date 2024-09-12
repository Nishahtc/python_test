#How Do You Display the Contents of a Text File in Reverse Order?
path=r"D:\Nishatxt\nisha.txt"
with open(path,'r')as f:
    data=f.read()
reversed_data = data[::-1]  # Reverse the string
print(reversed_data)
    