import sys
x = 10
x2 = x


#  BU KOD MUVAFFAQQIYATLI YAKUNLANDI

l1 = []

while x2 > 0:
    digit = x2 % 10
    l1.append(digit)
    x2 = x2 // 10

nimadir = None
counter = 0

if len(l1) % 2 == 0:
    print(l1)
    for i in range(len(l1) // 2):
        if l1[i] == l1[-(i+1)]:
            continue
        else:
            print(False)
            nimadir = False
            break
    if nimadir != False:
        print(True)
    sys.exit()    


if len(l1) % 2 == 1:
    # l1.insert(0, 0)
    for i in range((len(l1)) // 2):
        if l1[i] == l1[-1]:
            continue
        else:
            print(False)
            nimadir = False
            break
    if nimadir != False:
        print(True)