A, B = map(int, input().split())
K, X = map(int, input().split())

result = 0

for i in range(A, B + 1):
    if K - X <= i <= K + X:
        result += 1

print(result if result else 'IMPOSSIBLE')