# 플로이드 와샬 - 방향성 그래프에서 모든 노드에서 다른 모든 노드로의 가중치
# 해답: https://pacific-ocean.tistory.com/279

N = int(input())
M = int(input())
INF = 21e8
lst = [[INF] * N for _ in range(N)]

for m in range(M):
    a, b, c = map(int, input().split())
    if lst[a - 1][b - 1] > c:
        lst[a - 1][b - 1] = c

for k in range(N): # via
    for i in range(N): # start
        for j in range(N): # end
            if i != j and lst[i][j] > lst[i][k] + lst[k][j]:
                lst[i][j] = lst[i][k] + lst[k][j]

for n in range(N):
    for m in range(N):
        if lst[n][m] == INF:
            lst[n][m] = 0

for line in lst:
    print(*line)