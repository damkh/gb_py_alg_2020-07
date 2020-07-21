"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
import random


init_list = [random.randint(1, 100) for _ in range(0, 10)]
print(f'Начальный массив: {init_list}')

min_el = init_list[0]
max_el = init_list[0]
min_idx = 0
max_idx = 0
for idx in range(0, len(init_list)):
    if init_list[idx] > max_el:
        max_el = init_list[idx]
        max_idx = idx
    if init_list[idx] < min_el:
        min_el = init_list[idx]
        min_idx = idx
print(f'Минимальный элемент {min_el} с индексом {min_idx},'
      f'\nМаксимальный элемент {max_el} с индексом {max_idx}')

if min_idx > max_idx:
    min_idx, max_idx = max_idx, min_idx

s = 0
for idx in range(min_idx + 1, max_idx):
    s += init_list[idx]
print(f'Сумма между индексами {min_idx} и {max_idx}: {s}')


