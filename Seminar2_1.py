# Задача 0: Дано число N. ДНайти все его делители и для каждого делителя указать четный или нет.

#def check(number):
    #if n % 2 == 0:
        #return('четное')
    #else: return('нечетное')

#def zadacha_1():
    #num = int(input('Введите число: '))
# count = 1
# while count <= num:
#     print(count)
#     count +=1

    #for i in range(1, num + 1):
    #print(i)
        #if num % i == 0:
            #print(f'{i} {check(i)}')
        #     if i % 2 == 0: print (f'{i} четное')
        #     else: print(f'{i} нечетное')

#zadacha_1()

"""
Задача 9: Программа на вход принимает положительное число N.
На выход выдает факториал !N.
"""

n = int(input('Введите положительное число: '))
factorial = n
if n >= 0:
    for i in range(2, n):
        factorial *= i
    print(f'Факториал {n} = {factorial}')

else: print('Введенное число меньше 0')