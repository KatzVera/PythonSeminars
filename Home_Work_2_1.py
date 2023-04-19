# Задача 1: Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
# пусть N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def HomeWork2_1():
    N = int(input('Введите число: '))
    nums = []
    value = 1
    for i in range(1, N + 1):
        nums.append(value)
        value *= i + 1
    print(f'{N} -> {nums}')

HomeWork2_1()

