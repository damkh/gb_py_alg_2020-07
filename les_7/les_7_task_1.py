"""
1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Примечания:
a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

bubble_desc - метод пузырька без улучшений
bubble_desc_adv - метод пузырька с улучшением - если во внутреннем цикле не произошло ни одного обмена,
значит массив отсортирован, можно завершить внешний цикл.
Результаты замеров времени для обоих видов сортировки, улучшенный метод быстрее где-то на 5%:
python -m timeit -n 100 -s "import les_7_task_1" "les_7_task_1.bubble_desc()"
100 loops, best of 5: 80.5 msec per loop
python -m timeit -n 100 -s "import les_7_task_1" "les_7_task_1.bubble_desc_adv()"
100 loops, best of 5: 76.4 msec per loop
"""
import random
import copy


def bubble_desc(arr):
    n = 1
    while n < len(arr):
        k = 0
        for i in range(len(arr) - n):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                k += 1
        n += 1
    return arr


def bubble_desc_adv(arr):
    n = 1
    end_idx = len(arr)
    while n < end_idx:
        k = False
        for i in range(end_idx - n):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                k = True
        if not k:
            break
        n += 1
    return arr


lst = [random.randint(-100, 99) for _ in range(20)]

print(f'Начальный массив: {lst}')
lst_1 = bubble_desc(copy.deepcopy(lst))
print(f'Отсортированный массив: {lst_1}')
lst_2 = bubble_desc_adv(copy.deepcopy(lst))
print(f'Отсортированный массив улучшенный: {lst_2}')
print(f'Равны ли отсортированные массивы: {lst_1 == lst_2}')
