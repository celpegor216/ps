# dp 같은데 방법을 모르겠음
# 해답: https://devlibrary00108.tistory.com/155

while 1:
    N, M = map(int, input().split())

    if N == M == 0:
        break

    lst = [list(map(int, input().split())) for _ in range(N)]

    dp = [[0] * (M + 1) for _ in range(N + 1)]

    result = 0

    for n in range(1, N + 1):
        for m in range(1, M + 1):
            if lst[n - 1][m - 1]:
                dp[n][m] = min(dp[n - 1][m - 1], dp[n - 1][m], dp[n][m - 1]) + 1
                
                result = max(result, dp[n][m])
    
    print(result)