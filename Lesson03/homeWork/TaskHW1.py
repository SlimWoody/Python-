# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1
import random
n = int(input('Введите колличество элементов в списке: '))
list_1 = [random.randint(1, 9) for _ in range (n)]
print (*list_1)
x = int(input('Введите число для сравнения повторений в списке: '))
count = 0
for i in range(len(list_1)):
    if list_1[i] == x:
        count += 1
print(count)

