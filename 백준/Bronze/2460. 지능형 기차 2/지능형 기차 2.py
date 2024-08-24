N = 10

now = 0
result = 0

for _ in range(N):
    minus, plus = map(int, input().split())

    now = now - minus + plus
    result = max(result, now)

print(result)