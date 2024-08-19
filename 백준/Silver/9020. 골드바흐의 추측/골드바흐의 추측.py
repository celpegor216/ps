T = int(input())

MAX = 10 ** 4
primes = [0] * (MAX + 1)

for i in range(2, MAX + 1):
    if primes[i]:
        continue

    j = i * 2
    while j <= MAX:
        primes[j] = 1
        j += i

primes = [x for x in range(2, MAX + 1) if not primes[x]]
length = len(primes)

for _ in range(T):
    N = int(input())

    start = 0
    end = length - 1
    result = [0, MAX]

    while start <= end:
        if primes[start] + primes[end] == N:
            if primes[end] - primes[start] < result[-1] - result[0]:
                result = [primes[start], primes[end]]
            start += 1
            end -= 1
        elif primes[start] + primes[end] > N:
            end -= 1
        else:
            start += 1

    print(*result)