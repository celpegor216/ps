# 힌트: dp
# 해답: https://ku-hug.tistory.com/185

N = int(input())
lst = list(map(int, input().split()))

# 주어진 수열과 이를 뒤집은 수열의 최장 공통 부분 수열을 구하고
# 전체 길이에서 그걸 빼면 됨

dp = [[0] * (N + 1) for _ in range(N + 1)]

for n in range(1, N + 1):
    for m in range(1, N + 1):
        if lst[n - 1] == lst[-m]:
            dp[n][m] = dp[n - 1][m - 1] + 1
        else:
            dp[n][m] = max(dp[n][m - 1], dp[n - 1][m])

print(N - dp[-1][-1])