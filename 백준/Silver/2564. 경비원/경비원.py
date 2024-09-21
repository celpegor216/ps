M, N = map(int, input().split())
T = int(input())

result = 0

def find_pos(direction, distance):
    # 북쪽에 있음
    if direction == 1:
        return (0, distance)
    # 남쪽에 있음
    elif direction == 2:
        return (N, distance)
    # 서쪽에 있음
    elif direction == 3:
        return (distance, 0)
    # 동쪽에 있음
    else:
        return (distance, M)
    
lst = []
for _ in range(T):
    lst.append(find_pos(*map(int, input().split())))

direction, distance = map(int, input().split())
sy, sx = find_pos(direction, distance)

distances = dict()

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
d = 0 if direction < 2 else 1
dy, dx = directions[d]
y, x = sy, sx
cnt = 0

while 1:
    distances[(y, x)] = cnt
    cnt += 1

    ny, nx = y + dy, x + dx
    if not (0 <= ny <= N and 0 <= nx <= M):
        if d == 0:
            d = 1 if y == 0 else 3
        elif d == 1:
            d = 2 if x == M else 0
        elif d == 2:
            d = 3 if y == N else 1
        else:
            d = 0 if x == 0 else 2
        dy, dx = directions[d]
        ny, nx = y + dy, x + dx

    y, x = ny, nx

    if y == sy and x == sx:
        break

result = 0

for y, x in lst:
    distance = distances[(y, x)]
    result += min(distance, (N + M) * 2 - distance)

print(result)