# 스택인 줄 알았는데 dp였음
# 해답: https://velog.io/@myway00/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-274%EB%B2%88-%EB%B0%B1%EC%A4%80-%EB%B2%88

N = int(input())
lst = list(map(int, input().split()))

dp = [1 for _ in range(N)]

for i in range(1, N):
    for j in range(i):
        if lst[i] < lst[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))