# 해답: https://velog.io/@wlrhkd49/%EB%B0%B1%EC%A4%80-14002-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4-4-Python

N = int(input())
A = list(map(int, input().split()))

dp = [1] * N

for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[j] + 1, dp[i])

result = max(dp)
result_lst = []
cnt = result

for i in range(N - 1, -1, -1):
    if cnt == dp[i]:
        cnt -= 1
        result_lst.append(A[i])

print(result)
print(*result_lst[::-1])