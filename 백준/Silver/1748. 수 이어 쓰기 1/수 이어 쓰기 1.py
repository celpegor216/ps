# N = 1 ~ 9 -> 1 * N
# N = 10 ~ 99 -> 1 * 9 + 2 * (N - 9)
# N = 100 ~ 999 -> 1 * 9 * 1 + 2 * 9 * 10 + 3 * (N - 10 ** 2 + 1)

N = input()
sq = len(N)
N = int(N)

total = 0

for i in range(sq - 1):
    total += (i + 1) * 9 * (10 ** i)

total += sq * (N - (10 ** (sq - 1)) + 1)

print(total)