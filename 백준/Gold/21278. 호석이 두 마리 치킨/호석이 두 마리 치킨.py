N, M = map(int, input().split())
lst = [[21e8] * N for _ in range(N)]

for m in range(M):
    a, b = map(int, input().split())

    if a > b:
        a, b = b, a
    
    lst[a - 1][b - 1] = 1
    lst[b - 1][a - 1] = 1

for n in range(N):
    lst[n][n] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            lst[i][j] = min(lst[i][j], lst[i][k] + lst[k][j])

result = [-1, -1, 21e8]
for i in range(N):
    for j in range(i + 1, N):
        total = 0
        
        for n in range(N):
            total += min(lst[i][n], lst[j][n])
        
        if result[-1] > total * 2:
            result = [i + 1, j + 1, total * 2]

print(*result)