# Задача 1: Программа принимает на вход числа. На выход проверяет является ли одно квадратом другого.

#num1 = int(input('Введите 1-ео число: '))
#num2 = int(input('Введите 2-ое число: '))
#if num1**2 == num2:print(f'да, {num2} квадрат {num1}')
#else:print(f'нет, {num2} не квадрат {num1}')

"""
В школе решили набрать 3 новых математических класса
и оборудовать кабинеты для них новыми партами.
За каждой партой может сидеть 2 ученика. 
Известноколичество учищихся в каждом классе.
Выведите наименьшее количество парт, которое необходимо?
"""
classA = int(input("Введите число учеников A класса: "))
classB = int(input("Введите число учеников B класса: "))
classC = int(input("Введите число учеников C класса: "))

if classA % 2 == 0:
    tableA = classA //2
else:
    tableA = (classA // 2) + (classA % 2)

if classB % 2 == 0:
    tableB = classB //2
else:
    tableB = (classB // 2) + (classB % 2)

if classC % 2 == 0:
    tableC = classC //2
else:
    tableC = (classC // 2) + (classC % 2)

print(tableA + tableB + tableC)