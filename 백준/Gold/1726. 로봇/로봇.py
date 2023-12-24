from collections import deque

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
sy, sx, sd = map(int, input().split())
ey, ex, ed = map(int, input().split())

sy, sx, sd, ey, ex, ed = sy - 1, sx - 1, sd - 1, ey - 1, ex - 1, ed - 1

direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
left = [3, 2, 0, 1]
right = [2, 3, 1, 0]

q = deque()
q.append((sy, sx, sd, 0))

used = [[[21e8] * 4 for _ in range(M)] for _ in range(N)]
used[sy][sx][sd] = 0

result = 0

while q:
    y, x, d, cnt = q.popleft()

    if y == ey and x == ex and d == ed:
        result = cnt
        break

    for k in range(1, 4):
        dy, dx = y + direction[d][0] * k, x + direction[d][1] * k

        if not (0 <= dy < N and 0 <= dx < M) or lst[dy][dx]:
            break

        if used[dy][dx][d] > cnt + 1:
            used[dy][dx][d] = cnt + 1
            q.append((dy, dx, d, cnt + 1))
    
    if used[y][x][left[d]] > cnt + 1:
        used[y][x][left[d]] = cnt + 1
        q.append((y, x, left[d], cnt + 1))

    if used[y][x][right[d]] > cnt + 1:
        used[y][x][right[d]] = cnt + 1
        q.append((y, x, right[d], cnt + 1))

print(result)