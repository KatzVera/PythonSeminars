# Задача 4. Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.
# 5 -> 2, 4
# 8 -> 2, 4, 6, 8

def HomeWork1_4():

    N = int(input('Введите число: '))
    count = 1
    while count < N:
        count += 1
        if count % 2 == 0: print(f'{count}\t', end='')

HomeWork1_4()



