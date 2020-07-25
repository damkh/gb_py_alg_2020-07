import cProfile
import functools


def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')

@functools.lru_cache()
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def fib_dict(n):
    fib_d = {0: 0, 1: 1}

    def _fib_dict(n):
        if n in fib_d:
            return fib_d[n]

        fib_d[n] = _fib_dict(n - 1) + _fib_dict(n - 2)
        return fib_d[n]

    return _fib_dict(n)


def fib_list(n):
    fib_l = [None] * 1000
    fib_l[:2] = [0, 1]

    def _fib_list(n):
        if fib_l[n] is None:
            fib_l[n] = _fib_list(n - 1) + _fib_list(n - 2)
        return fib_l[n]

    return _fib_list(n)


def fib_loop(n):
    if n < 2:
        return n
    first, second = 0, 1
    for i in range(2, n + 1):
        first, second = second, first + second

    return second


# -----------------------
#test_fib(fib)

# "fibb.fib(10)"
# 1000 loops, best of 5: 17.5 usec per loop
# "fibb.fib(15)"
# 1000 loops, best of 5: 194 usec per loop
# "fibb.fib(20)"
# 1000 loops, best of 5: 2.23 msec per loop
# "fibb.fib(25)"
# 1000 loops, best of 5: 24.3 msec per loop

# cProfile.run('fib(10)')
# 180 function calls (4 primitive calls) in 0.000 seconds
# cProfile.run('fib(15)')
# 1976 function calls (4 primitive calls) in 0.000 seconds
# cProfile.run('fib(20)')
# 21894 function calls (4 primitive calls) in 0.005 seconds
# cProfile.run('fib(25)')
# 242788 function calls (4 primitive calls) in 0.057 seconds

# ----------------------------------
# functools.lru_cache
# "fibb.fib(10)"
# 1000 loops, best of 5: 81.6 nsec per loop
# python -m timeit -n 1000 -s "import fibb" "fibb.fib(100)"
# 1000 loops, best of 5: 84.3 nsec per loop
# "fibb.fib(200)"
# 1000 loops, best of 5: 84.1 nsec per loop

# cProfile.run('fib(10)')
# 11/1    0.000    0.000    0.000    0.000 fib.py:11(fib)
# cProfile.run('fib(20)')
# 21/1    0.000    0.000    0.000    0.000 fib.py:11(fib)
# cProfile.run('fib(100)')
# 101/1    0.000    0.000    0.000    0.000 fib.py:11(fib)
# cProfile.run('fib(200)')


# ---------------------------
#test_fib(fib_dict)
# "fibb.fib_dict(10)"
# 1000 loops, best of 5: 3.43 usec per loop
# "fibb.fib_dict(15)"
# 1000 loops, best of 5: 5.11 usec per loop
# "fibb.fib_dict(20)"
# 1000 loops, best of 5: 6.63 usec per loop
# "fibb.fib_dict(25)"
# 1000 loops, best of 5: 8.52 usec per loop
# "fibb.fib_dict(100)"
# 1000 loops, best of 5: 37.7 usec per loop
# "fibb.fib_dict(200)"
# 1000 loops, best of 5: 75.3 usec per loop
# "fibb.fib_dict(500)"
# 1000 loops, best of 5: 214 usec per loop

# cProfile.run('fib_dict(10)')
# 23 function calls (5 primitive calls) in 0.000 seconds
# cProfile.run('fib_dict(20)')
# 43 function calls (5 primitive calls) in 0.000 seconds
# cProfile.run('fib_dict(100)')
# 203 function calls (5 primitive calls) in 0.000 seconds
# cProfile.run('fib_dict(500)')
# 1003 function calls (5 primitive calls) in 0.001 seconds

# ---------------------------
# test_fib(fib_list)
# "fibb.fib_list(10)"
# 1000 loops, best of 5: 5.96 usec per loop
# "fibb.fib_list(20)"
# 1000 loops, best of 5: 9.45 usec per loop
# "fibb.fib_list(100)"
# 1000 loops, best of 5: 35.8 usec per loop
# "fibb.fib_list(200)"
# 1000 loops, best of 5: 69.1 usec per loop
# "fibb.fib_list(500)"

# cProfile.run('fib_list(10)')
# 23 function calls (5 primitive calls) in 0.000 seconds
# cProfile.run('fib_list(20)')
# 43 function calls (5 primitive calls) in 0.000 seconds
# cProfile.run('fib_list(100)')
# 203 function calls (5 primitive calls) in 0.000 seconds
# cProfile.run('fib_list(200)')
# 403 function calls (5 primitive calls) in 0.000 seconds
# cProfile.run('fib_list(500)')
# 1003 function calls (5 primitive calls) in 0.001 seconds

# ---------------------------
# test_fib(fib_loop)
# "fibb.fib_loop(10)"
# 1000 loops, best of 5: 588 nsec per loop
# "fibb.fib_loop(100)"
# 1000 loops, best of 5: 4.26 usec per loop
# "fibb.fib_loop(500)"
# 1000 loops, best of 5: 26.3 usec per loop
# "import fibb" "fibb.fib_loop(1000)"
# 1000 loops, best of 5: 61.3 usec per loop

# cProfile.run('fib_loop(10)')
# 1    0.000    0.000    0.000    0.000 fib.py:42(fib_loop)
# cProfile.run('fib_loop(100)')
# 1    0.000    0.000    0.000    0.000 fib.py:42(fib_loop)
# cProfile.run('fib_loop(500)')
# 1    0.000    0.000    0.000    0.000 fib.py:42(fib_loop)
# cProfile.run('fib_loop(1000)')