N = int(input())
primes = [2, 3, 5, 7]

def check(num):
    if num in primes:
        return

    if num == 1:
        return 1

    half = int(num ** 0.5)

    for i in range(2, half + 1):
        if not num % i:
            return 1

def dfs(level, now):
    if check(now) or (level and now < 10 ** (level - 1)):
        return

    if level == N:
        print(now)
        return

    for i in range(10):
        dfs(level + 1, now * 10 + i)

dfs(0, 0)