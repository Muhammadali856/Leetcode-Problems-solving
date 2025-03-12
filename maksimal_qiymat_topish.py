list = []

for i in range(5):
    i = input("Son kiriting: ")
    list.append(i)

a = list[0]
for i in list:
    if a < i:
        a = i
print(a)