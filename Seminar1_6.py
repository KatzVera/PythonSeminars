# Задача 5: Программа находит наибольшее и наименьшее число из списка значений.

numbers = [1, 2, 9, 10, -3, -4, 5]
print(f' список {numbers}')
# print(f' максимум {max(numbers)}') вывод без цикла с применением встроенных функций min & max
# print(f' минимум {min(numbers)}')
min_value = numbers[0]
max_value = numbers[0]

for el in numbers: # el - для каждого элемента (введенный в цикле счетчик)
    # print(el)
    if el < min_value:
        min_value = el
    if el > max_value:
        max_value = el

print(f' максимум {max_value}')
print(f' минимум {min_value}')