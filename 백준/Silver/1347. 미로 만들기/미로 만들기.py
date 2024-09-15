_ = int(input())
cmds = input()

y = x = d = 0

# 남쪽을 보고 시작함, 시계 방향
directions = ((1, 0), (0, -1), (-1, 0), (0, 1))

used = set()
used.add((y, x))
min_y = max_y = min_x = max_x = 0

for cmd in cmds:
    if cmd == 'F':
        dy, dx = directions[d]
        y += dy
        x += dx
        min_y = min(min_y, y)
        max_y = max(max_y, y)
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        used.add((y, x))
    elif cmd == 'L':
        d = (d - 1) % 4
    elif cmd == 'R':
        d = (d + 1) % 4

N = max_y - min_y + 1
M = max_x - min_x + 1

result = [['#'] * (M) for _ in range(N)]

for y, x in used:
    result[y - min_y][x - min_x] = '.'

print(*[''.join(line) for line in result], sep='\n')