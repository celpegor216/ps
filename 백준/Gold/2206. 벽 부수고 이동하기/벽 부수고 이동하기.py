from collections import deque

N, M = map(int, input().split())
lst = [input() for _ in range(N)]

result = 21e8

def bfs():
    global result

    q = deque()
    q.append((0, 0, 1, 0))

    used = [[[[21e8, 0], [21e8, 1]] for _ in range(M)] for _ in range(N)]
    used[0][0] = [[0, 0], [0, 1]]

    while q:
        nowy, nowx, nowc, noww = q.popleft()

        if nowy == N - 1 and nowx == M - 1:
            result = min(result, nowc)
            continue

        if nowc >= result:
            continue

        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ny, nx = nowy + dy, nowx + dx
            if 0 <= ny < N and 0 <= nx < M:
                if lst[ny][nx] == '1':
                    if noww == 0 and used[ny][nx][1][0] > nowc + 1:
                        q.append((ny, nx, nowc + 1, 1))
                        used[ny][nx][1][0] = nowc + 1
                else:
                    if noww == 0 and used[ny][nx][0][0] > nowc + 1:
                        q.append((ny, nx, nowc + 1, noww))
                        used[ny][nx][0][0] = nowc + 1
                    elif noww == 1 and used[ny][nx][1][0] > nowc + 1:
                        q.append((ny, nx, nowc + 1, 1))
                        used[ny][nx][1][0] = nowc + 1

bfs()

if result == 21e8:
    result = -1

print(result)
