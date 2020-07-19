"""
9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""


def dig_sum(x):
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s


quantity = int(input("Введите количество чисел (>0): "))
s_max = 0
num_max = 0

while quantity != 0:
    num = int(input("Введите число: "))
    curr_dig_sum = dig_sum(num)
    if curr_dig_sum >= s_max:
        num_max = num
        s_max = curr_dig_sum
    quantity -= 1

print(f'{num_max}:{s_max}')
