# Дано натуральное число N и последовательность
# из N элементов. Требуется вывести эту
# последовательность в обратном порядке.

# Примечание. В программе запрещается
# объявлять массивы и использовать
# циклы (даже для ввода и вывода).

def reverse(num):
    if num == 0:
        return ''
    m = input()
    return reverse(num-1) + m + " "

n = int(input())
print(reverse(n))