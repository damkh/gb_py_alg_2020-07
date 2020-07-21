"""
7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться.
"""
import random


init_list = [random.randint(1, 10) for _ in range(0, 10)]
print(f'Начальный массив: {init_list}')

n = 2
min_list = []
for i in range(0, n):
    min_el = init_list[0]
    min_idx = 0
    for idx in range(0, len(init_list)):
        if init_list[idx] <= min_el:
            min_el = init_list[idx]
            min_idx = idx
    min_list.append(min_el)
    if i < n - 1:
        init_list.pop(min_idx)

print(f'Два наименьших элемента: {min_list}')
