# 힌트: dp
# 해답: https://hongcoding.tistory.com/157

N = int(input())

lines = []

for n in range(N):
    a, b = map(int, input().split())
    lines.append([a, b])

lines.sort()

dp = [1] * N

# 최대 증가 수열
for n in range(1, N):
    for m in range(n):
        if lines[n][1] > lines[m][1]:
            dp[n] = max(dp[n], dp[m] + 1)

print(N - max(dp))