# Задача 1: Выведите таблицу истенности для выражения -X v Y
#   X   Y   XvY
#   0   0    1
#   0   1    1
#   1   0    0
#   1   1    1

#def zadacha_2():
    #print(f'x | y | XvY ')
    #for x in range(0,2):
        #for y in range(0,2):
            #print(f'{x} | {y} |  {int(not x or y)}')

#zadacha_2()

'''
Задача 11: Данов число A > 1. 
Определить и вывести каким по чету числом Фибаначи является число A.
Если A не является числом Фибоначчи, то вывести -1.
'''

a = int(input('Введите число A: '))
count = 3
n1, n2 = 0, 1

if a > 1:
    while n1 + n2 < a:
        count += 1
        n1, n2 = n2, n1 + n2

    if n1 + n2 == a:
        print(f'Число {a} является {count} по счету числом Фибоначчи')
    
    else: print(f'-1')

else: print('Введенное число должно быть больше 1')
