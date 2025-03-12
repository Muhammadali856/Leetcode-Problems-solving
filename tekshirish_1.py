son1 = int(input("Birinchi sonni kiriting:"))
son2 = int(input("ikkinchi sonni kiriting:"))

operator = input("Operatorni kiriting: ")


if son1.isdigit(True) and son2.isdigit(True):
    if operator == "+":
        print("Natija: ", son1 + son2)
    elif operator == "-":
        print("Natija: ", son1 - son2)
    elif operator == "*":
        print("Natija: ", son1 * son2)
    elif operator == "/":
        if son2 != 0:
            print("Natija: ", son1 + son2)
        else:
            print("Sonni nolga bo'lib bo'lmaydi")
else:
    print("Ilitimos son kiriting.")
