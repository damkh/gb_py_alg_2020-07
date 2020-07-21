"""
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""
import random


init_list = [random.randint(-5, 20) for _ in range(0, 10)]
print(f'Начальный массив: {init_list}')

# Поиск хотя бы одного отрицательного элемента
max_negative = 0
neg_idx = 0
flag = True
for idx in range(0, len(init_list)):
    if init_list[idx] < 0:
        if flag:
            max_negative = init_list[idx]
            neg_idx = idx
            flag = False
        if init_list[idx] > max_negative:
            max_negative = init_list[idx]
            neg_idx = idx
if max_negative == 0:
    print("Отрицательные элементы не найдены")
else:
    print(f'Максимальный отрицательный элемент {max_negative} с индексом {neg_idx}')


