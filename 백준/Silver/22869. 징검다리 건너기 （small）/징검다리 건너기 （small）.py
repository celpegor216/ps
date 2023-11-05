from collections import deque

N, K = map(int, input().split())
lst = list(map(int, input().split()))

dp = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(i + 1, N):
        if (j - i) * (1 + abs(lst[j] - lst[i])) <= K:
            dp[i][j] = 1

q = deque()
used = [0] * N

q.append(0)
used[0] = 1

result = 'NO'

while q:
    now = q.popleft()

    if now == N - 1:
        result = 'YES'
        break

    for n in range(now + 1, N):
        if not used[n] and dp[now][n]:
            q.append(n)
            used[n] = 1

print(result)