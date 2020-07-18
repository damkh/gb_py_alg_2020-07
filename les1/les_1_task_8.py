"""
8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
"""
try:
    a = float(input("Введите первое число a: "))
    b = float(input("Введите первое число b: "))
    c = float(input("Введите первое число c: "))

    min_n = min(a, b, c)
    max_n = max(a, b, c)

    if a != min_n and a != max_n:
        print(f'Среднее число: {a}')
    elif b != min_n and b != max_n:
        print(f'Среднее число: {b}')
    elif c != min_n and c != max_n:
        print(f'Среднее число: {c}')
    else:
        print("Некоторые или все числа равны")
except ValueError:
    print("Введено не число")
