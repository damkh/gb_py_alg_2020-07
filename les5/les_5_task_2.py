"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления,
задача решается в несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит.
Поэтому использование встроенных функций для перевода из одной системы счисления в другую в данной задаче под запретом.
"""
from collections import deque
from copy import deepcopy


def check16(lst):
    for idx, el in enumerate(lst):
        k = ord(el)
        if 48 > k or 57 < k < 65 or 70 < k < 97 or k > 102:
            print(f"{el} в {lst} не 16-ричный символ")
            return False
        lst[idx] = el.upper()
    return True


def ext_dim(n, m):
    if len(n) >= len(m):
        m = ['0' for _ in range(len(n) - len(m))] + m
    else:
        n = ['0' for _ in range(len(m) - len(n))] + n
    return n, m


# Функция для расчета суммы двух 16-ричных символов
def sum16_1(m, n):
    if len(m) > 1 or len(n) > 1:
        raise ValueError('Больше чем 1 символ')
    return sum16tab[t.index(m)][t.index(n)]


def sum16(m, n):
    res = deque()
    buff = '0'
    for i in range(-1, -len(m) - 1, -1):
        # print(i)
        s = sum16_1(m[i], n[i])
        # print(f'- {i} buff: {buff} s: {s}')
        buff0 = buff
        if len(s) > 1:
            # print(f's[0]: {s[0]}, s[1]: {s[1]}')
            buff = s[0]
            # print(f'-- {i} buff: {buff} s: {s}')
            s = sum16_1(s[1], buff0)
            # print(f'--- {i} buff: {buff} s: {s}')
        else:
            s = sum16_1(s, buff0)
            buff = '0'
        if len(s) > 1:
            # buff = s[0]
            res.appendleft(s[1])
            buff = s[0]
        else:
            res.appendleft(s)
        if i == -len(m) and buff != '0':
            res.appendleft(buff)
        # print(res)
    return list(res)


def mult16(m, n):
    s = ['1']
    one = ['1']
    res = m
    while s != n:
        s, n = ext_dim(deepcopy(s), deepcopy(n))
        s, one = ext_dim(deepcopy(s), deepcopy(one))
        s = sum16(s, one)
        res, m = ext_dim(deepcopy(res), deepcopy(m))
        res = sum16(res, m)
    return res


def gen16tab(t_deque):
    t_fix = list(t_deque)
    tab = [list(t_deque)]
    c = 1
    for i in t_fix[:-1]:
        t_deque.append(t_fix[c] + i)
        tab.append(list(t_deque))
    return tab


t = deque(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'], maxlen=16)
sum16tab = gen16tab(deepcopy(t))

num1 = list(input("Введите 1е число,например F3B1 (0-9a-fA-F): "))
num2 = list(input("Введите 2е число,например F3B1 (0-9a-fA-F): "))
if check16(num1) and check16(num2):
    print(f'num1: {num1}')
    print(f'num2: {num2}')
    num1, num2 = ext_dim(deepcopy(num1), deepcopy(num2))

    print(f'Сумма: {sum16(num1, num2)}')
    print(f'Произведение: {mult16(num1, num2)}')
