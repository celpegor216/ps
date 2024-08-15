MAXV = 10 ** 6
primes = [0] * (MAXV + 1)

for i in range(2, MAXV // 2 + 1):
    if primes[i]:
        continue

    j = i * 2
    while j <= MAXV:
        primes[j] = 1
        j += i

primes = [n for n in range(2, MAXV + 1) if not primes[n]]

T = int(input())
for _ in range(T):
    N = int(input())
    
    start = 0
    end = len(primes) - 1

    result = 0
    while start <= end:
        if primes[start] + primes[end] > N:
            end -= 1
        elif primes[start] + primes[end] < N:
            start += 1
        else:
            result += 1
            start += 1
            end -= 1
    
    print(result)