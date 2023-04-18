import random

n = input("Введите количество элементов в массииве: ")
x = input("Введите искомое число: ")
A = []
for i in range(int(n)):
    A.append(random.randint(0, 10))

print(A)

count_x = A.count(int(x))

if count_x == 0:
    print("Такого числа нет")
else:
    print("Число", x, "встречается ", count_x, "раз")