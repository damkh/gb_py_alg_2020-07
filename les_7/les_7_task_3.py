"""
3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
Примечание: задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, используйте метод сортировки,
который не рассматривался на уроках (сортировка слиянием также недопустима).
"""
import random
import copy


def get_median_sort(arr):
    arr = sorted(arr)
    print(f'sorted arr: {arr}')
    return arr[len(arr) // 2]


def get_median(arr):
    if len(arr) == 1:
        return arr[0]
    m_idx = len(arr) // 2
    while True:
        median = arr[0]
        left = []
        right = []
        medians = []
        for el in arr:
            if el < median:
                left.append(el)
            elif el > median:
                right.append(el)
            else:
                medians.append(el)
        if len(left) > m_idx:
            arr = left
        elif len(left) + len(medians) > m_idx:
            return medians[0]
        else:
            arr = right
            m_idx -= (len(left) + len(medians))


m = 3
lst = [random.randint(0, 20) for _ in range(2 * m + 1)]

print(f'Начальный массив: {lst}')
print(f'Отсортированный массив: {sorted(lst)}')
print(f'Решение с сортировкой: {get_median_sort(copy.deepcopy(lst))}')
print(f'Решение без сортировки: {get_median(copy.deepcopy(lst))}')
