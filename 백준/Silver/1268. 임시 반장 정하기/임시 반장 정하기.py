N = int(input())
M = 5
lst = [list(map(int, input().split())) for _ in range(N)]

maxv = 0
res_idx = 0

for n in range(N):
    v = 0

    for i in range(N):
        if n == i:
            continue

        for m in range(M):
            if lst[i][m] == lst[n][m]:
                v += 1
                break

    if maxv < v:
        maxv = v
        res_idx = n

print(res_idx + 1)
