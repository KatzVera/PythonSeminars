# Задача 3: Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

def HomeWork2_3():
    substring = input('Введите 1-ую строку: ')
    text = input('Введите 2-ую строку: ')
    length_text = len(text)
    length_substr = len(substring)

    for j in range(length_substr):
        count = 0
        for i in range(length_text):
            if substring [j] == text[i]:
                count += 1
        print(f'Символ {substring[j]} из 1-ой стронки, встречсается {count} раз во второй строке')
    

HomeWork2_3()