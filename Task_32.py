# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random

min = int(input('Введите минимальное значение элемента \n'))
max = int(input('Введите максимальное значение элемент \n'))
# n = int(input('Введите длину списка \n'))

list = [1, 3, 5, 6, 17, 9, 11, 13, 10, 6]

# list = [i for i in range(n)]
list_res = []

# print(list)

for i in range(len(list)):
    if list[i]>min and list[i]<max:
        list_res.append(i)
    
print(list)
print(list_res)