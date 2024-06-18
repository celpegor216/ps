from collections import deque

N, M = map(int, input().split())
dic = dict()

for _ in range(M):
    x, y, a, b = list(map(int, input().split()))
    x -= 1
    y -= 1
    a -= 1
    b -= 1

    if not dic.get((x, y)):
        dic[x, y] = []
    dic[x, y].append((a, b))

lights = [[0] * N for _ in range(N)]
used = [[0] * N for _ in range(N)]
checked = [[0] * N  for _ in range(N)]
q = deque()

lights[0][0] = 1
used[0][0] = 1
cnt = 1
q.append((0, 0))

while q:
    y, x = q.popleft()

    if not checked[y][x] and dic.get((y, x)):
        checked[y][x] = 1
        for i, j in dic[(y, x)]:
            if not lights[i][j]:
                lights[i][j] = 1
                cnt += 1

    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < N and lights[ny][nx] and used[ny][nx] < cnt:
            used[ny][nx] = cnt
            q.append((ny, nx))

print(cnt)