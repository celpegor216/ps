lst = [list(map(int, input().split())) for _ in range(9)]

rows = [[0] * 10 for _ in range(9)]
cols = [[0] * 10 for _ in range(9)]
squares = [[0] * 10 for _ in range(9)]

for i in range(9):
    for j in range(9):
        rows[i][lst[i][j]] = 1
        cols[j][lst[i][j]] = 1
        squares[(i // 3) * 3 + (j // 3)][lst[i][j]] = 1

result = []

def dfs(now):
    if result:
        return

    if now == 81:
        for line in lst:
            result.append(line[:])
        return
    
    y, x = now // 9, now % 9
    square = (y // 3) * 3 + (x // 3)

    if lst[y][x]:
        dfs(now + 1)
    else:
        for n in range(1, 10):
            if not rows[y][n] and not cols[x][n] and not squares[square][n]:
                rows[y][n] = 1
                cols[x][n] = 1
                squares[square][n] = 1
                lst[y][x] = n
                dfs(now + 1)
                rows[y][n] = 0
                cols[x][n] = 0
                squares[square][n] = 0
                lst[y][x] = 0

dfs(0)

for line in result:
    print(*line)