N, M = map(int, input().split())
lst = [input() for _ in range(N)]

lands = []

for n in range(N):
    for m in range(M):
        if lst[n][m] == 'X':
            lands.append((n, m))

length = len(lands)
used = [0] * length

for i in range(length):
    check = 0

    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        ny, nx = lands[i][0] + dy, lands[i][1] + dx
        if 0 <= ny < N and 0 <= nx < M and (ny, nx) in lands:
            check += 1
    
    if check > 1:
        used[i] = 1

lands = [lands[x] for x in range(length) if used[x]]

lands.sort()
y1, y2 = lands[0][0], lands[-1][0]

lands.sort(key=lambda x: x[1])
x1, x2 = lands[0][1], lands[-1][1]

result = [['.'] * (x2 - x1 + 1) for _ in range(y2 - y1 + 1)]

for land in lands:
    result[land[0] - y1][land[1] - x1] = 'X'

for line in result:
    print(''.join(line))