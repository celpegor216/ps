N = int(input())
edges = [list(map(int, input().split())) + [n] for n in range(N)]
edges.sort()

MAX = N + 1
lst = [[MAX] * N for _ in range(N)]
for n in range(N):
    lst[n][n] = 0

for i in range(N - 1):
    for j in range(i + 1, N):
        if edges[j][0] <= edges[i][1]:
            lst[edges[i][2]][edges[j][2]] = 1
            lst[edges[j][2]][edges[i][2]] = 1
        else:
            break

for k in range(N):
    for i in range(N):
        for j in range(N):
            lst[i][j] = min(lst[i][j], lst[i][k] + lst[k][j])

Q = int(input())
for _ in range(Q):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    print(lst[a][b] if lst[a][b] < MAX else -1)