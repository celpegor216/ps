N, M = map(int, input().split())
lst = list(map(int, input().split()))

temp = [0] * (9001)

for i in range(2, 4501):
    j = i * 2
    while j <= 9000:
        temp[j] = 1
        j += i

primes = [x for x in range(2, 9001) if not temp[x]]

result = set()
def dfs(level, next, total):
    if level == M:
        if total in primes:
            result.add(total)
        return

    for i in range(next, N):
        dfs(level + 1, i + 1, total + lst[i])

dfs(0, 0, 0)

if not result:
    print(-1)
else:
    print(*sorted(result))