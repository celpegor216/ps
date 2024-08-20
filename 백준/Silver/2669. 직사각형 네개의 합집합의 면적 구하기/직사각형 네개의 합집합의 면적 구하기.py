N = 101

used = [[0] * N for _ in range(N)]

for _ in range(4):
    l, d, r, u = map(int, input().split())

    for i in range(d, u):
        for j in range(l, r):
            used[i][j] = 1

result = 0
for i in range(N):
    for j in range(N):
        result += used[i][j]

print(result)