# 비슷한 유형의 dp를 풀었던 것 같은데...
# 해답: https://blog.naver.com/PostView.naver?blogId=kerochuu&logNo=222375177205&categoryNo=8&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView%EB%A5%BC

N, M = map(int, input().split())
lst = [0] + [int(input()) for _ in range(N)]

dp = [[0] * (M + 1) for _ in range(N + 1)]

for n in range(1, N + 1):
    dp[n][0] = dp[n - 1][0]

    for m in range(1, M + 1):
        dp[n][m] = dp[n - 1][m - 1] + lst[n]
    
    for m in range(1, M + 1):
        if n < m:
            break

        dp[n][0] = max(dp[n][0], dp[n - m][m])

print(dp[-1][0])