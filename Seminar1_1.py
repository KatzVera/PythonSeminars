# Программа принимает на вход число, на выход выдает его квадрат.
# Задача 0

#num = int(input('Введите число: '))
#num = int(num)
#print(f'Квадрат {num} = {num**2}')

"""
За день машина проезжает N километров.
Сколько дней нужно, чтобы машина проехала маршрут в M километров?
При решении нельзя пользоваться if или циклами.
"""
n = int(input('Введите кол-во км в день: '))
m = int(input('Введите длинну маршрута в км: '))

res = int(bool(m % n))
days = m // n + res

print(f'В день по {n} км, маршрут {m} км, пронадобится {days} дней')