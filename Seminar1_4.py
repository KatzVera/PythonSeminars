# Задача 3: Программа принимает на ввод число N.
#         На вывод выводич числа от -N до N


N = abs(
        int(input('Введите число N: ')))
# N = abs(N) # модуль числа - abs
i = -N
while i <= N:
    print(f'{i}\t', end='') # t - табуляция(большой пробел) end - для вывода в одну строку
    i += 1
