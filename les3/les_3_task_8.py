"""
8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

rows = 5
columns = 4
arr = []

for row_num in range(0, rows):
    row = []
    for col_num in range(0, columns):
        if col_num < columns - 1:
            row.append(int(input(f"Введите {col_num + 1}й элемент {row_num + 1}й строки: ")))
        else:
            s = 0
            for row_el in row:
                s += row_el
            row.append(s)
    arr.append(row)

for row in arr:
    for el in row:
        print(f'{el:>5}', end='')
    print()
