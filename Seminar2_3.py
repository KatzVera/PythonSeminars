# Задача 2: Программа принимает 2 строки и определяет кол-во вложений одной строки в другую.

#def zadach_3():
    #substring = input('Введите строку: ')
    #phrase = input('Введите фразу: ')
    #length_phrase = len(phrase)
    #length_substr = len(substring)
    #count = 0
    # for el in phrase:
    #     print(el, end=' ')
    #for i in range(length_phrase):
        #if phrase [i: i+length_substr] == substring:
            #count += 1
        #print(phrase[i: i+length_substr])
    #print(f'в фразе {phrase} подстрока {substring} встречается {count} раз')

#zadach_3()

'''
Задача 13: Программа на вход принимает количество дней N (1 <= N <= 100).
Каждое число среднесуточная температура. Температуры лежат в диапазоне -50 до 50.
Определить сколько дней было с температорой > 0.
'''
n = int(input('Введите количество дней: '))
count_plus_temp = 0
max_count = 0
for i in range(n):
    temp = int(input('Введите температуру от -50 до 50: '))
    if temp > 0:
        count_plus_temp +=1
    else:
        if count_plus_temp > max_count:
            max_count = count_plus_temp
            count_plus_temp = 0
    
print(max_count)



