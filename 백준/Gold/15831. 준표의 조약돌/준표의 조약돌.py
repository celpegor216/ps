N, B, W = map(int, input().split())
lst = input()

result = 0

start = 0
b = w = 0

for n in range(N):
    if lst[n] == 'B':
        b += 1
    else:
        w += 1
    
    while b > B:
        if lst[start] == 'B':
            b -= 1
        else:
            w -= 1
        start += 1
    
    if w >= W:
        result = max(result, n - start + 1)

print(result)