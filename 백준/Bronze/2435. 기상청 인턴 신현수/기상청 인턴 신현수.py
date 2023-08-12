N, K = map(int, input().split())
lst = list(map(int, input().split()))

now = sum(lst[:K])
result = now
for i in range(N - K):
    now -= lst[i]
    now += lst[i + K]
    result = max(result, now)

print(result)