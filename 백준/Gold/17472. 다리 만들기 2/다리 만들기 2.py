from collections import deque
import heapq

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

board = [[0] * M for _ in range(N)]

cnt = 0

for i in range(N):
    for j in range(M):
        if lst[i][j] and not board[i][j]:
            cnt += 1
            board[i][j] = cnt

            q = deque()
            q.append((i, j))

            while q:
                y, x = q.popleft()

                for dy, dx in directions:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < N and 0 <= nx < M and not board[ny][nx] and lst[ny][nx]:
                        board[ny][nx] = cnt
                        q.append((ny, nx))

graph = [[21e8] * (cnt + 1) for _ in range(cnt + 1)]

for i in range(N):
    for j in range(M):
        if board[i][j]:
            for dy, dx in directions:
                ny, nx = i + dy, j + dx
                dist = 1
                while 0 <= ny < N and 0 <= nx < M:
                    if board[ny][nx]:
                        if board[i][j] != board[ny][nx] and dist > 2:
                            graph[board[i][j]][board[ny][nx]] = min(graph[board[i][j]][board[ny][nx]], dist - 1)
                            graph[board[ny][nx]][board[i][j]] = min(graph[board[ny][nx]][board[i][j]], dist - 1)
                        break
                    ny += dy
                    nx += dx
                    dist += 1

group = [x for x in range(cnt + 1)]
result = 0

def find(a):
    if group[a] != a:
        group[a] = find(group[a])
    return group[a]

def union(a, b, c):
    global result

    group_a, group_b = find(a), find(b)

    if group_a != group_b:
        group[group_b] = group_a
        result += c

q = []

for i in range(1, cnt + 1):
    for j in range(i + 1, cnt + 1):
        if graph[i][j] != 21e8:
            heapq.heappush(q, (graph[i][j], i, j))

while q:
    c, a, b = heapq.heappop(q)

    union(a, b, c)

flag = 0

standard = find(1)
for i in range(2, cnt + 1):
    if standard != find(i):
        flag = 1
        break

if flag:
    print(-1)
else:
    print(result)