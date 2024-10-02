N = 6
K = int(input())
lst = [[0] * N for _ in range(N)]

lst[2][2] = lst[3][3] = -1
lst[2][3] = lst[3][2] = 1

side = 1
for k in range(K):
    y, x = map(lambda x: int(x) - 1, input().split())
    lst[y][x] = side

    for dy, dx in ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)):
        ny, nx = y + dy, x + dx
        cnt = 1
        while 0 <= ny < N and 0 <= nx < N and lst[ny][nx] == -side:
            ny += dy
            nx += dx
            cnt += 1

        if 0 <= ny < N and 0 <= nx < N and lst[ny][nx] == side:
            cnt -= 1
            for _ in range(cnt):
                ny -= dy
                nx -= dx
                lst[ny][nx] = side

    side = -side


W = B = 0
for i in range(N):
    for j in range(N):
        if lst[i][j] == 1:
            B += 1
            lst[i][j] = 'B'
        elif lst[i][j] == -1:
            W += 1
            lst[i][j] = 'W'
        else:
            lst[i][j] = '.'

for line in lst:
    print(''.join(line))
print('White' if W > B else 'Black')
