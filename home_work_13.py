'''
Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
и возводит число А в целую степень B с помощью рекурсии.
'''
def exp(a,b):
    if b == 1:
        return a
    return exp(a,b-1) * a

a = int(input("Введите число: "))
b = int(input("Введите степень числа(положительное число): "))
if b > 0:
    print(exp(a,b))
else:
    print('степень числа введена неверно')


