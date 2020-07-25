"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.

Вывод:
Для нахождения i-го по счёту простого числа реализовано 2 алгоритма:
1) "Решето Эратосфена"
2) "Наивный" или перебором
Алгоритм 1) работает медленнее примерно до n=1000 (до 1000го простого числа), сложность - O(nlog(log(n))).
Наивный алгоритм имеет сложнось O(n^2), поэтому на больших числа он начинает сильно замедляться.
Все реузльтаты по timeit и cProfile даны в конце файла.
"""
import cProfile


def sieve_erat(m):
    k = 0
    sieve = [i for i in range(n)]
    for i in range(2, n):
        if sieve[i] != 0:
            k += 1
            if k == m:
                return i
            j = i * 2
            while j < n:
                sieve[j] = 0
                j += i


def is_prime(p):
    i = 2
    while p % i != 0:
        i += 1
    return i == p


def find_prime(m):
    k = 0
    for p in range(2, n):
        if is_prime(p):
            k += 1
            if k == m:
                return p


n = 1000000

# print(sum(nat_nums))
# print(sieve_erat(10000))
# print(find_prime(10000))
# print(sum(nat_nums))

##### sieve_erat
## timeit
# "les_4_task_2.sieve_erat(2)"
# 10 loops, best of 5: 42.3 msec per loop
# "les_4_task_2.sieve_erat(10)"
# 10 loops, best of 5: 132 msec per loop
# "les_4_task_2.sieve_erat(100)"
# 10 loops, best of 5: 203 msec per loop
# "les_4_task_2.sieve_erat(1000)"
# 10 loops, best of 5: 257 msec per loop"
# "les_4_task_2.sieve_erat(5000)"
# 10 loops, best of 5: 371 msec per loop
# les_4_task_2.sieve_erat(10000)"
# 10 loops, best of 5: 376 msec per loop

## cProfile
# cProfile.run('sieve_erat(2)')
# 1    0.047    0.047    0.047    0.047 les_4_task_2.py:14(sieve_erat)
# cProfile.run('sieve_erat(10)')
# 1    0.173    0.173    0.173    0.173 les_4_task_2.py:14(sieve_erat)
# cProfile.run('sieve_erat(100)')
# 1    0.271    0.271    0.271    0.271 les_4_task_2.py:14(sieve_erat)
# cProfile.run('sieve_erat(1000)')
# 1    0.331    0.331    0.331    0.331 les_4_task_2.py:14(sieve_erat)
# cProfile.run('sieve_erat(10000)')
# 1    0.367    0.367    0.367    0.367 les_4_task_2.py:14(sieve_erat)


##### find_prime
## timeit
# "les_4_task_2.find_prime(2)"
# 5 loops, best of 5: 789 nsec per loop
# "les_4_task_2.find_prime(10)"
# 10 loops, best of 5: 9.73 usec per loop
# "les_4_task_2.find_prime(100)"
# 10 loops, best of 5: 1.28 msec per loop
# "les_4_task_2.find_prime(1000)"
# 10 loops, best of 5: 241 msec per loop
# "les_4_task_2.find_prime(5000)"
# 5 loops, best of 5: 7.89 sec per loop


## cProfile
# cProfile.run('find_prime(10)')
# 28    0.000    0.000    0.000    0.000 les_4_task_2.py:35(is_prime)
# cProfile.run('find_prime(100)')
# 540    0.001    0.000    0.001    0.000 les_4_task_2.py:35(is_prime)
# cProfile.run('find_prime(1000)')
# 7918    0.244    0.000    0.244    0.000 les_4_task_2.py:35(is_prime)
# cProfile.run('find_prime(5000)')
# 48610    7.807    0.000    7.807    0.000 les_4_task_2.py:35(is_prime)
# cProfile.run('find_prime(10000)')
# 104728   34.432    0.000   34.432    0.000 les_4_task_2.py:35(is_prime)







