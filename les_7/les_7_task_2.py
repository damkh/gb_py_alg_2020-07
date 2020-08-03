"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""
import random


def merge_sort(arr):
    if len(arr) > 1:
        left = arr[:len(arr) // 2]
        right = arr[len(arr) // 2:]

        left = merge_sort(left)
        right = merge_sort(right)

        i = j = 0
        arr2 = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr2.append(left[i])
                i += 1
            else:
                arr2.append((right[j]))
                j += 1

        while i < len(left):
            arr2.append(left[i])
            i += 1
        while j < len(right):
            arr2.append(right[j])
            j += 1
        return arr2
    else:
        return arr


lst = [random.randint(0, 59) for _ in range(9)]

print(f'Начальный массив: {lst}')
print(f'Отсортированный массив: {merge_sort(lst)}')
