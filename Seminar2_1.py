# Задача 0: Дано число N. ДНайти все его делители и для каждого делителя указать четный или нет.

def check(number):
    if number % 2 == 0: return('четное')
    else: return('нечетное')

def zadacha_1():
    num = int(input('Введите число: '))
# count = 1
# while count <= num:
#     print(count)
#     count +=1

    for i in range(1, num + 1):
    #print(i)
        if num % i == 0:
            print(f'{i} {check(i)}')
        #     if i % 2 == 0: print (f'{i} четное')
        #     else: print(f'{i} нечетное')

zadacha_1()