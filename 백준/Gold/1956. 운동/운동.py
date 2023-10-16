# 힌트: 플로이드 워셜

V, E = map(int, input().split())
lst = [[21e8] * (V + 1) for _ in range(V + 1)]

for e in range(E):
    a, b, c = map(int, input().split())
    lst[a][b] = c

for k in range(1, V + 1):
    for i in range(1, V + 1):
        for j in range(1, V + 1):
            lst[i][j] = min(lst[i][j], lst[i][k] + lst[k][j])

result = 21e8

for v in range(1, V + 1):
    result = min(result, lst[v][v])

if result == 21e8:
    print(-1)
else:
    print(result)