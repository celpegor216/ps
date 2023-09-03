import sys
sys.setrecursionlimit(10 ** 5)

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1] * N for _ in range(N)]

def dfs(y, x):
    cnt = 0

    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < N and lst[ny][nx] > lst[y][x]:
            if dp[ny][nx] != -1:
                cnt = max(cnt, dp[ny][nx] + 1)
            else:
                cnt = max(cnt, dfs(ny, nx) + 1)
    
    dp[y][x] = cnt
    return cnt

result = 0
for i in range(N):
    for j in range(N):
        if dp[i][j] == -1:
            result = max(result, dfs(i, j))

print(result + 1)