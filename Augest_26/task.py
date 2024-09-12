one = [1, 2, 3, 4, 5]
second = [10, 2, 4, 5]
output = []
for x in one:
    if x not in output:
        output.append(x)
for y in second:
    if y not in output:
        output.append(y)
print(output)