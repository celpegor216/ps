N, K = map(int, input().split())
lst = set()

for n in range(N):
    lst.add(int(input()))

lst = sorted(lst)
N = len(lst)

dp = [[21e8] * (K + 1) for _ in range(N)]

for n in range(N):
    if lst[n] > K:
        break
    
    for k in range(K + 1):
        if k < lst[n] and n > 0:
            dp[n][k] = dp[n - 1][k]
        elif k == lst[n]:
            dp[n][k] = 1
        else:
            dp[n][k] = min(dp[n][k - lst[n]] + 1, dp[n - 1][k])

result = min([dp[x][-1] for x in range(N)])

if result == 21e8:
    print(-1)
else:
    print(result)