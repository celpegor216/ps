from collections import deque

N = int(input())
lst = [input() for _ in range(N)]
B = []

for i in range(N):
    for j in range(N):
        if lst[i][j] == 'B':
            B.append((i, j))

q = deque()
used = [[[0] * 2 for _ in range(N)] for _ in range(N)] # 세로, 가로

rotate = 0 if B[0][0] != B[1][0] else 1
q.append((*B[1], rotate, 0))
used[B[1][0]][B[1][1]][rotate] = 1

result = 0

while q:
    y, x, r, c = q.popleft()

    if (r == 0 and lst[y - 1][x] == lst[y][x] == lst[y + 1][x] == 'E') or (r == 1 and lst[y][x - 1] == lst[y][x] == lst[y][x + 1] == 'E'):
        result = c
        break

    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        ny, nx = y + dy, x + dx

        flag = 0

        if r == 0: # 지금 세로인데
            if dy != 0: # 세로로 움직인다면
                if not(0 < ny < N - 1) or used[ny][nx][r] or lst[ny + dy][nx + dx] == '1':
                    flag = 1
            else: # 가로로 움직인다면
                b, n, f = (ny - 1, nx), (ny, nx), (ny + 1, nx)

                if not(0 <= nx < N) or used[ny][nx][r]:
                    flag = 1
                else:
                    for i, j in (b, n, f):
                        if lst[i][j] == '1':
                            flag = 1
                            break
        else: # 지금 가로인데
            if dy != 0: # 세로로 움직인다면
                b, n, f = (ny, nx - 1), (ny, nx), (ny, nx + 1)

                if not(0 <= ny < N) or used[ny][nx][r]:
                    flag = 1
                else:
                    for i, j in (b, n, f):
                        if lst[i][j] == '1':
                            flag = 1
                            break
            else: # 가로로 움직인다면
                if not(0 < nx < N - 1) or used[ny][nx][r] or lst[ny + dy][nx + dx] == '1':
                    flag = 1

        if not flag:
            used[ny][nx][r] = 1
            q.append((ny, nx, r, c + 1))

    oppo_r = 0 if r else 1
    if 0 < y < N - 1 and 0 < x < N - 1 and not used[y][x][oppo_r]:
        flag = 0

        for i in (-1, 0, 1):
            if flag:
                break

            for j in (-1, 0, 1):
                if lst[y + i][x + j] == '1':
                    flag = 1
                    break

        if not flag:
            used[y][x][oppo_r] = 1
            q.append((y, x, oppo_r, c + 1))

print(result)