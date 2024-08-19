N = 8
lst = [input() for _ in range(N)]

ranges = [range(0, N, 2), range(1, N, 2)]

cnt = 0
for i in range(N):
    for j in ranges[i % 2]:
        if lst[i][j] == 'F':
            cnt += 1

print(cnt)