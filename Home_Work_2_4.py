# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]

def HomeWork4_4():
    nums = []
    N = int(input('Введите число: '))
    newnums = []
    
    for el in range(-N, N+1):
        nums.append(el)
    print(nums)
    
    for i in nums:
        newnums.append(nums[i + 1])
    print(newnums)
        

HomeWork4_4()
