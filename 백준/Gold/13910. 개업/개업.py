N, M = map(int, input().split())
lst = list(map(int, input().split()))

# 조합으로 나올 수 있는 모든 웍 크기 계산
S = set(lst)

for i in range(M):
    for j in range(i + 1, M):
        S.add(lst[i] + lst[j])

lst = sorted(S)

# 최소 요리 횟수를 계산
M = len(lst)
dp = [[10 ** 5] * (N + 1) for _ in range(M)]

for i in range(M):
    for j in range(N + 1):
        if lst[i] > j:
            dp[i][j] = dp[i - 1][j]
        elif lst[i] == j:
            dp[i][j] = 1
        else:
            dp[i][j] = min(dp[i][j - lst[i]] + 1, dp[i - 1][j])

if dp[-1][-1] == 10 ** 5:
    print(-1)
else:
    print(dp[-1][-1])