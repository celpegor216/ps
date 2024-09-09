N = int(input())
M = 5
lst = [list(map(int, input().split())) for _ in range(N)]

maxv = 0
res_idx = N

for i in range(N - 1, -1, -1):
    v = 0

    for a in range(M - 2):
        total = lst[i][a]
        for b in range(a + 1, M - 1):
            total += lst[i][b]
            for c in range(b + 1, M):
                total += lst[i][c]
                v = max(v, total % 10)
                total -= lst[i][c]
            total -= lst[i][b]

    if maxv < v:
        maxv = v
        res_idx = i + 1

print(res_idx)