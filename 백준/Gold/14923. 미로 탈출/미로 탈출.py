# 해답: https://handhand.tistory.com/156
# 3차원 배열 사용

from collections import deque

N, M = map(int, input().split())
hx, hy = map(int, input().split())
ex, ey = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

hx -= 1
hy -= 1
ex -= 1
ey -= 1

result = 21e8
def bfs():
    global result

    q = deque()
    q.append((hx, hy, 1, 0))

    used = [[[0, 0] for _ in range(M)] for _ in range(N)]
    used[hx][hy] = [1, 1]

    while q:
        nowx, nowy, nowm, nowc = q.popleft()

        if nowx == ex and nowy == ey:
            return nowc

        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nx, ny = nowx + dx, nowy + dy
            if 0 <= nx < N and 0 <= ny < M:
                if not used[nx][ny][nowm]:
                    if nowm and lst[nx][ny]:
                        used[nx][ny][0] = 1
                        q.append((nx, ny, 0, nowc + 1))
                    elif not lst[nx][ny]:
                        used[nx][ny][nowm] = 1
                        q.append((nx, ny, nowm, nowc + 1))

    return 21e8

result = bfs()
print(result if result != 21e8 else -1)