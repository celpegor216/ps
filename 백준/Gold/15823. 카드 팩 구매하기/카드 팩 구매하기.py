N, M = map(int, input().split())
lst = list(map(int, input().split()))

dp = [0] * N
now = set()
j = 0

for i in range(N):
    while j < N:
        if lst[j] in now:
            break
        now.add(lst[j])
        j += 1
    dp[i] = len(now)
    now.remove(lst[i])

start, end = 1, N // M
result = start

while start <= end:
    middle = (start + end) // 2

    cnt = 0
    idx = 0
    while idx < N and cnt < M:
        if dp[idx] >= middle:
            cnt += 1
            idx += middle
        else:
            idx += 1
    
    if cnt == M:
        result = max(result, middle)
        start = middle + 1
    else:
        end = middle - 1

print(result)