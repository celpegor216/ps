# dp를 적용해야 하는 건 알겠는데 어떻게 해야 할지 모르겠음
# 해답: https://studyandwrite.tistory.com/387


import sys
sys.setrecursionlimit(10 ** 5)

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

dp = [[-1] * M for _ in range(N)]

def dfs(y, x):
    if y == N - 1 and x == M - 1:
        return 1
    
    if dp[y][x] == -1:
        tmp = 0

        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and lst[y][x] > lst[ny][nx]:
                tmp += dfs(ny, nx)
        
        dp[y][x] = tmp
    
    return dp[y][x]

print(dfs(0, 0))