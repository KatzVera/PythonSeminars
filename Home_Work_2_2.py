# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.
# X   Y   Z   (X ∧ Y) ¬(X ∧ Y)    ¬(X ∧ Y) ∨ Z
# 0   0   0      0        1             1  
# 0   0   1      0        1             1
# 0   1   0      0        1             1
# 0   1   1      0        1             1
# 1   0   0      0        1             1
# 1   0   1      0        1             1
# 1   1   0      1        0             0
# 1   1   1      1        0             1


def HomeWork2_2():
    print(f'X | Y | Z | ¬(X ∧ Y) ∨ Z ')
    for x in range(0,2):
        for y in range(0,2):
            for z in range(0,2):
                print(f'{x} | {y} | {z} |   {int(not (x and y)or z)}')

HomeWork2_2()