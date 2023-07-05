# 해답: https://velog.io/@sunkyuj/python-%EB%B0%B1%EC%A4%80-15486-%ED%87%B4%EC%82%AC-2
# 인덱스를 N - 1에서부터 1씩 빼는 방식으로 진행했는데 틀림

import sys
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * N

for n in range(N):
    dp[n] = max(dp[n], dp[n - 1])
    finish = lst[n][0] + n - 1

    if finish < N:
        dp[finish] = max(dp[finish], dp[n - 1] + lst[n][1])

print(max(dp))