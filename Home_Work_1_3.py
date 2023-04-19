# Задача 3: Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).
# 1 -> x > 0, y > 0

def HomeWork1_3():
    N = int(input('Введите номер четверти: '))

    if N < 1 or N > 4: print('Такой четверти не существует')
    elif N == 1: print(f'Для {N}-ой четверти диапазон координат x > 0 и y > 0')
    elif N == 2: print(f'Для {N}-ой четверти диапазон координат x < 0 и y > 0')
    elif N == 3: print(f'Для {N}-ей четверти диапазон координат x < 0 и y < 0')
    elif N == 4: print(f'Для {N}-ой четверти диапазон координат x > 0 и y < 0')

HomeWork1_3()