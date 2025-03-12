import math

print("Bu dastur faqat sinusning lyuboy gradusini topish uchun ishlaydi")
gradus = int(input("Gradusni kiriting: "))
radian = gradus/57

i = 1

sin_gradus = (radian / math.factorial(i)) - ((radian**3) / math.factorial(i+2)) + ((radian**5) / math.factorial(i+4))

print("Natija: ",sin_gradus)