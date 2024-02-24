N, M = map(int, input().split())
graph = [[21e8] * (N + 1) for _ in range(N + 1)]

for n in range(N + 1):
    graph[n][n] = 0

for m in range(M):
    u, v, b = map(int, input().split())

    if b == 0:
        graph[u][v] = 0
        graph[v][u] = 1
    else:
        graph[u][v] = 0
        graph[v][u] = 0

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])            

K = int(input())
for k in range(K):
    s, e = map(int, input().split())
    print(graph[s][e])