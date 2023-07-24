import sys
input = sys.stdin.readline

S = input().strip()
Q = int(input())
N = len(S)

dp = [[] for _ in range(2)] # 0 ~ ..., ... ~ N

result = [0] * 26
for i in range(N):
    result[ord(S[i]) - ord('a')] += 1
    dp[0].append(result[:])

dp[1].append(result[:])
for i in range(N - 1):
    result[ord(S[i]) - ord('a')] -= 1
    dp[1].append(result[:])

for q in range(Q):
    s, start, end = input().split()

    start, end = int(start), int(end)
    idx = ord(s) - ord('a')

    if start == 0:
        print(dp[0][end][idx])
    elif end == N - 1:
        print(dp[1][start][idx])
    else:
        print(dp[0][-1][idx] - dp[0][start - 1][idx] - dp[1][end + 1][idx])