N = int(input())
lst = list(map(int, input().split()))
M = int(input())

dp = [''] * (M + 1)

for i in range(N):
    if lst[i] <= M:
        dp[lst[i]] = str(i)

for m in range(1, M + 1):
    for i in range(1, m + 1):
        a = dp[i] + dp[m - i]
        b = dp[m - i] + dp[i]

        tmp = []

        if a:
            tmp.append(int(a))
        if b:
            tmp.append(int(b))
        if dp[m]:
            tmp.append(int(dp[m]))
        
        if tmp:
            dp[m] = str(max(tmp))

print(dp[-1])