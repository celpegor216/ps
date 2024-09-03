N, K, P = map(int, input().split())
lst = list(map(int, input().split()))

result = 0
for n in range(0, N * K, K):
    cnt = 0
    for k in range(K):
        if not lst[n + k]:
            cnt += 1
    if cnt < P:
        result += 1

print(result)