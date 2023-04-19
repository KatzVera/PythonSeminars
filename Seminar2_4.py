# Задача 3: Дано число N. Заполните список длинной N элементами: 1, -3, 9, -27, 81, -243

def zadacha_4():
    numbers = []
    N = int(input('Введите число: '))
    
    for el in range(N):
        numbers.append((-3)**el) # append - команда добавляющая элемент в список
        # print(f'{el} -> {(-3)**el}')
    print(numbers)

zadacha_4()
