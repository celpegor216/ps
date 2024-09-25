# 1층부터 N층, K자리수, P개 반전, 현재 X층
N, K, P, X = map(int, input().split())

numbers = [
    [1, 1, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 1],
    [0, 1, 1, 1, 0, 1, 0],
    [1, 1, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1],
]

diffs = [[0] * 10 for _ in range(10)]

for i in range(10):
    for j in range(i + 1, 10):
        for k in range(7):
            if numbers[i][k] != numbers[j][k]:
                diffs[i][j] += 1
                diffs[j][i] += 1

now = [0] * K
n = X
for k in range(K):
    now[K - 1 - k] = n % 10
    n //= 10
    if not n:
        break

result = 0
def dfs(level, p):
    global result

    if level == K:
        total = 0
        for k in range(K):
            total = total * 10 + now[k]
        if 1 <= total <= N:
            result += 1
        return

    for i in range(10):
        diff = diffs[now[level]][i]
        if diff > p:
            continue
        tmp = now[level]
        now[level] = i
        dfs(level + 1, p - diff)
        now[level] = tmp

dfs(0, P)

print(result - 1)