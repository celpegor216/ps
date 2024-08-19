import sys
input = sys.stdin.readline

MAX = 10 ** 6
primes = [0] * (MAX + 1)

for i in range(3, MAX + 1, 2):
    if primes[i]:
        continue

    j = i * 2
    while j <= MAX:
        primes[j] = 1
        j += i

primes = [x for x in range(3, MAX + 1, 2) if not primes[x]]
length = len(primes)

# N보다 작으면서 가장 큰 소수의 인덱스 찾기
def find_right():
    start = 0
    end = length - 1
    res = -1

    while start <= end:
        middle = (start + end) // 2

        if primes[middle] > N:
            end = middle - 1
        else:
            res = max(res, middle)
            start = middle + 1

    return res

while 1:
    N = int(input())

    if not N:
        break

    left = 0
    right = find_right()
    result = []

    while left <= right:
        if primes[left] + primes[right] == N:
            result = [primes[left], primes[right]]
            break
        elif primes[left] + primes[right] > N:
            right -= 1
        else:
            left += 1

    if not result:
        print("Goldbach's conjecture is wrong.")
    else:
        print(f'{N} = {result[0]} + {result[1]}')