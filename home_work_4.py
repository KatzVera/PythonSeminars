'''
Задача 8: Требуется определить, можно ли от шоколадки 
размером N x M долек отломить K долек, 
если разрешается сделать один разлом по прямой между дольками 
(то есть разломить шоколадку на два прямоугольника).
'''
n = int(input('Введите длинну долек шоколадки: '))
m = int(input('Введите ширину долек шоколадки: '))
k = int(input('Сколько долек отломить: '))
if k < m * n and ((k % n == 0) or (k % m == 0)):
    print(f'Можно разделить шоколадку на {k} долек')
else:
    print(f'Нельза поделить шоколадку на {k} долек')