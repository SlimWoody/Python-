# Задача 2: Найдите сумму цифр трехзначного числа. 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0

num = int(input('Введите 3-х значное число: '))


# Второе решение 
sum = 0

if (num > 99 and num < 1000):
    while (num>0):
        temp = num % 10
        sum +=temp
        num //= 10
else:
    print('Введены не корректные данные!')

print(f'Сумма чисел {sum}')

# Первое решение
#  
# c = n%10  
# n = n//10
# b = n%10
# n = n//10
# a = n%10

# sum = c + b + a 
# print(sum)