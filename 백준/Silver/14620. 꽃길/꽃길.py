N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

used = [[0] * N for _ in range(N)]
result = 21e8

def dfs(level, temp):
    global result

    if level == 3:
        total = 0

        for i in range(3):
            for j in range(i + 1, 3):
                if abs(temp[i][0] - temp[j][0]) + abs(temp[i][1] - temp[j][1]) < 3:
                    total = 21e8

        if not total:
            for item in temp:
                for dy, dx in ((0, 0), (0, 1), (1, 0), (0, -1), (-1, 0)):
                    ny, nx = item[0] + dy, item[1] + dx
                    total += lst[ny][nx]
        
        result = min(result, total)
        return
    
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if not used[i][j]:
                used[i][j] = 1
                dfs(level + 1, temp + [(i, j)])
                used[i][j] = 0

dfs(0, [])

print(result)