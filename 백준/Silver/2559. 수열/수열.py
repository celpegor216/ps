N, K = map(int, input().split())
lst = list(map(int, input().split()))

now = sum(lst[:K])
result = now

for n in range(N - K):
    now -= lst[n]
    now += lst[n + K]
    result = max(result, now)

print(result)