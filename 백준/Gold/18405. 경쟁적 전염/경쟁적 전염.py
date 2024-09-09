from collections import deque


# 맵 크기 N, 바이러스 종류 K
N, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
S, Y, X = map(int, input().split())
Y -= 1
X -= 1

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

virus = []
for i in range(N):
    for j in range(N):
        if lst[i][j]:
            virus.append((lst[i][j], i, j))

q = deque(sorted(virus))

for _ in range(S):
    flag = 0

    for _ in range(len(q)):
        k, y, x = q.popleft()

        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and not lst[ny][nx]:
                lst[ny][nx] = k
                q.append((k, ny, nx))
                flag = 1

    if lst[Y][X] or not flag:
        break

print(lst[Y][X])