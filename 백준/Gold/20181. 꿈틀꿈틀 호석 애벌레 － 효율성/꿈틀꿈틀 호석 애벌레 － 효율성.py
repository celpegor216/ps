# dp 같은데 풀이를 모르겠음
# 해답: https://baby-ohgu.tistory.com/33

N, K = map(int, input().split())
lst = list(map(int, input().split()))

dp = [0] * N

# maxv: left 이전까지의 최댓값의 합
maxv = now = left = right = 0

while 1:
    if now >= K:
        maxv = max(maxv, dp[left - 1])
        dp[right - 1] = max(dp[right - 1], maxv + now - K)
        now -= lst[left]
        left += 1
    elif right == N:
        break
    else:
        now += lst[right]
        right += 1

print(max(dp))