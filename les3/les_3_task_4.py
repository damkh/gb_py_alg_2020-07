"""
4. Определить, какое число в массиве встречается чаще всего.
"""
import random


init_list = [random.randint(1, 5) for _ in range(0, 10)]
print(f'Начальный массив: {init_list}')

max_count_el = init_list[0]
max_count = 0
for el in init_list:
    curr_count = init_list.count(el)
    if curr_count > max_count:
        max_count_el = el
        max_count = curr_count

print(f'Элемент {max_count_el} повторяется чаще остальных - {max_count}')
