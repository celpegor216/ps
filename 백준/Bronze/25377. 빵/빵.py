N = int(input())

result = 1001

for _ in range(N):
    A, B = map(int, input().split())
    if A <= B:
        result = min(result, B)

print(result if result != 1001 else -1)