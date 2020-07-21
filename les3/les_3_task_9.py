"""
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""
import random


rows = 5
columns = 4

arr = [[random.randint(1, 10) for _ in range(0, columns)] for _ in range(0, rows)]
for row in arr:
    for el in row:
        print(f'{el:>5}', end='')
    print()

max_min = None
flag = True
for col in range(0, columns):
    min_col = arr[0][col]
    for el in range(0, rows):
        if arr[el][col] < min_col:
            min_col = arr[el][col]
    print(f'Минимальный элемент в солбце {col + 1}: {min_col}')
    if flag:
        max_min = min_col
        flag = False
    if min_col > max_min:
        max_min = min_col

print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: {max_min}')