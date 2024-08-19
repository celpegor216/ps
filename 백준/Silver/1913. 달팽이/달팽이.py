N = int(input())
T = int(input())

lst = [[0] * N for _ in range(N)]
cnt = 1
y = x = N // 2
dist = 1
direction = -1

ty = tx = -1

while 1:
    for i in range(dist):
        if cnt == T:
            ty = y
            tx = x

        lst[y][x] = cnt
        y += direction
        cnt += 1

    if y == -1:
        break

    direction *= -1

    for i in range(dist):
        if cnt == T:
            ty = y
            tx = x

        lst[y][x] = cnt
        x += direction
        cnt += 1

    dist += 1

for line in lst:
    print(*line)

print(ty + 1, tx + 1)