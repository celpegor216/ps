N, M, K = map(int, input().split())

result = 0
for _ in range(N):
    tmp = input().split('1')
    for item in tmp:
        if len(item) >= K:
            result += len(item) - K + 1

print(result)