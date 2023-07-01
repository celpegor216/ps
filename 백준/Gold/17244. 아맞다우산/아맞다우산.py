from collections import deque

M, N = map(int, input().split())
lst = [input() for _ in range(N)]

items = []
for n in range(N):
    for m in range(M):
        if lst[n][m] == 'S':
            start = (n, m)
        elif lst[n][m] == 'E':
            end = (n, m)
        elif lst[n][m] == 'X':
            items.append((n, m))

items = [start] + items + [end]

length = len(items)
board = []

# 각 노드에서 각 노드까지의 최단 거리 구하기
for i in range(length):
    temp = [21e8] * length

    q = deque()
    q.append((items[i][0], items[i][1], 0))
    used = [[0] * M for _ in range(N)]
    used[items[i][0]][items[i][1]] = 1

    while q:
        y, x, cost = q.popleft()

        if (y, x) in items:
            temp[items.index((y, x))] = cost
        
        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and not used[ny][nx] and lst[ny][nx] != '#':
                used[ny][nx] = 1
                q.append((ny, nx, cost + 1))

    board.append(temp[:])

result = 21e8
# 아이템 챙기는 순서 정하기
used = [0] * (length - 2)
def dfs(level, path):
    global result

    if level == length - 2:
        total = board[0][path[0]]
        path.append(-1)

        for i in range(length - 2):
            total += board[path[i]][path[i + 1]]
        
        result = min(result, total)
        return
    
    for i in range(length - 2):
        if not used[i]:
            used[i] = 1
            dfs(level + 1, path + [i + 1])
            used[i] = 0

if length > 2:
    dfs(0, [])
else:
    result = board[0][1]
print(result)