H, W = map(int, input().split())
lst = list(map(int, input().split()))

result = 0

for h in range(1, H + 1):
    now = -1
    for w in range(W):
        if lst[w] >= h:
            if now != -1:
                result += w - now - 1
            now = w

print(result)