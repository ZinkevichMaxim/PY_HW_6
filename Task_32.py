# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random

min = int(input('Введите минимальное значение элемента \n'))
max = int(input('Введите максимальное значение элемент \n'))
n = int(input('Введите длину списка \n'))


list = [random.randint(1, 100) for i in range(n)]   # Генерация списка вариант 1
# list = [i for i in range(n)]                        # Генерация списка вариант 2
list_res = []


for i in range(n):
    if list[i] >=  min and list[i] <= max:
        list_res.append(i)
    
print(list)
print(list_res)

