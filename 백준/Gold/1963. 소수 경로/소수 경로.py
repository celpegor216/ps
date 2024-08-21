from collections import deque

N = 10000
primes = [0] * N

for i in range(2, N):
    if primes[i]:
        continue

    j = i * 2

    while j < N:
        primes[j] = 1
        j += i

primes = set([str(n) for n in range(1000, N) if not primes[n]])
length = len(primes)

TC = int(input())

for _ in range(TC):
    A, B = input().split()

    used = set()
    used.add(A)

    q = deque()
    q.append((A, 0))

    result = -1
    while q:
        now, cnt = q.popleft()

        if now == B:
            result = cnt
            break

        for i in range(4):
            for j in range(10):
                if now[i] == str(j):
                    continue
                tmp = now[:i] + str(j) + now[i + 1:]

                if tmp in primes and tmp not in used:
                    used.add(tmp)
                    q.append((tmp, cnt + 1))

    print(result if result != -1 else 'Impossible')