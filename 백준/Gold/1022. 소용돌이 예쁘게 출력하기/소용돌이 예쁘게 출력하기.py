U, L, D, R = map(int, input().split())

N, M = D - U + 1, R - L + 1
result = [[0] * M for _ in range(N)]

blank_cnt = N * M

directions = ((0, 1), (-1, 0), (0, -1), (1, 0))

y = x = d = 0
idx = 1
cnt = 0
max_cnt = 1
update_max_cnt = 0
while blank_cnt:
    if U <= y <= D and L <= x <= R:
        result[y - U][x - L] = str(idx)
        blank_cnt -= 1

    idx += 1
    dy, dx = directions[d]
    y += dy
    x += dx
    cnt += 1

    if cnt == max_cnt:
        cnt = 0
        update_max_cnt += 1
        d = (d + 1) % 4

        if update_max_cnt == 2:
            max_cnt += 1
            update_max_cnt = 0


max_length = 0
for i in range(N):
    for j in range(M):
        max_length = max(max_length, len(result[i][j]))

for i in range(N):
    for j in range(M):
        print(' ' * (max_length - len(result[i][j])) + result[i][j], end=' ')
    print()