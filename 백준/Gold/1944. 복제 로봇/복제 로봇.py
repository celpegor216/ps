from collections import deque

N, M = map(int, input().split())
lst = [input() for _ in range(N)]

keys = dict()
cnt = 1

for i in range(N):
    for j in range(N):
        if lst[i][j] == 'S':
            keys[(i, j)] = 0
        if lst[i][j] == 'K':
            keys[(i, j)] = cnt
            cnt += 1

dist = [[21e8] * (M + 1) for _ in range(M + 1)]

for key, idx in keys.items():
    i, j = key

    q = deque()
    q.append((i, j, 0))

    used = [[0] * N for _ in range(N)]
    used[i][j] = 1

    while q:
        nowy, nowx, nowc = q.popleft()

        if not (i == nowy and j == nowx) and lst[nowy][nowx] == 'K':
            target = keys[(nowy, nowx)]
            dist[idx][target] = nowc
            dist[target][idx] = nowc
        
        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ny, nx = nowy + dy, nowx + dx
            if 0 <= ny < N and 0 <= nx < N and not used[ny][nx] and lst[ny][nx] != '1':
                used[ny][nx] = 1
                q.append((ny, nx, nowc + 1))
    
group = [x for x in range(M + 1)]
edges = []

for i in range(M):
    for j in range(i + 1, M + 1):
        if dist[i][j] != 21e8:
            edges.append((i, j, dist[i][j]))

edges.sort(key=lambda x: x[2])

def find(a):
    if group[a] != a:
        group[a] = find(group[a])
    return group[a]

def union(a, b):
    group_a, group_b = find(a), find(b)

    if group_a != group_b:
        group[group_b] = group_a
        return True
    return False

result = 0

for a, b, c in edges:
    if union(a, b):
        result += c

flag = 0
standard = find(0)

for m in range(1, M + 1):
    if find(m) != standard:
        flag = 1
        break

if flag:
    print(-1)
else:
    print(result)