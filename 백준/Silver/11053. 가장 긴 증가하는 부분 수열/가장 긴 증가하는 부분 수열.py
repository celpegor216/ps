# 해답: https://pacific-ocean.tistory.com/153
# 현재의 길이 = 현재 인덱스의 값보다 작은 값들 중 길이가 가장 긴 것 + 1
# 이전 값을 이용하므로 dp 문제

N = int(input())
lst = list(map(int, input().split()))

dp = [0] * N

for n in range(N):
    for i in range(n):
        if lst[n] > lst[i] and dp[n] < dp[i]:
            dp[n] = dp[i]
    dp[n] += 1

print(max(dp))