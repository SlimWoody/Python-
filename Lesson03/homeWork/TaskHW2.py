# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  
# строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

import random
n = int(input('Введите колличество элементов в списке: '))
list_1 = [random.randint(1, 9) for _ in range (n)]
print (*list_1)
x = int(input('Введите число для поиска ближайшего из списка: '))
nearest_x = list_1[0]

for i in list_1:
    if abs(x-i) < abs(x-nearest_x):
        nearest_x=i
print(nearest_x)