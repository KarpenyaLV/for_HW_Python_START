# Напишите программу, которая принимает на вход строку, и отслеживает, 
# сколько раз каждый символ уже встречался. Количество повторов добавляется к символам 
# с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Для решения данной задачи используйте функцию .split()

# arr = input('Введите символы через пробел: ').split()
# mn = list(set(arr))
# res = []

# k = [0 for i in range(len(mn))]

# for i in arr:
#     if i not in res:
#         res.append(i)
#     else:
#         for j in range(len(mn)):
#             if i == mn[j]:
#                 k[j] += 1
#                 res.append(i + "_" + str(k[j]))

# print(*res)

# #Вариант 2
# arr = input('Введите символы через пробел: ').split()
# d = {}

# for letter in arr:
#     if letter in d:
#         print(f'{letter}_{d[letter]}', end=' ')
#         # d[letter] += 1
#     else:
#         print(f'{letter}', end=' ')
#         # d[letter] = 1
#     d[letter] = d.get(letter, 0) + 1




# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов
# идущих подряд, слова разделены одним или большим числом пробелов. Определите, сколько различных слов
# содержится в этом тексте.

# Input: She sells sea shells on the sea shore The shells that she sells are sea shells 
# I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shor

# # Output: 13

# w = str(input()).split()

# print(len(set(w)))

# #второй вариант
# n = input('Введите несколько слов\n')
# n = n.upper()
# a = n.split()
# a = set(a)
# count = len(a)
# print(count)

# Ваня и Петя поспорили, кто быстрее решит следующую задачу: 
# “Задана последовательность неотрицательных целых чисел. 
# Требуется определить значение наибольшего элемента последовательности, 
# которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”. 
# Однако 2  друга оказались не такими смышлеными. 
# Никто из ребят не смог до конца сделать это задание. Они решили так: 
# у кого будет меньше ошибок в коде, тот и выиграл спор. 
# За помощью товарищи обратились к Вам, студентам.

# w = int(input())

# max = 0
# while w > 0:
#     w = int(input())
#     if w > max:
#         max = w

# print(max)

#второй вариант
max = 0
while n := int(input("Введите число: ")): # не сравниваем с 0, т.к. while работает пока условие true. 0 = false по умолчанию
    if n > max:
        max = n
print(f'Максимальное число в последовательности: {max}')