import sys
input = sys.stdin.readline


MAX = 5 * (10 ** 6)
primes = [1] * (MAX + 1)
primes[0] = primes[1] = 0

for i in range(2, int(MAX ** 0.5) + 1):
    if not primes[i]:
        continue

    j = i * 2

    while j <= MAX:
        primes[j] = 0
        j += i


N = int(input())

A = []
B = []

score_A = score_B = 0

for _ in range(N):
    a, b = map(int, input().split())

    if primes[a] == 0:
        B.sort()
        if len(B) < 3:
            score_B += 1000
        else:
            score_B += B[-3]
    elif primes[a] != 1:
        score_A -= 1000
    else:
        A.append(a)
        primes[a] = 2

    if primes[b] == 0:
        A.sort()
        if len(A) < 3:
            score_A += 1000
        else:
            score_A += A[-3]
    elif primes[b] != 1:
        score_B -= 1000
    else:
        B.append(b)
        primes[b] = 2


if score_A > score_B:
    print('소수의 신 갓대웅')
elif score_A < score_B:
    print('소수 마스터 갓규성')
else:
    print('우열을 가릴 수 없음')