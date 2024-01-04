N = int(input())
lst = [[21e8] * (N + 1) for _ in range(N + 1)]

for n in range(N + 1):
    lst[n][n] = 0

while 1:
    a, b = map(int, input().split())

    if a == b == -1:
        break

    lst[a][b] = 1
    lst[b][a] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            lst[i][j] = min(lst[i][j], lst[i][k] + lst[k][j])

minv = 21e8
result = []

for n in range(1, N + 1):
    maxv = max(lst[n][1:])

    if maxv < minv:
        minv = maxv
        result = [n]
    elif maxv == minv:
        result.append(n)

print(minv, len(result))
print(*sorted(result))