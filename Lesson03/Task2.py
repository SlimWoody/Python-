# Дана последовательность из N целых чисел и число 
# K. Необходимо сдвинуть всю последовательность 
# (сдвиг - циклический) на K элементов вправо, K – 
# положительное число.

# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# Примечание: Пользователь может вводить значения 
# списка или список задан изначально.

# list_1 = list(map(int, input().split())) # .split разбивка символы по пробелам. map() применяет int ко всем элементам. list формирует список. 
# k = int(input()) % len(list_1) - len(list_1) 
# [print(list_1[i+k], end=' ') for i in range(len(list_1))]

list_num = list(map(int, input().split()))
steps = int(input())

for i in range (steps):
    list_num.insert(0, list_num.pop())
print(list_num)