import heapq

N, M = map(int, input().split())
graph = [[21e8] * (N + 1) for _ in range(N + 1)]
result = [[0] * (N + 1) for _ in range(N + 1)]

for m in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)
    graph[b][a] = min(graph[b][a], c)
    result[a][b] = b
    result[b][a] = a

for n in range(1, N + 1):
    graph[n][n] = 0
    result[n][n] = '-'

for start in range(1, N + 1):
    q = []

    for i in range(1, N + 1):
        if graph[start][i] < 21e8:
            heapq.heappush(q, (graph[start][i], i, i))

    while q:
        cost, first, now = heapq.heappop(q)

        for j in range(1, N + 1):
            if start != j and graph[start][j] > cost + graph[now][j]:
                graph[start][j] = cost + graph[now][j]
                result[start][j] = first
                heapq.heappush(q, (graph[start][j], first, j))

for i in range(1, N + 1):
    for j in range(1, N + 1):
        print(result[i][j], end=' ')
    print()