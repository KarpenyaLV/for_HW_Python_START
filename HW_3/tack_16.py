# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai (можно использовать псевдогенерацию). 
# Последняя строка содержит число X.

# *Пример:*

# 5
#     7 -2 3 5 1
#     3
#     -> 1

N = abs(int(input('Введите количество элементов массива А: ')))
A_entered = input("Введите через пробел элементы массива: ").split()
A_num = list(map(int, A_entered))
if len(A_num) != N:
    print('Введенные элементы не соответствуют заявленному количеству!')
else:
    X = int(input('Введите число X, которое необходимо найти в массиве: '))
    count = 0
    for i in range(N):
        if A_num[i] == X:
            count += 1
    print(f'Число {X} встречается в массиве A {count} раз') 