# Задача 2: Программа принимает 2 строки и определяет кол-во вложений одной строки в другую.

def zadach_3():
    substring = input('Введите строку: ')
    phrase = input('Введите фразу: ')
    length_phrase = len(phrase)
    length_substr = len(substring)
    count = 0
    # for el in phrase:
    #     print(el, end=' ')
    for i in range(length_phrase):
        if phrase [i: i+length_substr] == substring:
            count += 1
        #print(phrase[i: i+length_substr])
    print(f'в фразе {phrase} подстрока {substring} встречается {count} раз')

zadach_3()