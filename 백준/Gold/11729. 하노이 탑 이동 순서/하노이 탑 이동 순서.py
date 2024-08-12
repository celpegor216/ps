N = int(input())
result = []

def move(n, now, nxt):
    if n > 1:
        move(n - 1, now, 6 - now - nxt)
    result.append((now, nxt))
    if n > 1:
        move(n - 1, 6 - now - nxt, nxt)

move(N, 1, 3)

print(len(result))
for line in result:
    print(*line)