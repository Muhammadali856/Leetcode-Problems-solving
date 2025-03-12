l1 = [2,4,3]
l2 = [5,6,4]

a1 = []

for i in l1:
    a1.append(i)

b1 = []

for i in l2:
    b1.append(i)


combined_list1 = ''.join(map(str, a1[::-1]))
combined_list2 = ''.join(map(str, b1[::-1]))

a2 = int(combined_list1)
b2 = int(combined_list2)

print(a2, b2)