import heapq


N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
K = int(input())

q = []
used = [[0] * M for _ in range(N)]

for i in range(N):
    used[i][0] = 1
    heapq.heappush(q, (-lst[i][0], i, 0))
    used[i][-1] = 1
    heapq.heappush(q, (-lst[i][-1], i, M - 1))

for j in range(M):
    used[0][j] = 1
    heapq.heappush(q, (-lst[0][j], 0, j))
    used[-1][j] = 1
    heapq.heappush(q, (-lst[-1][j], N - 1, j))

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

result = 0
for _ in range(K):
    while 1:
        value, i, j = heapq.heappop(q)

        if used[i][j] != 2:
            print(i + 1, j + 1)
            used[i][j] = 2

            for dy, dx in directions:
                ny, nx = i + dy, j + dx
                if 0 <= ny < N and 0 <= nx < M and not used[ny][nx]:
                    used[ny][nx] = 1
                    heapq.heappush(q, (-lst[ny][nx], ny, nx))
            
            break