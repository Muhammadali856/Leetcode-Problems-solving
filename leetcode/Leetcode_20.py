s = "(){}([]"

given_list = list(s)

tekshirish1 = False

qavs1 = ['(', ')']
qavs2 = ['{', '}']
qavs3 = ['[', ']']


for i in range(len(given_list)):
    tekshirish2 = False
    tekshirish3 = False
    if given_list[i] == qavs1[0]:
        for j in range(i+1, len(given_list)):
            if given_list[j] == qavs1[1]:
                tekshirish2 = True
                tekshirish3 = True
                break
    elif given_list[i] == qavs2[0]:
        for j in range(i+1, len(given_list)):
            if given_list[j] == qavs2[1]:
                tekshirish2 = True
                tekshirish3 = True
                break
    
    elif given_list[i] == qavs3[0]:
        for j in range(i+1, len(given_list)):
            if given_list[j] == qavs3[1]:
                tekshirish2 = True
                tekshirish3 = True
                break
    else:
        pass
    
    if tekshirish2 == False:
        tekshirish1 == False
        break
    elif tekshirish3 == False:
        tekshirish1 = False
        break
    else:
        tekshirish1 = True
        break

print(tekshirish1)