"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
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

print(f'min: {min_el}, max: {max_el}')
init_list[min_idx], init_list[max_idx] = max_el, min_el
print(f'Измененный массив: {init_list}')
