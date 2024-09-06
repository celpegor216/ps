N, K = map(int, input().split())
checks = (K % 10, (K * 2) % 10)

result = []

for n in range(1, N + 1):
    if n % 10 not in checks:
        result.append(n)

print(len(result))
print(*result)