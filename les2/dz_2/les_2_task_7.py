"""
7. Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n — любое натуральное число.
"""
n = int(input("Введите n: "))
s = 0
for i in range(1, n + 1):
    s += i

if s == n * (n + 1) / 2:
    print("Результаты совпадают")
else:
    print("Результаты не совпадают")