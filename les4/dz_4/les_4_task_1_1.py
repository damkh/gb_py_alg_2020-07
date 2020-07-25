"""
Задача:
2.4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.

Вывод
Было проанализировано 3 различных варианта решения задачи:
1) Через цикл while (n_sum_while)
2) Через рекурсию (n_sum_rec)
3) Через формулу суммы элементов геометрической прогрессии (n_sum_gp)
Ограничения:
Метод 2 имеет ограничения вложенности рекурсии (при дефолтных настройках получилось посчитать максимум для n=991)
Скорость:
Самым медленным оказался метод 2 - при n=991 время 1000 выполнений составило около 229 usec на цикл
Средним по скорости оказался метод 1 - при n=1000 время 1000 выполнений составило около 80 usec на цикл
Быстрее всего считает метод 3 - через формулу суммы n первых элементов геометриеской прогрессии, так как
этот способ по сути не содержит циклов (кроме встроенной операции возведения в степень),
время 1000 выполнений составило около 0.3 usec на цикл и почти не менялось при изменении n от 10 до 10000000.
Все реузльтаты по timeit и cProfile даны в конце файла.
"""
import cProfile


def test_f(func):
    lst = [1, 0.5, 0.75, 0.625, 0.6875, 0.65625, 0.671875, 0.6640625, 0.66796875, 0.666015625]
    for i, item in enumerate(lst):
        assert item == func(i + 1)
        print(f'Test {i} OK')


def n_sum_while(n):
    if n == 1:
        return n
    s_n = 0
    n_1 = 1
    while n > 0:
        s_n += n_1
        n_1 *= step
        n -= 1
    return s_n


def n_sum_rec(n):
    n_1 = 1
    if n == 1:
        return n_1
    s_n = 1 + step * n_sum_rec(n - 1)
    return s_n


def n_sum_gp(n):
    n_1 = 1
    s_n = n_1 * (1 - step ** n) / (1 - step)
    return s_n


step = -0.5
#####
### n_sum_while - через цикл while:
## timeit
# "les_4_task_1_1.n_sum_while(10)"
# 1000 loops, best of 5: 895 nsec per loop
# "les_4_task_1_1.n_sum_while(100)"
# 1000 loops, best of 5: 7.21 usec per loop
# "les_4_task_1_1.n_sum_while(1000)"
# 1000 loops, best of 5: 80 usec per loop
# "les_4_task_1_1.n_sum_while(10000)"
# 1000 loops, best of 5: 825 usec per loop

## cProfile
# cProfile.run('n_sum_while(10)')
# 1    0.000    0.000    0.000    0.000 les_4_task_1_1.py:15(n_sum_while)
# cProfile.run('n_sum_while(100)')
# 1    0.000    0.000    0.000    0.000 les_4_task_1_1.py:15(n_sum_while)
# cProfile.run('n_sum_while(1000)')
# 1    0.000    0.000    0.000    0.000 les_4_task_1_1.py:15(n_sum_while)
# cProfile.run('n_sum_while(10000)')
# 1    0.001    0.001    0.001    0.001 les_4_task_1_1.py:15(n_sum_while)
# cProfile.run('n_sum_while(100000)')
# 1    0.010    0.010    0.010    0.010 les_4_task_1_1.py:15(n_sum_while)
# cProfile.run('n_sum_while(1000000)')
# 1    0.101    0.101    0.101    0.101 les_4_task_1_1.py:15(n_sum_while)

#####
### n_sum_rec - через рекурсию
## timeit
# "les_4_task_1_1.n_sum_rec(10)"
# 1000 loops, best of 5: 1.4 usec per loop
# "les_4_task_1_1.n_sum_rec(100)"
# 1000 loops, best of 5: 14.7 usec per loop
# "les_4_task_1_1.n_sum_rec(500)"
# 1000 loops, best of 5: 86.1 usec per loop
# "les_4_task_1_1.n_sum_rec(991)"
# 1000 loops, best of 5: 229 usec per loop


## cProfile
# cProfile.run('n_sum_rec(10)')
# 10/1    0.000    0.000    0.000    0.000 les_4_task_1_1.py:27(n_sum_rec)
# cProfile.run('n_sum_rec(100)')
# 100/1    0.000    0.000    0.000    0.000 les_4_task_1_1.py:27(n_sum_rec)
# cProfile.run('n_sum_rec(500)')
# 500/1    0.000    0.000    0.000    0.000 les_4_task_1_1.py:27(n_sum_rec)
# cProfile.run('n_sum_rec(991)')
# 991/1    0.001    0.000    0.001    0.001 les_4_task_1_1.py:39(n_sum_rec)

#####
### n_sum_gp - через формулу суммы геометрической прогрессии
## timeit
# "les_4_task_1_1.n_sum_gp(10)"
# 1000 loops, best of 5: 306 nsec per loop
# "les_4_task_1_1.n_sum_gp(100)"
# 1000 loops, best of 5: 310 nsec per loop
# "les_4_task_1_1.n_sum_gp(1000)"
# 1000 loops, best of 5: 312 nsec per loop
# "les_4_task_1_1.n_sum_gp(10000)"
# 1000 loops, best of 5: 321 nsec per loop

## cProfile
# cProfile.run('n_sum_gp(100)')
# 1    0.000    0.000    0.000    0.000 les_4_task_1_1.py:35(n_sum_gp)
# cProfile.run('n_sum_gp(10000)')
# 1    0.000    0.000    0.000    0.000 les_4_task_1_1.py:35(n_sum_gp)
# cProfile.run('n_sum_gp(1000000)')
# 1    0.000    0.000    0.000    0.000 les_4_task_1_1.py:35(n_sum_gp)
