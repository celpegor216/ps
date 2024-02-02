# dp로 했을 때는 틀렸고 bfs로 했을 때는 시간 초과,,,
# 해답: 

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

dp = [[[0, -1] for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        left, up = dp[i][j - 1], dp[i - 1][j]
        
        left_check = (left[1] + 1) % 3 == lst[i][j]
        up_check = (up[1] + 1) % 3 == lst[i][j]

        left_cnt = left[0] + left_check
        up_cnt = up[0] + up_check

        if left_cnt > up_cnt:
            dp[i][j][0] = left_cnt
            dp[i][j][1] = lst[i][j] if left_check else left[1]
        else:
            dp[i][j][0] = up_cnt
            dp[i][j][1] = lst[i][j] if up_check else up[1]

print(dp[-1][-1][0])