# 힌트: DP로 풀어야 함
# 해답: https://animoto1.tistory.com/entry/%EB%B0%B1%EC%A4%80-9251-LCS-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Python

a = input()
b = input()

a_len = len(a)
b_len = len(b)

dp = [[0] * (b_len + 1) for _ in range(a_len + 1)]

for i in range(1, a_len + 1):
    for j in range(1, b_len + 1):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])
