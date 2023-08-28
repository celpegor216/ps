# dp, lis까지는 알겠는데 구현을 어떻게 하는지 모르겠음
# 해답: https://propercoding.tistory.com/43

N = int(input())
lst = list(map(int, input().split()))

dp = lst[:]
dp[0] = lst[0]

for n in range(1, N):
    for m in range(n):
        if lst[n] < lst[m]:
            dp[n] = max(dp[n], dp[m] + lst[n])

print(max(dp))