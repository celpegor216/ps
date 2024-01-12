N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
maxv = 21e8

dp = [[[maxv, maxv, maxv] for _ in range(N)] for _ in range(N)]
for n in range(N):
    dp[n][n] = [0, lst[n][0], lst[n][1]]

def find(a, b):
    if dp[a][b][0] == maxv:
        for n in range(a, b):
            left, right = find(a, n), find(n + 1, b)
            tmp = left[0] + right[0] + left[1] * left[2] * right[2]

            if dp[a][b][0] > tmp:
                dp[a][b][0] = tmp
                dp[a][b][1] = left[1]
                dp[a][b][2] = right[2]
        
    return dp[a][b]

print(find(0, N - 1)[0])