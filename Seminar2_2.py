# Задача 1: Выведите таблицу истенности для выражения -X v Y
#   X   Y   XvY
#   0   0    1
#   0   1    1
#   1   0    0
#   1   1    1

def zadacha_2():
    print(f'x | y | XvY ')
    for x in range(0,2):
        for y in range(0,2):
            print(f'{x} | {y} |  {int(not x or y)}')

zadacha_2()