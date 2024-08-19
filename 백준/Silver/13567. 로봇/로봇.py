N, M = map(int, input().split())
directions = ((0, 1), (-1, 0), (0, -1), (1, 0))

cmds = [input().split() for _ in range(M)]

y = x = d = 0
result = (-1, )
for cmd, num in cmds:
    num = int(num)

    if cmd == 'MOVE':
        ny, nx = y + directions[d][0] * num, x + directions[d][1] * num
        if 0 <= ny <= N and 0 <= nx <= N:
            y, x = ny, nx
        else:
            break
    else:
        if num == 0:    # 왼쪽으로 회전
            d -= 1
            if d < 0:
                d = 3
        else:    # 오른쪽으로 회전
            d += 1
            if d > 3:
                d = 0
else:
    result = (x, y)

print(*result)