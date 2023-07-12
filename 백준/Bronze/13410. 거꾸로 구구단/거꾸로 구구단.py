N, K = map(int, input().split())

result = 0

for k in range(1, K + 1):
    result = max(int(str(N * k)[::-1]), result)

print(result)