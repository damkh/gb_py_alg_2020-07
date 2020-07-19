n = 40
sieve = [i for i in range(n)]
sieve[1] = 0
print(sieve)

for i in range(2, n):
    print(i)
    if sieve[i] != 0:
        j = i * 2
        while j < n:
            sieve[j] = 0
            j += i

result = [i for i in sieve if i != 0]
print(result)
