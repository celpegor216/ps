N, M, H = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

sy, sx = 0, 0
milks = []

for i in range(N):
    for j in range(N):
        if lst[i][j] == 1:
            sy, sx = i, j
        elif lst[i][j] == 2:
            milks.append((i, j))

result = 0
length = len(milks)
used = [0] * length

def dfs(y, x, h, cnt):
    global result, sy, sx
    
    for m in range(length):
        move = abs(milks[m][0] - y) + abs(milks[m][1] - x)
        if not used[m] and move <= h:
            used[m] = 1
            dfs(milks[m][0], milks[m][1], h - move + H, cnt + 1)
            used[m] = 0
    
    if abs(sy - y) + abs(sx - x) <= h:
        result = max(result, cnt)

dfs(sy, sx, M, 0)

print(result)