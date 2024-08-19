def pos(now):
    return ord(now[0]) - ord('A'), N - int(now[1])

N = 6
directions = ((1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2))

used = [[0] * N for _ in range(N)]

sy, sx = pos(input())    # 시작점
y, x = sy, sx
used[y][x] = 1

result = 'Valid'
for n in range(N ** 2 - 1):
    ny, nx = pos(input())

    if (y - ny, x - nx) in directions and not used[ny][nx]:
        used[ny][nx] = 1
        y, x = ny, nx
    else:
        result = 'Invalid'
        break

if n == N ** 2 - 2 and (y - sy, x - sx) in directions:
    print(result)
else:
    print('Invalid')