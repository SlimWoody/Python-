# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

num = int(input('Введите шестизначное число: '))

sumThreeDigitsA = 0
sumThreeDigitsB = 0 

if (num > 99999 and num < 1000000):
    tempA = num // 1000
    while (tempA > 0):
        digitA = tempA%10
        sumThreeDigitsA += digitA
        tempA //= 10

    tempB = num % 1000
    while (tempB > 0):
        digitB = tempB%10
        sumThreeDigitsB += digitB 
        tempB //= 10
else:
    print('Введены не коректные данные') 

if sumThreeDigitsA == sumThreeDigitsB:
    print('Yes')
else:
    print('No')
