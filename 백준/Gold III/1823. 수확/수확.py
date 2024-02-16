# 투 포인터가 맞는 것 같은데 반례를 모르겠음
# dp였음,,,
# 해답: https://devlibrary00108.tistory.com/578

N = int(input())
lst = [0] + [int(input()) for _ in range(N)]

# dp[i][j] : i ~ j를 N번부터 거꾸로 골랐을 때의 최댓값
dp = [[lst[j] * N if i == j else 0 for j in range(N + 1)] for i in range(N + 1)]

for end in range(1, N + 1):
    for start in range(end - 1, 0, -1):
        dp[start][end] = max(
            dp[start + 1][end] + lst[start] * (N - end + start),
            dp[start][end - 1] + lst[end] * (N - end + start)
        )

print(dp[1][N])