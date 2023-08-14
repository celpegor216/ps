N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
airs = []
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for n in range(N):
    for m in range(M):
        if lst[n][m] == 9:
            airs.append((n, m))

used = [[0] * M for _ in range(N)]

for y, x in airs:
    used[y][x] = 1
    for d in range(4):
        nowy, nowx, nowd = y, x, d
        nowy += directions[nowd][0]
        nowx += directions[nowd][1]
    
        while 0 <= nowy < N and 0 <= nowx < M:
            used[nowy][nowx] = 1
            if lst[nowy][nowx] == 0 or (lst[nowy][nowx] == 1 and nowd % 2) or (lst[nowy][nowx] == 2 and not nowd % 2):
                nowy += directions[nowd][0]
                nowx += directions[nowd][1]
            elif lst[nowy][nowx] == 3:
                if nowd == 0:
                    nowd = 3
                elif nowd == 1:
                    nowd = 2
                elif nowd == 2:
                    nowd = 1
                else:
                    nowd = 0
                nowy += directions[nowd][0]
                nowx += directions[nowd][1]
            elif lst[nowy][nowx] == 4:
                if nowd == 0:
                    nowd = 1
                elif nowd == 1:
                    nowd = 0
                elif nowd == 2:
                    nowd = 3
                else:
                    nowd = 2
                nowy += directions[nowd][0]
                nowx += directions[nowd][1]
            else:
                break

result = 0
for n in range(N):
    for m in range(M):
        if used[n][m]:
            result += 1
print(result)