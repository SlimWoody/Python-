# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем 
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

import random

number = int(input("Введите максимум чисел: "))
list_1 = []
for i in range(number):
    list_1.append(random(-3, 3))
print(list_1)
print(len(set(list_1))) #set() выводит множиство, а во множестве хранятся только уникальные значения

# print(len(set(input().split())))

