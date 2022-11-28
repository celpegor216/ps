from collections import deque

M, N = map(int, input().split())

lst = [list(map(int, input().split())) for _ in range(N)]
used = [[0] * M for _ in range(N)]

def bfs():
    q = deque()
    max_c = 0

    for i in range(N):
        for j in range(M):
            if lst[i][j] == 1:
                q.append((i, j, 0))

    while q:
        nowy, nowx, nowc = q.popleft()

        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ny, nx = nowy + dy, nowx + dx
            if 0 <= ny < N and 0 <= nx < M and not used[ny][nx] and lst[ny][nx] == 0:
                used[ny][nx] = 1
                q.append((ny, nx, nowc + 1))
                max_c = nowc + 1

    result = max_c

    for i in range(N):
        if result == -1:
            break

        for j in range(M):
            # 안 익은 토마토인데 익지 않은 경우
            if lst[i][j] == 0 and used[i][j] == 0:
                result = -1
                break

    return result

print(bfs())