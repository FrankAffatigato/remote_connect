list1 = [1, 2, 3, 4, 5]
output = []

for i in list1:
    output.append(sum(list1[:list1.index(i) + 1]))

print(output)
